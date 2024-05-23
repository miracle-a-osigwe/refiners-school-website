// Update content based on the movement of the object

document.addEventListener("DOMContentLoaded", function () {
    if (document.querySelector(".content-slider")) {
    const slider = document.querySelector(".content-slider");
    const length = document.querySelectorAll(".content2").length
    let estimate = (length * 0.5) - 0.5
    let currentIndex = -estimate;
    

    function nextSlide() {
        currentIndex++;
        if (currentIndex >= length - (length/2)) {
        currentIndex = -estimate;
        }
        updateSlider();
    }

    function updateSlider() {
        const translateValue = -currentIndex * 100 + "vw";
        slider.style.transform = "translateX(" + translateValue + ")";
    }

    // Initialize the slider position
    updateSlider();

    setInterval(nextSlide, 5000); // Change slide every 5 seconds
    } else {
        // Do nothing
    }
});

// const images = document.querySelectorAll('.gallery-swipe img-gallery');
// let currentIdx = 0;

// function showImage(index) {
//     images.forEach((img, i) => {
//         img.style.opacity = ( i === index ) ? 1 : 0;
//     });
// }

// function nextImage() {
//     currentIdx = (currentIdx + 1) % images.length;

//     showImage(currentIdx);
// }

// setInterval(nextImage, 3000);


document.addEventListener("DOMContentLoaded", function () {
    if (document.querySelector("#gallery")) {        
        const swiper = document.querySelector(".gallery-slides");
    
        const len = document.querySelectorAll(".gallery-content").length
        let est = 1/len
        let currentIdx = 0;
        let count = 0
        
        function nextSwipe() {
        currentIdx += est;
        count++;
        if (count >= len) {
            currentIdx= count = 0;
        }
        updateSwiper();
        }
    
        function updateSwiper() {
        const translateV = -currentIdx * 100 + "%";
        swiper.style.transform = "translateX(" + translateV + ")";
        }
    
        // Initialize the slider position
        updateSwiper();
    
        setInterval(nextSwipe, 5000); // Change slide every 5 seconds
    }  else {
        // Do nothing
    }
});

// JavaScript for sliding content
// let currentIndex = 0;
// const totalContents = document.querySelectorAll('.content-section').length;

// function showNextContent() {
//     currentIndex = (currentIndex + 1) % totalContents;
//     updateGallery();
// }

// function updateGallery() {
//     const galleryContainer = document.getElementById('gallery-container');
//     galleryContainer.style.transform = `translateX(-${currentIndex * 50}%)`;
// }

// // Automatically slide content every 5 seconds
// setInterval(showNextContent, 5000);