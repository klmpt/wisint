import sys
import pyfiglet
import datetime
import os
from colorama import init, Fore, Style

# Importing modules
from modules.recon import ReconEngine
from modules.extractor import DataExtractor
from modules.storage import Storage
from modules.image_analyzer import ImageAnalyzer
from modules.phone_lookup import search_phone
from modules.dns_enum import get_dns_records
from modules.port_scanner import quick_scan
from modules.file_entropy import check_entropy
from modules.logger import log_action
from modules.web_logger import WebLogger

init(autoreset=True)

def print_banner():
    banner = pyfiglet.figlet_format("wisint", font="slant")
    print(Fore.CYAN + banner)
    print(Fore.YELLOW + "    btw best free osint tool by wissy <3")
    print(Style.BRIGHT + "========================================")

def main():
    print_banner()
    menu = {
        "1": "Network Auto-Search",
        "2": "Analyze Domain/URL",
        "3": "DNS Recon",
        "4": "Phone Number Lookup",
        "5": "Port Scanner",
        "6": "Analyze Image Metadata",
        "7": "Check File Entropy",
        "8": "View Recent Logs",
        "9": "Create PHP Web Trap",
        "0": "Exit"
    }

    while True:
        print(f"\n{Fore.GREEN}[MENU] Available Modules:")
        for k, v in menu.items():
            print(f"{Fore.CYAN}{k}{Style.RESET_ALL} -> {v}")
        
        choice = input(f"\n{Fore.YELLOW}>> {Style.RESET_ALL}")
        log_action(f"Module selected: {choice}")

        if choice == "1":
            target = input(f"{Fore.YELLOW}Enter target nickname/name: {Style.RESET_ALL}")
            log_action(f"Recon target: {target}")
            links = ReconEngine(target).search()
            print(f"{Fore.GREEN}[+] Found {len(links)} sources.")
        
        elif choice == "2":
            url = input(f"{Fore.YELLOW}URL: {Style.RESET_ALL}")
            log_action(f"Analyzing URL: {url}")
            data = DataExtractor().extract(url)
            print(Fore.MAGENTA + str(data))

        elif choice == "3":
            domain = input(f"{Fore.YELLOW}Domain: {Style.RESET_ALL}")
            print(Fore.YELLOW + get_dns_records(domain))

        elif choice == "4":
            phone = input(f"{Fore.YELLOW}Phone number: {Style.RESET_ALL}")
            print(Fore.CYAN + f"Search link: {search_phone(phone)}")

        elif choice == "5":
            ip = input(f"{Fore.YELLOW}IP address: {Style.RESET_ALL}")
            print(Fore.RED + f"Open ports: {quick_scan(ip)}")

        elif choice == "6":
            path = input(f"{Fore.YELLOW}Image path: {Style.RESET_ALL}")
            print(Fore.YELLOW + str(ImageAnalyzer().get_exif(path)))

        elif choice == "7":
            path = input(f"{Fore.YELLOW}File path: {Style.RESET_ALL}")
            print(Fore.GREEN + f"Entropy: {check_entropy(path)}")

        elif choice == "8":
            print(f"{Fore.CYAN}--- RECENT LOGS ---")
            log_file = datetime.datetime.now().strftime("%Y-%m-%d") + ".log"
            path = os.path.join('logs', log_file)
            if os.path.exists(path):
                with open(path, "r") as f:
                    print(Fore.WHITE + "".join(f.readlines()[-10:]))
            else:
                print(Fore.RED + "Logs not found.")

        elif choice == "9":
            filename = input(f"{Fore.YELLOW}Filename (default: trap.php): {Style.RESET_ALL}") or "trap.php"
            url = input(f"{Fore.YELLOW}Redirect URL: {Style.RESET_ALL}") or "https://google.com"
            result = WebLogger().create_trap(filename, url)
            log_action(f"Created web trap: {filename}")
            print(Fore.GREEN + f"[+] {result}")

        elif choice == "0":
            log_action("System shutdown")
            print(Fore.RED + "[!] Exiting.")
            break
        else:
            print(Fore.RED + "[-] Invalid choice.")

if __name__ == "__main__":
    main()