from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

todo = []
tasks = []


@app.route('/', methods=['GET'])
def index():
    return render_template('index.html', todo=todo, task=tasks)


@app.route('/add', methods=['POST'])
def add_todo():
    todos = request.form.get("todo")
    if todos:
        todo.append(todos)
        tasks.append(False)
    return redirect(url_for('index'))


@app.route('/update/<int:task_id>', methods=['GET', 'POST'])
def update_todo(task_id):
    if request.method == 'POST':
        new_task = request.form.get("Up")
        todo[task_id] = new_task  # Update the task in the list
        return redirect(url_for('index'))
    else:
        task = todo[task_id]  # Get the specific task to edit
        return render_template('update.html', task=task, task_id=task_id)
    # Pass only the task to the template


@app.route('/done/<task>')
def mark_done(task):
    if task in todo:
        index = todo.index(task)
        tasks[index] = True
    return redirect(url_for('index'))


@app.route('/undo/<task>')
def undo_done(task):
    if task in todo:
        index = todo.index(task)
        tasks[index] = False
    return redirect(url_for('index'))


if __name__ == '__main__':
    app.run(debug=True)
