# This module is rather boring. We're simulating a nosql database using a dictionary.
# This is a good example of stubbing, though, since we put this in an external module
# in comparison to all the modules that require user info. This means that conceivably,
# if we were to connect this to an actual database, the rest of our code would remain
# (largely) unchanged. Go Modular Design!

def get(userID):
    if userID in users:
        return userID, users[userID]
    else:
        return '1111111111', users['1111111111']

users = {
        "2012475876" : {
            "name" : "Anthony",
            "addresses" : ["home", "work", "girlfriend"],
            "trips" : [ 
                { 
                    "source" : "girlfriend",
                    "destination" : "home",
                    "title" : "Route 17 to Route 4",
                    "map" : "http://goo.gl/maps/cUup"
                }, { 
                    "source" : "girlfriend",
                    "destination" : "home",
                    "title" : "Oradell Ave to Kinderkamack Rd to Route 4",
                    "map" : "http://goo.gl/maps/PPmJ"
                }, { 
                    "source" : "girlfriend",
                    "destination" : "home",
                    "title" : "Backroads to the Palisades",
                    "map" : "http://goo.gl/maps/PPmJ"
                } 
            ]
        }, "1111111111" : {
            "name" : "Demo",
            "addresses" : ["port authority", "south station"],
            "trips" : [ 
                { 
                    "source" : "port authority",
                    "destination" : "south station",
                    "title" : "I 95 all the way",
                    "map" : "http://goo.gl/maps/Cxpu"
                }, { 
                    "source" : "port authority",
                    "destination" : "south station",
                    "title" : "I 95 to I 90",
                    "map" : "http://goo.gl/maps/fVl7"
                }, { 
                    "source" : "port authority",
                    "destination" : "south station",
                    "title" : "Connecticut Route 15 to I 90",
                    "map" : "http://goo.gl/maps/Yz1p"
                }, { 
                    "source" : "south station",
                    "destination" : "port authority",
                    "map" : "http://goo.gl/maps/BHB9"
                }
            ]
}
}
