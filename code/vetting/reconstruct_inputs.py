# Reconstruct the inputs used for lc/everest.npz and fit/vet_everest.json (EPIC 220179502). usage: python -I recon.py
import sys, json, numpy as np
sys.path.insert(0, 'k2-deep/scripts'); import lcs
D = 'k2-deep/220179502'
z = np.load(f'{D}/lc/everest.npz'); t0, f0 = z['t_raw'], z['f_raw']
for P, T0, dh in [(6.592387, 2565.5132, 1.85), (6.5923867185087035, 2565.5131840982035, 1.5099875131328373), (6.593106033728739, 2598.4781823609073, 1.7810701849925068)]:
    t, f = lcs.flat(t0, f0, P, T0, dh/24)
    same = len(t) == len(z['t']) and np.allclose(t, z['t']) and np.allclose(f, z['f'], rtol=0, atol=1e-12)
    print('prep', P, T0, dh, 'n', len(t), 'identical', same, 'maxdiff', np.max(np.abs(f - z['f'])) if len(t) == len(z['t']) else None)
V = json.load(open(f'{D}/fit/vet_everest.json')); t, f = z['t'], z['f']
R = json.load(open(f'{D}/fit/result_everest.json')); P, T0 = R['P_d'][0], R['T0_BKJD'][0]
def vet(P, T0, T14):
    ph = lcs.phase(t, P, T0); ep = np.round((t - T0)/P).astype(int)
    oot = (np.abs(ph) > T14) & (np.abs(ph) < 0.5); inn = np.abs(ph) < 0.35*T14
    def dep(mi, mo): return np.median(f[mo]) - np.mean(f[mi]), np.std(f[mo])/np.sqrt(mi.sum()), mi.sum()
    a = dep(inn, oot); o = dep(inn & (ep % 2 == 1), oot); e = dep(inn & (ep % 2 == 0), oot)
    per = []
    for k in np.unique(ep[inn]):
        m = inn & (ep == k); mo = oot & (ep == k); per.append(dep(m, mo if mo.sum() > 5 else oot)[:2])
    per = np.array(per); mu = np.average(per[:, 0], weights=1/per[:, 1]**2)
    return a[0]*1e6, abs(o[0]-e[0])/np.hypot(o[1], e[1]), np.sum(((per[:, 0]-mu)/per[:, 1])**2), len(per)-1
for P_, T0_, lab in [(P, T0, 'fitted'), (6.5923867185087035, 2565.5131840982035, 'search')]:
    for th in [1.51, 1.7810701849925068, 1.85, 1.9]:
        print('vet', lab, th, ['%.6g' % x for x in vet(P_, T0_, th/24)])
print('stored', V['all'][0], V['odd_even_sigma'], V['per_transit_chi2'], V['per_transit_dof'])
