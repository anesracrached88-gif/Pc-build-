import os
from flask import Flask, render_template, request

app = Flask(__name__)

build_data = {
    "new": {
        "budget_low": {"cpu": "Ryzen 5 5600G", "gpu": "Integrated", "ram": "16GB", "storage": "500GB", "mobo": "B450M"},
        "budget_high": {"cpu": "i5-13400F", "gpu": "RTX 4060", "ram": "16GB", "storage": "1TB", "mobo": "B760"}
    },
    "used": {
        "budget_low": {"cpu": "i7-8700K", "gpu": "GTX 1080 Ti", "ram": "16GB", "storage": "512GB", "mobo": "Z370"},
        "budget_high": {"cpu": "Ryzen 9 5900X", "gpu": "RTX 3080", "ram": "32GB", "storage": "1TB", "mobo": "X570"}
    }
}

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/get_build', methods=['POST'])
def get_build():
    try:
        budget = int(request.form.get('budget', 500))
    except:
        budget = 500
    condition = request.form.get('condition', 'new').lower()
    category = "budget_low" if budget < 1000 else "budget_high"
    selected_condition = condition if condition in build_data else "new"
    return render_template('result.html', build=build_data[selected_condition][category], budget=budget, condition=selected_condition)

@app.route('/sw.js')
def serve_sw():
    return app.send_static_file('sw.js')

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 10000))
    app.run(host='0.0.0.0', port=port)
