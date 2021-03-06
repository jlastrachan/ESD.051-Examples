#!/usr/bin/python
import cgi
import getUser

# purpose of this module is to accept caller id from angel and then hit the database
# to see if they're a registered user. If not, it assigned them 1111111111 as a number,
# which is the corresponding id for the demo account in the database. That way, they can
# demo the application without being registered.

def numToInfo(number):
    info = {}
    userid, user = getUser.get(number)
    # queries the database for the user object (MongoDB database)
    info = {'name' : user['name'], 'id' : userid, "addresses" : user['addresses']}
    info['demo'] = user['name'] == 'Demo'
    return info
    
def toAngelXML(info):
    # converts the data stored in info (a dictionary) into AngelXML that either plays nothing or
    # plays a demo prompt (if the user has been connected to the demo account), and then assigns two
    # variables. The first is 'number', which is the same as the callerID. The second is 'addresses', a list
    # of the user'd saved addresses
    demo = '<PROMPT type=\"text\">.</PROMPT>'
    if info['demo']:
        demo = '<PROMPT type="externalaudio">http://dl.dropbox.com/u/1593539/Audio/9000_Demo.wav</PROMPT>'
    xmlstring = """<ANGELXML><MESSAGE><PLAY>"""
    xmlstring += demo + """</PLAY>\n"""
    xmlstring += '<GOTO destination="/1000" />'
    xmlstring += """</MESSAGE><VARIABLES><VAR name=\"name\" value="""
    xmlstring += '"' + info['name'] + '"' + """/> 
        <VAR name="number" value="""
    xmlstring += '"' + info['id'] + '"' + """/> 
        <VAR name="addresses" value=""" + '"'
    for a in range(len(info['addresses'])):
        xmlstring += info['addresses'][a]
        if a < len(info['addresses']) - 1:
            xmlstring += ', '
    xmlstring += '" type="list" separator=","/>\n' + """</VARIABLES></ANGELXML>"""
    return xmlstring

# This next part will be consistent for all Angel responses - it defines the content type,
# adds a blank line to signify the end of the header, and then uses the cgi library to pull
# inputted url parameters into python

print "Content-Type: text/html"     # HTML is following
print                               # blank line, end of headers
inputs = cgi.FieldStorage()
if "number" not in inputs:
    num = "1111111111"
else:
    num = inputs["number"].value
print toAngelXML(numToInfo(num))


