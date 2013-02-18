FILE = thesis
SHELL=/bin/bash
OUTPUTNAME = thesis

all: build

build:
	pdflatex -jobname=$(OUTPUTNAME) $(FILE).tex
	bibtex $(FILE)
	pdflatex -jobname=$(OUTPUTNAME) $(FILE).tex
	pdflatex -jobname=$(OUTPUTNAME) $(FILE).tex 

clean:
	@echo -e "\033[1mCleaning up...\033[0m"
	@rm -f *.{blg,bbl,toc,out,log,aux,dvi,snm,nav,ps,brf,synctex.gz}
	@rm -f *~

fast:
	pdflatex -jobname=$(OUTPUTNAME) $(FILE).tex
