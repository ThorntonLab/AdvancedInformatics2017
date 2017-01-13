#Week 1 materials

* __READ:__ [Phil Spector's notes on Python](https://www.stat.berkeley.edu/~spector/python).  No, not
  [that](https://en.wikipedia.org/wiki/Phil_Spector) Phil Spector!
* [Notes](https://www.stat.berkeley.edu/~spector/pythonslides.pdf) corresponding to the above document.
* __READ:__ [My intro to git/github](https://github.com/ThorntonLab/intro2github).  (This was presented in Evolution Journal Club back in 2014)
* __For future reference:__ [Crash course in scicomp modules for Python](https://anonimops.de/PythonCrash/PythonNumpy.pdf) 

## General comments/editorializing on Python.

* Indentation/spacing matters in Python.  There is no requirement as to the _number_ of spaces/tabs for each level of
  indentation, but there is a requirement that indentation is _consistent_ for each level:  For example:
  
~~~{.python}
def foo(x):
    """
    Yes, this is a dumb function...
    """
    if x is None:
        raise TypeError("x cannot be None!")
    try:
        return int(x)/2
    except:
        return None
~~~
  
* I recommend spaces instead of tabs. Fans of [Silicon Valley](https://www.youtube.com/watch?v=SsoOG6ZeyUI)'s main
  character are free to disagree. (The link acknowledges the existence of sex.)
* __It is imperative to have a text editor capable of editing Python files.__  The "big two" of the Unix world
  ([Emacs](http://www.gnu.org/software/emacs)
  and [vim](http://www.vim.org)) work very well.  I personally use [neovim](https://neovim.io/) with the
  [YouCompleteMe](https://valloric.github.io/YouCompleteMe/)
  module for Python/C/C++ code completion.  There are [a
  lot](https://www.elegantthemes.com/blog/resources/the-11-best-code-editors-available-in-2015) of editors available for the OS X system.  Many of them
  cost money.  One exception that a few colleagues have recommended is [Atom](https://atom.io/), but I cannot personally
  vouch for it.  For Windows users, I have no idea, but Atom seems to support that system.
* [This is a style guide for Python code.](https://www.python.org/dev/peps/pep-0008/)  Style guides are not gospel,
  although many treat them as such.  The advice here is good, though.
* [Official Python docs](http://docs.python.org)  Note that there are docs for several different versions of the
  language.  

## Comments on Spector's notes.

* His notes violate a fundamental tenet of programming, which is "know your standard library." (The "standard library"
  is the set of types, functions, etc., that come with the language by default, meaning they are available without need
  for any third-party add-ons.) For example, his
  discussion of counting (section 4.9 of his notes) is "non-Pythonic", meaning he is hand-rolling a solution when a
  better, safer, and more idiomatic method is available in the langauge's standard library.  To be fair, he is doing
  this for pedagogical reasons, but reinventing the wheel is a bad habit that a few seconds with Google can usually help
  you avoid.

* They are Python2-centric.  The current language standard is Python3.  See
  [here](http://python3porting.com/differences.html) for Py2/Py3 differences. Many of these differences will lead to
  failure under Py3.  The big one is "printing", which is now a function in Py3. To save your sanity, get used to saying
  this in your PyX scripts:

~~~{.python}
#importing from __future__ 
#must be at the VERY top
#of yours scripts, meaning
#BEFORE any other imports
from __future__ import print_function

#In Py2, you'd say print x, but
#that is now deprecated
print(x)
~~~

Similarly, there is only one integer type in Py3.  For example, this Py2 code no longer works:

~~~{.python}
#Assign x to be an "unlimited" precision integer.
#type(x) would say 'long'.
x = 100L
~~~

Py3 has but one integer type:

~~~{.python}
#This is type 'int'
x=100
~~~

* When working interactively (_e.g._ in a terminal), it is often nicer to work with [iPython](https://ipython.org/).  It
  allows for auto-completion, a "sweet" help system, graphics display, etc.  In many ways, it is more like working
  within the [R](http://www.r-project.org) shell. iPython is also the engine behind "Jupyter" notebooks, which we'll
  cover later in this course.

## Other relevant materials:

* Enthought provides [Python training](https://training.enthought.com/A). Look [here](https://store.enthought.com/licenses/academic/) for how to get a license.  Thanks to Edwin!
* UCI's [Data Science Initiative](http://datascience.uci.edu/) runs many [short courses](http://datascience.uci.edu/education/short-courses/) during the year.  These cover many topics, including Python.  They're free, too.

# Lab/homework exercise.

Write a Python script to count number of occurrences of every word in a file.  Do it idiomatically, using the Python standard library.  The file
  to parse is the [GNU General Public License, version 3](https://www.gnu.org/licenses/gpl-3.0.en.html), aka GPL3.

To obtain a plain-text version of the GPL3, we need some tools that JJ hopefully covered in part 1 of this course :).
  You may use the wget utility to get the file:

~~~{.sh}
wget https://www.gnu.org/licenses/gpl-3.0.txt
~~~

If 'wget' doesn't exist (which is the default case on Apple's OS X system), use curl instead: 

~~~{.sh}
curl https://www.gnu.org/licenses/gpl-3.0.txt > gpl-3.0.txt 
~~~

To accomplish this task you need to figure out how to:

* strip punctuation from text
* it would also be nice to convert all words to lower case

__Advanced:__ do your work in a git repo.  Optionally, get a github account and put all of your work there.

# More info/resources about Python

Larry asked about efficiency of things like lists. Efficiency is an important topic in general.  Fortunately, Python is
relatively efficient.  That said, there are situations where you run into performance bottlenecks. Much like R, you can
write extensions to Python using C/C++ ([Py2 docs](https://docs.python.org/2/extending/extending.html) and [Py3 docs](https://docs.python.org/3/extending/extending.html)).  Python's C application programming interface, or API, is quite nice.  However, this is the hard way to go: you need to know C/C++.  Another option is to use [Cython](http://www.cython.org), which allows you to write Python code that gets turned into the equvalent C code.  It also allows you to functions from other C/C++ libraries in Python by generating Python wrappers to the libraries.  We use it quite a bit in the lab.
