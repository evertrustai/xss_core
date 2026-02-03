from core.colors import Colors

def display_banner():
    # font: standard or doom (simulated here for "XSS CORE")
    banner = f"""
{Colors.CYAN}{Colors.BOLD}
__  __ ____ ____    ____ ___  ____  _____ 
\\ \\/ // ___/ ___|  / ___/ _ \\|  _ \\| ____|
 \\  / \\___ \\___ \\ | |  | | | | |_) |  _|  
 /  \\  ___) |__) || |__| |_| |  _ <| |___ 
/_/\\_\\|____/____/  \\____\\___/|_| \\_\\_____|
                                          
{Colors.RESET}
{Colors.BLUE}Created by : evertrustai{Colors.RESET}
{Colors.MAGENTA}Instagram  : evertrustai{Colors.RESET}
{Colors.WHITE}GitHub     : https://github.com/evertrustai{Colors.RESET}
"""
    print(banner)
    print(f"{Colors.YELLOW}WELCOME TO XSS CORE - THE SENTINEL OF SECURITY{Colors.RESET}")
    print(f"{Colors.RED}WARNING: For authorized ethical testing only.\n{Colors.RESET}")
