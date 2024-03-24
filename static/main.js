"use strict";
let elem = document.getElementById('ham')
let ham = document.getElementById('navItems')
let main = document.getElementsByTagName('main')
let nav_blog = document.getElementById('nav-blog')

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


nav_blog.addEventListener("click",function () {
  document.querySelector("body").style.transitionTimingFunction = 'ease'
  document.querySelector("body").style.transitionDuration = '2s'
//   document.querySelector("body").style.scrollBehavior = "smooth"
  document.querySelector("body").scroll(0,100)
})