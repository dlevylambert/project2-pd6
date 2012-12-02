import time

class Logger(object):
    def __init__(self, f, p = False):
       self.f = f
       self.p = p

    def log(self, message, level = "DEBUG"):
        with open(self.f, "a+") as f:
            t = time.strftime("%c", time.localtime())
            m = "[%s] %s %s" %(level, t, message)
            f.write(m + "\n")
            if self.p:
                print(m)
