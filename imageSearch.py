import os
import sys
import time
from urllib import FancyURLopener
import urllib2
import simplejson

def getImagesForTerm(searchTerm, numberOfImages):
    # Replace spaces ' ' in search term for '%20' in order to comply with request
    searchTerm = searchTerm.replace(' ','%20')


    # Start FancyURLopener with defined version 
    class MyOpener(FancyURLopener): 
        version = 'Mozilla/5.0 (Windows; U; Windows NT 5.1; it; rv:1.8.1.11) Gecko/20071127 Firefox/2.0.0.11'
    myopener = MyOpener()

    # Set count to 0
    # count= 0

    # for i in range(0,numberOfImages):
    # Notice that the start changes for each iteration in order to request a new set of images for each loop
    url = ('https://ajax.googleapis.com/ajax/services/search/images?' + 'v=1.0&q='+searchTerm+'&start='+str(numberOfImages)+'&userip=MyIP')
    # print url
    request = urllib2.Request(url, None, {'Referer': 'testing'})
    response = urllib2.urlopen(request)

    # Get results using JSON
    results = simplejson.load(response)
    data = results['responseData']
    dataInfo = data['results']

    # print "\nstarting loop\n"

    # Iterate for each result and get unescaped url
    # for myUrl in dataInfo:
    # count = count + 1
    # print myUrl['unescapedUrl']

    #just nameing the file the same as the search term
    # myopener.retrieve(dataInfo[0]['unescapedUrl'],str(count)+'.jpg')
    for i in range(numberOfImages):
        myopener.retrieve(dataInfo[i]['unescapedUrl'], "test"+'.jpg')


        # Sleep for one second to prevent IP blocking from Google
    time.sleep(1)

getImagesForTerm("hello world", 1)