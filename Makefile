.SUFFIXES=.md

%.html: %.md
	 pandoc -S -s -c pandoc.css  -o $@ $<

all: index.html materials/week1.html materials/week2.html materials/week3.html materials/week4.html materials/week5.html README.html
