"""
Garden Advice Application
Provides gardening tips and advice based on the month and season.

This module serves as the main application interface for the Garden App.
It handles user interactions and coordinates with other modules for data
retrieval and display formatting.

Improvements implemented:
- Input validation for month numbers (1-12)
- Proper error handling and logging
- Separation of concerns (constants, data, UI)
- Enhanced docstrings with examples
- Menu-driven CLI interface
- Color-coded output for better readability
"""

import logging
from constants import MONTH_SEASONS, MONTH_NAMES, MIN_MONTH, MAX_MONTH, CATEGORIES
from advice_database import ADVICE_DATABASE
from ui import (print_header, print_section, print_menu, print_error, 
                print_success, print_info, print_categories)

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)


def validate_month(month_number):
    """
    Validate that the month number is within acceptable range.
    
    Args:
        month_number (int): The month number to validate
        
    Returns:
        bool: True if valid, False otherwise
        
    Examples:
        >>> validate_month(5)
        True
        >>> validate_month(13)
        False
    """
    if not isinstance(month_number, int):
        logger.warning(f"Invalid type for month: {type(month_number)}")
        return False
    
    if month_number < MIN_MONTH or month_number > MAX_MONTH:
        logger.warning(f"Month out of range: {month_number}")
        return False
    
    logger.debug(f"Month {month_number} is valid")
    return True


def get_month_name(month_number):
    """
    Get the full month name for a given month number.
    
    This function validates the input and returns the corresponding
    month name. Input must be between 1 and 12.
    
    Args:
        month_number (int): Month number (1-12)
        
    Returns:
        str: Full month name (e.g., "January") or "Unknown" if invalid
        
    Raises:
        ValueError: If month_number is not a valid integer
        
    Examples:
        >>> get_month_name(1)
        'January'
        >>> get_month_name(12)
        'December'
        >>> get_month_name(5)
        'May'
    """
    if not validate_month(month_number):
        logger.error(f"Invalid month number: {month_number}")
        return "Unknown"
    
    return MONTH_NAMES[month_number - 1]


def get_season(month_number):
    """
    Get the season for a given month number.
    
    Args:
        month_number (int): Month number (1-12)
        
    Returns:
        str: Season name or "unknown" if invalid
        
    Examples:
        >>> get_season(1)
        'winter'
        >>> get_season(6)
        'summer'
    """
    if not validate_month(month_number):
        logger.error(f"Invalid month for season lookup: {month_number}")
        return "unknown"
    
    return MONTH_SEASONS.get(month_number, "unknown")


def get_advice(season, category):
    """
    Get gardening advice for a specific season and category.
    
    This function retrieves advice from the database with proper error
    handling for invalid inputs. It logs all operations for debugging.
    
    Args:
        season (str): Season name (spring, summer, fall, winter)
        category (str): Advice category (watering, planting, pruning, pest_control)
        
    Returns:
        str: Gardening advice or error message if not found
        
    Examples:
        >>> get_advice("spring", "planting")
        'Plant warm-season vegetables...'
        >>> get_advice("invalid", "watering")
        'No advice available for the requested season and category.'
    """
    logger.debug(f"Retrieving advice for season={season}, category={category}")
    
    # Validate season
    if season not in ADVICE_DATABASE:
        logger.error(f"Invalid season: {season}")
        return "No advice available for the requested season and category."
    
    # Validate category
    if category not in ADVICE_DATABASE[season]:
        logger.error(f"Invalid category '{category}' for season '{season}'")
        return "No advice available for the requested season and category."
    
    advice = ADVICE_DATABASE[season][category]
    logger.info(f"Successfully retrieved advice for {season} - {category}")
    return advice


def display_seasonal_advice(month_number):
    """
    Display all gardening advice for the given month.
    
    This function retrieves all advice categories for a given month
    and displays them in a formatted, color-coded output.
    
    Args:
        month_number (int): Month number (1-12)
    """
    if not validate_month(month_number):
        print_error("Invalid month number. Please enter a number between 1 and 12.")
        logger.warning(f"Invalid month provided: {month_number}")
        return

    month_name = get_month_name(month_number)
    season = get_season(month_number)

    print_header(f"Garden Advice for {month_name} ({season.capitalize()})")

    for category in CATEGORIES:
        advice = get_advice(season, category)
        print_section(category.replace('_', ' ').title(), advice)
    
    logger.info(f"Displayed seasonal advice for {month_name}")


def display_all_seasons():
    """Display all garden advice for all seasons."""
    print_header("Garden Advice - All Seasons")
    
    for season in ["spring", "summer", "fall", "winter"]:
        print_info(f"{season.upper()}:")
        for category in CATEGORIES:
            advice = get_advice(season, category)
            print_section(category.replace('_', ' ').title(), advice)
    
    logger.info("Displayed all seasonal advice")


def display_advice_by_category(season):
    """
    Display all advice for a specific season, organized by category.
    
    Args:
        season (str): Season name (spring, summer, fall, winter)
    """
    if season not in ADVICE_DATABASE:
        print_error(f"Invalid season: {season}")
        logger.error(f"Invalid season requested: {season}")
        return
    
    print_header(f"Garden Advice for {season.capitalize()}")
    
    for category in CATEGORIES:
        advice = get_advice(season, category)
        print_section(category.replace('_', ' ').title(), advice)
    
    logger.info(f"Displayed advice for season: {season}")


def interactive_menu():
    """Display an interactive menu-driven interface for the application."""
    while True:
        try:
            print_menu()
            choice = input("Select an option (0-3): ").strip()
            
            if choice == "0":
                print_success("Thank you for using the Garden Advice Application. Happy gardening!")
                logger.info("User exited the application")
                break
            
            elif choice == "1":
                try:
                    month = int(input("Enter the month number (1-12): ").strip())
                    display_seasonal_advice(month)
                except ValueError:
                    print_error("Please enter a valid number between 1 and 12.")
                    logger.warning("Invalid month input from user")
            
            elif choice == "2":
                print_categories()
                print("Enter the season (spring, summer, fall, winter): ")
                season = input().strip().lower()
                display_advice_by_category(season)
            
            elif choice == "3":
                display_all_seasons()
            
            else:
                print_error("Invalid option. Please select 0, 1, 2, or 3.")
                logger.warning(f"Invalid menu option selected: {choice}")
        
        except KeyboardInterrupt:
            print("\nApplication terminated by user.")
            logger.info("Application terminated by user (Ctrl+C)")
            break
        except Exception as e:
            print_error(f"An unexpected error occurred: {str(e)}")
            logger.error(f"Unexpected error: {str(e)}", exc_info=True)


def main():
    """Main application entry point."""
    logger.info("Starting Garden Advice Application")
    
    print_info("Welcome to the Garden Advice Application!")
    print_info("This app provides gardening tips based on the month and season.\n")
    
    interactive_menu()
    
    logger.info("Garden Advice Application closed")


if __name__ == "__main__":
    main()

