import os
import colorama
import port_scanner


def menu_bar():
    print(colorama.Fore.GREEN, "Tools: ")
    print(colorama.Fore.YELLOW, """
        [1] Port scanner
        [2] WiFi deauth tool""")

    tool_number = input("Choose tool(print number):\n")

    if tool_number == '1':
        print(colorama.Fore.GREEN, "Chosen *Port scanner*")
        try:
            for port in range(100):
                port_scanner.port_scanner(port)
        except Exception as e:
            print("This tool is not exist yet")
            exit()
        except KeyboardInterrupt:
            print("Exiting...")
            exit()
    elif tool_number == '2':
        print(colorama.Fore.GREEN, "Chosen *WiFi deauth tool*")
        try:
            pass
        except Exception as e:
            print("This tool is not exists yet")
        except KeyboardInterrupt:
            print("Exiting...")
            exit()


#  Check if user run this app with sudo
if not 'SUDO_UID' in os.environ.keys():
    print("Run this script with sudo.\n")
    print("Exiting...")
    exit()


def main():
    #  Basic user interface
    print(colorama.Fore.YELLOW, f"""________________________________

    Hello,  {os.getlogin()}!
    Welcome to Wi-Py!""")
    print(""" ________________________________

    [*]  Created by Akatsa
    [*]  Open-source project
    [*]  GitHub: https://github.com/AkatsaZXC 
 ________________________________""")

    #  Calling menu_bar function
    menu_bar()


if __name__ == '__main__':
    main()
