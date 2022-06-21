# 2021-S1-MX-14

More later.

## OBSNUM

First night beams 14,15 really bad. 8 maps taken. Not till 99561 did those two come back.
beam 0 always bad -
beam 5 sometimes a bit (check, we included it) - 
beam 2 or 6 might have the birdy, but it's in the line region. Still, it gives bad maps,
so before we do proper birdie flagging, take beams 2 and 6 out as well.


More detailed descriptions are in the file **mk_runs.py**.


## LMTOY Data Reduction

There are two ways to run the SLpipeline, using a different $WORK_LMT directory where the root
of the data processing occurs

1. Use the WORK_LMT that came with where **lmtoy** was installed. This will likely require
   write permission from the owner

   This is the way it runs on Unity.

2. Set WORK_LMT to a directory here in this directory,  something like

              WORK_LMT=`pwd`

   and no permissions in the $LMTOY tree are. Of course you still need to have LMTOY
   installed. The pipeline will then create all  data products in this local directory.

### Creating the run files

A master script **mk_runs** contains all the information on which obsnums are good,
which beams are good, etc.  You always will need to re-run this script to create the
SLpipeline *run* files. The script also uses the (optional) **OBSNUM.args** files, where
arguments specific to this obsnum can be stored. These files should be edited by
a user to create a new "final" dataset. Any optional post-processing after the
pipeline will not be described here (but is of course recommended?).

This command creates the run files (it uses the **mk_runs** scripts):

      make runs
	  

### Running the pipeline


With [SLURM](https://slurm.schedmd.com/documentation.html) this is the way:

      sbatch_lmtoy 2021-S1-MX-14.run1a
      # wait for it to finish
      sbatch_lmtoy 2021-S1-MX-14.run1b
      # wait for it to finish
      sbatch_lmtoy 2021-S1-MS-14.run2

Files:

      2021-S1-MX-14.run1a         start from scratch again
	  2021-S1-MX-14.run1b         incremental
      2021-S1-MX-14.run2          combination
