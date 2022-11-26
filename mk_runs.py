#! /usr/bin/env python
#
#   script generator for project="2021-S1-MX-14"
#
#

import os
import sys

# in prep of the new lmtoy module
try:
    lmtoy = os.environ['LMTOY']
    sys.path.append(lmtoy + '/lmtoy')
    import runs
except:
    print("No LMTOY with runs.py")
    sys.exit(0)

project="2021-S1-MX-14"

#        obsnums per source (make it negative if not added to the final combination)
on = {}
on['L1157-B1'] = [99000, 99001, 99025, 99026, 99030, 99031, 99035, 99036,                 # 4-may   (all have bad 14,15 0 too)
                  99382, 99383, 99385, 99386, 99390, 99391, 99393, 99394, 99398, 99399,   # 10-may  (all have bad 14,15 0 too)
                  99561, 99562, 99564, 99565, 99569,-99570,-99572,-99573, 99579, 99580,   # 14-may  (-0, 5?)
                         99582, 99583, 99589, 99590, 99592, 99593,                        #       
                  99765, 99766, 99770, 99771, 99776, 99777,-99778,                        # 17-may   -0,-2?,-5?
                  99901, 99902, 99906, 99907,                                             # 18-may
                  100232, 100233, 100235, 100236,-100240,-100241, 100243, 100244,         # 24-may
                          100248, 100249,
                  100611, 100612, 100614, 100615, 100617, 100618, 100622, 100623,         # 1-jun
                          100625, 100626,
                 ]

#        common parameters per source on the first dryrun (run1, run2)
pars1 = {}
pars1['L1157-B1'] = "dv=250 dw=500 extent=250"
pars1['L1157-B1'] = "dv=250 dw=150 extent=250"
# at this setting beam 2 often has a birdie at ~220, thus dv=250 should be preventing it in the baseline
# dw=400 might start to show the CO filter problem, use smaller?
# earlier data (e.g. 99382) have bad tsys v < -400

#        common parameters per source on subsequent runs (run1a, run2a)
pars2 = {}
pars2['L1157-B1'] = "pix_list=1,3,4,7,8,9,10,11,12,13,14,15"
pars2['L1157-B1'] = "pix_list=1,2,3,4,6,7,8,9,10,11,12,13,14,15"
# 99286-99538 has bad beams 14,15
# for birdies, see obsnum.args

runs.mk_runs(project, on, pars1, pars2)
