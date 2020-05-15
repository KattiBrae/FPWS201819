all: build/main.pdf clean

############################################################
# Anpassbare Optionen:
#
# Präfix der PDF-Dokumente. Struktur ist: Präfix_BlattXY.pdf
Prefix = FP_WS2019
############################################################

# Automatisch ermittelter Name
Filename = $(addprefix $(Prefix)_, $(addsuffix .pdf,$(notdir $(CURDIR))))
# LaTeX-Optionen, um unnötiges Generve auszuschalten

TeXOptions = --interaction=interactivemode \
			 --halt-on-error \
			 --output-directory=build \

build/main.pdf: main.tex content/*.tex header.tex | build
	# Optionaler doppelter Aufruf verhindert Darstellungsfehler
	lualatex $(TeXOptions) main.tex
	biber build/main.bcf
	lualatex $(TeXOptions) main.tex
	lualatex $(TeXOptions) main.tex
	cp build/main.pdf $(Filename) # PDF bewegen und umbenennen

build:
	mkdir -p build/

clean:
	rm -f *log # Globales Log löschen
	rm -rf build # Build

.PHONY: all clean
