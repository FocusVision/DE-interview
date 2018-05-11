(function() {
    'use strict';

    const $TODO_LIST = $('#todo-list');
    const $NEW_TODO = $('#new-todo');
    const TodoApi = {
        _api: '/api/todo/v1',

        get(id) {
            let url = id ? `${this._api}/tasks/${id}` : `${this._api}/tasks`;
            return $.get(url);
        },

        create(data) {
            let url = `${this._api}/tasks`;
            return $.ajax({
                url,
                type: 'POST',
                data: JSON.stringify(data),
                contentType: 'application/json'
            }); 
        },

        update(data) {
            // TODO: Implement me!
        },

        delete(id) {
            // TODO: Implement me!
        }
    };

    function createTodoList() {
        TodoApi.get().then(res => {
            res.tasks.forEach(task => {
                addTodoItem(task);
            });
        });
    }

    function addTodoItem(task) {
        let $task = $(`
            <div id="task-${task.id}" class="card">
                <div class="card-body">
                    ${task.done ? '<span class="badge badge-success">Done</span>' : ''}
                    <p type="text" class="card-text"></p>
                    <button id="delete-${task.id}" class="btn btn-sm btn-danger">Delete</button>
                    ${task.done ? '' : '<button id="complete-${task.id}" class="btn btn-sm btn-primary">Complete</button>'}
                </div>
            </div>
        `);
        $task.find('.card-text').text(task.note);
        $TODO_LIST.append($task);
    }

    function handleSubmit(evt) {
        evt.preventDefault();
        let note = $(this).serializeArray()[0];
        if (note.value) {
            TodoApi.create({'note': note.value})
                .then(res => {
                    addTodoItem(res['task']);
                });
        }
    }

    function bootstrap() {
        $NEW_TODO.submit(handleSubmit);
        createTodoList();
    }

    bootstrap();
}());
