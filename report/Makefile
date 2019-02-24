LATEX    = latex
DVIPS    = dvips

BASENAME = L_Pomega

default: testlatex clean

testlatex1:
	latex  ${BASENAME}
	latex  ${BASENAME}
	dvipdf ${BASENAME}

testlatex:
	latex  ${BASENAME}
	latex  ${BASENAME}
	dvipdf -sPAPERSIZE=a4 -dPDFSETTINGS=/prepress ${BASENAME}

testpdflatex:
	pdflatex  ${BASENAME}
	pdflatex  ${BASENAME}

#
## standard Latex targets
#
#
%.dvi:	%.tex 
	$(LATEX) $<


%.ps:	%.dvi
	$(DVIPS) $< -o $@

%.pdf:	%.tex
	$(PDFLATEX) $<

.PHONY: clean

clean:
	rm -f *.aux *dvi *.log *.out *.nav *.snm *.toc 
	gv L_Pomega.pdf &
