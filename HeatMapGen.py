import arcpy

radius = 100

inPath = "D:/GD/WGiSR/_Konferencje/Plener 2018/heatMap/HeatMap_knajpy.mxd"
outPath = "D:/GD/WGiSR/_Konferencje/Plener 2018/heatMap/_genMaps"
outFileName = "D:/GD/WGiSR/_Konferencje/Plener 2018/heatMap/_genMaps/HeatMap_radius_" + str(radius) + ".jpg"

mxd = arcpy.mapping.MapDocument(inPath)
df = arcpy.mapping.ListDataFrames(mxd)

for lyr in arcpy.mapping.ListLayers(mxd):
    print lyr

arcpy.mapping.ExportToJPEG(mxd, outFileName)


'''
cellSize = 10
radius = 0
x = 1
while x <= 10:
    print "cellSize: " + str(cellSize)
    print "radius: "+ str(radius)
    cellSize += 10
    radius += 500
    x += 1
'''
