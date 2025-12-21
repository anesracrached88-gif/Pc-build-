import requests
from bs4 import BeautifulSoup
from flask import Flask, render_template, request

app = Flask(__name__)

def get_ebay_price(item_name):
    try:
        url = f"https://www.ebay.com/sch/i.html?_nkw={item_name.replace(' ', '+')}&_sop=15&LH_ItemCondition=3000"
        headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'}
        response = requests.get(url, headers=headers, timeout=7)
        soup = BeautifulSoup(response.text, 'html.parser')
        price_tag = soup.select_one('.s-item__price')
        return price_tag.get_text() if price_tag else "N/A"
    except:
        return "N/A"

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/result', methods=['POST'])
def result():
    budget = int(request.form.get('budget', 0))
    condition = request.form.get('condition')
    
    # 50$ Step Logic with Famous Brands
    if budget < 450:
        pc = {"CPU": "Intel i3-10100F", "GPU": "MSI GT 1030", "MOBO": "ASRock H410M", "PSU": "EVGA 400W", "Case": "Cooler Master Q300L"}
        new_p = {"CPU": "75$", "GPU": "90$", "MOBO": "70$", "PSU": "40$", "Case": "45$"}
    elif budget < 500:
        pc = {"CPU": "Intel i3-12100F", "GPU": "ASUS Phoenix GTX 1650", "MOBO": "Gigabyte H610M", "PSU": "Corsair CV450", "Case": "DeepCool Matrexx 30"}
        new_p = {"CPU": "95$", "GPU": "160$", "MOBO": "80$", "PSU": "50$", "Case": "45$"}
    elif budget < 550:
        pc = {"CPU": "AMD Ryzen 5 4500", "GPU": "Gigabyte RX 6500 XT", "MOBO": "ASUS Prime A520M", "PSU": "EVGA 500W BR", "Case": "Antec NX200"}
        new_p = {"CPU": "80$", "GPU": "150$", "MOBO": "75$", "PSU": "55$", "Case": "50$"}
    elif budget < 600:
        pc = {"CPU": "Intel i3-13100F", "GPU": "MSI Mech RX 6600", "MOBO": "MSI PRO B760M-P", "PSU": "Corsair CV550", "Case": "Zalman S2"}
        new_p = {"CPU": "110$", "GPU": "200$", "MOBO": "100$", "PSU": "60$", "Case": "55$"}
    elif budget < 650:
        pc = {"CPU": "AMD Ryzen 5 5600", "GPU": "ASUS Dual RTX 3060", "MOBO": "Gigabyte B550M DS3H", "PSU": "Corsair CX650M", "Case": "NZXT H510"}
        new_p = {"CPU": "135$", "GPU": "280$", "MOBO": "110$", "PSU": "70$", "Case": "75$"}
    elif budget < 700:
        pc = {"CPU": "Intel i5-12400F", "GPU": "Zotac RTX 4060 Solo", "MOBO": "ASUS Prime B660M", "PSU": "Thermaltake 600W", "Case": "Fractal Design Focus G"}
        new_p = {"CPU": "150$", "GPU": "300$", "MOBO": "120$", "PSU": "65$", "Case": "65$"}
    elif budget < 750:
        pc = {"CPU": "AMD Ryzen 5 7600", "GPU": "MSI Ventus RTX 4060 Ti", "MOBO": "MSI PRO B650M-A", "PSU": "Corsair RM750e", "Case": "Montech AIR 100"}
        new_p = {"CPU": "200$", "GPU": "380$", "MOBO": "150$", "PSU": "100$", "Case": "65$"}
    else:
        pc = {"CPU": "Intel i5-13600K", "GPU": "ASUS TUF RTX 4070 Super", "MOBO": "MSI MAG Z790 Tomahawk", "PSU": "Corsair RM850x", "Case": "NZXT H7 Flow"}
        new_p = {"CPU": "300$", "GPU": "600$", "MOBO": "250$", "PSU": "130$", "Case": "130$"}

    prices = {}
    if condition == "used":
        for key in pc:
            prices[key] = get_ebay_price(pc[key])
    else:
        prices = new_p

    return render_template('result.html', pc=pc, prices=prices, condition=condition, budget=budget)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=8080)
