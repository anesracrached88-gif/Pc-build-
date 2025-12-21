from flask import Flask, render_template, request

app = Flask(__name__)

def get_pc_build(budget, condition):
    budget = int(budget)
    if condition == "new":
        if budget < 450:
            return [("CPU", "AMD Ryzen 5 4500", "80"), ("GPU", "MSI GTX 1650 Ventus", "155"), ("MB", "ASUS Prime A520M-K", "70"), ("RAM", "16GB Corsair Vengeance", "45"), ("SSD", "500GB Kingston", "35"), ("PSU", "EVGA 500W 80+", "50")]
        elif budget < 500:
            return [("CPU", "Intel Core i3-12100F", "95"), ("GPU", "Gigabyte RX 6500 XT", "165"), ("MB", "MSI PRO H610M-G", "80"), ("RAM", "16GB Kingston FURY", "50"), ("SSD", "512GB Crucial M.2", "40"), ("PSU", "Corsair CV550", "60")]
        elif budget < 550:
            return [("CPU", "AMD Ryzen 5 5500", "105"), ("GPU", "Sapphire Pulse RX 6600", "210"), ("MB", "Gigabyte B450M DS3H", "75"), ("RAM", "16GB G.Skill Ripjaws", "55"), ("SSD", "500GB Samsung 980", "50"), ("PSU", "Cooler Master 550W", "55")]
        else: # Build for $600+
            return [("CPU", "Intel i5-12400F", "140"), ("GPU", "ASUS Dual RTX 3060", "290"), ("MB", "ASUS Prime B760M-A", "120"), ("RAM", "16GB Corsair DDR4", "60"), ("SSD", "1TB WD Blue", "70"), ("PSU", "Corsair CX650", "80")]
    else: # Used from eBay
        if budget < 500:
            return [("CPU (Used)", "Ryzen 5 3600", "60"), ("GPU (Used)", "GTX 1080 Ti", "160"), ("MB (Used)", "B450 Board", "65"), ("RAM", "16GB", "35"), ("Total", "Calculated for eBay", "320")]
        else:
            return [("CPU (Used)", "i7-10700K", "130"), ("GPU (Used)", "RTX 2080 Super", "210"), ("MB (Used)", "Z490 Board", "100"), ("RAM", "16GB", "40"), ("Total", "Calculated for eBay", "480")]

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
