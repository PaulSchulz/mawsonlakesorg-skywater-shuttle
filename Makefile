.PHONY: doc

doc:
	make -C doc

text:
	libraries/sky130_pschulz_xx_hd/scripts/text2magic.py > magic/test.tcl
