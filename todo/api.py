from flask import Blueprint, jsonify, abort, request


api = Blueprint('api', __name__, url_prefix='/api/todo/v1')
# An in memeory store works for now. A more robust implementation would persist
# the data.
tasks = [
    {
        'id': 1,
        'note': 'Buy Milk',
        'done': False
    },
    {
        'id': 2,
        'note': 'Pick up laundry',
        'done': False
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
    return jsonify({'tasks': tasks}), 200


@api.route('/tasks', methods=['POST'])
def create_task():
    if not request.json or 'note' not in request.json:
        abort(400)

    next_id = max([t['id'] for t in tasks]) + 1
    new_task = {
        'id': next_id,
        'note': request.json['note'],
        'done': False
    }
    tasks.append(new_task)
    return jsonify({'task': new_task}), 201


@api.route('/tasks/<int:task_id>', methods=['GET'])
def get_task(task_id):
    # TODO: Implement Me!
    abort(501)


@api.route('/tasks/<int:task_id>', methods=['PUT'])
def update_task(task_id):
    # TODO: Implement Me!
    abort(501)


@api.route('/tasks/<int:task_id>', methods=['DELETE'])
def remove_task(task_id):
    # TODO: Implement Me!
    abort(501)
