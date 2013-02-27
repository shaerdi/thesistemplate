FILE = thesis
SHELL=/bin/bash
OUTPUTNAME = Masterarbeit_shaerdi

all: build

build:
	sed -i 's/oe;/ö/g; s/ae;/ä/g; s/ue;/ü/g' Chapters/*
	sed -i 's/Oe;/Ö/g; s/Ae;/Ä/g; s/Ue;/Ü/g' Chapters/*
	pdflatex -jobname=$(OUTPUTNAME) $(FILE).tex
	bibtex $(OUTPUTNAME)
	makeindex $(OUTPUTNAME).nlo -s nomencl.ist -o $(OUTPUTNAME).nls
	pdflatex -jobname=$(OUTPUTNAME) $(FILE).tex
	pdflatex -jobname=$(OUTPUTNAME) $(FILE).tex 

clean:
	@echo -e "\033[1mCleaning up...\033[0m"
	@rm -f *.{blg,bbl,toc,out,log,aux,dvi,snm,nav,ps,brf,synctex.gz}
	@rm -f *~

fast:
	pdflatex -jobname=$(OUTPUTNAME) $(FILE).tex
