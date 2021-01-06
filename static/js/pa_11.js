function init() {
    let button = document.getElementById('submit-button');
    button.addEventListener('click', display);
}

async function api_request(inputText) {
    const response = await fetch(`/pa_11_2?input-text=${inputText}`);
    document.getElementById('results').innerHTML = "";
    return await response.json();
}

async function display() {
    let inputText = document.getElementById('dropdown').value;
    let results = await api_request(inputText);
    let inputField = document.getElementById('results');
    for (let row of results) {
        inputField.insertAdjacentHTML('beforeend',
            '<tr>' + '<td>' + row['title'] + '</td>' + '<td>' + row['season_number'] + '</td>' + '<td>' +
            row['episode_number'] + '</td>' + '</tr>');
    }
}

init()