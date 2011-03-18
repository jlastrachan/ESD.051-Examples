#!/usr/bin/python
import cgi
import getUser

# this module dynamically creates and AngelXML page to ask the user for their source address.
# It's dynamic because we have to create the list of accepted responses based on the names
# of addresses they've saved in the database.

def idToInfo(number):
    # gets user info from db, same as 9000
    num, user = getUser.get(number)
    info = {}
    return {'id' : num, 'addresses' : user['addresses']}

def toAngelXML(info):
    # uses user info and saved addresses to dynamically create a page in AngelXML that asks the user
    # for a source address and dynamically populates the list of acceptable keywords responses based
    # on their saved addresses from the database.
    xmlstring = """<ANGELXML><QUESTION var="source"><PLAY><PROMPT type=\"externalaudio\">"""
    xmlstring += "http://dl.dropbox.com/u/1593539/Audio/91001.wav"
    xmlstring += """</PROMPT></PLAY><RESPONSE><KEYWORD>\n"""
    # This adds an accepted response for each address they've saved
    for a in info['addresses']:
        xmlstring += '<LINK keyword="' + a + '" returnValue="' + a + '" destination="/9200" />\n'
    # This adds two default resonses, list and help
    xmlstring += '<LINK keyword="list" returnValue="list" destination="/1110" />\n'
    xmlstring += '<LINK keyword="help" returnValue="list" destination="/1110" />\n'
    # The next part defines two noinput and nomatch prompts to be played in the event of any problems
    xmlstring += """</KEYWORD></RESPONSE><ERROR_STRATEGY type="noinput"> 
            <PROMPT type="externalaudio">http://dl.dropbox.com/u/1593539/Audio/91002.wav</PROMPT>
            <PROMPT type="externalaudio">http://dl.dropbox.com/u/1593539/Audio/91003.wav</PROMPT>
            <GOTO destination="/1110" />
        </ERROR_STRATEGY><ERROR_STRATEGY type="nomatch"> 
            <PROMPT type="externalaudio">http://dl.dropbox.com/u/1593539/Audio/91004.wav</PROMPT>
            <PROMPT type="externalaudio">http://dl.dropbox.com/u/1593539/Audio/91005.wav</PROMPT>
            <GOTO destination="/1110" /></ERROR_STRATEGY></QUESTION></ANGELXML>"""
    return xmlstring

# see 9000 for explanation

print "Content-Type: text/html"     # HTML is following
print                               # blank line, end of headers
inputs = cgi.FieldStorage()
if "number" not in inputs:
    num = "1111111111"
else:
    num = inputs["number"].value
print toAngelXML(idToInfo(num))
