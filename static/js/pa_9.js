function init() {
    let button = document.getElementById('search-button');
    button.addEventListener('click', display);
}

async function api_request(inputText) {
    const response = await fetch(`/pa_9_2?input-text=${inputText}`);
    document.getElementById('data-holder').innerHTML = "";
    return await response.json();
}

async function display(event) {
    event.preventDefault()
    let inputText = document.getElementById('search').value;
    let results = await api_request(inputText);
    let inputField = document.getElementById('data-holder');
    for (let row of results) {
        inputField.insertAdjacentHTML('beforeend',
            '<li>' + row['actorname'] + ' played ' + row['charactername'] + ' in ' + row['title'] + '</li>');
    }
}

init()