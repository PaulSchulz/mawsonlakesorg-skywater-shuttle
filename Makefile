.PHONY: all clean doc doc-clean help

all:
	make -C src
	cp src/*.gds gds/

doc:
	make -C doc

doc-clean:
	-make -C doc clean

help:
	@echo "make       - build gdm files"
	@echo "clean      - remove intermediate files"
	@echo "doc        - build html doc/images"
	@echo "doc-clean  - clean doc directory"
