# 🌍 Web Scraping de Países con Python & Pandas

Este proyecto es una herramienta de automatización diseñada para extraer, limpiar y filtrar datos demográficos de países desde la web. Forma parte de mi portafolio de ingeniería de datos, enfocado en la creación de pipelines eficientes y profesionales.

## 🚀 Características

- **Extracción de Datos:** Utiliza `BeautifulSoup4` y `Requests` para obtener información en tiempo real.
- **Procesamiento con Pandas:** Los datos se transforman en un `DataFrame` para una manipulación rápida.
- **Manejo de Valores Críticos (Numpy):** Implementación de lógica para gestionar divisiones por cero o datos infinitos (`np.inf`), garantizando que el pipeline nunca se detenga.
- **Limpieza Automática:** Incluye una función robusta para convertir textos con formatos variados (comas, puntos, espacios) en números enteros.
- **Filtrado Inteligente:** Solo exporta países con una población superior a los 10 millones de habitantes.
- **Exportación Profesional:** Genera un archivo `.csv` optimizado para ser abierto directamente en Excel (separado por `;` y con encoding `UTF-8-SIG`).

## 🛠️ Tecnologías Utilizadas

* **Python 3.x**
* **Pandas:** Para el análisis y estructuración de datos.
* **Numpy:** Gestión de valores numéricos extremos y constantes matemáticas.
* **BeautifulSoup4:** Para el parseo de HTML.
* **Requests:** Para la comunicación HTTP.
* **Git:** Para el control de versiones.

## 📋 Requisitos e Instalación

1. **Clonar el repositorio:**
   ```bash
   git clone [https://github.com/DiegoAguirret/web-scraping-countries.git](https://github.com/DiegoAguirret/web-scraping-countries.git)
   cd web-scraping-countries