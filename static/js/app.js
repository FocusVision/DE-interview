(function() {
    const $TODO_LIST = $('#todo-list');
    const $NEW_FORM = $('#new-todo'); 
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
            // TODO: Implement Me!
        },

        delete(id) {
            // TODO: Implement Me!
        }
    };

    function createTodoList() {
        TodoApi.get().then(res => {
            res.tasks.forEach(task => {
                addTodoItem(task)
            });
        });
    }

    function addTodoItem(task) {
        let $task = $('<div/>');
        let $done = $('<input/>',{
            type: 'checkbox',
            id: `done-${task.id}`,
            checked: task.done
        });

        $task.text(task.note);
        $task.prepend($done);
        $TODO_LIST.append($task);
    }

    function handleSubmit(evt) {
        evt.preventDefault();
        let note = $(this).serializeArray()[0];
        if (note.value) {
            TodoApi.create({'note': note.value})
                .then((res) => {
                    addTodoItem(res['task']);
                });
        }
    }
    
    function bootstrap() {
        $NEW_FORM.submit(handleSubmit);
        createTodoList();
    }

    bootstrap();
}());
