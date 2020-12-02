.PHONY : all install clean

OBJS := \
	sky130-font.gds \
	skywater.gds \
	the-elements.gds \
	war-of-the-worlds.gds \
	babbage.gds

all : $(OBJS)

%.tcl : %.txt
	../libraries/sky130_pschulz_xx_hd/scripts/text2magic.py \
		-c $* -l ../libraries < $< > $@

%.gds : %.tcl
	magic -nocolsole -dnull $<
