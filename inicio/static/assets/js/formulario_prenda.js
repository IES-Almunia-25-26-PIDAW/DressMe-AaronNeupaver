function abrirFormularioPrenda() {
    document.getElementById('formularioPrendaFlotante').style.display = 'flex';
}

function cerrarFormularioPrenda() {
    document.getElementById('formularioPrendaFlotante').style.display = 'none';
}

window.onclick = function(event) {
    var formulario = document.getElementById('formularioPrendaFlotante');
    if (event.target == formulario) {
        cerrarFormularioPrenda();
    }
}
