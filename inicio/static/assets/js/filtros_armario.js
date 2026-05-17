function filtrarPrendas(categoria, botonElement) {
    const botones = document.querySelectorAll('.cuerpo-principal-filtros button');
    botones.forEach(btn => {
        btn.classList.remove('cuerpo-principal-filtros-boton-activo');
        btn.classList.add('cuerpo-principal-filtros-boton');
    });
    
    botonElement.classList.remove('cuerpo-principal-filtros-boton');
    botonElement.classList.add('cuerpo-principal-filtros-boton-activo');

    const prendas = document.querySelectorAll('.cuerpo-principal-añadidos-item-añadido');
    prendas.forEach(prenda => {
        if (categoria === 'Todos') {
            prenda.style.display = '';
        } else {
            if (prenda.getAttribute('data-categoria') === categoria) {
                prenda.style.display = '';
            } else {
                prenda.style.display = 'none';
            }
        }
    });
}
