from flask import Flask, render_template, request, jsonify

app = Flask(__name__)
students = []

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/add', methods=['GET', 'POST'])
def add_student():
    if request.method == 'POST':
        name = request.form.get('name')
        course = request.form.get('course')
        students.append({'name': name, 'course': course})
        return render_template('add_student.html', success=True)
    return render_template('add_student.html', success=False)

@app.route('/api/students', methods=['GET'])
def get_students():
    return jsonify(students)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

