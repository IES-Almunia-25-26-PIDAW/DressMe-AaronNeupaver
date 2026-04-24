document.addEventListener("DOMContentLoaded", () => {
    const campoUsuario = document.getElementById('usuario');
    const campoCorreo = document.getElementById('email');
    const campoContrasena = document.getElementById('password');
    const formulario = document.querySelector('.iniciar-sesion__formulario');

    // Función para mostrar notificación personalizada
    function mostrarNotificacion(mensaje, tipo, callback = null) {
        // Remover notificación existente si hay alguna
        const notificacionExistente = document.querySelector('.notificacion');
        if (notificacionExistente) {
            notificacionExistente.remove();
        }

        const notificacion = document.createElement('div');
        notificacion.classList.add('notificacion', `notificacion--${tipo}`);
        notificacion.textContent = mensaje;
        document.body.appendChild(notificacion);

        // Activar animación
        setTimeout(() => {
            notificacion.classList.add('mostrar');
        }, 10);

        // Ocultar y remover después de 2 segundos, luego ejecutar el callback
        setTimeout(() => {
            notificacion.classList.remove('mostrar');
            setTimeout(() => {
                notificacion.remove();
                if (callback) callback();
            }, 300); // Tiempo que tarda la transición en CSS
        }, 2000);
    }

    // Función para redirigir a la página de registro
    function irARegistro() {
        const btnRegistro = document.querySelector('.iniciar-sesion__btn-registro');
        if (btnRegistro && btnRegistro.getAttribute('data-url')) {
            window.location.href = btnRegistro.getAttribute('data-url');
        } else {
            // Fallback por si acaso no encuentra el botón
            window.location.href = '/registro/'; // O el URL por defecto de registro
        }
    }

});
