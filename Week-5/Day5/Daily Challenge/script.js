const taskArr = [];
let counter = 0;
let ulIsAmpty = true;
let container = document.body.firstElementChild;
let form = document.forms[0];
let addCase = form.lastElementChild;
let toDoList = container.lastElementChild;

let title = document.createElement("h1");
title.innerHTML = "TO-DO LIST";
title.style.color = "white";
title.style.margin = "20px";
container.insertBefore(title, container.firstChild);

addCase.addEventListener("click", addTask);

function createClear() {
    let clear = document.createElement("button");
    clear.className = "btn";
    clear.innerHTML = "Clear";
    clear.addEventListener("click", clearList);
    toDoList.appendChild(clear);
}

function addTask(e) {
    e.preventDefault();
    if (ulIsAmpty) {
        ulIsAmpty = !ulIsAmpty;
        let ul = document.createElement("ul");
        toDoList.appendChild(ul);
        createClear();
    }
    let ul = toDoList.firstElementChild;
    let input = form.firstElementChild.value;
    if (input == 0) {
        form.firstElementChild.value = prompt("What the task?");
    }
    input_object = {
        task_id: counter,
        text: input,
        done: false,
    };
    console.log(taskArr);
    counter++;
    taskArr.push(input_object);
    let li = document.createElement("li");
    let button = document.createElement("button");
    button.innerHTML = "X";
    // button.addEventListener('click',removeTask)
    button.style.fontFamily = "Awesome";
    let checkbox = document.createElement("input");
    checkbox.type = "checkbox";
    // checkbox.addEventListener('click', checkTask)
    li.innerHTML = input;
    li.insertBefore(checkbox, li.firstChild);
    li.insertBefore(button, li.firstChild);
    console.log(li);
    ul.appendChild(li);
    form.firstElementChild.value = "";
}

function clearList(e) {
    e.preventDefault();
    
    toDoList.innerHTML = "";
    ulIsAmpty = true;
}
