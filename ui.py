"""
Garden Advice UI Module
Handles display and formatting of gardening advice.
"""

import sys

# ANSI Color Codes for Terminal Output
class Colors:
    """ANSI color codes for terminal formatting."""
    HEADER = '\033[95m'
    BLUE = '\033[94m'
    CYAN = '\033[96m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    END = '\033[0m'


def print_header(text, width=50):
    """
    Print a formatted header with decorative borders.
    
    Args:
        text (str): The header text to display
        width (int): Width of the header box (default: 50)
    """
    print(f"\n{Colors.BOLD}{Colors.CYAN}{'='*width}{Colors.END}")
    print(f"{Colors.BOLD}{Colors.CYAN}{text.center(width)}{Colors.END}")
    print(f"{Colors.BOLD}{Colors.CYAN}{'='*width}{Colors.END}\n")


def print_section(title, content):
    """
    Print a formatted section with title and content.
    
    Args:
        title (str): The section title
        content (str): The section content
    """
    print(f"{Colors.BOLD}{Colors.GREEN}{title}:{Colors.END}")
    print(f"  {content}\n")


def print_menu():
    """Display the main menu options."""
    print(f"\n{Colors.BOLD}{Colors.YELLOW}Garden Advice Application Menu:{Colors.END}")
    print("  1. Get Seasonal Advice (by Month)")
    print("  2. Get Advice by Category")
    print("  3. View All Seasons' Advice")
    print("  0. Exit")
    print()


def print_categories():
    """Display available advice categories."""
    from constants import CATEGORIES
    print(f"{Colors.BOLD}{Colors.YELLOW}Available Categories:{Colors.END}")
    for i, category in enumerate(CATEGORIES, 1):
        print(f"  {i}. {category.replace('_', ' ').title()}")
    print()


def print_error(message):
    """
    Print an error message in red.
    
    Args:
        message (str): The error message to display
    """
    print(f"{Colors.RED}{Colors.BOLD}Error: {message}{Colors.END}\n")


def print_success(message):
    """
    Print a success message in green.
    
    Args:
        message (str): The success message to display
    """
    print(f"{Colors.GREEN}{Colors.BOLD}{message}{Colors.END}\n")


def print_info(message):
    """
    Print an info message in cyan.
    
    Args:
        message (str): The info message to display
    """
    print(f"{Colors.CYAN}{Colors.BOLD}{message}{Colors.END}\n")
