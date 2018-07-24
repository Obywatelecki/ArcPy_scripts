import HeatMapGen

# Tool variables
radius = 100
cellSize = 50

i = 1
while i <= 40:
    print "Processing " + str(i) + " iteration..."
    HeatMapGen.heatMapGen(radius, cellSize)
    radius += 100
    i += 1
    print "End of " + str(i) + " iteration..."
