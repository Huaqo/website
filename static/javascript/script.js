const lightbox = document.createElement('div');
lightbox.id = 'lightbox';
document.body.appendChild(lightbox);

const images = document.querySelectorAll('img');
const imageArray = Array.from(images);

let currentImageIndex = 0;

function showImage(image) {
  lightbox.classList.add('active');
  const img = document.createElement('img');
  img.src = image.src;
  while (lightbox.firstChild) {
    lightbox.removeChild(lightbox.firstChild);
  }

  // Add previous button
  const prevButton = document.createElement('button');
  prevButton.classList.add('prevButton');
  prevButton.innerHTML = '<';
  prevButton.addEventListener('click', showPreviousImage);
  lightbox.appendChild(prevButton);

  // Add next button
  const nextButton = document.createElement('button');
  nextButton.classList.add('nextButton');
  nextButton.innerHTML = '>';
  nextButton.addEventListener('click', showNextImage);
  lightbox.appendChild(nextButton);

  // Add image
  lightbox.appendChild(img);
}

function hideImage() {
  lightbox.classList.remove('active');
}

function showNextImage() {
  currentImageIndex++;
  if (currentImageIndex >= imageArray.length) {
    currentImageIndex = 0;
  }
  showImage(imageArray[currentImageIndex]);
}

function showPreviousImage() {
  currentImageIndex--;
  if (currentImageIndex < 0) {
    currentImageIndex = imageArray.length - 1;
  }
  showImage(imageArray[currentImageIndex]);
}

images.forEach((image) => {
  image.addEventListener('click', (e) => {
    currentImageIndex = imageArray.indexOf(image);
    showImage(image);
  });
});

lightbox.addEventListener('click', (e) => {
  if (e.target !== e.currentTarget) return;
  hideImage();
});

document.addEventListener('keydown', (e) => {
  if (!lightbox.classList.contains('active')) return;
  if (e.key === 'ArrowRight') {
    showNextImage();
  } else if (e.key === 'ArrowLeft') {
    showPreviousImage();
  } else if (e.key === 'Escape') {
    hideImage();
  }
});

// Current year
const currentYear = new Date().getFullYear();
document.getElementById('currentYear').textContent = currentYear;