todos = []
new_todo_content = Element('new-task-content')
todo_list = Element('todo-list')
todo_template = Element('todo-template').select('.todo', from_content = True)

def add_todo(*args):

    todo_id = f'task-{len(todos)}'

    todo = {
        'id': todo_id,
        'content': new_todo_content.element.value,
    }    

    todos.append(todo)

    todo_html = todo_template.clone(todo_id, to=todo_list)
    todo_html_content = todo_html.select('p')
    todo_html_content.element.innerText = todo["content"]
    todo_html_check = todo_html.select('input')
    todo_list.element.appendChild(todo_html.element)