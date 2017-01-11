.SUFFIXES: .txt

all: gpl3counts.txt

gpl-3.0.txt:
	curl https://www.gnu.org/licenses/gpl-3.0.txt > gpl-3.0.txt

gpl3counts.txt: gpl-3.0.txt wordcounter.py
	python wordcounter.py gpl-3.0.txt

clean:
	rm -f gpl3counts.txt gpl-3.0.txt
