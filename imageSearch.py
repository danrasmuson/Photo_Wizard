import os
import sys
import time
from urllib import FancyURLopener
import urllib2
import simplejson
import re

#todo add support for dimensions
#todo add support for refreshing image or choosing image
#todo add controller for log file
class Errors(object):
    """A way to log errors to the system"""
    def __init__(self):
        self.file = open("errors.txt","w")
    def close(self):
        self.file.close()
    def log(self, message):
        print message
        self.file.write(message)

        
        

def getImagesForTerm(searchTerm, numberOfImages):
    # Replace spaces ' ' in search term for '%20' in order to comply with request


    # Start FancyURLopener with defined version 
    class MyOpener(FancyURLopener): 
        version = 'Mozilla/5.0 (Windows; U; Windows NT 5.1; it; rv:1.8.1.11) Gecko/20071127 Firefox/2.0.0.11'
    myopener = MyOpener()

    # remove non letters and numbers
    searchTerm = re.sub(r'\W|_', ' ', searchTerm) #searchTerm.replace(' ','%20')

    webSearchTerm = searchTerm.replace(' ','%20')
    print webSearchTerm
    # Notice that the start changes for each iteration in order to request a new set of images for each loop
    url = ('https://ajax.googleapis.com/ajax/services/search/images?' + 'v=1.0&q='+webSearchTerm+'&start='+str(numberOfImages)+'&userip=MyIP')
    # print url
    request = urllib2.Request(url, None, {'Referer': 'testing'})
    response = urllib2.urlopen(request)

    # Get results using JSON
    results = simplejson.load(response)
    data = results['responseData']
    dataInfo = data['results']

    #just nameing the file the same as the search term
    saveFileName = searchTerm.replace(" ","_")
    saveFileName = searchTerm.replace("__","_")
    saveFileName = searchTerm.strip("_")

    if len(dataInfo) >= numberOfImages:
        for i in range(numberOfImages):
            #todo - add photos to folder
            #TODO - error handleing for if filename already exist - just overwrites at moment
            myopener.retrieve(dataInfo[i]['unescapedUrl'], "photos/"+saveFileName+'.jpg')
    else:
        error.log("No Results for Query: "+saveFileName)


        # Sleep for one second to prevent IP blocking from Google
    time.sleep(1)

def getQueries(path):
    textFile = open(path,"r")
    queries = textFile.readlines()
    textFile.close()
    return queries

error = Errors()

for query in getQueries("wineNames.txt"): 
    getImagesForTerm(query, 1)

# getImagesForTerm("10293020idlfsdjfl34", 1)

error.close()