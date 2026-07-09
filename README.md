## data-csv-normalizer-pandas
Herramienta interactiva por línea de comandos (CLI) desarrollada en Python y Pandas, diseñada para automatizar el diagnóstico, la normalización y el tratamiento inteligente de valores faltantes en conjuntos de datos estructurados (CSV).
El sistema analiza dinámicamente las propiedades del archivo para aislar identificadores (IDs) y fechas mediante reglas contextuales, ofreciendo menús de limpieza personalizados (imputación estadística o manual) y exportando el resultado limpio de forma dinámica y automatizada. Ideal para agilizar la etapa de preprocesamiento en flujos de trabajo de Ciencia de Datos.

---

## 🎯 Características Clave

*   **Diagnóstico Automatizado (`info`):**
    Inspección rápida del DataFrame que detalla dimensiones, tipos de datos de Pandas y conteo preciso de valores nulos (`NaN`) por columna.
  
*   **Normalización Estándar de Columnas:**
*   Remoción de espacios en blanco, conversión a minúsculas y sustitución de espacios por guiones bajos (`snake_case`) de manera automatizada.
  
*   **Tratamiento Inteligente de Nulos:**
*   El programa muestra diferentes opciones para el tratamiento de nulos dependiendo el tipo de dato de los valores que almacena la columna mediante **Moda, Promedio, Mediana, valores fijos o edición manual uno a uno (1x1)** (interactivo).
*   Detecta automáticamente si una columna es un **ID/Matrícula** para un tratamiento de los valores nulos mas personalizado como: limpieza manual o llenado de los registros vacíos 1x1.
*   Detecta columnas de **fechas** aplicando parseo flexible y formateo estandarizado.
  
*   **Gestión Dinámica de Archivos:**
*   Exportación automatizada que hereda el nombre del archivo original y le añade el sufijo `_clean.csv` de forma transparente utilizando la librería estándar `pathlib`.

---

## 🛠️ Tecnologías Utilizadas

*   **Python 3.x**
*   **Pandas:** Para la manipulación eficiente de estructuras de datos en memoria.
*   **Pathlib:** Para la gestión e inferencia segura de rutas en el sistema de archivos.

---

## 💻 Requisitos e Instalación

1. Clona este repositorio en tu máquina local:
   ```bash
   git clone https://github.com/3rick-CR/data-csv-normalizer-pandas.git
   cd data-csv-normalizer-pandas
