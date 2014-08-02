class Errors():
    """A way to log errors to the system"""
    def __init__(self, folder="."):
        self.name = folder+"error.txt"
    def log(self, message):
        print message
        self.file = open(self.name,"w")
        self.file.write(message)
        self.file.close()