// calculator.js - Frontend logic for BMI calculator

document.addEventListener('DOMContentLoaded', function() {
    const form = document.getElementById('bmi-form');
    const resultDiv = document.getElementById('bmi-result');
    const categoryDiv = document.getElementById('bmi-category');
    const pointer = document.getElementById('bmi-pointer');
    const meter = document.querySelector('.bmi-meter');

    function validateInput() {
        // Simple validation for presence & numbers
        const height = document.getElementById('height').value;
        const weight = document.getElementById('weight').value;
        if (!height || !weight || isNaN(height) || isNaN(weight)) {
            return false;
        }
        return true;
    }

    function mapBMIToPercent(bmi) {
        // Map BMI (0-50) to meter width (0-100%)
        // Show pointer at far right for BMI 50+
        if (bmi >= 50) return 96;
        if (bmi <= 0) return 1;
        return (bmi / 50) * 96;
    }

    form.addEventListener('submit', function(event) {
        event.preventDefault();
        if (!validateInput()) {
            resultDiv.textContent = 'Please enter valid numbers.';
            resultDiv.style.color = '#e03131';
            categoryDiv.textContent = '';
            pointer.style.left = '0%';
            return;
        }

        const height = parseFloat(document.getElementById('height').value);
        const weight = parseFloat(document.getElementById('weight').value);
        const heightUnit = document.getElementById('height-unit').value;
        const weightUnit = document.getElementById('weight-unit').value;

        fetch('/calculate', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({
                height: height,
                weight: weight,
                height_unit: heightUnit,
                weight_unit: weightUnit
            })
        })
        .then(resp => resp.json())
        .then(data => {
            if (data.error) {
                resultDiv.textContent = data.error;
                resultDiv.style.color = '#e03131';
                categoryDiv.textContent = '';
                pointer.style.left = '0%';
                return;
            }
            // BMI display
            resultDiv.textContent = `Your BMI: ${data.bmi}`;
            resultDiv.style.color = '#1871bc';
            categoryDiv.textContent = `${data.category} — ${data.description}`;
            categoryDiv.style.color = '#46525c';
            pointer.style.left = mapBMIToPercent(data.bmi) + '%';
        })
        .catch(() => {
            resultDiv.textContent = 'Calculation failed.';
            resultDiv.style.color = '#e03131';
            categoryDiv.textContent = '';
            pointer.style.left = '0%';
        });
    });
});
