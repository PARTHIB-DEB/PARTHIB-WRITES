let elem = document.getElementById('ham')
let b = document.getElementById('opham')
let c = document.getElementById('main')

elem.onclick = function () {
    if (elem.style.transform === 'rotate(0deg)') {
        elem.style.transform = 'rotate(90deg)'
        main.style.transitionDuration = '0.5s'
        main.style.transitionTimingFunction = 'ease-in'
        main.style.transform = 'translateY(0rem)'
    }
    
    if (elem.style.transform === 'rotate(90deg)') {
        elem.style.transform = 'rotate(0deg)'
        main.style.transitionDuration = '0.5s'
        main.style.transitionTimingFunction = 'ease-out'
        main.style.transform = 'translateY(-5rem)'
    }
}