
import os
from flask import Flask, render_template, request

app = Flask(__name__)

# قاعدة البيانات (تأكد من شمولية الميزانيات)
builds = {
    "500": {"cpu": "Ryzen 5 5600G", "gpu": "Integrated Vega", "ram": "16GB DDR4", "storage": "500GB NVMe"},
    "1000": {"cpu": "Core i5-13400F", "gpu": "RTX 4060", "ram": "16GB DDR5", "storage": "1TB NVMe"}
}

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/get_build', methods=['POST'])
def get_build():
    budget = request.form.get('budget')
    condition = request.form.get('condition')
    selected_build = builds.get(budget)
    
    # التأكد من إرسال البيانات لملف result.html
    return render_template('result.html', build=selected_build, budget=budget, condition=condition)

if __name__ == '__main__':
    # إعدادات متوافقة مع Render و Termux
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
