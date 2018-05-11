import unittest
from copy import deepcopy
from json import loads, dumps

import todo
from todo import api


class ApiTestCase(unittest.TestCase):
    TASKS = api.TASKS

    def setUp(self):
        api.TASKS = deepcopy(self.TASKS)
        todo.app.testing = True
        self.app = todo.app.test_client()

    def test_get_tasks(self):
        response = self.app.get('/api/todo/v1/tasks')
        tasks = loads(response.data)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(api.TASKS, tasks.get('tasks', []))

    def test_create_task(self):
        new_task = {'note': 'Buy Milk'}
        response = self.app.post(
            '/api/todo/v1/tasks',
            data=dumps(new_task),
            content_type='application/json'
        )
        response_task = loads(response.data).get('task', {})
        self.assertEqual(response_task.get('note', ''), new_task['note'])
        self.assertEqual(len(api.TASKS), 3)

    def test_update_task(self):
        # TODO: Implement me!
        pass

    def test_delete_task(self):
        # TODO: Implement me!
        pass
