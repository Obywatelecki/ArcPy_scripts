import HeatMapGen

#Tool variables
radius = 50
cellSize = 150
tempLyr_hypso = "D:/GD/WGiSR/_Konferencje/Plener 2018/heatMap/kd_temp_hypso.lyr"
knajpy = "knajpy"

i = 1
while i <= 3:
    print "Processing " + str(i) + " iteration..."
    HeatMapGen.heatMapGen(radius,cellSize, tempLyr_hypso, knajpy)
    radius += 50
    i+=1
    print "End of " + str(i) + " iteration..."