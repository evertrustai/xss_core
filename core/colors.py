import colorama
from colorama import Fore, Style

colorama.init(autoreset=True)

class Colors:
    RED = Fore.RED
    GREEN = Fore.GREEN
    YELLOW = Fore.YELLOW
    BLUE = Fore.BLUE
    CYAN = Fore.CYAN
    MAGENTA = Fore.MAGENTA
    WHITE = Fore.WHITE
    RESET = Style.RESET_ALL
    BOLD = Style.BRIGHT
    
    @staticmethod
    def print_error(msg):
        print(f"{Colors.RED}[!] {msg}{Colors.RESET}")

    @staticmethod
    def print_success(msg):
        print(f"{Colors.GREEN}[+] {msg}{Colors.RESET}")
        
    @staticmethod
    def print_info(msg):
        print(f"{Colors.BLUE}[*] {msg}{Colors.RESET}")

    @staticmethod
    def print_warning(msg):
        print(f"{Colors.YELLOW}[!] {msg}{Colors.RESET}")
