from flask import Flask, render_template, request, redirect

app = Flask(__name__)
tasks = []

app.jinja_env.globals.update(enumerate=enumerate)

@app.route('/')
def index():
    return render_template('index.html', tasks=tasks)

@app.route('/add', methods=['POST'])
def add():
    task = request.form.get('task')
    if task:
        tasks.append(task)
    return redirect('/')

@app.route('/delete/<int:i>')
def delete(i):
    tasks.pop(i)
    return redirect('/')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
