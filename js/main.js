// Simple CV interactivity
document.addEventListener('DOMContentLoaded', function() {
    // Smooth scroll for any internal links
    document.querySelectorAll('a[href^="#"]').forEach(anchor => {
        anchor.addEventListener('click', function (e) {
            e.preventDefault();
            const target = document.querySelector(this.getAttribute('href'));
            if (target) {
                target.scrollIntoView({
                    behavior: 'smooth'
                });
            }
        });
    });

    // Add print functionality
    const addPrintButton = () => {
        const header = document.querySelector('.header');
        if (header && !document.querySelector('.print-button')) {
            const printBtn = document.createElement('button');
            printBtn.textContent = 'Print CV';
            printBtn.className = 'print-button';
            printBtn.style.cssText = `
                position: fixed;
                bottom: 20px;
                right: 20px;
                padding: 12px 24px;
                background: #3498db;
                color: white;
                border: none;
                border-radius: 4px;
                cursor: pointer;
                font-size: 1rem;
                box-shadow: 0 2px 10px rgba(0,0,0,0.2);
                z-index: 1000;
            `;
            printBtn.addEventListener('click', () => window.print());
            document.body.appendChild(printBtn);
        }
    };

    addPrintButton();
});
