#!/usr/bin/python
import cgi
import getUser

# Gets the destination address, functionally similar to 9100 so see that for explanation

def idToInfo(number):
    num, user = getUser.get(number)
    info = {}
    return {'id' : num, 'addresses' : user['addresses']}
def toAngelXML(info):
    xmlstring = """<ANGELXML><QUESTION var="destination"><PLAY>"""
    xmlstring += "<PROMPT type=\"externalaudio\">http://dl.dropbox.com/u/1593539/Audio/92002.wav"
    xmlstring += """</PROMPT></PLAY><RESPONSE><KEYWORD>\n"""
    for a in info['addresses']:
        xmlstring += '<LINK keyword="' + a + '" returnValue="' + a + '" destination="/9300" />\n'
    xmlstring += '<LINK keyword="list" returnValue="list" destination="/1110" />\n' 
    xmlstring += '<LINK keyword="help" returnValue="list" destination="/1110" />\n'
    xmlstring += """</KEYWORD></RESPONSE><ERROR_STRATEGY type="noinput"> 
            <PROMPT type="externalaudio">http://dl.dropbox.com/u/1593539/Audio/92003.wav</PROMPT>
            <PROMPT type="externalaudio">http://dl.dropbox.com/u/1593539/Audio/92004.wav</PROMPT><GOTO destination="/1110" /></ERROR_STRATEGY><ERROR_STRATEGY type="nomatch"> 
            <PROMPT type="externalaudio">http://dl.dropbox.com/u/1593539/Audio/92005.wav</PROMPT>
            <PROMPT type="externalaudio">http://dl.dropbox.com/u/1593539/Audio/92006.wav</PROMPT><GOTO destination="/1110" /></ERROR_STRATEGY></QUESTION></ANGELXML>"""
    return xmlstring

print "Content-Type: text/html"     # HTML is following
print                               # blank line, end of headers
inputs = cgi.FieldStorage()
if "number" not in inputs:
    num = "1111111111"
else:
    num = inputs["number"].value
print toAngelXML(idToInfo(num))


