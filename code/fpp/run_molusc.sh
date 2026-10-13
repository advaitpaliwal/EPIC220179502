#!/bin/zsh
# MOLUSC 2 x 100k (RUWE + Gaia contrast) = 200,000 companions, M = 0.387706 Msun (TIC 423360694 = TRICERATOPS M_s). Copied from ../../211038138/fpp_joint/scripts/run_molusc.sh.
F=k2-deep/220179502/fpp_joint
PYM=python
cd $F
for s in 21 22; do
  SEED=$s $PYM -I -W ignore molusc_run.py -v --ruwe --gaia -a $F/molusc_out/m100k_s$s 00h59m13.9586s -- -00d48m27.361s 100000 0.387706 > molusc_out/m100k_s$s.log 2>&1
done
echo MOLUSC_DONE >> molusc_out/pids
