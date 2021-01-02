function init() {
    let people = document.getElementsByClassName("people");
    for (let person of people) {
        if ((person.innerHTML.includes("🥇")) || (person.innerHTML.includes("🥈")) || (person.innerHTML.includes("🥉"))) {
            console.log(person.innerHTML[person.innerHTML.length -1])
        }
    }
}

init()