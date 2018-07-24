import arcpy

inTable = "Srem_A2_B2"
field = "naz_glowna"
newField = "naz"

arcpy.AlterField_management(inTable,field,newField)