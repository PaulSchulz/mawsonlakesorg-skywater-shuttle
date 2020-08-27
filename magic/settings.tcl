# Settings
# Import into Magic with
#   source magic/settings.tcl
addpath "libraries/sky130_ml_xx_hd/mag"
addpath "magic"

# Display the current path
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

load master
