LabNotebooks
========================================================
author: Kevin Thornton
date: Advanced Informatics, Week 3

The problem
========================================================

* Often not a physical lab notebook for computational work
* It is hard to turn shell scripts, REAMDE.md files, etc., into nice-looking "reports" for you, your lab meetings, PI, etc.

Some solutions that we will NOT talk about
=================================

* Google docs
* Evernote

They both track changes, allow images to be added, etc.

Ultimately, my opinion is that these kind of tools are insufficient for a variety of reasons.

(They are really mobile device-friendly, though!)

One cool tool that you should know about
================================================

* [Google Keep](http://keep.google.com)
* [A semit-rant about why you should use it](http://www.computerworld.com/article/3144450/enterprise-applications/why-you-should-start-using-google-keep-right-away.html)

Tools that do work really well
=====================================

* [Rstudio](http://www.rstudio.org)
* [Jupyter notebooks](http://jupyter.org/)

These are true report-generating tools, and make excellent lab notebooks (to the extent that one works in R, Python, or a combo of the two.)

TL;DR
======================================
**If you take only one thing away from this week:**

* Rstudio is the superior product in just about every way.
* *But,* it is R-only.

What do they do??
========================================

**Briefly:**

* They allow code and "markup" to be mixed in the same document.
* They are easily converted into HTML, pdf (via LaTex), and other formats.

A digression: pandoc
=======================================

* [Pandoc](http://pandoc.org/)
* You heard it here first...
* This is likely to be a big part of the future of manuscript preparation.
* You need this for Rstudio...

Rstudio features
=======================================

* Create reports, presentations. (These slides are done in Rstudio!)
* Mix Markdown and R syntax
* Git integration
* Code editor for R and C++ (for use with [Rcpp](http://www.rcpp.org))
* Different output formats are supported with a [knitr](https://yihui.name/knitr/)/[pandoc](http://www.pandoc.org) workflow that "just works" with little input from the user.

Rmarkdown
=========================================

A flavor of Markdown used by Rstudio.


```r
plot(sin,xlim=c(0,10))
```

![plot of chunk unnamed-chunk-1](LabNotebooks-figure/unnamed-chunk-1-1.png)

The recipe (ignore the backslashes!)
=====================================

~~~
\`\`\`{r, options}
plot(sin,xlim=c(0,10)
\`\`\`
~~~

LaTeX is supported.
================================

Math formatting works. LaTeX code in single dollar signs is inlined.  For example, the formula for Watterson's (1975) estimator of $4N_e\mu$ is $\hat{\theta}=\frac{S}{\sum_{i=1}^{n-1}{1/i}}$.

LaTeX in double dollar signs is centered.  The average number of pairwise differences can be calculated as the sum of site heterozygosities, which for biallelic variants is equivalent to $$\pi = \sum_{i=1}^S\frac{k_i(n-k_i)}{n(n-1)}$$, where $k_i$ is the count of an allele at the $i^{th}$ variant position.

Rstudio: methods of use
==================================

* Standalone app.
* Client/server model via browser.

Jupyter notebooks
=======================

* Originally called iPython notebook.
* Renamed Jupyter as scope has increased beyond Python.
* Support for Python, R, Julia, Scala, more????
* Very similar in feeling to a Mathematica notebook.
* Client/server only, works via a web browser.

Jupyter downsides
========================

* Weak file system navigation.
* Requires some funky "magic" lines at top to use Python graphics
* Not as "git-friendly".  The notebook itself is a large JSON file, which contains your graphics as binary "blobs", making commits/diffs BIG.  People are [working on this](https://gab41.lab41.org/commit-and-push-to-github-from-jupyter-notebooks-579f5743a50b#.8bpyfbvex), but fixes aren't readily available.

Jupyter downsides (con't)
========================
* Editor not as good.  Rstudio default to GNU readline key bindings (similar to many Emacs bindings) and has options for vim bindings, too.  Jupyter is limited to "whatever your browser supports", which can really stink...
* Conversion to other formats done via command line program called **nbconvert**, as opposed to in-app as in Rstudio.
* Working remotely is painful (slow) through X forwarding.

Jupyter + R
==========================

* [Instructions](https://irkernel.github.io/)

Jupyter and X forwarding
===========================
**Simply put: DON'T!!!!**

* Use [SSH port forwarding](https://gist.github.com/molpopgen/3267efe08a0a4c23835249a955db37a2) instead.  
* Allows you to use your **local** browser!
