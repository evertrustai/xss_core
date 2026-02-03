import os
from core.colors import Colors
from prompt_toolkit import prompt
from prompt_toolkit.completion import PathCompleter
from prompt_toolkit.styles import Style

# Define a custom style for the prompt (matching the requested image/theme)
custom_style = Style.from_dict({
    'completion-menu.completion': 'bg:#008888 #ffffff',
    'completion-menu.completion.current': 'bg:#00aaaa #000000',
    'scrollbar.background': 'bg:#88aaaa',
    'scrollbar.button': 'bg:#222222',
})

def get_input(prompt_text):
    try:
        return input(f"{Colors.CYAN}{prompt_text} {Colors.RESET}").strip()
    except KeyboardInterrupt:
        print()
        Colors.print_warning("Operation cancelled by user.")
        return None

def get_path_input(prompt_text):
    """
    Uses prompt_toolkit to provide file path autocompletion.
    """
    completer = PathCompleter()
    try:
        # prompt_toolkit's prompt function doesn't support ANSI colors in the prompt string directly 
        # in the same way basic input() does for some terminals, but we can print the prompt first 
        # or use formatted text. For simplicity and consistency with existing code, we'll print title.
        
        # However, to get the exact inline feel "Enter path: [input]", we use simple string.
        # We strip the color codes for the actual prompt function to avoid issues, 
        # or we just rely on the user seeing the text before.
        
        print(f"{Colors.CYAN}{prompt_text}{Colors.RESET}", end=" ")
        user_input = prompt("", completer=completer, style=custom_style).strip()
        return user_input
    except KeyboardInterrupt:
        print()
        Colors.print_warning("Operation cancelled.")
        return None

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def read_file_lines(filepath):
    """Reads a file and returns non-empty lines."""
    if not os.path.isfile(filepath):
        Colors.print_error(f"File not found: {filepath}")
        return []
    
    try:
        with open(filepath, 'r', encoding='utf-8', errors='ignore') as f:
            lines = [line.strip() for line in f if line.strip()]
        return lines
    except Exception as e:
        Colors.print_error(f"Error reading file {filepath}: {e}")
        return []
