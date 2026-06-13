# Documentación Técnica - DressMeProject

## 1. Introducción
**DressMe** es una aplicación web desarrollada bajo el framework **Django** (Python) que permite a los usuarios digitalizar su armario, subir fotos de sus prendas clasificadas por categorías y generar *outfits* (conjuntos) de manera automática mediante un algoritmo generativo. Además, ofrece la posibilidad de guardar los conjuntos favoritos en el perfil del usuario.

## 2. Arquitectura del Sistema
El proyecto sigue la arquitectura estándar **MTV (Model-Template-View)** de Django, asegurando una clara separación de responsabilidades:
- **Modelos (`models.py`)**: Definen la estructura de la base de datos relacional y las restricciones de integridad (ej. borrado en cascada).
- **Vistas (`views.py`)**: Contienen la lógica de negocio, gestionando peticiones HTTP, algoritmos de selección y comunicación con la base de datos.
- **Plantillas (`templates/`)**: Archivos HTML que utilizan el motor de plantillas de Django para renderizar contenido dinámico, estilizados con CSS nativo (`styles.css` con +1000 líneas de reglas estructuradas usando variables nativas y *flexbox*/*grid*).

## 3. Modelo de Datos (Diagrama Entidad-Relación)
El sistema utiliza una base de datos relacional (preparada para SQLite en desarrollo y migrable a PostgreSQL en producción) con tres entidades principales.

### Entidades y Atributos

**1. Tabla `auth_user` (Django Standard)**
- `id`: PK (Clave Primaria)
- `username`: String, Unique
- `password`: String (Hashed)
- `email`: String

**2. Tabla `Prenda`**
- `id`: PK, AutoField
- `usuario`: FK -> `auth_user(id)`, ON DELETE CASCADE. Cada prenda pertenece a un usuario específico.
- `nombre`: CharField (max 100)
- `categoria`: CharField (Camiseta, Pantalón, Zapato, Accesorio)
- `imagen`: ImageField (almacena la ruta en disco, procesada con la librería `Pillow`)
- `fecha_creacion`: DateTimeField (AutoNowAdd)

**3. Tabla `OutfitFavorito`**
- `id`: PK, AutoField
- `usuario`: FK -> `auth_user(id)`, ON DELETE CASCADE
- `fecha_creacion`: DateTimeField (AutoNowAdd)
- **Relación N:M (Many-To-Many)**: A través de una tabla intermedia implícita hacia `Prenda`. Un outfit contiene múltiples prendas y una prenda puede pertenecer a múltiples outfits.

### Triggers / Señales (`Signals`)
Se ha implementado una señal `post_delete` de Django en `models.py` que se asegura de eliminar **físicamente** la imagen del disco/servidor cuando el registro de la `Prenda` es borrado de la base de datos por el usuario, optimizando así el almacenamiento del sistema y evitando "archivos huérfanos".

## 4. Algoritmo de Generación de Outfits (IA / Algoritmia)
La funcionalidad de "Generar Outfit" ubicada en la vista `ia_outfits` implementa un algoritmo de filtrado, clasificación y selección probabilística. 

**Proceso Lógico:**
1. **Extracción y Filtrado**: Se consulta la base de datos mediante el ORM filtrando únicamente las prendas pertenecientes al usuario de la sesión actual.
2. **Clasificación Lógica**: Se dividen las prendas en cuatro categorías lógicas en memoria: `Camisetas`, `Pantalones`, `Zapatos` y `Accesorios`.
3. **Validación de Completitud**: El algoritmo verifica que exista el mínimo viable en el sistema para crear un conjunto lógico (al menos 1 elemento de torso, 1 de piernas y 1 de calzado). De no ser así, frena la ejecución y levanta una alerta controlada.
4. **Composición Base**: Selecciona aleatoriamente una prenda de las categorías obligatorias.
5. **Modificador de Complejidad**: Introduce una variación estadística (70% de probabilidad) para decidir dinámicamente si el outfit incluye un accesorio extra, imitando el razonamiento humano de variabilidad al vestir.

## 5. Endpoints y Lógica de Vistas Principales
- `home`: Landing page introductoria.
- `register_user` / `inicio_sesion`: Autenticación y control de acceso seguro mediante hashing PBKDF2 y manejo de middlewares de sesiones.
- `dashboard`: Panel de control analítico. Realiza múltiples consultas (ORM) para calcular porcentajes lógicos de uso de armario y extraer estadísticas temporales (outfits de los últimos 7 días).
- `armario`: Permite el CRUD de las prendas, manejando codificación `multipart/form-data` para la subida segura de imágenes al servidor.
- `eliminar_prenda`: Endpoint protegido por ID de prenda. Realiza un borrado en cascada.
- `ia_outfits`: Punto de entrada del algoritmo generativo de ropa.
- `favoritos` y `guardar_outfit`: Gestión compleja de guardado donde se insertan tuplas en la tabla intermedia de la relación M2M.

## 6. Consideraciones Técnicas y de Rendimiento
- **Middlewares de Producción**: Uso intensivo de `whitenoise` configurado en `settings.py` para servir archivos estáticos (CSS, Assets) eficientemente con compresión en entornos de producción (Railway).
- **Seguridad Activa**: Todas las vistas funcionales validan el estado de sesión `request.user.is_authenticated`, evitando accesos directos a URLs sin permiso (Bypass routing). Implementación estricta de protección **CSRF (Cross-Site Request Forgery)** en todos los formularios.
- **Diseño UI/UX (CSS Arquitectónico)**: Interfaz completamente nativa (Vanilla CSS) de más de 1000 líneas. No se ha dependido de frameworks genéricos pesados (como Bootstrap/Tailwind) para garantizar el máximo rendimiento de renderizado en el navegador, utilizando en su lugar el control total mediante variables nativas CSS (`:root`), Flexbox y Grid Layout.
