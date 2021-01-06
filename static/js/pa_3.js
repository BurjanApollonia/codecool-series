function init() {
    let titles = document.querySelectorAll('.pa_3_title');
    let names = document.querySelectorAll('.pa_3_name');
    titles.forEach((title) =>{
        title.addEventListener("mouseover", titlesevent)
        title.addEventListener("mouseleave", eventover)
    })
    names.forEach((name) =>{
        name.addEventListener("mouseover", namesevent)
        name.addEventListener("mouseleave", eventover)
    })
}

function titlesevent() {
    let title = event.currentTarget
    let title_id = title.id
    let names = document.querySelectorAll('.pa_3_name')
    title.classList.add("highlight");
    for (let name of names) {
        if (name.id === title_id) {
            name.classList.add("highlight");
        }
    }
}

function namesevent() {
    let name = event.currentTarget
    let name_id = name.id
    let titles = document.querySelectorAll('.pa_3_title')
    name.classList.add("highlight");
    for (let title of titles) {
        if (title.id === name_id) {
            title.classList.add("highlight");
        }
    }
}

function eventover() {
    let titles = document.querySelectorAll('.pa_3_title');
    let names = document.querySelectorAll('.pa_3_name');
    for (let title of titles) {
        title.classList.remove("highlight");
    }
    for (let name of names) {
        name.classList.remove("highlight");
    }
}

init()