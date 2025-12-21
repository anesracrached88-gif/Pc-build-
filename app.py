from flask import Flask, render_template, request

app = Flask(__name__)

def get_pc_build(budget, condition):
    budget = int(budget)
    # قاعدة بيانات بسيطة تتغير كل 50 دولار
    # يمكنك توسيع هذه القائمة لاحقاً
    if condition == "new":
        if budget < 400:
            return [("CPU", "Ryzen 3 3200G", "90"), ("RAM", "8GB DDR4", "30"), ("SSD", "256GB NVMe", "25"), ("Total", "", str(budget))]
        elif budget < 450:
            return [("CPU", "Ryzen 5 4500", "110"), ("GPU", "RX 580", "120"), ("RAM", "16GB DDR4", "50"), ("Total", "", "420")]
        else: # 500+
            return [("CPU", "i5-12400F", "150"), ("GPU", "RTX 3060", "280"), ("RAM", "16GB DDR4", "50"), ("Total", "", "480")]
    else: # Used from eBay
        if budget < 400:
            return [("CPU (Used)", "Ryzen 5 3600", "60"), ("GPU (Used)", "GTX 1070", "110"), ("RAM", "16GB", "40"), ("Total", "", "210")]
        else:
            return [("CPU (Used)", "i7-9700K", "120"), ("GPU (Used)", "RTX 2070", "180"), ("RAM", "16GB", "40"), ("Total", "", "340")]

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/get_pc', methods=['POST'])
def get_pc():
    budget = request.form.get('budget')
    condition = request.form.get('condition')
    build = get_pc_build(budget, condition)
    return render_template('result.html', build=build, budget=budget, condition=condition)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
