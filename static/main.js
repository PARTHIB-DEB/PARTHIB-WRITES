"use strict";

let elem = document.getElementById('ham')
let ham = document.getElementById('navItems')
let main = document.getElementsByTagName('main')

const rotate=()=> {
    if (elem.style.transform === 'rotate(0deg)') {
        elem.style.transform = 'rotate(90deg)'
        ham.style.display = "flex"
        ham.style.transform = 'translateY(0rem)'
        ham.style.transitionTimingFunction = 'jump-start'
        ham.style.transitionDuration = '1s'
    } else {
        elem.style.transform = 'rotate(0deg)'
        ham.style.transform = 'translateY(-30rem)'
        ham.style.transitionTimingFunction = 'jump-end'
    }
}
elem.addEventListener("click",rotate);

const small_nav = document.getElementById("nav-blog")
const big_nav = document.getElementById("nav-blog-big")
const small_plat = document.getElementById("plat-small")
const big_plat = document.getElementById("plat-big")
small_nav.addEventListener('click', () => window.scrollTo({
    top: 400,
    behavior: 'smooth',
}));
big_nav.addEventListener('click', () => window.scrollTo({
    top: 400,
    behavior: 'smooth',
}));
small_plat.addEventListener('click', () => window.scrollTo({
    top: 1200,
    behavior: 'smooth',
}));
big_plat.addEventListener('click', () => window.scrollTo({
    top: 1200,
    behavior: 'smooth',
}));