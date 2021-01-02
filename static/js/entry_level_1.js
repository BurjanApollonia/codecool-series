function init() {
      let numbers = document.getElementsByClassName('episode-number');
      for (let number of numbers) {
        if (number.innerHTML % 2 === 0) {
            number.classList.add("entry-green")
        }
        else {
            number.classList.add("entry-blue")
        }
    }
}

init()