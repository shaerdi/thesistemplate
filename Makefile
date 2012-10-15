FILE = thesis

all: build

build:
	pdflatex $(FILE)
	bibtex $(FILE)
	pdflatex $(FILE).tex
	pdflatex $(FILE).tex

clean:
	@echo -e "\033[1mCleaning up...\033[0m"
	@rm -f *.{blg,bbl,toc,out,log,aux,dvi,snm,nav,ps,brf,synctex.gz}
	@rm -f *~

fast:
	pdflatex $(FILE).tex
