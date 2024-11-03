## 🌟 Proyecto: Tokenizador 📂

¡Este proyecto ofrece una aplicación con interfaz gráfica (GUI) para dividir archivos de texto grandes en fragmentos más pequeños, usando el poderoso *tokenizador BERT* de la biblioteca Transformers! Perfecto para proyectos de procesamiento de lenguaje natural (NLP). 🧠

---

### 🚀 Preparación del Entorno 🌍

1. **Crea un Entorno Virtual:** Es recomendable usar un entorno virtual para manejar las dependencias del proyecto.
   ```bash
   python3 -m venv .venv
   ```
2. **Activa el Entorno:**
   - **Linux/macOS:** `source .venv/bin/activate`
   - **Windows:** `.venv\Scripts\activate`
3. **Instala Requerimientos:** Instala los paquetes necesarios:
   ```bash
   pip install -r requirements.txt
   ```

---

### 📂 Estructura del Proyecto

- **`gui.py`**: Implementación de la GUI con PyQt5. 🖼️ Ofrece una interfaz para seleccionar archivos, configurar límites de tokens, y activar los procesos.
- **`logic.py`**: 💡 Contiene la lógica de tokenización y división de archivos usando el tokenizador BERT de la biblioteca `transformers`.
- **`main.py`**: El punto de inicio del programa. Inicia la aplicación PyQt5 y muestra la interfaz gráfica.

---

### 🔄 Flujo de Trabajo

1. **Selección de Archivo:** Selecciona el archivo de texto grande desde la interfaz gráfica. 📜
2. **Establecer Límite de Tokens:** Ingresa el número deseado de tokens por archivo.
3. **Tokenización:** `logic.py` usa el tokenizador BERT para procesar el texto. 🧩
4. **División de Archivos:** El archivo se divide en varios fragmentos, cada uno con la cantidad de tokens especificada.
5. **Resultado:** La app te notifica sobre el éxito de la división y muestra el total de tokens procesados. ✔️

---

### ✨ Funcionalidades

- **Interfaz Gráfica (GUI)**: ¡Fácil de usar y amigable para el usuario! 🎉
- **Tokenizador BERT**: Tokenización robusta y precisa para dividir el texto. 🔍
- **Límites Ajustables**: Elige la cantidad de tokens por archivo según tus necesidades. ⚙️
- **Salida Limpia**: Los archivos resultantes contienen texto tokenizado limpio y listo para su uso. ✨

---

### 🏃‍♂️ Cómo Ejecutar

1. Lanza la aplicación ejecutando `main.py`:
   ```bash
   python main.py
   ```

---

### 📌 Notas Adicionales

- Los recursos (imágenes) para el tema de la GUI están en la carpeta `resources`.
- Todas las dependencias están listadas en el archivo `requirements.txt`.

Con esta herramienta, tendrás una solución práctica para tokenizar y dividir archivos grandes, ideal para tareas de procesamiento de lenguaje natural. ¡Disfruta el proceso de preparación de datos! 🌈