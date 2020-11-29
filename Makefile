.PHONY: all doc \
	text-skywater \
	text-babbage \
	text-the-elements \
	text-war-of-the-worlds

all: \
	text-skywater \
	text-babbage \
	text-the-elements \
	text-war-of-the-worlds

doc:
	make -C doc

text:
	@echo "Build text output with 'make text-<filename>'"

text-skywater: data/skywater.txt
	libraries/sky130_pschulz_xx_hd/scripts/text2magic.py \
		< data/skywater.txt \
		> tcl/skywater.tcl

text-babbage: data/babbage.txt
	libraries/sky130_pschulz_xx_hd/scripts/text2magic.py \
		< data/babbage.txt \
		> tcl/babbage.tcl

text-the-elements: data/the-elements.txt
	libraries/sky130_pschulz_xx_hd/scripts/text2magic.py \
		< data/the-elements.txt \
		> tcl/the-elements.tcl

text-war-of-the-worlds: data/war-of-the-worlds.txt
	libraries/sky130_pschulz_xx_hd/scripts/text2magic.py \
		< data/war-of-the-worlds.txt \
		> tcl/war-of-the-worlds.tcl
