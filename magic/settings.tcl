# Settings
# Import into Magic with
#   source magic/settings.tcl
addpath "lib/font-sky130"
addpath "magic"
path

grid on
grid 50nm
snap grid

box width 150nm
box height 150nm
box position 0 0
view
findbox zoom
zoom 10

getcell master
