import time

print "Importing Arcpy...." + str(time.ctime())
import arcpy
print "         Arcpy imported! " + str(time.ctime())


def heatMapGen(radius, cellSize):
    print "Setting database and workspace..." + str(time.ctime())
    arcpy.env.workspace = "D:/GD/WGiSR/_Konferencje/Plener 2018/heatMap/data.gdb"
    print "         Database and workspace set! " + str(time.ctime())

    print "Setting local variables..." + str(time.ctime())
    mxd = arcpy.mapping.MapDocument("D:/GD/WGiSR/_Konferencje/Plener 2018/heatMap/HeatMap.mxd")
    df = arcpy.mapping.ListDataFrames(mxd)[0]
    template = "D:/GD/WGiSR/_Konferencje/Plener 2018/heatMap/kd_temp_hypso.lyr"
    inData = "OSM_STOPS_2180"
    print "         Local variables set! " + str(time.ctime())

    print "     Generating Heat Map..." + str(time.ctime())
    arcpy.Delete_management("kd")
    arcpy.CheckOutExtension("Spatial")
    kd = arcpy.sa.KernelDensity(inData,
                                "NONE",
                                cellSize,
                                radius,
                                "SQUARE_KILOMETERS")
    kd.save("kd")
    arcpy.BuildPyramids_management("kd")
    arcpy.MakeRasterLayer_management("kd")
    layer = arcpy.mapping.Layer("kd")
    tempLyr = arcpy.mapping.Layer(template)
    arcpy.ApplySymbologyFromLayer_management(layer, tempLyr)
    arcpy.mapping.AddLayer(df, layer)
    mxd.save()
    print "             Heat Map generated! " + str(time.ctime())

    print "     Exporting map..." + str(time.ctime())
    arcpy.mapping.ExportToJPEG(mxd, "D:/GD/WGiSR/_Konferencje/Plener 2018/heatMap/_genMaps/HeatMap_radius_" + str(
        radius) + ".jpg")
    print "             Map exported! " + str(time.ctime())
