from flask import Blueprint, jsonify, abort, request


api = Blueprint('api', __name__, url_prefix='/api/todo/v1')
# An in memory store works for now. A more robust implementation would persist
# the data.
NEXT_ID = 3
TASKS = [
    {
        'id': 1,
        'note': 'Buy Milk',
        'done': False
    },
    {
        'id': 2,
        'note': 'Pick up laundry',
        'done': True
    }
]


@api.errorhandler(501)
def not_implemented(error):
    return jsonify({'error': 'Not Implemented'}), 501


@api.errorhandler(400)
def bad_request(error):
    return jsonify({'error': 'Bad Request'}), 400


@api.route('/tasks', methods=['GET'])
def get_tasks():
    return jsonify({'tasks': TASKS}), 200


@api.route('/tasks', methods=['POST'])
def create_task():
    global NEXT_ID
    if not request.json or 'note' not in request.json:
        abort(400)

    new_task = {
        'id': NEXT_ID,
        'note': request.json['note'],
        'done': False
    }
    NEXT_ID += 1
    TASKS.append(new_task)
    return jsonify({'task': new_task}), 201


@api.route('/tasks/<int:task_id>', methods=['PUT'])
def update_task(task_id):
    if not request.json or 'done' not in request.json:
        abort(400)

    task = [t for t in TASKS if t['id'] == task_id]
    if not task:
        abort(400)

    task[0]['done'] = request.json['done']
    return jsonify({'task': task[0]}), 200


@api.route('/tasks/<int:task_id>', methods=['DELETE'])
def remove_task(task_id):
    index = None
    for i, task in enumerate(TASKS):
        if task['id'] == task_id:
            index = i
            break

    if index is None:
        abort(400)

    TASKS.pop(index)
    return '', 200
