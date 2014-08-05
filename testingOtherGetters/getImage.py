import urllib
def downloadImage(url, saveName):
	urllib.urlretrieve(url, saveName)
downloadImage("http://www.gunnerkrigg.com//comics/00000001.jpg", "00000001.jpg")