import time

print "Importing Arcpy...." + str(time.ctime())
import arcpy
print "         Arcpy imported! " + str(time.ctime())

print "Setting local variables" + str(time.ctime())
arcpy.env.workspace = "D:/GD/IHPAN/Gaul/_Mapy/_metaarkusze/data.gdb"
# mxd = arcpy.mapping.MapDocument("D:/GD/WGiSR/_Konferencje/Plener 2018/heatMap/HeatMap.mxd")
# df = arcpy.mapping.ListDataFrames(mxd)[0]
print "         Local variables set!" + str(time.ctime())

print "Clipping..."  + str(time.ctime())
arcpy.Clip_management(
    r"GAUL_RASTER\Babimost_A2_B2_meta.tif",
    "265690.022579334 444111.323305845 333117.820225502 527358.613670745",
    "D:\GD\IHPAN\Gaul\_Mapy\_metaarkusze\data.gdb\Babimost_clip",
    r"GAUL_MASKS\POWIAT_Babimost",
    256,
    "ClippingGeometry",
    "MAINTAIN_EXTENT")
arcpy.Clip_management(
    r"GAUL_RASTER\Poznan_A1-B2_meta.tif",
    "299400.899102051 470779.676501803 382321.502278291 540453.896805332",
    "D:\GD\IHPAN\Gaul\_Mapy\_metaarkusze\data.gdb\Poznan_clip",
    r"GAUL_MASKS\POWIAT_Poznań",
    256,
    "ClippingGeometry",
    "MAINTAIN_EXTENT")
arcpy.Clip_management(
    r"GAUL_RASTER\Srem_A2-B2_meta.tif",
    "335720.040082338 441921.717819948 400351.860474886 515204.67834739",
    "D:\GD\IHPAN\Gaul\_Mapy\_metaarkusze\data.gdb\Srem_clip",
    r"GAUL_MASKS\POWIAT_Śrem",
    256,
    "ClippingGeometry",
    "MAINTAIN_EXTENT")
arcpy.Clip_management(
    r"GAUL_RASTER\Miedzyrzecz_A2-B2_meta.tif",
    "231042.34059775 485283.89837235 332281.278737942 559072.743229139",
    "D:\GD\IHPAN\Gaul\_Mapy\_metaarkusze\data.gdb\Miedzyrzecz_clip",
    r"GAUL_MASKS\POWIAT_Międzyrzecz",
    256,
    "ClippingGeometry",
    "MAINTAIN_EXTENT")
arcpy.Clip_management(
    r"GAUL_RASTER\Wschowa_A2-B2_meta.tif",
    "277331.797332692 411648.690308725 359810.429110255 482980.143615188",
    "D:\GD\IHPAN\Gaul\_Mapy\_metaarkusze\data.gdb\Wschowa_clip",
    r"GAUL_MASKS\POWIAT_Wschowa",
    256,
    "ClippingGeometry",
    "MAINTAIN_EXTENT")
arcpy.Clip_management(
    r"GAUL_RASTER\Krobia_A1_meta.tif",
    "325559.668889663 387037.86742851 395016.309742185 470321.802898691",
    "D:\GD\IHPAN\Gaul\_Mapy\_metaarkusze\data.gdb\Krobia_clip",
    r"GAUL_MASKS\POWIAT_Krobia",
    256,
    "ClippingGeometry",
    "MAINTAIN_EXTENT")
arcpy.Clip_management(
    r"GAUL_RASTER\Oborniki_A1-B2_meta.tif",
    "289538.110717687 498943.938028237 379936.142480935 573069.735483128",
    "D:\GD\IHPAN\Gaul\_Mapy\_metaarkusze\data.gdb\Oborniki_clip",
    r"GAUL_MASKS\POWIAT_Oborniki",
    256,
    "ClippingGeometry",
    "MAINTAIN_EXTENT")
arcpy.Clip_management(
    r"GAUL_RASTER\Koscian_A2-B2_meta.tif",
    "302944.357398094 432303.434413203 369814.26984427 507153.17713879",
    "D:\GD\IHPAN\Gaul\_Mapy\_metaarkusze\data.gdb\Koscian_clip",
    r"GAUL_MASKS\POWIAT_Kościan",
    256,
    "ClippingGeometry",
    "MAINTAIN_EXTENT")
print "     Clipped!" + str(time.ctime())

print "Mosaicking rasters...." + str(time.ctime())

arcpy.MosaicToNewRaster_management(
    "Babimost_clip; Koscian_clip; Oborniki_clip; Krobia_Clip; Wschowa_clip; Miedzyrzecz_clip; Srem_clip; Poznan_clip",
    r"D:/GD/IHPAN/Gaul/_Mapy/_metaarkusze/data.gdb",
    "GAUL_mosaicked",
    "",
    "8_BIT_UNSIGNED",
    "",
    3,
    "FIRST",
    "FIRST"
)
print "     Rasters mosaicked!" + str(time.ctime())



