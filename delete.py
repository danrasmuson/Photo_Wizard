import os  

# haveFiles = []
for fn in os.listdir('photos'):
    # haveFiles.append(fn)
    # os.rename(fn, fn[1:]) #rename
    # os.remove(filePath) #delete
    # os.system('command to execute')
    print("images/study_at_yale/wines/"+fn)

# textFile = open("wineNames.txt","r")
# lines = textFile.readlines()
# textFile.close()

# # print "\n\n"
# # print "done!"
# # print "\n\n"

# import re
# wantedFiles = []
# for line in lines:
#     line = re.sub(r"\W|_"," ", line)
#     line = line.replace("  "," ")
#     # line = line.replace("  "," ")
#     line = line.strip(" ")
#     print line+".jpg"


# # nameList = sorted(nameList)

# # for i in range(len(wantedFiles)):
#     # wantedFiles[i]
# # for name in sorted(nameList):
#     # print name