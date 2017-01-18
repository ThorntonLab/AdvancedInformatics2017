# Week 2: Advanced (?) HPC usage

Some background reading:

* [HPC at UCI](https://hpc.oit.uci.edu/)
* [Hardware overview](https://hpc.oit.uci.edu/HPC_Overview.html)
* [An old tutorial that I wrote](https://hpc.oit.uci.edu/~krthornt/BioClusterGE.pdf)
* [Newer tutorial that I wrote](https://github.com/ThorntonLab/biocluster)

[My notes for week2 lecture](HPC.html)

# Lab exercise.

We are going to concoct a "bioinformatics workflow" that has the following features:

1. It uses dependent jobs.
2. Each step checks that the output from the previous step exists.
3. Ideally, we do everything using only bash commands.  (You could do a lot of it with custom Python scripts, but that
   adds a lot of extra work.)

The workflow will do the following:

1. Job1: create a list of all files in your user's home directory.
2. Job2: get the word count for each file in the list created in Job1.
3. Job3: Make a list of every file with fewer than 100 lines, using the output from Job2.
4. Job4: (or 3b.) Make a list of every file smaller than 5Kb in size.

The goal here is that you get a robust set of scripts that check for errors, etc.  Although this example is really
trivial, you will also learn some new shell commands that are really useful.
