.PHONY: all clean

all: font-sky130.html \
	open-source-hardware.html \
	mawsonlakes-org.html

font-sky130.html: ../gds/font-sky130.gds
	python3 ../../GDS2WebGL/gds2webgl.py \
	-i $< -o $@

open-source-hardware.html: ../gds/open-source-hardware.gds
	python3 ../../GDS2WebGL/gds2webgl.py \
	-i $< -o $@

mawsonlakes-org.html: ../gds/mawsonlakes-org.gds
	python3 ../../GDS2WebGL/gds2webgl.py \
	-i $< -o $@

clean:
	rm font-sky130.html \
	  open-source-hardware.html \
      mawsonlakes-org.html
