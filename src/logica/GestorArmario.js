// src/logica/GestorArmario.js


export const Categorias = Object.freeze({
    PARTE_SUPERIOR: "Parte Superior",
    PARTE_INFERIOR: "Parte Inferior",
    CALZADO: "Calzado",
    ACCESORIOS: "Accesorios"
});
// Simulamos una base de datos con un array (luego esto será PostgreSQL)
const baseDeDatos = [];

export function agregarPrenda(nombre, categoria, color) {
    const nuevaPrenda = {
        id: baseDeDatos.length + 1,
        nombre,
        categoria, // Aquí llegará el valor del Enum
        color,
        fecha: new Date().toISOString()
    };
    baseDeDatos.push(nuevaPrenda);
    return nuevaPrenda;
}

export function obtenerTodas() {
    return baseDeDatos;
}

export function buscarPorCategoria(categoria) {
    return baseDeDatos.filter(prenda => prenda.categoria === categoria);
}

// Aquí iría tu lógica de IA más adelante
export function sugerirOutfit() {
    if (baseDeDatos.length === 0) return "El armario está vacío.";
    const random = Math.floor(Math.random() * baseDeDatos.length);
    return baseDeDatos[random];
}