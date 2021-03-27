import os
import colorama
import port_scanner

def main():
    #  Basic user interface
    print(colorama.Fore.YELLOW,f"""_________________________________

    Hello,  {os.getlogin()}!
    Welcome to Wi-Py!""")
    print(""" ________________________________

    [*]  Created by Akatsa
    [*]  Open-source project
    [*]  GitHub: https://github.com/AkatsaZXC 
 ________________________________""")
#  Check if user run this app with sudo
if not 'SUDO_UID' in os.environ.keys():
    print("Run this script with sudo.\n")
    print("Exiting...")
    exit()

if __name__ == '__main__':
    main()
