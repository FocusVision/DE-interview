(function() {
    'use strict';

    const $TODO_LIST = $('#todo-list');
    const $NEW_TODO = $('#new-todo');
    const TodoApi = {
        _api: '/api/todo/v1',
        _contentType: 'application/json',

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
                contentType: this._contentType
            }); 
        },

        update(id, data) {
            let url = `${this._api}/tasks/${id}`;
            return $.ajax({
                url,
                type: 'PUT',
                data: JSON.stringify(data),
                contentType: this._contentType
            });
        },

        delete(id) {
            let url = `${this._api}/tasks/${id}`;
            return $.ajax({
                url,
                type: 'DELETE'
            });
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
                    <span class="badge badge-success">Done</span>
                    <p type="text" class="card-text"></p>
                    <button id="delete-${task.id}" class="btn btn-sm btn-danger">Delete</button>
                    <button id="complete-${task.id}" class="btn btn-sm btn-primary">Complete</button>
                </div>
            </div>
        `);
        let $completeBtn = $task.find(`#complete-${task.id}`);
        let $deleteBtn = $task.find(`#delete-${task.id}`);
        let $doneBadge = $task.find('.badge-success');

        if (task.done) {
            $completeBtn.hide();
        } else {
            $completeBtn.click(handleComplete.bind(task));
            $doneBadge.hide();
        }
        $deleteBtn.click(handleDelete.bind(task));
        $task.find('.card-text').text(task.note);
        $TODO_LIST.append($task);
    }

    function handleDelete(evt) {
        TodoApi.delete(this.id)
            .then(res => {
                $(`#task-${this.id}`).remove();
            });
    }

    function handleComplete(evt) {
        TodoApi.update(this.id, {done: true})
            .then(res => {
                let $completeBtn = $(evt.target);
                if (res['task'].done) {
                    $completeBtn.hide();
                    $completeBtn.siblings('.badge-success').show();

                }
            });
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
