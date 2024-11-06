
# 0x02. i18n

## Description
This project demonstrates how to implement internationalization (i18n) in a Flask application. By using Flask-Babel, the app can serve content in multiple languages, adapt to user preferences, and format timestamps according to locale settings.

## Features
- **Language Selection**: Dynamically serve content in different languages.
- **Locale Inference**: Automatically detect and set language preferences based on URL parameters, user settings, or request headers.
- **Timestamp Localization**: Display timestamps formatted to match the user's locale.

## Getting Started

### Prerequisites
- Python 3.x
- Flask
- Flask-Babel

### Installation
1. **Clone the repository**:
   ```bash
   git clone https://github.com/yourusername/0x02-i18n.git
   ```
2. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

### Usage

1. **Set up translation files**:
   - Create a `translations` directory.
   - Generate translation files for each language (e.g., `en`, `fr`, `es`) using Babel CLI commands.

2. **Run the application**:
   ```bash
   flask run
   ```

3. **Visit the application**:
   - Use URL parameters (e.g., `/?lang=fr`) to change languages.
   - Alternatively, the app will infer the language from the browser’s settings.

### Example
To view content in French, navigate to:
```
http://localhost:5000/?lang=fr
```

## Project Structure
- **app.py**: Main application file.
- **templates/**: Contains Jinja2 templates with translatable content.
- **translations/**: Contains `.po` and `.mo` files for each supported language.

## Additional Information
- **Locale Selector**: The `locale_selector` function in `app.py` infers the user’s preferred language.
- **Timestamp Formatting**: Dates and times are automatically formatted based on locale
