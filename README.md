# BMI Calculator

A fully responsive web app to calculate Body Mass Index (BMI) using a modern Python Flask backend, with dynamic HTML, CSS, and JavaScript on the front end. Supports both metric and imperial units, provides categorized BMI results, and is built for seamless cross-device usage.

---

## 🚀 Live Deployment
You can try the app instantly here: [bmi-calculator-phi-seven-98.vercel.app](https://bmi-calculator-phi-seven-98.vercel.app)

---

## Features
- Multi-platform responsive UI (mobile, tablet, desktop)
- Enter height and weight in **metric (cm, kg)** or **imperial (ft/in, lbs)** units
- Instant and accurate BMI calculation with clear category (underweight, normal, overweight, obesity)
- Smart unit conversion and error handling
- Interactive BMI meter gauge with color-coded feedback
- Deployable out-of-the-box on Vercel with optimized settings (no legacy configs)

---

## Quick Start
1. **Clone the repo:**
    ```bash
    git clone https://github.com/heytanix/BMI_Calculator.git
    cd BMI_Calculator
    ```
2. **Install dependencies:**
    ```bash
    pip install flask
    ```
3. **Develop locally:**
    ```bash
    python api/index.py
    # Or use flask run with FLASK_APP set
    ```
4. **Deploy to Vercel:**
    - Push to GitHub and link the repository in your [Vercel dashboard](https://vercel.com/).

---

## Usage Guide
- Enter your stats in either unit system.
- The UI updates BMI and classifies you in real time.
- The interactive gauge shows your result visually for clarity.

---

## Project Structure
```
BMI_Calculator/
│
├── api/             # Flask backend (index.py)
├── public/          # Frontend static assets (HTML, CSS, JS)
├── templates/       # Jinja2/HTML templates for Flask
├── requirements.txt # Python dependencies
├── vercel.json      # Vercel deployment/rewrites configuration
└── README.md        # Project documentation
```

---

## Future Work
- Integration of Gemini API to suggest personalized diet plans based on BMI results, supporting users to achieve and maintain a healthy BMI.

---

## License
MIT License. This project is free and open for any use.

---

## Credits
Created by Thanish C (@heytanix) as a quick deployable BMI tool for universal access.
