var slideIndex = 0;
// adding variable to keep track of current slide index
function moveSlide(n) {
    var slides = document.getElementsByClassName("gallery-image");
    if (n === 1 && slideIndex === slides.length - 1) {
        slideIndex = 0;
    } else if (n === -1 && slideIndex === 0) {
        slideIndex = slides.length - 1;
    } else {
        slideIndex += n;
    }
    var offset = -slideIndex * 100;
    document.querySelector(".gallery-slider").style.transform = "translateX(" + offset + "%)";
}
