class Errors():
    """A way to log errors to the system"""
    def __init__(self, folder="."):
        self.name = folder+"error.txt"
    def log(self, message):
        print message

        # if the file exists append
        try:
            # if it can't read it means it hasn't been created
            textFile = open(self.name,"r")
            text = textFile.read()
            textFile.close()
            textFile = open(self.name,"w")
            textFile.write(text+"\n"+message)
            textFile.close()
        # else create a new file
        except IOError:
            textFile = open(self.name,"w")
            textFile.write(message)
            textFile.close()
