function simplifyCodeBlocks() {
    // Verifica si el ancho de la pantalla es menor a 800px
    if (window.innerWidth < 800) {
        // Selecciona todos los bloques <code> dentro de .code-window
        const codeBlocks = document.querySelectorAll('.code-window code');

        codeBlocks.forEach(block => {
            // Si ya fue simplificado, no lo vuelvas a hacer
            if (!block.hasAttribute('data-original-html')) {
                // Guarda el contenido original por si se necesita restaurar
                block.setAttribute('data-original-html', block.innerHTML);
                // Reemplaza el contenido HTML con texto plano
                block.textContent = block.textContent;
            }
        });
    } else {
        // Si la pantalla se agranda de nuevo, restauramos el HTML original
        const codeBlocks = document.querySelectorAll('.code-window code');

        codeBlocks.forEach(block => {
            const original = block.getAttribute('data-original-html');
            if (original) {
                block.innerHTML = original;
                block.removeAttribute('data-original-html');
            }
        });
    }
}

// Ejecuta cuando se carga la página
window.addEventListener('load', simplifyCodeBlocks);
// También cuando se cambia el tamaño de la ventana
window.addEventListener('resize', simplifyCodeBlocks);
