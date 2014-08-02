class Errors():
    """A way to log errors to the system"""
    def __init__(self, folder="."):
        self.file = open(folder+"errors.txt","w")
    def close(self):
        self.file.close()
    def log(self, message):
        print message
        self.file.write(message)