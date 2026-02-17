# Garden Advice Application

A comprehensive Python application that provides gardening tips and advice based on the month and season. This project demonstrates professional code organization, error handling, logging, and a menu-driven user interface.

## Features

- **Seasonal Advice**: Get gardening tips for different seasons (Spring, Summer, Fall, Winter)
- **Category-Based Tips**: Browse advice by category:
  - Watering
  - Planting
  - Pruning
  - Pest Control
- **Input Validation**: Robust validation of user inputs with helpful error messages
- **Comprehensive Logging**: Detailed logs for debugging and monitoring
- **Color-Coded Output**: Enhanced terminal display with ANSI color codes
- **Interactive Menu**: User-friendly menu-driven interface

## Project Structure

```
garden-app/
├── garden_advice.py       # Main application module
├── constants.py           # Configuration and constants
├── advice_database.py     # Centralized advice data
├── ui.py                  # UI and formatting module
├── README.md              # This file
├── .gitignore            # Git ignore file
└── repo.txt              # Repository information
```

## Installation

1. Clone the repository:
```bash
git clone https://github.com/YOUR_USERNAME/garden-app.git
cd garden-app
```

2. Ensure Python 3.6+ is installed:
```bash
python --version
```

3. No external dependencies required for basic functionality

## Usage

Run the application:
```bash
python garden_advice.py
```

### Menu Options

1. **Get Seasonal Advice (by Month)**
   - Enter a month number (1-12)
   - View all gardening advice for that month

2. **Get Advice by Category**
   - Select a season (Spring, Summer, Fall, Winter)
   - View advice for all categories in that season

3. **View All Seasons' Advice**
   - See complete advice database for all seasons and categories

4. **Exit** (Option 0)
   - Safely close the application

## Code Quality Improvements

### ✓ Separation of Concerns
- **constants.py**: All configuration values and constants
- **advice_database.py**: Data storage and management
- **ui.py**: Display and user interface logic
- **garden_advice.py**: Core application logic and orchestration

### ✓ Input Validation
- `validate_month()` function ensures valid month input (1-12)
- All functions perform type and value checking
- User-friendly error messages guide users to correct input

### ✓ Error Handling
- Try-except blocks for robust error handling
- Graceful handling of invalid inputs
- Comprehensive error logging

### ✓ Logging
- Configured logging for debugging
- Log levels: DEBUG, INFO, WARNING, ERROR
- Timestamp and context included in log messages

### ✓ Documentation
- Module-level docstrings
- Function docstrings with:
  - Description of functionality
  - Args with types
  - Return value specification
  - Usage examples
- Inline comments for complex logic

### ✓ User Experience
- Color-coded terminal output (Green, Red, Yellow, Cyan)
- Formatted headers and sections
- Clear success and error messages
- Interactive menu system

## Example Usage

### Getting Seasonal Advice
```
Select an option (0-3): 1
Enter the month number (1-12): 5

Garden Advice for May (Spring)
=================================================

Watering:
  Water regularly as plants are actively growing. Check soil moisture daily.

Planting:
  Plant warm-season vegetables like tomatoes, peppers, and squash.

Pruning:
  Prune dead branches from winter damage.

Pest Control:
  Watch for early spring pests. Apply organic solutions as needed.
```

## GitHub Workflow

This project demonstrates professional GitHub workflow practices:

### Issues Created
1. **Issue #1**: Refactor Code Structure and Separation of Concerns
2. **Issue #2**: Enhance Input Validation and Error Handling

### Pull Request Process
1. Create feature branch from issues
2. Implement changes
3. Commit with descriptive messages
4. Push to GitHub
5. Create pull request
6. Code review and approval
7. Merge to main branch
8. Close associated issue

## Technical Details

### Python Version
- Python 3.6 or higher

### Dependencies
- Standard library only (no external packages required)

### Modules
- `logging`: For application logging
- `constants`: Custom module for configuration
- `advice_database`: Custom module for data
- `ui`: Custom module for display

## Testing

Test the application with various inputs:

```bash
# Test valid month input
$ python garden_advice.py
Select an option (0-3): 1
Enter the month number (1-12): 6

# Test invalid month
$ python garden_advice.py
Select an option (0-3): 1
Enter the month number (1-12): 13
Error: Invalid month number. Please enter a number between 1 and 12.

# Test exit
$ python garden_advice.py
Select an option (0-3): 0
```

## Future Enhancements

- [ ] Add database integration (SQLite)
- [ ] Implement web interface (Flask/Django)
- [ ] Add location-based recommendations
- [ ] Integrate weather API
- [ ] Multi-language support
- [ ] Mobile application
- [ ] User profiles and saved preferences

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Commit with descriptive messages
5. Push to GitHub
6. Create a pull request

## License

This project is provided as part of HyperionDev coursework.

## Author

Your Name / HyperionDev Student

## Contact

For questions or suggestions, please create an issue on GitHub.

---

**Repository**: https://github.com/YOUR_USERNAME/garden-app

**Last Updated**: February 2026

**Status**: Active Development
