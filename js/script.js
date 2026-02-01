document.addEventListener('DOMContentLoaded', () => {
    // Smooth scrolling for navigation links
    document.querySelectorAll('a[href^="#"]').forEach(anchor => {
        anchor.addEventListener('click', function (e) {
            e.preventDefault();
            const targetId = this.getAttribute('href').substring(1);
            const targetElement = document.getElementById(targetId);

            if (targetElement) {
                targetElement.scrollIntoView({
                    behavior: 'smooth'
                });
            }
        });
    });


    // Auto-hide floating dock when reaching the bottom footer/education area
    const dockContainer = document.querySelector('.floating-dock-container');
    // Distance from bottom to trigger hide (roughly the height of the education card + margins)
    const fadeThreshold = 200;

    if (dockContainer) {
        window.addEventListener('scroll', () => {
            const scrollPosition = window.scrollY + window.innerHeight;
            const docHeight = document.documentElement.scrollHeight;

            // If we are close to the bottom, hide the dock
            if (scrollPosition >= docHeight - fadeThreshold) {
                dockContainer.classList.add('dock-hidden');
            } else {
                dockContainer.classList.remove('dock-hidden');
            }
        });
    }
});
