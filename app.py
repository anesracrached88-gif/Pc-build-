from flask import Flask, render_template, request

app = Flask(__name__)

# قاعدة بيانات التجميعات (أمثلة تتغير بناءً على الميزانية)
def get_pc_build(budget, condition):
    # ميزانية افتراضية إذا كان الإدخال أقل من 300
    if budget < 300: budget = 300
    
    builds = {
        300: {"cpu": "Ryzen 3 3200G", "gpu": "Integrated Vega 8", "ram": "8GB DDR4"},
        350: {"cpu": "Ryzen 5 4600G", "gpu": "Integrated Vega 7", "ram": "16GB DDR4"},
        400: {"cpu": "Intel i3-12100F", "gpu": "GTX 1650", "ram": "16GB DDR4"},
        450: {"cpu": "Intel i3-12100F", "gpu": "RX 6500 XT", "ram": "16GB DDR4"},
        500: {"cpu": "Ryzen 5 5500", "gpu": "RX 6600", "ram": "16GB DDR4"},
        # يمكنك إضافة المزيد من الفئات هنا (550, 600, إلخ)
    }
    
    # اختيار أقرب فئة ميزانية (مثلاً 470 تصبح 450)
    closest_budget = (budget // 50) * 50
    if closest_budget > 500: closest_budget = 500 # حد أقصى للمثال
    
    result = builds.get(closest_budget, builds[300])
    
    # إذا كانت الحالة مستعملة (eBay)، نفترض قطع أقوى قليلاً بنفس السعر
    if condition == "used":
        if closest_budget == 500:
            result = {"cpu": "Ryzen 5 5600X", "gpu": "RTX 3060 Ti (Used)", "ram": "16GB DDR4"}
            
    return result, closest_budget

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        budget = int(request.form.get('budget', 0))
        condition = request.form.get('condition')
        
        build, final_budget = get_pc_build(budget, condition)
        
        return render_template('result.html', build=build, budget=final_budget, condition=condition)
    
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
