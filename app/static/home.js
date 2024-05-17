var slideIndex = 0;
// adding variable to keep track of current slide index
function moveSlide(n) {
    var slides = document.getElementsByClassName("gallery-image");
    // check if the slide index is at the end if user wants to move forward
    if (n === 1 && slideIndex === slides.length - 1) {
        slideIndex = 0;
    // check if the index is at the beginning and user wants to move backwards
    } else if (n === -1 && slideIndex === 0) {
        slideIndex = slides.length - 1;
    } else {
        slideIndex += n;// if neither at end or beginning move by given offset
    }
    var offset = -slideIndex * 100;// calculate horizontal offset
    // apply offset to move slider horizontally. 
    document.querySelector(".gallery-slider").style.transform = "translateX(" + offset + "%)";
}
