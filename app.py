import os
from flask import Flask, render_template, request

app = Flask(__name__)

# قاعدة بيانات التجميعات (Brand New vs Used/eBay)
build_data = {
    "new": {
        "budget_low": {
            "cpu": "AMD Ryzen 5 5600G (New)",
            "gpu": "Radeon Graphics (Integrated)",
            "ram": "16GB Corsair Vengeance DDR4 (New)",
            "storage": "500GB Kingston NV2 NVMe",
            "mobo": "Gigabyte B450M DS3H WIFI"
        },
        "budget_high": {
            "cpu": "Intel Core i5-13400F (New)",
            "gpu": "ASUS Dual RTX 4060 8GB (New)",
            "ram": "16GB G.Skill Trident Z5 DDR5",
            "storage": "1TB Samsung 980 Pro",
            "mobo": "MSI PRO B760-P WIFI"
        }
    },
    "used": {
        "budget_low": {
            "cpu": "Intel Core i7-8700K (eBay Deal)",
            "gpu": "EVGA GTX 1080 Ti 11GB (Used)",
            "ram": "16GB HyperX Fury DDR4 (Used)",
            "storage": "512GB Crucial MX500 SSD",
            "mobo": "ASUS ROG Strix Z370-E"
        },
        "budget_high": {
            "cpu": "AMD Ryzen 9 5900X (Used/Mint)",
            "gpu": "Gigabyte RTX 3080 10GB (eBay Refurbished)",
            "ram": "32GB Corsair Dominator Platinum",
            "storage": "1TB WD Black SN850X",
            "mobo": "ASROCK X570 Taichi"
        }
    }
}

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/get_build', methods=['POST'])
def get_build():
    try:
        budget = int(request.form.get('budget', 0))
    except:
        budget = 500

    condition = request.form.get('condition', 'New').lower()

    # اختيار الفئة بناءً على الميزانية والحالة
    category = "budget_low" if budget < 1000 else "budget_high"
    
    # تأكد من أن الحالة موجودة في البيانات، وإلا استعمل "new" كافتراضي
    selected_condition = condition if condition in build_data else "new"
    selected_build = build_data[selected_condition][category]

    return render_template('result.html', build=selected_build)

# --- كود التحقق لـ PropellerAds / Monetag ---
@app.route('/sw.js')
def serve_sw():
    return
 app.send_static_file('sw.js')
# --------------------------------------------

if __name__ == '__main__':
    # بورت 10000 هو الأنسب لـ Render
    port = int(os.environ.get("PORT", 10000))
    app.run(host='0.0.0.0', port=port)
