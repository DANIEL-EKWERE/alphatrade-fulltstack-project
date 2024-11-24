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

document.addEventListener("DOMContentLoaded", () => {
  const carouselContainer = document.querySelector(".carouselContainer");
  const allEachCarousel = document.querySelectorAll(".eachCarousel");
  const allIndicator = document.querySelectorAll(".indicator");

  const eachCarouselWidth = allEachCarousel[0].offsetWidth + 10; // Includes gap
  let currentIndex = 0;

  const slideCarousel = (index) => {
      currentIndex = index;

      // Update active styles
      allEachCarousel.forEach((carousel, idx) => {
          carousel.classList.toggle("eachCarouselBorder", idx === index);
      });
      allIndicator.forEach((indicator, idx) => {
          indicator.classList.toggle("activeIndicator", idx === index);
      });

      // Scroll to the appropriate position
      carouselContainer.scrollTo({
          left: index * eachCarouselWidth,
          behavior: "smooth",
      });
  };

  // Auto-slide function
  const startAutoSlide = () => {
      setInterval(() => {
          currentIndex = (currentIndex + 1) % allEachCarousel.length; // Loop to start
          slideCarousel(currentIndex);
      }, 3000); // Adjust the delay (3 seconds here)
  };

  // Initialize carousel
  slideCarousel(0);
  startAutoSlide();
});


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

    $('eachCarousel').owlCarousel({
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



// $(window).load(function(){
//     $(".preloader").hide();
//     // $("#webpage"").show();
//   })

// document.addEventListener("DOMContentLoaded", () => {
//     // Wait until the entire page is fully loaded
//     window.onload = () => {
//         const preloader = document.querySelector(".preloader");

//         // Add a class to hide the preloader with animation
//         preloader.classList.add("hidden");
//     };
// });


// window.onload = () => {
//     document.querySelector(".preloader").style.display = "none";
// };



var myVar;

function myFunction() {
  myVar = setTimeout(showPage, 3000);
}

function showPage() {
    document.getElementById("loader").style.display = "none";
//   document.getElementById("preloader").style.display = "none";
}


// Define variables for preloader handling
var preloaderTimeout;

function startPreloader() {
    // Set a timeout to simulate page loading
    preloaderTimeout = setTimeout(hidePreloader, 3000); // Adjust time as needed
}

function hidePreloader() {
    // Hide the preloader by setting its display to "none"
    const preloader = document.querySelector(".preloader");
    preloader.style.display = "none";
}
// Start the preloader function when the page starts loading
window.onload = startPreloader;