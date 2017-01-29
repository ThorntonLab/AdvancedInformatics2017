Makefiles
========================================================
author: Kevin Thornton
date: Advanced Informatics, week 4
autosize: true

The problem
==============================

* You have a bunch of scripts expecting input and generating output
* How do you *quickly* figure out if everthing is done?
* How do you *know* every file is based on the latest code?

One solution
===========================

Manually inspect the time stamp of each any every file.

**Hint:** that doesn't really work well.

Another solution
===========================

Generate a "master" shell script that checks time stamps, etc., and only does the work if something has changed.

**Hint:** this is re-inventing an extremely complex wheel.

Another solution
===========================

* A Makefile
* The program "make" **is** that really complicated shell script that I just referred to.

What does it do?
==========================

* It combines "targets", "patterns", "dependencies", and "rules" into a workflow.
* Individual steps only run when dependencies change.

Why was it created?
========================

* To compile source code into programs
* This is a hugely repetitive task where the same pattern is used over an over

Why do this?
========================

* Because it tells you when you are done!

~~~{.sh}
make 
make: Nothing to be done for `all'.
~~~

Example
====================
~~~{.sh}
all: Figs/fig1.pdf

Figs/fig1.pdf: R/fig1.R
  cd R;R --no-save --quiet < fig1.R
  
clean:
  find . -name '*.pdf' | xargs rm -f
~~~

Break it down
====================
* **all** is the *default target* executed by make.
* Here, "all" means we make a single figure that'll end up in the subdirectory "Figs"

~~~{.sh}
all: Figs/fig1.pdf
~~~

Break it down
===================

* This is the rule to make fig1.pdf
* It depends on R/fig1.R
* The command to run is given in the rule

~~~
Figs/fig1.pdf: R/fig1.R
  cd R;R --no-save --quiet < fig1.R
~~~

Break it down
=======================

* clean is the name of another target
* it deletes all the pdf files
* **Be really careful  how you write your clean targets!!**

~~~
clean:
  find . -name '*.pdf' | xargs rm -f
~~~

Target dependencies can be complex
================
~~~{.sh}
Figs/fig2.pdf: R/fig2.R R/makefig2data.R data/fig2data.txt
  cd R;R --no-save --quiet < fig2.R
  
data/fig2data.txt: R/makefig2data.R
  cd R;R --no-save --quiet < fig2.R
~~~

Hmmm, this is getting repetitive...
===============================
~~~{.sh}
all: Figs/fig1.pdf Figs/fig2.pdf

Figs/fig1.pdf: R/fig1.R
	cd R;R --no-save --quiet < fig1.R

Figs/fig2.pdf: R/fig2.R R/makefig2data.R data/fig2data.txt 
	cd R;R --no-save --quiet < fig2.R

data/fig2data.txt: R/makefig2data.R
	cd R;R --no-save --quiet < makefig2data.R
~~~~~

Patterns!!!
==============================

* We can write **rules** that apply to a **filename pattern**.

~~~{.sh}
Figs/%.pdf: R/%.R
  cd R;R --no-save --vanilla $(<F)
~~~

* The '%' is a wildcard
* $(<F) is an [automatic variable](http://www.gnu.org/software/make/manual/make.html#Automatic-Variables) which refers to the file part of the first dependency.

Getting more compact
=======================
~~~{.sh}
all: Figs/fig1.pdf Figs/fig2.pdf

Figs/%.pdf: R/%.R
	cd R;R --no-save --quiet <  $(<F)

Figs/fig1.pdf: R/fig1.R

Figs/fig2.pdf: R/fig2.R R/makefig2data.R data/fig2data.txt 

data/fig2data.txt: R/makefig2data.R
	cd R;R --no-save --quiet < makefig2data.R

clean:
	find . -name '*.pdf' | xargs rm -f
	rm -f data/*
~~~~

General comments
==========================
* make tranlates to "make -f Makefile all" by default
* The file name is Makefile not makefile.  (This messes up OS X users all the time.)
* Multilple Makefiles are totally fine (and in fact encouraged!!!):

~~~{.sh}
make -f Makefile.process_intermediate_files
make -f Makefile.figures
make -f Makefile.latex
~~~

Use cases
==========================

* Packagable, highly-repetitive tasks
* Take a list of FASTQ files + a reference.  Run the aligner.
* Given a list of .bam files, do something with samtools.
* Given a list of .vcf files, do something with GATK.

Pros
============

* Reproducibility.
* Forced organization.  Your file names all gotta make sense.
* Your project's work flow becomes **self-documenting** (to the extent that a Makefile is readable by mortals).
* Automagic parallel computing:

~~~{.sh}
make -j 8 Makefile.figs
~~~

Cons
==============

* It slows you down
* It is whole lot of arcane Unix nerdiness
* Advanced pattern/rule stuff is tricky.

More resources
====================

* [Karl Broman](http://kbroman.org/minimal_make/)
* [Byron Smith](https://bsmith89.github.io/make-bml/)
* [A paper](https://academic.oup.com/bib/article/doi/10.1093/bib/bbw020/2562749/A-review-of-bioinformatic-pipeline-frameworks) on using make for bioinformatics.
* [GNU make documentation](https://www.gnu.org/software/make/manual/make.html)
* [Snakemake](https://academic.oup.com/bioinformatics/article/28/19/2520/290322/Snakemake-a-scalable-bioinformatics-workflow) and references therein.
