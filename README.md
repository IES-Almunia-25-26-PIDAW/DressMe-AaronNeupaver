<h2 align="center">🌐 Otros Idiomas</h2>

<p align="center">
  <a href="#">
    🇪🇸 <strong>Spanish</strong>
  </a> &nbsp;·&nbsp;
  <a href="#">
    🇫🇷 <strong>French</strong>
  </a> &nbsp;·&nbsp;
  <a href="#">
    🇯🇵 <strong>Japanese</strong>
  </a>
</p>

<h1 align="center">👕 DressMe</h1>

<p align="center">
  <em>Porque a veces la única forma de decidir qué ponerte... es que una IA lo haga por ti.</em>
</p>

<p align="center">
  Esta idea nació del clásico problema de mirar un armario lleno de ropa y pensar: "No tengo nada que ponerme".<br>
  Combinar colores, recordar qué prendas tienes limpias o simplemente tener creatividad por la mañana a veces es una auténtica pesadilla.<br><br>
  <strong>¡Aquí tienes la solución!</strong><br>
  Esta aplicación web digitaliza tu armario y utiliza algoritmos para generarte el outfit perfecto para cada día.
</p>

---

<p align="center">
  <a href="https://dressme-aaronneupaver-production.up.railway.app/">
    <img src="https://img.shields.io/badge/🚀 Demo-DressMe-blue?style=for-the-badge" alt="Demo">
  </a>
  &nbsp;
  <a href="#">
    <img src="https://img.shields.io/badge/📘 Wiki-Documentation-green?style=for-the-badge" alt="Wiki">
  </a>
  &nbsp;
  <a href="#">
    <img src="https://img.shields.io/badge/📘 Contributing-Documentation-pink?style=for-the-badge" alt="CONTRIBUTING">
  </a>
</p>

## Significado de la aplicación
DressMe es un gestor de armario digital y asistente de moda. Permite a los usuarios tener un inventario visual de su ropa, categorizarla y delegar la decisión de combinar prendas en un algoritmo generativo de conjuntos (*outfits*).

## Arquitectura del Proyecto

1. Construido con el framework **Django** (Python) usando el patrón Modelo-Plantilla-Vista (MTV).
2. Estilos personalizados mediante **CSS Nativo** (+1000 líneas).
3. Base de datos relacional para gestionar Usuarios, Prendas y Outfits Favoritos.

## ¿Cómo instalar el proyecto en local?

1. Clona este repositorio en tu ordenador.
2. Abre la consola en la carpeta del proyecto.
3. Activa un entorno virtual (recomendado): `python -m venv env` y luego actívalo con `env\Scripts\activate` (Windows).
4. Instala las dependencias necesarias:
   ```bash
   pip install -r requirements.txt
   ```
5. Realiza las migraciones para crear la base de datos:
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```
6. Ejecuta el servidor local:
   ```bash
   python manage.py runserver
   ```
7. Abre el navegador en `http://127.0.0.1:8000`.

**¡LISTO PARA DIGITALIZAR TU ARMARIO!**

---

## PREGUNTAS DE EVALUACIÓN

### Ciclo de vida del dato (5b)

#### ¿Cómo se gestionan los datos desde su generación hasta su eliminación en tu proyecto?
Los datos se generan cuando el usuario se registra o sube una nueva prenda (imagen + categoría). Se almacenan en una base de datos relacional (SQLite en desarrollo). Para la eliminación, se ha implementado un `Signal` de Django (`post_delete`) que asegura que al borrar una prenda, no solo se elimine el registro de la BBDD, sino también el archivo físico de la imagen en el servidor.

#### ¿Qué estrategia sigues para garantizar la consistencia e integridad de los datos?
- Uso de claves foráneas (`ForeignKey`) vinculadas a los usuarios mediante `on_delete=models.CASCADE`.
- Validación a través del ORM de Django para asegurar que los campos obligatorios se rellenan.
- Las imágenes pasan por la librería `Pillow` para garantizar que el archivo subido es efectivamente una imagen válida.

### Almacenamiento en la nube (5f)

#### Si tu software usa almacenamiento en la nube, ¿cómo garantizas la seguridad y disponibilidad?
- En producción (ej. Railway), se sirve usando HTTPS y `WhiteNoise` para la entrega eficiente de archivos estáticos.
- La base de datos es aislada y se realizan copias de seguridad de los volúmenes.

#### ¿Qué alternativas consideraste y por qué elegiste esta?
Se usó SQLite para el entorno de desarrollo por su inmediatez, pero se preparó el proyecto para inyectar bases de datos en la nube (PostgreSQL) usando variables de entorno para producción.

#### ¿Cómo podrías integrar la nube en el futuro?
Integrando Amazon S3 (AWS) o Cloudinary para almacenar y procesar las imágenes de las prendas, lo que reduciría la carga en el servidor web.

### Seguridad y regulación (5i)

#### ¿Qué medidas de seguridad implementaste?
- Las contraseñas de usuario nunca se guardan en texto plano, están hasheadas mediante PBKDF2 (gestión nativa de Django).
- Se aplica protección CSRF (Cross-Site Request Forgery) en todos los formularios para evitar ataques de suplantación.
- Verificación estricta de sesiones (`request.user.is_authenticated`) en todas las vistas privadas.

#### ¿Qué normativas podrían afectar (como GDPR)?
Al recopilar correos electrónicos e imágenes de pertenencias, aplica la GDPR. El sistema cumple el derecho al olvido: si un usuario borra su cuenta, la cascada de la BBDD elimina absolutamente todos sus datos y fotos del servidor automáticamente.

### Implicación de las THD en negocio y planta (2e)

#### ¿Qué impacto tendría en un negocio o planta?
A nivel de negocio de Retail/Moda, digitalizar inventarios a nivel usuario permite la integración con tiendas online (sugerir comprar un pantalón negro si la IA detecta que no tienes uno para hacer match con tus camisetas).

#### ¿Cómo podría mejorar procesos o decisiones?
Agiliza la toma de decisiones diaria (ahorro de tiempo por la mañana) y fomenta la moda sostenible, ayudando al usuario a sacar partido a ropa que ya tiene en lugar de comprar compulsivamente.

#### ¿Qué otros entornos se beneficiarían?
El sector del e-commerce de moda y los estilistas personales o asesores de imagen.

### Mejoras en IT y OT (2f)

#### ¿Cómo puede facilitar integración IT-OT?
Adaptado al retail, los datos del usuario (IT) se pueden cruzar con el inventario físico (OT) de un almacén para sugerir compras basadas en combinaciones algorítmicas de stock real.

#### ¿Qué procesos específicos se beneficiarían?
- La catalogación y categorización de inventarios personales.
- La generación automática de propuestas y combinatorias.

### Tecnologías Habilitadoras Digitales (2g)

#### ¿Qué THD has usado o podrías usar?
- **Algoritmia y Lógica Combinatoria:** Usada actualmente para generar los *outfits* basados en filtros lógicos.
- **Computer Vision / IA (Futuro):** Una red neuronal que autocategorice la ropa (ej. si es manga larga, corta, color) con solo subir la foto, sin que el usuario tenga que etiquetarla a mano.

#### ¿Cómo mejoran la funcionalidad o alcance?
La IA visual (Computer Vision) eliminaría la barrera de entrada para digitalizar un armario (escribir características una a una), haciendo el proceso masivo y automático, multiplicando el uso potencial de la aplicación.
