from flask import Flask, render_template, request, jsonify, send_from_directory
import os

app = Flask(__name__, 
            template_folder=os.path.join(os.path.dirname(__file__), '..', 'templates'),
            static_folder=os.path.join(os.path.dirname(__file__), '..', 'static'))

@app.route('/static/<path:path>')
def send_static(path):
    """Explicitly serve static files for Vercel deployments"""
    static_folder = os.path.join(os.path.dirname(__file__), '..', 'static')
    return send_from_directory(static_folder, path)

@app.route('/')
def index():
    """Serve the main BMI calculator page"""
    return render_template('index.html')

@app.route('/calculate', methods=['POST'])
def calculate_bmi():
    """Calculate BMI from provided height and weight data"""
    try:
        data = request.get_json()
        
        # Extract input values
        height_value = float(data.get('height'))
        weight_value = float(data.get('weight'))
        height_unit = data.get('height_unit')  # 'cm', 'ft', 'in'
        weight_unit = data.get('weight_unit')  # 'kg', 'lbs'
        
        # Convert height to meters
        if height_unit == 'cm':
            height_m = height_value / 100
        elif height_unit == 'ft':
            # Expecting height_value to be in format: feet + (inches/12)
            height_m = height_value * 0.3048
        elif height_unit == 'in':
            height_m = height_value * 0.0254
        else:
            return jsonify({'error': 'Invalid height unit'}), 400
        
        # Convert weight to kilograms
        if weight_unit == 'kg':
            weight_kg = weight_value
        elif weight_unit == 'lbs':
            weight_kg = weight_value * 0.453592
        else:
            return jsonify({'error': 'Invalid weight unit'}), 400
        
        # Calculate BMI: weight(kg) / height(m)^2
        bmi = weight_kg / (height_m ** 2)
        
        # Determine BMI category
        if bmi < 18.5:
            category = 'Underweight'
            description = 'BMI less than 18.5'
        elif 18.5 <= bmi < 25:
            category = 'Healthy Weight'
            description = 'BMI 18.5 to 24.9'
        elif 25 <= bmi < 30:
            category = 'Overweight'
            description = 'BMI 25 to 29.9'
        elif 30 <= bmi < 35:
            category = 'Obesity Class 1'
            description = 'BMI 30 to 34.9'
        elif 35 <= bmi < 40:
            category = 'Obesity Class 2'
            description = 'BMI 35 to 39.9'
        else:
            category = 'Obesity Class 3'
            description = 'BMI 40 and above'
        
        return jsonify({
            'bmi': round(bmi, 2),
            'category': category,
            'description': description
        })
    
    except (ValueError, TypeError, KeyError) as e:
        return jsonify({'error': f'Invalid input: {str(e)}'}), 400

# For local development
if __name__ == '__main__':
    app.run(debug=True)
