HPC
========================================================
author: Kevin Thornton
date: 1/17/17

HPC

========================================================

For overview/docs

- http://hpc.oit.uci.edu
- https://hpc.oit.uci.edu/~krthornt/BioClusterGE.pdf

Modules
========================================================
- module avail
- module load foo/version

You can install your own modules!!!!

- module load krthornt/anaconda/3

"Custom", or "User" modules
========================================================

- The program itself goes in /data/apps/user_contributed_software/$USER
- The "module file" goes in /data/modulefiles/user_contributed_software/$USER

($USER == your user name!)

"Custom", or "User" modules
========================================================
This is **advanced**.  You need to know things:

- $PATH if you are installing a binary
- The difference between CPPFLAGS, CFLAGS, CXXFLAGS if you are installing a C/C++ library
- LDFLAGS, LD_LIBRARY_FLAGS, etc., if you are installing a library
- Other shell variables that may apply

**Feel free to email me if you want to do this**

Common HPC issues
======================================================

- Resource requests
- Resource use
- Checkpointing
- Zotfiles

Resources
=======================================================

- Queues
- RAM
- CPU
- Disk space

Queues
===========================================

- "PI" queues: krt, krti
- Priority queues: bio
- Public queues: pub64, pub8, pub72
- Free queues: free64, etc.

~~~{.sh}
#Get a list of what queues you have
#access to & what is free
q
~~~

RAM
========================================

- 64 core nodes have either 256Gb or 512Gb

This means you are limited to 512/64 = 8 or 264/64 = 4 Gb of RAM per job.

HPC does not enforce this.  You have to know how much RAM your jobs take!

~~~{.sh}
#!/bin/bash

#$ -q bio

#Output will be time (seconds) and peak RAM
#use (in bytes).  Divide by 1024^2 to get Gb.
/usr/bin/time -f "%e %M" -o memtime.txt command params
~~~

RAM
========================================

If a single task takes more than 8Gb RAM,
request more cores as needed:

~~~{.sh}
#$ -pe openmp 2 #for 8-16Gb needed
#$ -pe openmp 3 #for 15-24Gb needed
~~~

**Do not request 64 cores "just because"***

BIG RAM jobs
========================================

If your job will consume all RAM on the 256Gb nodes, simply avoid them:

~~~{.sh}
#Only run on nodes with 512Gb RAM
#$ -l mem_size=512
~~~

CORES
=========================================

- A program either uses multiple cores, or it doesn't.  
- Requesting multiple cores doesn't magically make a program multi-threaded.
- Read the documentation for your program.

Dynamic core requests
================================================

~~~{.sh}
#!/bin/bash

#request anywhere from 16-64 cores
#$ -pe openmp 16-64

#The no. cores given gets assigned
#automagically to CORES
program --nthreads $CORES
~~~

Testing jobs
=====================================

**Do not test on HPC.**  

It is a shared resource.

Test on your own systems.

Yes, that may be tricky, but too bad.

General advice
====================================

- When using multiple cores, prefer homogenous nodes.
- Don't mix 64 and 8 core nodes unless you are confident you know what you are doing.

Types of jobs
=====================================
- Simple, single-task
- Array
- Dependent

Simple, single-task job
=====================================
Probably the most common type.

~~~{.sh}
#!/bin/bash
#$ -q krt,krti,bio,pub64
cd $SGE_O_WORKDIR
module load foo
foo infile outfile
~~~

Array
=====================================
Great for repetitive tasks.
~~~{.sh}
#!/bin/bash
#$ -q bio,abio,free64,pub64
#$ -t 1-1000
cd $SGE_O_WORKDIR
module load krthornt/anaconda/3
SEED=`echo "$SGE_TASK_ID*$RANDOM"|bc -l`
SEED2=`echo "$SEED*$RANDOM"|bc -l`
SEED3=`echo "$SEED2*$SGE_TASK_ID*$RANDOM"|bc -l`
mspms 100 1 -t 1000 -r 1000 10000 | gzip > mspms.$SGE_TASK_ID.out.gz
~~~

Brute-force array jobs
=========================================================

- You need to execute a large number of commands.
- The commands are a bit complex somehow.
- Let's assume you can write a Python program to write all those commands into a file, called "commands.txt"
_ The commands must be INDEPENDENT of one another, as they execute asychronously on the cluster!!!

~~~{.sh}
#!/bin/bash
#replace 100 with no. lines in commands.txt
#$ -t 1-100
`head -n $SGE_TASK_ID commands.txt | tail -n 1`
~~~


Dependent jobs
=========================

- Two job scripts: job1.sh and job2.sh.
- job2.sh requires that job1.sh be finished.

~~~{.sh}
qsub -N JOB1NAME job1.sh
qsub -N JOB2NAME -hold_jid JOB1NAME job2.sh
~~~

**Job 2 will wait in the queue until job 1 completes!**

Workflows
==========================

