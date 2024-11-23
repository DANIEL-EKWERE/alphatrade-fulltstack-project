// header
const bar = document.getElementById("bar");
const nav = document.getElementById("nav");

bar.onclick = (e) => {
    const icon = e.target.getAttribute("class")
    if(icon == "fa-solid fa-bars"){
        e.target.setAttribute("class","fa-solid fa-xmark")

    }else{
        e.target.setAttribute("class","fa-solid fa-bars")
    }
    nav.classList.toggle("showNav")
}


// carousel
const carouselContainer = document.querySelector(".carouselContainer");
const eachCarousel = document.querySelector(".eachCarousel").clientWidth;
const allEachCarousel = document.querySelectorAll(".eachCarousel");
const allIndicator = document.querySelectorAll(".indicator");

const slideCarousel = (index) => {
    for(let x = 0; x<allEachCarousel.length;x++){
        if(x === index){
            allEachCarousel[x].classList.add("eachCarouselBorder")
            allIndicator[x].classList.add("activeIndicator")
        }else{
            allEachCarousel[x].classList.remove("eachCarouselBorder")
            allIndicator[x].classList.remove("activeIndicator")
        }
    }
   carouselContainer.scrollLeft = (index * (eachCarousel + 10))
   console.log(carouselContainer.scrollLeft)
}

document.querySelectorAll('.pricing-card').forEach((card) => {
    card.addEventListener('mouseenter', () => {
      card.style.transform = 'scale(1.05)';
    });
  
    card.addEventListener('mouseleave', () => {
      card.style.transform = 'scale(1)';
    });
  });
  


  const track = document.querySelector('.carousel-track');
const dots = Array.from(document.querySelectorAll('.dot'));

let currentIndex = 0;

// function updateCarousel() {
//     const slideWidth = track.children[0].getBoundingClientRect().width * 3; // 3 cards at a time
//     track.style.transform = `translateX(-${currentIndex * slideWidth}px)`;

//     dots.forEach((dot, index) => {
//         dot.classList.toggle('active', index === currentIndex);
//     });
// }

// // Auto Slide
// setInterval(() => {
//     currentIndex = (currentIndex + 1) % dots.length;
//     updateCarousel();
// }, 3000);

// // Manual Navigation
// dots.forEach((dot, index) => {
//     dot.addEventListener('click', () => {
//         currentIndex = index;
//         updateCarousel();
//     });
// });

// // Initialize
// updateCarousel();


$(document).ready(function(){

    $('.owl-carousel').owlCarousel({
        center: true,
        loop:true,
        margin:10,
        nav:true,
        autoplay:true,
        autoplayHoverPause:true,
        smartSpeed: 1500,
        responsive:{
            0:{
                items:1
            },
            600:{
                items:1
            },
            1000:{
                items:3
            }
        }
    })

})




function copyToClipboard() {
  const referralIdElement = document.getElementById('referral-id');

  if (!referralIdElement) {
    alert("Referral ID not found!");
    return;
  }

  const referralIdText = referralIdElement.textContent; // Get the text content

  // Use the Clipboard API
  navigator.clipboard.writeText(referralIdText)
    .then(() => {
      alert(`Copied to clipboard: ${referralIdText}`);
    })
    .catch((err) => {
      console.error("Clipboard write failed:", err);
      alert(`Failed to copy Referral ID: ${err}`);
    });
}
