.SUFFIXES=.md

%.html: %.md
	 pandoc -S -s -c pandoc.css  -o $@ $<

all: index.html materials/week1.html materials/week2.html README.html
