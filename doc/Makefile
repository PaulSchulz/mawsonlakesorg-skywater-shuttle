.PHONY: all clean

all: font-sky130.html \
	open-source-hardware.html \
	mawsonlakes-org.html \
	skywater.html \
	babbage.html \
	the-elements.html \
	war-of-the-worlds.html

font-sky130.html: ../gds/font-sky130.gds
	python3 ../../GDS2WebGL/gds2webgl.py \
	-i $< -o $@

open-source-hardware.html: ../gds/open-source-hardware.gds
	python3 ../../GDS2WebGL/gds2webgl.py \
	-i $< -o $@

mawsonlakes-org.html: ../gds/mawsonlakes-org.gds
	python3 ../../GDS2WebGL/gds2webgl.py \
	-i $< -o $@

skywater.html: ../gds/skywater.gds
	python3 ../../GDS2WebGL/gds2webgl.py \
	-i $< -o $@

babbage.html: ../gds/babbage.gds
	python3 ../../GDS2WebGL/gds2webgl.py \
	-i $< -o $@

the-elements.html: ../gds/the-elements.gds
	python3 ../../GDS2WebGL/gds2webgl.py \
	-i $< -o $@

war-of-the-worlds.html: ../gds/war-of-the-worlds.gds
	python3 ../../GDS2WebGL/gds2webgl.py \
	-i $< -o $@


clean:
	rm *.html
