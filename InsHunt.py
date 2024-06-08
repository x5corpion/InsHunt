# coding=utf-8
#!/usr/bin/env python3



from libs.check_modules import check_modules
from sys import exit
from os import _exit

check_modules()


from os import path

from libs.logo import print_logo
from libs.utils import print_success
from libs.utils import print_error
from libs.utils import ask_question
from libs.utils import print_status
from libs.utils import parse_proxy_file
from libs.proxy_harvester import find_proxies
from libs.attack import report_profile_attack
from libs.attack import report_video_attack

from multiprocessing import Process
from colorama import Fore, Back, Style

def chunks(lst, n):
    """Yield successive n-sized chunks from lst."""
    for i in range(0, len(lst), n):
        yield lst[i:i + n]

def profile_attack_process(username, proxy_list):
    if (len(proxy_list) == 0):
        for _ in range(10):
            report_profile_attack(username, None)
        return

    for proxy in proxy_list:
        report_profile_attack(username, proxy)

def video_attack_process(video_url, proxy_list):
    if (len(proxy_list) == 0):
        for _ in range(10):
            report_video_attack(video_url, None)
        return

    for proxy in proxy_list:
        report_video_attack(video_url, proxy)

def video_attack(proxies):
    video_url = ask_question("Enter the link of the video you want to report:")
    print(Style.RESET_ALL)
    if (len(proxies) == 0):
        for k in range(5):
            p = Process(target=video_attack_process, args=(video_url, [],))
            p.start()
            print_status(str(k + 1) + ". Transaction Opened!")
            if (k == 5): print()
        return

    chunk = list(chunks(proxies, 10))

    print("")
    print_status("Video complaint attack is being launched!\n")

    i = 1
    for proxy_list in chunk:
        p = Process(target=video_attack_process, args=(video_url, proxy_list,))
        p.start()
        print_status(str(i) + ". Transaction Opened!")
        if (k == 5): print()
        i = i + 1

def profile_attack(proxies):
    username = ask_question("Enter the username of the person you want to report:")
    print(Style.RESET_ALL)
    if (len(proxies) == 0):
        for k in range(5):
            p = Process(target=profile_attack_process, args=(username, [],))
            p.start()
            print_status(str(k + 1) + ". Transaction Opened!")
        return

    chunk = list(chunks(proxies, 10))

    print("")
    print_status("Profile complaint attack is being launched!\n")

    i = 1
    for proxy_list in chunk:
        p = Process(target=profile_attack_process, args=(username, proxy_list,))
        p.start()
        print_status(str(i) + ". Transaction Opened!")
        if (k == 5): print()
        i = i + 1

def main():
    print_success("Modules loaded!\n")

    ret = ask_question("Would you like to use a proxy? [Y/N]")

    proxies = []

    if (ret == "Y" or ret == "N"):
        ret = ask_question("Do you want to collect your proxies from the internet? [Y/N]: ")

        if (ret == "Y" or ret == "N"):
            print_status("Collecting proxies from the internet! This may take a while.\n")
            proxies = find_proxies()
        elif (ret == "Y" or ret == "N"):
            print_status("Please allow a maximum of 50 proxies in one file!")
            file_path = ask_question("Enter the path to your proxy list:")
            proxies = parse_proxy_file(file_path)
        else:
            print_error("The answer was not understood, exiting!")
            exit()

        print_success(str(len(proxies)) + " Number of proxies found!\n")
    elif (ret == "Y" or ret == "N"):
        pass
    else:
        print_error("The answer was not understood, exiting!")
        exit()

    

    print("")
    print_status("1 - Report the profile.")
    print_status("2 - Report a video.")
    report_choice = ask_question("Please select complaint method: ")
    print("")

    if (report_choice.isdigit() == False):
        print_error("The answer was not understood.")
        exit(0)
    
    if (int(report_choice) > 2 or int(report_choice) == 0):
        print_error("The answer was not understood.")
        exit(0)

    if (int(report_choice) == 1):
        profile_attack(proxies)
    elif (int(report_choice) == 2):
        video_attack(proxies)

if __name__ == "__main__":
    print_logo()
    try:
        main()
        print(Style.RESET_ALL)
    except KeyboardInterrupt:
        print("\n\n" + Fore.RED + "[ * ] The program is being closed!")
        print(Style.RESET_ALL)
        _exit(0)