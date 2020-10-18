function createTask() {
    var user_name = document.getElementById("username").value;
    var task_name = document.getElementById("taskname").value;

    var task = {
        name: task_name,
        start: null,
        end: null,
        user: user_name
    }

    localStorage.setItem(task_name, JSON.stringify(task));
    console.log("Task created");
}

function registerTaskStart() {
    var task_name = document.getElementById("taskToStart").value;

    var task = JSON.parse(localStorage.getItem(task_name));

    task.start = Date.now();

    localStorage.setItem(task_name, JSON.stringify(task));

    console.log(task)
}

