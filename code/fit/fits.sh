#!/bin/sh
cd k2-deep
for s in everest k2sff k2sc; do OPENBLAS_NUM_THREADS=1 python -I -u scripts/fit.py 220179502 $s 6.592387 2565.5132 1.85 6.21 0.93 0.3967 0.02 3602 157 40000 > 220179502/fit/run_$s.log 2>&1; done
