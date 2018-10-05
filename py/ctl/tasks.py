import flask

tasks_ctl = flask.Blueprint('tasks', __name__, url_prefix='/tasks')

task_info = {'prg-1': 'Sample task 1', 'prg-2': 'Sample task 2', 'prg-3':'Sample task 3'}

@tasks_ctl.route('/')
def task_list():
    return flask.render_template('tasks/list.html', data = task_info)

@tasks_ctl.route('/<id>')
def task_view(id):
    # add preprocessing to filter id, have to be lowercase, digits, or -
    # we filter to get clean id / throw extra elements
    # add the end of the day id == cleaned_id
    id_checked = [c for c in id if (c.islower() or c.isdigit() or c == '-')]
    if id in task_info and id == id_checked:
        return flask.render_template('tasks/view.html', data = [id,task_info[id]])
    else:
        flask.abort(404)
