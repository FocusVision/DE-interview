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

    def get_task(self, id):
        app_task = [t for t in api.TASKS if t['id'] == id]
        if app_task:
            return app_task[0]
        return None

    def test_get_tasks(self):
        response = self.app.get('/api/todo/v1/tasks')
        tasks = loads(response.data)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(api.TASKS, tasks.get('tasks', []))

    def test_create_task(self):
        new_task = {'note': 'Pay bills'}
        response = self.app.post(
            '/api/todo/v1/tasks',
            data=dumps(new_task),
            content_type='application/json'
        )
        response_task = loads(response.data).get('task', {})
        self.assertEqual(response.status_code, 201)
        self.assertEqual(response_task.get('note', ''), new_task['note'])
        self.assertEqual(len(api.TASKS), 3)

    def test_update_task(self):
        id = 1
        for payload in [{'done': True}, {'done': False}]:
            response = self.app.put(
                '/api/todo/v1/tasks/%s' % id,
                data=dumps(payload),
                content_type='application/json'
            )

            app_task = self.get_task(id)
            response_task = loads(response.data).get('task', {})
            self.assertEqual(response.status_code, 200)
            self.assertEqual(response_task.get('done'), payload['done'])
            self.assertEqual(response_task.get('done', ''), app_task['done'])

        response = self.app.put(
            '/api/todo/v1/tasks/999',
            data=dumps({'done': True}),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, 400)

    def test_delete_task(self):
        id = 1
        response = self.app.delete('/api/todo/v1/tasks/%s' % id)
        app_task = self.get_task(id)
        self.assertEqual(response.status_code, 200)
        self.assertIsNone(self.get_task(id))

        # can't delete twice
        response = self.app.delete('/api/todo/v1/tasks/%s' % id)
        self.assertEqual(response.status_code, 400)
