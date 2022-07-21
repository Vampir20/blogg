let slider = document.getElementById("slider")
let slide = 1
let slides = document.querySelectorAll(".slide")
let slideWrapper = document.querySelector(".slider-wrapper")
if (slideWrapper){
    slideWrapper.style.width = `${slides.length * 100}%`
}


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

let profileBlog = document.querySelector(".profile-blog")
let profileButton = document.querySelector(".profile-button")
let profileWrapper = document.querySelector(".profile-wrapper")

profileButton.addEventListener("click", function (event){
    event.preventDefault()
    if (profileBlog.classList.contains("show")){
        profileWrapper.classList.remove("open")
        profileBlog.classList.remove("show")
    }else{
        profileBlog.classList.add("show")
        profileWrapper.classList.add("open")
    }
})