- Jobs cannot submit jobs.  Use dependent jobs instead
- Automate your job submission w/a script (or Makefile, which we'll cover later in the course)

**Example script:**
~~~{.sh}
#!/bin/bash
for i in $(ls *.sh | grep -i jobs)
do
  qsub $i
done
~~~

Workflows
====================================

- It is harder to automate submitting dependent jobs, but brute force will do.
- *Such scripts document your workflow.*

**Example script**
~~~{.sh}
#!/bin/bash
qsub -N STEP1 step1.sh
qsub -N STEP2 -hold_jid STEP1 step2.sh
qsub -N STEP3 -hold_jid STEP2 step3.sh
~~~

The free queues
====================================

- Never, ever submit jobs to the free queues that do not use checkpointig or restarting.
- Otherwise, your job sits there in "suspend mode", which means no CPU consumed, but RAM is still allocated.  This is rude!

**A "rude" script:**
~~~{.sh}
#!/bin/bash
#This job submits to free
#queues but will pause if
#priority user comes along
#$ -q bio,abio,free64
#$ -q pe openmp 32

mycommand
~~~

Restart and Checkpointing
=====================================
- Only applies to jobs run on free queues (incl. abio)

**Restart**

- Your job is running. Owner comes along.  Your job is killed and resubmitted to the queue.

**Checkpointing**

- Your job is running.  Ownwer comes along.  Your job is serialized to disk, resubmitted, starts up where it left of.  (At least on paper.)

Restart
=================================================================

**Fixing the  "rude" script:**
~~~{.sh}
#!/bin/bash
#$ -q bio,abio,free64
#$ -q pe openmp 32
#$ -ckpt restart
mycommand
~~~

**Use case:** 

- When jobs run quickly, so starting from scratch isn't a big loss.  
- Example: array jobs where tasks have short run times.  (Short <= 1 hour??)

Checkpoint + continue
==============================
**Fixing the  "rude" script:**
~~~{.sh}
#!/bin/bash
#$ -q bio,abio,free64
#$ -q pe openmp 32
#$ -ckpt blcr
mycommand
~~~

**Use case:** 

- Very long jobs.  *De novo* assembly of eukaryotic genomes, etc.
- This is fragile. Some programs don't get along well with this method.  You have to experiment.  If it works, it is well worth it!
- Does not currently work with MPI.

Advanced trick 1: GNU parallel
================================================

- parallel is a swiss army knife command for running commands in parallel.
- Tutorial: https://www.gnu.org/software/parallel/parallel_tutorial.html
- A very powerful tool that can be very easy or very complex to use
- Use it when you have to run a lot of serial jobs.

Advanced trick 1: GNU parallel
================================================
*Example 1*

In file "commands.txt":
~~~
ls -lhrt > out1
ls -lhrS > out2
~~~

To execute those commands in parallel (asynchronously):

~~~{.sh}
parallel :::: commands.txt
~~~

Advanced trick 1: GNU parallel
================================================
Let's revisit this using GNU parallel:
~~~{.sh}
#!/bin/bash
#$ -q bio,abio,free64,pub64
#$ -t 1-1000
cd $SGE_O_WORKDIR
module load krthornt/anaconda/3
SEED=`echo "$SGE_TASK_ID*$RANDOM"|bc -l`
SEED2=`echo "$SEED*$RANDOM"|bc -l`
SEED3=`echo "$SEED2*$SGE_TASK_ID*$RANDOM"|bc -l`
mspms 100 1 -t 1000 -r 1000 10000 | gzip > mspms.$SGE_TASK_ID.out.gz
~~~

Advanced trick 1: GNU parallel
================================================
Why would we want to do this?

- It may be more efficient.
- It'll let us improve our job to be more reproducible (those pesky RNG seeds!).
- The more tricks you know, the better!

Advanced trick 1: GNU parallel
================================================
**Step 1: generate seeds**

~~~{.sh}
#!/bin/bash
for i in {1..1000}
do
echo $RANDOM $RANDOM $RANDOM
done > seeds
~~~

Now, we have a fixed set of seeds.  Yay for reproducibility!

Advanced trick 1: GNU parallel
================================================
**Step 2: figuring out parallel**

The command is this:

~~~{.sh}
parallel --colsep ' ' mspms 100 10 -t 5000 -r 5000 50000 --random-seeds {} :::: seeds
~~~

Oh boy--let's break that down

Breaking down the command
===========================================

~~~{.sh}
mspms 100 10 -t 5000 -r 5000 50000 --random-seeds {}
~~~

* This is the command to run.
* The {} is the suff contained in the file of RNG seeds.
* parallel copies the command and applies the stuff from the input file.

Breaking down the command
===========================================

~~~{.sh}
parallel --colsep ' ' 
~~~

Take the stuff from the input file (seeds), and break it into chunks separated by a space.

~~~{.sh}
:::: seeds
~~~

Use the stuff in a file called seeds to:

1. Decide on no. jobs
2. Get the values to be passed to each job.

The job script
================================
It is simple:
~~~{.sh}
#!/bin/bash
#$ -q bio
#$ -q pe openmp 64
cd $SGE_O_WORKDIR
parallel --colsep ' ' mspms 100 10 -t 5000 -r 5000 50000 --random-seeds {} :::: seeds
~~~

What does that give us?
====================================

Rather than submit 1,000 jobs to the queue via an array job, we take over an entire nodee and use all 64 cores to crank through the jobs.

The two strategies can be mixed and matched:

~~~{.sh}
#!/bin/bash
#$ -q bio
cd $SGE_O_WORKDIR
#untested :)
parallel [args for parallel] command :::: args.$SGE_TASK_D
~~~


