#!/usr/bin/python
import urllib2
from lxml import etree as ET
import cgi

wbURL = "http://www.google.com/ig/api?weather="

def toAngel(zipcode):
    weatherdata = urllib2.urlopen(wbURL + zipcode) 
    weather = ET.parse(weatherdata).find('weather')
    condition = weather.find('current_conditions').find('condition').get('data')
    curtemp = weather.find('current_conditions').find('temp_f').get('data')
    return condition + ", with a temperature of " + curtemp + " degrees."

print "Content-Type: text/html"
print
inputs = cgi.FieldStorage()
z = inputs['zipcode'].value
print toAngel(z)

