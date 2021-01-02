function init() {
    let stars = document.querySelectorAll(".fa-star, .fa-star-o");
    stars.forEach((star) => {
        star.addEventListener("mouseover", hover)
    })
}

function hover() {
    let star = event.currentTarget
    let stars_p = star.parentElement
    let stars = stars_p.querySelectorAll(".fa-star, .fa-star-o");
    for (let i = 0; i < stars.length; i++) {
        let id = i.toString()
        stars[i].setAttribute('id', id)
    }
    let star_id = star.id
    stars.forEach((s) => {
            if (s.id <= star_id) {
                s.className = "fa fa-star"
            }
            else {
                s.className = "fa fa-star-o"
            }
        })
}

init()
