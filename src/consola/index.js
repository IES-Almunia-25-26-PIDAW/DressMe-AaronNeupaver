// src/consola/index.js
import readline from 'readline';
import {agregarPrenda, obtenerTodas, Categorias, sugerirOutfit} from '../logica/GestorArmario.js';
const rl = readline.createInterface({ input: process.stdin, output: process.stdout });

function pedirPrenda() {
    rl.question('Nombre de la prenda: ', (nombre) => {
        // Mostramos las opciones del "Enum"
        console.log("\nSelecciona una categoría:");
        console.log("1. Parte Superior");
        console.log("2. Parte Inferior");
        console.log("3. Calzado");
        console.log("4. Accesorios");

        rl.question('Elige el número: ', (num) => {
            let catSeleccionada;
            switch(num) {
                case '1': catSeleccionada = Categorias.PARTE_SUPERIOR; break;
                case '2': catSeleccionada = Categorias.PARTE_INFERIOR; break;
                case '3': catSeleccionada = Categorias.CALZADO; break;
                case '4': catSeleccionada = Categorias.ACCESORIOS; break;
                default: catSeleccionada = Categorias.ACCESORIOS;
            }

            rl.question('Color: ', (color) => {
                agregarPrenda(nombre, catSeleccionada, color);
                console.log(`\n✅ ¡${nombre} guardado en ${catSeleccionada}!`);
                mostrarMenu();
            });
        });
    });
}

function mostrarMenu() {
    console.log("\n=== DRESSME (MODO CONSOLA) ===");
    console.log("1. Ver Armario");
    console.log("2. Añadir Prenda");
    console.log("3. Sugerir Outfit (IA Beta)");
    console.log("4. Salir");

    rl.question('Elige una opción: ', (opcion) => {
        switch(opcion) {
            case '1':
                console.log("\n--- TU ROPA ---");
                console.table(obtenerTodas()); // console.table queda muy pro
                mostrarMenu();
                break;


            case '2':
                // Borra todo el código viejo de rl.question que había aquí
                pedirPrenda(); // Llama a la función que usa el Enum
                break;

            case '3':
                console.log("\n🤖 DRESSME AI SUGIERE:");
                console.log(sugerirOutfit());
                mostrarMenu();
                break;

            case '4':
                console.log("¡Adiós!");
                rl.close();
                break;

            default:
                console.log("Opción no válida");
                mostrarMenu();
        }
    });
}

// Arrancamos la app
mostrarMenu();