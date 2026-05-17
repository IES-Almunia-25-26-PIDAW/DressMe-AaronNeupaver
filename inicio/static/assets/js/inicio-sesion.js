document.addEventListener("DOMContentLoaded", () => {
    const campoUsuario = document.getElementById('usuario');
    const campoCorreo = document.getElementById('email');
    const campoContrasena = document.getElementById('password');
    const formulario = document.querySelector('.iniciar-sesion__formulario');

    function mostrarNotificacion(mensaje, tipo, callback = null) {
        const notificacionExistente = document.querySelector('.notificacion');
        if (notificacionExistente) {
            notificacionExistente.remove();
        }

        const notificacion = document.createElement('div');
        notificacion.classList.add('notificacion', `notificacion--${tipo}`);
        notificacion.textContent = mensaje;
        document.body.appendChild(notificacion);


        setTimeout(() => {
            notificacion.classList.add('mostrar');
        }, 10);


        setTimeout(() => {
            notificacion.classList.remove('mostrar');
            setTimeout(() => {
                notificacion.remove();
                if (callback) callback();
            }, 300);
        }, 2000);
    }


    function irARegistro() {
        const btnRegistro = document.querySelector('.iniciar-sesion__btn-registro');
        if (btnRegistro && btnRegistro.getAttribute('data-url')) {
            window.location.href = btnRegistro.getAttribute('data-url');
        } else {

            window.location.href = '/registro/';
        }
    }

});
