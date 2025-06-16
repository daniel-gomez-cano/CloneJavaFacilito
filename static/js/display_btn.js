document.addEventListener("DOMContentLoaded", () => {
    const sidebar = document.querySelector(".sidebar");
    const overlay = document.getElementById("overlay");
    const toggleBtn = document.getElementById("menu-toggle");
    const menuLinks = document.querySelectorAll(".menu a");

    // Mostrar sidebar (responsive)
    toggleBtn.addEventListener("click", () => {
        sidebar.classList.add("show");
        overlay.classList.add("active");
        toggleBtn.classList.add("hidden"); // Oculta botón
    });

    // Ocultar sidebar
    overlay.addEventListener("click", () => {
        sidebar.classList.remove("show");
        overlay.classList.remove("active");
        toggleBtn.classList.remove("hidden"); // Vuelve a mostrar botón
    });

    // Ocultar sidebar al navegar (responsive)
    menuLinks.forEach(link => {
        link.addEventListener("click", () => {
            if (window.innerWidth <= 1024) {
                sidebar.classList.remove("show");
                overlay.classList.remove("active");
                toggleBtn.classList.remove("hidden");
            }
        });
    });
});
