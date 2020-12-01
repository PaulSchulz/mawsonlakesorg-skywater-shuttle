.PHONY: all doc doc-clean clean help

all: \
	gds/sky130-font.gds \
	gds/skywater.gds \
	gds/the-elements.gds \
	gds/war-of-the-worlds.gds

#	gds/babbage.gds \

doc:
	make -C doc

doc-clean:
	-make -C doc clean

help:
	@echo "make  - build gdm files"
	@echo "doc   - build html doc/images"
	@echo "clean - remove intermediate files"

gds/sky130-font.gds: data/sky130-font.txt
	libraries/sky130_pschulz_xx_hd/scripts/text2magic.py \
		-c sky130-font < $< > tcl/sky130-font.tcl
	magic -nocolsole -dnull tcl/sky130-font.tcl

gds/skywater.gds: data/skywater.txt
	libraries/sky130_pschulz_xx_hd/scripts/text2magic.py \
		-c skywater < $< > tcl/skywater.tcl
	magic -nocolsole -dnull tcl/skywater.tcl

gds/babbage.gds: data/babbage.txt
	libraries/sky130_pschulz_xx_hd/scripts/text2magic.py \
		-c babbage < $< > tcl/babbage.tcl
	magic -nocolsole -dnull tcl/babbage.tcl

gds/the-elements.gds: data/the-elements.txt
	libraries/sky130_pschulz_xx_hd/scripts/text2magic.py \
		-c the-elements < $< > tcl/the-elements.tcl
	magic -nocolsole -dnull tcl/the-elements.tcl

gds/war-of-the-worlds.gds: data/war-of-the-worlds.txt
	libraries/sky130_pschulz_xx_hd/scripts/text2magic.py \
		-c war-of-the-worlds < $< > tcl/war-of-the-worlds.tcl
	magic -nocolsole -dnull tcl/war-of-the-worlds.tcl

clean: doc-clean
	-rm tcl/*
	-rm gds/*
