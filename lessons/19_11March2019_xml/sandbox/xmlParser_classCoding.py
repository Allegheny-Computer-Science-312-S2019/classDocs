#!/usr/bin/env python3

from xml.dom import minidom


def begin(xmldoc):
    """The parser and driver function for the program"""
    kml = xmldoc.getElementsByTagName("kml")[0]
    document = kml.getElementsByTagName("Document")[0]
    placemarks = kml.getElementsByTagName("Placemark")

    for placemark in placemarks:
        print("Current placemark :",placemark)
        print(" ____ New record ____ ")
        desc = placemark.getElementsByTagName("description")[0].firstChild.nodeValue
        name = placemark.getElementsByTagName("name")[0].firstChild.nodeValue
        print(" desc :",desc)
        print(" name :", name)
    #end of begin()



print("Hello! This is my XML parser!")

fileName = "cityData.xml"
xmldoc = minidom.parse(fileName) # load and parse the data file
print("xmlDoc :", xmldoc)

# run the program
begin(xmldoc) #driver function
