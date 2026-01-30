import express from 'express';
import { obtenerTodas, agregarPrenda } from '../logica/GestorArmario.js'; // ¡Reusas la lógica!

const app = express();
app.use(express.json());

// Endpoint para que React pida la ropa
app.get('/api/ropa', (req, res) => {
    const ropa = obtenerTodas();
    res.json(ropa);
});

// Endpoint para subir ropa desde React
app.post('/api/ropa', (req, res) => {
    const { nombre, categoria, color } = req.body;
    const nueva = agregarPrenda(nombre, categoria, color);
    res.json(nueva);
});

app.listen(3000, () => console.log('Servidor DressMe corriendo en puerto 3000'));