#!/usr/bin/env python3

DATE = "11 March 2019"
VERSION = "1"
AUTHOR = "Oliver Bonham-Carter"

# This is demo code to extract information from xml tree. This code has been hard coded to work with cityData.xml. A similar method could be used for any xml document.

from xml.dom import minidom

def begin(xmldoc):
    """ driver function of this program"""

    kml = xmldoc.getElementsByTagName("kml")[0]
    # note: KML is a file format used to display geographic data in an Earth browser such as Google Earth.
    document = kml.getElementsByTagName("Document")[0]
    placemarks = document.getElementsByTagName("Placemark")

    for placemark in placemarks:
        print("\n <---+ New record +---------------------> ")
    #    print  placemark
        desc = placemark.getElementsByTagName("description")[0].firstChild.nodeValue
        name = placemark.getElementsByTagName("name")[0].firstChild.nodeValue
    #    point = placemark.getElementsByTagName("Point")[0].firstChild.nodeValue
        coords = placemark.getElementsByTagName("coordinates")[0].firstChild.nodeValue
        line_list = coords.split(",")
        long_list = line_list[0]
        lat_list =  line_list[1]
        print("  Desc      : ", desc)
        print("  Name      : ", name)
    #    print("  Point    : ", point)
        print("  Coords    : ", coords)
        print("  Latitude  : ", lat_list)
        print("  Longitude : ", long_list)

#end of begin()

###########################################################
#load the file
xmldoc = minidom.parse("cityData.xml") # load the data file
#print xmldoc


# run the program!
begin(xmldoc)
