.PHONY: all clean

OBJS := index.html \
	sky130-font.html \
	skywater.html \
	babbage.html \
	the-elements.html \
	war-of-the-worlds.html \
	open-source-hardware.html

all : $(OBJS)

index.html:
	cp ../../GDS2WebGL/$@ .

sky130-font.html: ../gds/sky130-font.gds
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

open-source-hardware.html: ../gds/open-source-hardware.gds
	python3 ../../GDS2WebGL/gds2webgl.py \
	-i $< -o $@

clean:
	rm *.html
