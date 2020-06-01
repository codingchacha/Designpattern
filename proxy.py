""" Started a finncial company  and you wanted to restrict  certain website 
in your organisation like , gmail , utube , twitter , facebook e.t.c
create a design to handle this"""

class Internet:
    def connect(self , host):
        print("conntecting to " + host)


class Proxy:
    def __init__(self):
        self.internet = Internet()
        self.banned_sites = {"www.gmail.com" , "www.youtube.com" , "www.facebook.com" , "www.twitter.com"}
    def connect(self , host):
        if host in self.banned_sites:
            print("This Site is unauthorized to access")
            return
        self.internet.connect(host)
class Employee:
    def connect_to_web(self , host):
        inter = Proxy()
        inter.connect(host)
emp = Employee()
emp.connect_to_web("www.facebook.com")
emp.connect_to_web("www.educative.com")
emp.connect_to_web("www.facebook.com")
# your code goes here