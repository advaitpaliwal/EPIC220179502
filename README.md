# EPIC 220179502.01: a 1.2 Earth-radius planet candidate on a 6.6-day orbit around an M dwarf from K2 Campaign 8

Advait Paliwal (independent researcher, advaitpaliwal@gmail.com), 2026-10-13.

A dip in brightness of about 0.09% repeats every 6.59 days in K2 Campaign 8 (2016) photometry of EPIC 220179502, an early-M dwarf 124 pc away. Eleven transits fall in the campaign. If it is a planet, it is about 1.2 times the size of Earth and receives about nine times the sunlight Earth does.

| | |
|---|---|
| Host | EPIC 220179502 = TIC 423360694 = Gaia DR3 2535800235461780864 = 2MASS J00591394-0048272, M dwarf (TIC Teff 3602 ± 157 K, R 0.397 ± 0.012 R☉, M 0.388 M☉), Gaia DR3 parallax 7.979 mas, G = 15.04, Kp = 15.03, RUWE 1.02 |
| Period | 6.59311 (+0.00129/−0.00105) d |
| Mid-transit | 2457431.4782 ± 0.0033 BJD_TDB |
| Depth / duration | 911 (+124/−126) ppm / 1.78 (+0.13/−0.16) h (EVEREST light curve) |
| Radius | 1.18 (+0.12/−0.11) R⊕ (for R★ = 0.397 R☉) |
| Equilibrium temperature / insolation | 489 (+25/−24) K / 9.5 (+2.1/−1.7) S⊕ |
| Data | K2 C8 (2016 January–March), 30-minute cadence; 11 transits |
| False-positive probability | 0.0096 ± 0.0013 (TRICERATOPS with MOLUSC Gaia limits, 10 runs, range 0.0077–0.0116); 0.064 without MOLUSC; NFPP 0 |

Status: **planet candidate**. Not a TOI, CTOI or K2 candidate in the NASA Exoplanet Archive or ExoFOP, and not in SIMBAD, as of 2026-10-13. Odd and even transits agree (0.9σ), there is no secondary eclipse (−13 ± 79 ppm at phase 0.5), the eleven transit depths are consistent (χ² = 6.6 for 10 degrees of freedom), and the fitted depths from EVEREST (911 ppm), K2SFF (910 ppm) and K2SC (1087 ppm) agree within 1σ. The in-transit difference-image centroid sits 3.7″ (5.2σ by the bootstrap error) from the out-of-transit centroid, but 25% of 60 difference images made at phases without a transit show an offset at least as large; the same test on the known planet K2-151 b gives 0.27″. TESS (Sectors 3, 30, 42, 43, 97) cannot detect the transit at T = 13.96 (expected SNR at most 1.1 per sector). High-resolution imaging and more precise photometry are the next observations.

## Contents

- `note/figure1_EPIC220179502.png` — (a) C8 EVEREST photometry folded on the fitted ephemeris with 30-minute bins and the median model; (b) the whole campaign before and after detrending; (c) four single transits
- `data/lc/` — the detrended light curve with phase and model (`everest_detrended_c08.csv`), the undetrended EVEREST light curve, and box depths per reduction
- `data/fit/` — posterior summary (`posterior_summary_everest.csv`, 40 walkers × 40,000 steps) and fit outputs for EVEREST, K2SFF and K2SC
- `data/vetting/`, `data/injection/` — odd/even, secondary-eclipse, phase-scan and per-transit checks; injection-recovery and null searches
- `data/pixels/` — difference image, its null test and depth-versus-aperture results, with the same difference-image tests on K2-151 b for reference
- `data/fpp/` — false-positive probability runs (per-run results, scenario tables, MOLUSC summary, TRICERATOPS star list)
- `data/tess/`, `data/catalogue/`, `data/search/` — TESS coverage and sensitivity, catalogue queries with their URLs (including the 2026-10-13 recheck), and the search detection
- `code/` — search, light-curve, fit, vetting, pixel, FPP, TESS, catalogue and figure scripts

Data: K2 (NASA, via MAST), EVEREST, K2SFF and K2SC high-level science products, TESS (TESScut), ESA Gaia DR3, TIC v8.2. Software: lightkurve, batman, emcee, transitleastsquares, wotan, TRICERATOPS, MOLUSC, tess-point, astropy, matplotlib. Licences: code MIT; text, figures and data CC BY 4.0.

Scripts are kept as run. File locations inside them are given relative to a single working directory (for example `k2-deep/220179502/`); set that directory up, or edit the paths, to rerun them.
