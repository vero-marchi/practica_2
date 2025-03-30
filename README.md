# Proyecto: TRABAJO PRÁCTICO N°2

## Descripción
Este proyecto consiste en la solución de los ejercicicios del trabajo práctico 2.
Por un lado se encuentran la solución al ejercicio 10 y por otro lado la solución al resto de los ejercicios.

En cuanto al ejercicio 10, el programa es una simulación de un juego de Shooter Online donde se procesan las estadísticas de los jugadores a lo largo de varias rondas. 
El programa calcula puntos acumulados, busca jugadores MVP en cada ronda y genera un ranking final con la sumatoria de puntos de todas las rondas.

---

## Estructura del Proyecto
El proyecto está organizado de la siguiente manera:
- notebooks/:
    - shooter_online.ipynb (Notebook del programa que da solución al ejercicio 10)
    - ejercicios.ipynb (Notebook del programa que da solución al resto de los ejercicios)
- src/:
    - game_functions.py (Archivo con todas las funciones necesarias para ejecutar el programa shooter_online)
    - funciones.py (Archivo con las funciones necesarias para ejecutar las soluciones de ejercicios.py)
- __init__.py (Hace que la carpeta src sea un paquete Python para importar funciones)
- .gitignore (Excluye archivos innecesarios del repositorio)
- requirements.txt (lista de dependencias necesarias para ejecutar el programa)
- README.md (guía del proyecto)

---

## Instalación

Realiza los pasos detallados a continuación para instalar y ejecutar el proyecto:

### 1. Obtener el repositorio
- Opción 1:
Descargar como archivo ZIP desde github. Desde el botón verde **Code** y selecciona **Download ZIP**. Luego extrae el contenido en tu máquina local.
- Opción 2: 
Descarga el proyecto desde GitHub usando el siguiente comando en tu terminal:
git clone https://github.com/vero-marchi/practica_2.git


### 2. Activar entorno virtual

Crear y activar un entorno virtual
Ejecuta los siguientes comandos:
```bash
python -m venv venv
```
En Windows:
```bash
venv\Scripts\activate
```

En Mac/Linux:
```bash
source venv/bin/activate
```
Una vez activado el entorno, deberías ver (venv) al inicio de tu terminal, indicando que estás trabajando dentro del entorno virtual.

### 3. Instalar dependencias
Con el entorno virtual activado, instala las dependencias necesarias usando el archivo requirements.txt:
```bash
pip install -r requirements.txt
```

### Ejecución del Programa
Abre el notebook principal en Jupyter Notebook:
```bash
jupyter notebook notebooks/shooter_online.ipynb
```

Ejecuta las celdas del notebook para simular el programa. 
Asegúrate de seguir las instrucciones iniciales para realizar los imports necesarios.

### Observaciones
- Este proyecto fue desarrollado y probado con **Python 3.12.9**, pero debería ser compatible con Python 3.8 o superior. Verifica tu versión ejecutando:
```bash
python --version
```
### Datos alumna
Veronica Mariana Marchi
leg. 18161/8



