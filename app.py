import os  # ضروري جداً لتشغيل البورت
from flask import Flask, render_template, request

app = Flask(__name__)

# بيانات المكونات الأساسية لبناء تجميعة ديناميكية
parts = {
    "low": {
        "cpu": "AMD Ryzen 5 5600G (Integrated Graphics)",
        "gpu": "Radeon™ Graphics",
        "ram": "16GB Corsair Vengeance DDR4",
        "storage": "500GB Kingston NV2",
        "mobo": "Gigabyte B450M DS3H"
    },
    "mid": {
        "cpu": "Intel Core i5-13400F",
        "gpu": "NVIDIA RTX 4060 8GB",
        "ram": "16GB G.Skill DDR5",
        "storage": "1TB Samsung 980 Pro",
        "mobo": "MSI PRO B760-P"
    },
    "high": {
        "cpu": "Intel Core i7-14700K",
        "gpu": "NVIDIA RTX 4080 Super",
        "ram": "32GB DDR5 6000MHz",
        "storage": "2TB NVMe Gen4",
        "mobo": "ASUS ROG Z790"
    }
}

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/get_build', methods=['POST'])
def get_build():
    # استقبال الميزانية كرقـم
    try:
        budget = int(request.form.get('budget', 0))
    except:
        budget = 500

    condition = request.form.get('condition')

    # منطق اختيار التجميعة بناءً على أي مبلغ يدخله المستخدم
    if budget < 800:
        selected_build = parts["low"]
    elif budget < 1500:
        selected_build = parts["mid"]
    else:
        selected_build = parts["high"]

    return render_template('result.html', build=selected_build, budget=budget, condition=condition)

if __name__ == '__main__':
    # إعدادات البورت للتشغيل على السيرفرات العالمية أو Termux
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
