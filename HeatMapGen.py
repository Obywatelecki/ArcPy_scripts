import arcpy

database = "D:/GD/WGiSR/_Konferencje/Plener 2018/heatMap/data.gdb"
arcpy.env.workspace = database
arcpy.env.OverwriteOutput = 1

radius = 100
inPath = "D:/GD/WGiSR/_Konferencje/Plener 2018/heatMap/HeatMap_knajpy.mxd"
outPath = "D:/GD/WGiSR/_Konferencje/Plener 2018/heatMap/_genMaps"
outKDName = str(database) + str(radius)
outMapName = "D:/GD/WGiSR/_Konferencje/Plener 2018/heatMap/_genMaps/HeatMap_radius_" + str(radius) + ".jpg"
mxd = arcpy.mapping.MapDocument(inPath)
df = arcpy.mapping.ListDataFrames(mxd)[0]

##Kernel Density variables
inFeatures = "knajpy"
popField = "NONE"
cellSize = 30

arcpy.CheckOutExtension("Spatial")

kd = arcpy.sa.KernelDensity(inFeatures,
                            popField,
                            cellSize,
                            radius,
                                          "SQUARE_KILOMETERS")

kd.save(database+ "//" + "kd_test")
arcpy.BuildPyramids_management("kd_test")
arcpy.mapping.AddLayer(df, "kd_test", "BOTTOM")

for lyr in arcpy.mapping.ListLayers(mxd):
    print lyr

##TO DO

'''

addLayer
setSymbology
exportMap

makeItLooped :-)

'''


'''
for lyr in arcpy.mapping.ListLayers(mxd):
    print lyr

arcpy.mapping.ExportToJPEG(mxd, outFileName)


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
