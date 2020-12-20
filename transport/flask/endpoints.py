from flask import jsonify, request

from usecases.tasks import Task, Tasks
from .tasks import TasksTransport


@TasksTransport.app.route('/tasks', methods=['GET'])
def list_tasks():
    tasks = Tasks.list()
    return jsonify(Task.serialize_multiple(tasks))


@TasksTransport.app.route('/tasks', methods=['POST'])
def create_tasks():
    body = request.get_json()
    task = Tasks.new(Task(body['name'], body.get('description')))
    return jsonify(task.serialize())
