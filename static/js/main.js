let slider = document.getElementById("slider")
let slide = 1
let slides = document.querySelectorAll(".slide")
let slideWrapper = document.querySelector(".slider-wrapper")
slideWrapper.style.width = `${slides.length * 100}%`

function runSlider() {
    if (slide === slides.length) {
        slide = 0
    }

    let sliderParent = slider.parentElement.clientWidth

    slider.style.transform = `translateX(-${sliderParent * slide}px)`
    slide++
}

setInterval(() => {
    runSlider()
}, 2000)