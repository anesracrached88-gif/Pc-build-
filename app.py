import os
from flask import Flask, render_template, request

app = Flask(__name__)

# بيانات احترافية مع الماركات
builds = {
    "500": {
        "cpu": "AMD Ryzen 5 5600G (6-Core)",
        "gpu": "Radeon™ Graphics (Integrated)",
        "ram": "16GB (2x8GB) Corsair Vengeance DDR4 3200MHz",
        "storage": "500GB Kingston NV2 NVMe Gen4",
        "mobo": "Gigabyte B450M DS3H WIFI"
    },
    "1000": {
        "cpu": "Intel® Core™ i5-13400F",
        "gpu": "NVIDIA GeForce RTX 4060 8GB (ASUS Dual)",
        "ram": "16GB (2x8GB) G.Skill Trident Z5 RGB DDR5",
        "storage": "1TB Samsung 980 Pro NVMe",
        "mobo": "MSI PRO B760-P WIFI"
    }
}

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/get_build', methods=['POST'])
def get_build():
    budget = request.form.get('budget')
    condition = request.form.get('condition')
    selected_build = builds.get(budget, builds["500"])
    return render_template('result.html', build=selected_build, budget=budget, condition=condition)

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
