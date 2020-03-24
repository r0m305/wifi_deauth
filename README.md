        ▖  ▖ ▝   ▗▀  ▝       ▗▖     ▗▄▄     ▗▄▖              ▗  ▐
        ▌▐ ▌▗▄  ▗▟▄ ▗▄       ▐▌     ▐ ▝▌    ▐ ▝▖ ▄▖  ▄▖ ▗ ▗ ▗▟▄ ▐▗▖
        ▘▛▌▌ ▐   ▐   ▐       ▌▐     ▐▄▟▘    ▐  ▌▐▘▐ ▝ ▐ ▐ ▐  ▐  ▐▘▐
        ▐▌█▘ ▐   ▐   ▐       ▙▟     ▐       ▐  ▌▐▀▀ ▗▀▜ ▐ ▐  ▐  ▐ ▐
        ▐ ▐ ▗▟▄  ▐  ▗▟▄     ▐  ▌ ▐  ▐       ▐▄▞ ▝▙▞ ▝▄▜ ▝▄▜  ▝▄ ▐ ▐ 
Scan wireless networks for active hosts and deauthenticate users from the wireless network

Usage: wifi_deauth.py [options]

[+] Written by Romeos CyberGypsy
Contact:
        Email:  lewiswaigwa30@gmail.com
        Telegram: https://t.me/Romeos_CyberGypsy
        Facebook: Romeos CyberGypsy


Options:
  -h, --help            show this help message and exit
  --scan                Specify you want to scan a network
  --deauth              Specify you want to deauthenticate users from the
                        network
  --target-cidr=TARGET  Target CIDR to scan
  --gateway=GATEWAY     Target MAC Address of gateway from which to
                        deauthenticate  users
  --interface=INTERFACE
                        Interface to throw packets e.g wlan0mon
  --packets=PACKETS     Number of packets to throw per thread
  --loop=LOOP           Number of times to repeat the attack

EXAMPLE USAGES:
To scan a network for active hosts alongside their MAC Addresses, do as follows:
  python3 wifi_deauth.py --scan --target-cidr=192.168.43.0/24


To deauthenticate users from a network that you are connected, do as follows:
  python3 wifi_deauth.py --deauth --target-cidr=192.168.43.0/24 --gateway=e3:99:bc:56:10:a2 --interface=wlan0mon --packets=10 --loop=10

  NOTE:
  1. To use this script, you must be connected to the same network
  2. Your network interface should be in monitor mode. This can be done as follows:
      airmon-ng start wlan0
      where wlan0 represents your intended network interface
  3. This script is for educational purposes only
