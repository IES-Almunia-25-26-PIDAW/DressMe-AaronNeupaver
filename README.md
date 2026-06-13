

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
