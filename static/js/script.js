var navbarLinks = document.querySelectorAll('.navbar-center a');

navbarLinks.forEach(link => {
    link.addEventListener('click', event => {

    navbarLinks.forEach(navLink => {
        navLink.classList.remove('active');
    });

    link.classList.add('active');
    });
});

//changing of words

const words = [
   { text: 'A treasure trove of food knowledge to explore.', color: 'white' },
   { text: 'Sharing recipes, tips, and flavors galore.', color: 'white' },
   { text: 'A food lover\'s hub, exploring culinary delights.', color: 'white' }
];

// Get the changing-text element
const changingText = document.getElementById('changing-text');

// Index to keep track of the current word
let currentIndex = 0;

// Function to change the word periodically
function changeWord() {
  const { text, color } = words[currentIndex];
  changingText.innerHTML = `<span class="changing-word" style="color: ${color}">${text}</span>`;

  // Increment the index for the next word
  currentIndex = (currentIndex + 1) % words.length;
}

// Call the changeWord function every 3 seconds (3000 milliseconds)
setInterval(changeWord, 3000);

const dots = document.querySelectorAll('.dot');
const images = document.querySelector('.carousel-images');
let currentSlide = 0;

dots.forEach((dot, index) => {
  dot.addEventListener('click', () => {
    currentSlide = index;
    updateCarousel();
  });
});

function updateCarousel() {
  images.style.transform = `translateX(-${currentSlide * 100}%)`;

  dots.forEach((dot, index) => {
    if (index === currentSlide) {
      dot.classList.add('active');
    } else {
      dot.classList.remove('active');
    }
  });
}

function slideNext() {
  currentSlide = (currentSlide + 1) % dots.length;
  updateCarousel();
}

setInterval(slideNext, 3000); // Auto slide every 3 seconds





