## Data CSV Normalizer (Pandas)

Herramienta interactiva por línea de comandos (CLI) desarrollada en Python y Pandas, diseñada para automatizar el diagnóstico, la normalización y el tratamiento inteligente de valores faltantes en conjuntos de datos estructurados (CSV).

El sistema analiza dinámicamente las propiedades del archivo para aislar identificadores (IDs) y fechas mediante reglas contextuales, ofreciendo menús de limpieza personalizados (imputación estadística o manual) y exportando el resultado limpio de forma dinámica y automatizada. Ideal para agilizar la etapa de preprocesamiento en flujos de trabajo de Ciencia de Datos.

---

## 🎯 Características Clave

* **Diagnóstico Automatizado (`info`):** Inspección rápida del DataFrame que detalla dimensiones, tipos de datos de Pandas y conteo preciso de valores nulos (`NaN`) por columna.
  
* **Normalización Estándar de Columnas:** Remoción de espacios en blanco, conversión a minúsculas y sustitución de espacios por guiones bajos (`snake_case`) de manera automatizada.
  
**Tratamiento Inteligente de Nulos:**
  
  * **Opciones por Tipo de Dato:** El programa muestra diferentes opciones para el tratamiento de nulos dependiendo el tipo de dato de los valores que almacena la columna mediante **Moda, Promedio, Mediana, valores fijos o edición manual uno a uno (1x1)** interactiva.
  * **Detección de ID/Matrícula:** Detecta automáticamente si una columna es un ID para un tratamiento más personalizado como: limpieza manual o llenado de los registros vacíos 1x1.
  * **Detección de Fechas:** Detecta columnas de fechas aplicando parseo flexible y formateo estandarizado.
  
* **Gestión Dinámica de Archivos:** Exportación automatizada que hereda el nombre del archivo original y le añade el sufijo `_clean.csv` de forma transparente utilizando la librería estándar `pathlib`.

---

## 🛠️ Tecnologías Utilizadas

* **Python 3.x**
* **Pandas:** Para la manipulación eficiente de estructuras de datos en memoria.
* **Pathlib:** Para la gestión e inferencia segura de rutas en el sistema de archivos.

---

## 💻 Requisitos e Instalación

Sigue estos pasos para configurar y ejecutar la herramienta en tu entorno local de manera sencilla:

1. **Preparar el entorno de desarrollo:**
   * **Contar con Python instalado:** Este proyecto fue desarrollado en **Python 3.x**. Si no lo tienes, descárgalo desde su [sitio oficial](https://www.python.org). Durante la instalación en Windows, asegúrate de marcar la casilla **"Add Python to PATH"**.
   * **Instalar la librería Pandas:** Abre tu terminal (CMD) e instala la dependencia requerida ejecutando:
     ```bash
     pip install pandas
     ```

2. **Clonar el repositorio y acceder al directorio:**
   Obtén una copia local del proyecto directamente en tu escritorio y navega hacia la carpeta raíz ejecutando el siguiente comando:
   ```bash
   cd Desktop && git clone https://github.com/3rick-CR/data-csv-normalizer-pandas.git
   ```

   Nota: se creara una carpeta en el escritorio "data-csv-normalizer-pandas" contiene el .py

   - Una vez configurado el entorno, ir a la ruta de la carpeta que se creo en el paso anterior con el siguiente comando:
   ```bash
   cd data-csv-normalizer-pandas
   ```
3. **Ejecutar el programa:**
   
   **Importante**: antes de continuar verificar que el archivo csv a limpiar se encuentre dentro de la misma carpeta "data-csv-normalizer-pandas" en el escritorio

    Continuamos en la terminal CMD y ejecutamos el programa con el siguiente comando:
   
   ```bash
   python normalizador_csv.py
   ```

### 🛠️ Vista Previa del Programa (CLI):
