# BMI Calculator

A responsive BMI calculator web application built with Python (Flask backend), HTML, CSS, and JavaScript. It allows users to input height and weight in any unit (Metric/Imperial), handles conversion logic, displays a dynamic BMI meter UI, and classifies BMI into standardized categories. Optimized for phones, tablets, laptops, and desktops. Ready for deployment on Vercel.

## Features
- Responsive UI for mobile, tablet, and desktop
- Height/Weight input supports Metric (cm, kg) and Imperial (ft/in, lbs) units
- Automatic unit conversion
- Real-time BMI calculation and interactive meter
- BMI categories:
  - Underweight (<18.5)
  - Healthy weight (18.5–24.9)
  - Overweight (25–29.9)
  - Obesity:
    - Class 1 (30–34.9)
    - Class 2 (35–39.9)
    - Class 3 (≥40)
- Visual feedback using meter widget

## Installation
1. Fork or clone this repository.
2. Install dependencies:
    ```bash
    pip install flask
    ```
3. For local development:
    ```bash
    python app.py
    ```
4. For Vercel deployment, see [Vercel configuration](#vercel-deployment).

## Usage
- Enter your height and weight in the preferred unit.
- The app converts units automatically and shows BMI + category class.

## Vercel Deployment
The repository includes necessary configuration for Vercel. Simply link this repo to your Vercel account.

### vercel.json
The configuration is set to use Flask as backend and serve the front-end statically.

## File Structure
- `app.py` - Flask backend
- `static/` - Static files (HTML, CSS, JS)
- `templates/` - HTML templates
- `vercel.json` - Vercel configuration
- `README.md`

## License
MIT License
