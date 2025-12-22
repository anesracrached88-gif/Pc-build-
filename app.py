from flask import Flask, render_template, request

app = Flask(__name__)

# قاعدة بيانات القطع (يمكنك تعديل الأسعار هنا)
parts_data = {
    "cpus": {
        "Intel Core i9-13900K": 580,
        "AMD Ryzen 7 7800X3D": 450,
        "Intel Core i5-13600K": 320
    },
    "gpus": {
        "NVIDIA RTX 4090": 1600,
        "NVIDIA RTX 4080": 1100,
        "RTX 3060": 300
    },
    "rams": {
        "32GB DDR5": 150,
        "16GB DDR4": 60
    }
}

# المسار الرئيسي للموقع (يسمح بـ GET و POST)
@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        # الحصول على البيانات المختارة من النموذج
        cpu_name = request.form.get('cpu')
        gpu_name = request.form.get('gpu')
        ram_name = request.form.get('ram')
        
        # حساب السعر
        total = (parts_data['cpus'].get(cpu_name, 0) +
                 parts_data['gpus'].get(gpu_name, 0) +
                 parts_data['rams'].get(ram_name, 0))
        
        # الانتقال لصفحة النتيجة
        return render_template('result.html', total=total, cpu=cpu_name, gpu=gpu_name, ram=ram_name)
    
    return render_template('index.html', parts=parts_data)

if __name__ == '__main__':
    app.run(debug=True)
