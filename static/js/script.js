document.addEventListener('DOMContentLoaded', function() {
    const newsForm = document.getElementById('news-form');
    const newsText = document.getElementById('news-text');
    const characterCount = document.querySelector('.character-count');
    const resultCard = document.getElementById('result-card');
    const loadingSpinner = document.getElementById('loading');
    
    // Update character count
    newsText.addEventListener('input', function() {
        const count = this.value.length;
        characterCount.textContent = `${count} characters`;
        
        // Change color based on length
        if (count > 1000) {
            characterCount.style.color = '#e74c3c';
        } else if (count > 500) {
            characterCount.style.color = '#f39c12';
        } else {
            characterCount.style.color = '';
        }
    });
    
    // Form submission - show loading
    if (newsForm) {
        newsForm.addEventListener('submit', function() {
            if (newsText.value.trim() === '') {
                alert('Please enter a news article or headline.');
                return false;
            }
            
            // Show loading spinner
            loadingSpinner.classList.add('show');
        });
    }
    
    // Reset form
    if (newsForm) {
        newsForm.addEventListener('reset', function() {
            // Reset character count
            characterCount.textContent = '0 characters';
            characterCount.style.color = '';
            
            // Hide result card if it exists
            if (resultCard) {
                resultCard.classList.remove('show');
            }
            
            // Focus on input
            newsText.focus();
        });
    }
    
    // If there's a confidence-fill element, animate it after page load
    const confidenceFill = document.getElementById('confidence-fill');
    if (confidenceFill && confidenceFill.style.width === '') {
        setTimeout(() => {
            const width = confidenceFill.getAttribute('data-width') || '0';
            confidenceFill.style.width = width + '%';
        }, 100);
    }
    
    // Add parallax effect to background shapes
    document.addEventListener('mousemove', function(e) {
        const shapes = document.querySelectorAll('.news-shape');
        const x = e.clientX / window.innerWidth;
        const y = e.clientY / window.innerHeight;
        
        shapes.forEach((shape, index) => {
            const speed = (index + 1) * 20;
            const xOffset = (x - 0.5) * speed;
            const yOffset = (y - 0.5) * speed;
            
            shape.style.transform = `translate(${xOffset}px, ${yOffset}px)`;
        });
    });
});