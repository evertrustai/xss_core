import sys
import os
import subprocess
from core.banner import display_banner
from core.colors import Colors
from core.utils import get_input, get_path_input, clear_screen, read_file_lines
import core.scanner as scanner

def main_menu():
    while True:
        clear_screen()
        display_banner()
        print(f"{Colors.BOLD}MAIN MENU{Colors.RESET}")
        print(f"{Colors.CYAN}[1] XSS Scanner{Colors.RESET}")
        print(f"{Colors.CYAN}[2] Tool Update{Colors.RESET}")
        print(f"{Colors.CYAN}[3] Exit{Colors.RESET}")
        print()
        
        choice = get_input("Enter your choice >")
        
        if choice == '1':
            run_scanner_workflow()
            input(f"\n{Colors.YELLOW}Press Enter to return to main menu...{Colors.RESET}")
        elif choice == '2':
            run_update()
            input(f"\n{Colors.YELLOW}Press Enter to return to main menu...{Colors.RESET}")
        elif choice == '3':
            clean_exit()
        else:
            Colors.print_error("Invalid choice. Please try again.")
            time.sleep(1)

def run_scanner_workflow():
    clear_screen()
    display_banner()
    print(f"{Colors.BOLD}XSS SCANNER{Colors.RESET}")
    print("-" * 30)
    
    # 1. URL Input
    print("1️⃣ URL INPUT")
    url_input = get_path_input("Enter the path to the input file containing URLs (or press Enter to enter a single URL):")
    
    urls = []
    if url_input:
        urls = read_file_lines(url_input)
        if not urls:
            Colors.print_error("No valid URLs found in file.")
            return
    else:
        single_url = get_input("[?] Enter a single URL to scan:")
        if single_url:
            urls = [single_url]
        else:
            Colors.print_error("No URL provided.")
            return

    # 2. Payload Input
    print("\n2️⃣ PAYLOAD INPUT")
    payload_input = get_path_input("Enter the path to the XSS payload file:")
    
    payloads = []
    if payload_input:
        payloads = read_file_lines(payload_input)
        if not payloads:
             Colors.print_error("No valid payloads found in file.")
             return
    else:
        Colors.print_error("Payload file is required.")
        return
        
    # Start Scan
    scanner.scan_target(urls, payloads)

def run_update():
    print(f"\n{Colors.BLUE}[*] Checking for updates...{Colors.RESET}")
    if not os.path.exists(".git"):
        Colors.print_error("Not a git repository. Cannot update.")
        return

    try:
        subprocess.check_call(["git", "pull"])
        Colors.print_success("Updated successfully!")
    except subprocess.CalledProcessError:
        Colors.print_error("Update failed. Please check your git configuration.")
    except FileNotFoundError:
        Colors.print_error("Git not installed or not in PATH.")

def clean_exit():
    print(f"\n{Colors.GREEN}Thank you for using XSS CORE. Happy Hunting!{Colors.RESET}")
    sys.exit(0)

import time # Imported here to be available in main_menu loop sleep
if __name__ == "__main__":
    try:
        main_menu()
    except KeyboardInterrupt:
        clean_exit()
