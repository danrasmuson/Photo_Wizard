import os
import sys
import time
from urllib import FancyURLopener
import urllib2
import simplejson
import re
# from Errors import Errors
#todo add support for dimensions
#todo add support for refreshing image or choosing image
#todo add controller for log file

def getImageForTerm(searchTerm, minHeight=300, minWidth=300):
    # remove special chrs
    searchTerm = re.sub(r'\W|_', ' ', searchTerm) #searchTerm.replace(' ','%20')

    # Start FancyURLopener with defined version 
    class MyOpener(FancyURLopener): 
        version = 'Mozilla/5.0 (Windows; U; Windows NT 5.1; it; rv:1.8.1.11) Gecko/20071127 Firefox/2.0.0.11'
    myopener = MyOpener()

    # Replace spaces ' ' in search term for '%20' in order to comply with request
    webSearchTerm = searchTerm.replace(' ','%20')
    # Notice that the start changes for each iteration in order to request a new set of images for each loop
    url = ('https://ajax.googleapis.com/ajax/services/search/images?' + 'v=1.0&q='+webSearchTerm+'&start='+str(0)+'&userip=MyIP')
    # print url
    request = urllib2.Request(url, None, {'Referer': 'testing'})
    response = urllib2.urlopen(request)

    # Get results using JSON
    results = simplejson.load(response)
    data = results['responseData']
    dataInfo = data['results']

    #todo - add photos to folder
    #TODO - error handleing for if filename already exist - just overwrites at moment
    if len(dataInfo) >= 1:
        for image in dataInfo:
            height = image["height"]
            width = image["width"]
            if minHeight < int(height) and minWidth < int(width):
                savePath = "photos\\"+searchTerm+'.jpg'
                myopener.retrieve(image['unescapedUrl'], "static\\"+savePath)
                return savePath
        # else:
            # error.log("No Valid Sizes for Query: "+searchTerm+". Height: "+str(height)+" Width: "+str(width))
    # else:
        # error.log("No Results for Query: "+searchTerm)


        # Sleep for one second to prevent IP blocking from Google
    time.sleep(1)