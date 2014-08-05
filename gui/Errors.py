class Errors():
    """A way to log errors to the system"""
    def __init__(self):
        self.file = open("errors.txt","w")
    def close(self):
        self.file.close()
    def log(self, message):
        print message
        self.file.write(message)