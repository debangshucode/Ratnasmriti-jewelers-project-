document.addEventListener('DOMContentLoaded', () => {
    // Mobile navigation toggle functionality
    const menuToggle = document.getElementById('menu-toggle');
    if (menuToggle) {
        menuToggle.addEventListener('click', function() {
            var nav = document.querySelector('.mobile-nav');
            if (nav) {
                nav.classList.toggle('open');
            }
        });
    }

    // Slider functionality
    let slideIndex = 0;
    let slides = document.getElementsByClassName("slide");
    let slidesContainer = document.querySelector(".slides");

    if (slides.length > 0 && slidesContainer) {
        function showSlides() {
            slidesContainer.style.transition = "transform 0.5s ease-in-out";
            slidesContainer.style.transform = `translateX(${-slideIndex * 100}%)`;
        }

        function nextSlide() {
            slideIndex = (slideIndex + 1) % slides.length;
            showSlides();
        }

        function prevSlide() {
            slideIndex = (slideIndex - 1 + slides.length) % slides.length;
            showSlides();
        }

        document.querySelector(".next").addEventListener("click", nextSlide);
        document.querySelector(".prev").addEventListener("click", prevSlide);

        // Set interval to change slides automatically every 5 seconds (5000 milliseconds)
        setInterval(nextSlide, 5000);

        // Initial call to set the first slide
        showSlides();
    }

    // Quantity change functionality
    const quantityInput = document.getElementById('quantity');
    if (quantityInput) {
        document.getElementById('decrease').addEventListener('click', () => changeQuantity(-1));
        document.getElementById('increase').addEventListener('click', () => changeQuantity(1));

        function changeQuantity(amount) {
            let currentQuantity = parseInt(quantityInput.value);
            currentQuantity += amount;

            if (currentQuantity < 1) {
                currentQuantity = 1;
            }

            quantityInput.value = currentQuantity;
        }
    }
    const mainImage = document.getElementById('main-product-image');
    const zoomResult = document.getElementById('zoom-result');

    if (mainImage && zoomResult) {
        const zoomLens = document.createElement('div');
        zoomLens.style.position = 'absolute';
        zoomLens.style.border = '1px solid #d4d4d4';
        zoomLens.style.width = '100px';
        zoomLens.style.height = '100px';
        zoomLens.style.opacity = '0.4';
        zoomLens.style.backgroundColor = 'white';
        zoomLens.style.cursor = 'move';
        mainImage.parentElement.insertBefore(zoomLens, mainImage);

        zoomResult.style.backgroundImage = `url('${mainImage.src}')`;

        const moveLens = (e) => {
            e.preventDefault();
            const pos = getCursorPos(e);
            let x = pos.x - (zoomLens.offsetWidth / 2);
            let y = pos.y - (zoomLens.offsetHeight / 2);

            if (x > mainImage.width - zoomLens.offsetWidth) { x = mainImage.width - zoomLens.offsetWidth; }
            if (x < 0) { x = 0; }
            if (y > mainImage.height - zoomLens.offsetHeight) { y = mainImage.height - zoomLens.offsetHeight; }
            if (y < 0) { y = 0; }

            zoomLens.style.left = `${x}px`;
            zoomLens.style.top = `${y}px`;

            zoomResult.style.backgroundPosition = `-${x * 3}px -${y * 3}px`;
            zoomResult.style.display = 'block';
        };

        const getCursorPos = (e) => {
            e = e || window.event;
            const a = mainImage.getBoundingClientRect();
            const x = e.pageX - a.left;
            const y = e.pageY - a.top;
            return { x: x - window.pageXOffset, y: y - window.pageYOffset };
        };

        mainImage.addEventListener('mousemove', moveLens);
        zoomLens.addEventListener('mousemove', moveLens);

        mainImage.addEventListener('mouseleave', () => {
            zoomResult.style.display = 'none';
        });

        zoomLens.addEventListener('mouseleave', () => {
            zoomResult.style.display = 'none';
        });

        zoomLens.addEventListener('mousemove', moveLens);
    }
});
