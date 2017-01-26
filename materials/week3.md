# Week 3: Rstudio, Jupyter notebooks, and publication-quality graphics

Background materials:

* [Rstudio website](https://www.rstudio.com/)
* [Rstudio tutorial](http://web.cs.ucla.edu/~gulzar/rstudio/basic-tutorial.html) from UCLA
* [Jupyter project](http://jupyter.org/)
* [Jupyter quickstart guide](https://jupyter-notebook-beginner-guide.readthedocs.io/en/latest/)
* [Jupyter notebook tutorial](https://www.datacamp.com/community/tutorials/tutorial-jupyter-notebook)

[Lecture notes](LabNotebooks.html)

For the lab this week, we will work through this [set of exercises](http://tutorials.iq.harvard.edu/R/Rgraphics/Rgraphics.html).

If you know ggplot well already and/or have time, work through
[this](http://genomicsclass.github.io/book/pages/dplyr_tutorial.html) tutorial about dplyr.

Useful free resources:

* [ggplot tutorial](http://zevross.com/blog/2014/08/04/beautiful-plotting-in-r-a-ggplot2-cheatsheet-3/) from 2014.

Books:

* [R for data science](https://www.amazon.com/Data-Science-Transform-Visualize-Model/dp/1491910399/)
* [ggplot book](https://www.amazon.com/ggplot2-Elegant-Graphics-Data-Analysis/dp/331924275X)
* Basically anything by Hadley Wickham is the future of nice stuff for R.

# Getting image files ready for publication.

There are a lot of ways to do this!  Here's one that works well.

## Background

* R does not make "true" pdf files!! Rather, it generates a wrapper around some other form of graphic file.  In our
  experience, pdf generated from R raise red flags at journals like PLoS.

So, here is what we do:

1. Save graphics as 600dpi TIFF:

~~~{.r}
tiff('plot.tiff',height=x,width=y,res=600)
~~~

This makes a really big file!

2. Use [ImageMagick](https://www.imagemagick.org/) to convert to smaller tiff:

~~~{.sh}
convert plot.tiff -set colorspace RGB -layers flatten -alpha off \
-compress lzw -depth 8  -density 600 -adaptive-resize 4500x2400  plot.compressed.tif
~~~

3. Use ImageMagick again to make a final pdf:

~~~{.sh}
convert plot.compressed.tif plot.compressed.pdf
~~~
