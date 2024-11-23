# Chess Analysis Dashboard

Este proyecto es un dashboard de análisis de partidas de ajedrez que permite visualizar estadísticas y gráficos interactivos basados en datos de partidas. Utiliza **Flask** para el backend y **Plotly** para la visualización en el frontend.

---

## 🚀 **Características**

### 1. Visualización de **Win Rate**
- Analiza el porcentaje de victorias, derrotas y empates para las primeras dos jugadas seleccionadas (blancas y negras).
  
### 2. **Tipos de Incremento**
- Gráfico circular que muestra los tipos de incremento utilizados (por ejemplo, `+10`, `1|0`, etc.), filtrado por un intervalo de ELO seleccionado.

### 3. **Cantidad de Jugadores por Intervalo de ELO**
- Gráfico de barras que categoriza la cantidad de jugadores en:
  - Menos de **1000**.
  - Entre **1000 y 2000**.
  - Más de **2000**.

---

## ⚙️ **Requisitos**

- **Python 3.x**
- **Flask**
- **Plotly**

---

## 📥 **Instalación**

1. Clona este repositorio:
   ```bash
   git clone https://github.com/tu-usuario/chess-analysis-dashboard.git
   cd chess-analysis-dashboard
   ```

2. Crea un entorno virtual e instala las dependencias:
   ```bash
   python -m venv venv
   source venv/bin/activate  # En Windows usa `venv\Scripts\activate`
   pip install -r requirements.txt
   ```

3. Asegúrate de que el archivo **CSV** con los datos de las partidas esté ubicado en:  
   **`data/games.csv`**.

4. Ejecuta el script de preprocesamiento para generar el archivo **JSON**:
   ```bash
   python preprocesar.py
   ```

5. Inicia el servidor Flask:
   ```bash
   python app.py
   ```
---

## 📂 **Estructura del Proyecto**

```
chess-analysis-dashboard/
│
├── app.py               # Archivo principal de la aplicación Flask
├── preprocesar.py       # Script para convertir CSV a JSON
│
├── static/              # Archivos estáticos (HTML, JS, CSS)
│   ├── index.html       # Página principal del dashboard
│   ├── botones.js       # Lógica del frontend
│
├── data/                # Datos de las partidas
│   ├── games.csv        # Archivo CSV original
│   ├── games.json       # Archivo JSON generado
│
└── requirements.txt     # Dependencias necesarias
```

---

## 🛠️ **Uso**

### 1. **Visualización de Win Rate**
- Selecciona una jugada para las blancas y otra para las negras en la tabla.
- Haz clic en el botón **"Mostrar Win Rate"**.
- Se genera un gráfico de barras con el porcentaje de victorias, derrotas y empates.

### 2. **Tipos de Incremento**
- Selecciona un intervalo de ELO en el menú desplegable.
- Haz clic en el botón **"Mostrar Incremento"**.
- Se genera un gráfico circular con los tipos de incremento utilizados.

### 3. **Cantidad de Jugadores por Intervalo de ELO**
- Haz clic en el botón **"Visualizar Cantidad de Jugadores"**.
- Se genera un gráfico de barras con la cantidad de jugadores por intervalo de ELO.

---

## 🔎 **Justificación de Decisiones**

### **Backend**
- **Flask**: Framework ligero y flexible para crear aplicaciones web rápidamente.  
  - Se implementaron **POO**, **programación funcional** y **lógica** para estructurar el código.

#### Paradigmas utilizados:
1. **Programación Orientada a Objetos (POO)**  
   - Clases como `GameData` para manejar operaciones relacionadas con los juegos.
   - Clase `FilteredGameData` extiende `GameData` para operaciones específicas de filtrado.

2. **Programación Funcional**  
   - Uso de la función `filter` para manipular datos de forma declarativa.

3. **Programación Lógica**  
   - Condiciones definidas en funciones como `filter_games` para segmentar datos por intervalos de ELO.

---

### **Frontend**
- **HTML5** para la estructura de la página.
- **Plotly** para gráficos interactivos y atractivos, con integración directa desde Python.

---

### **Datos**
- Conversión de **CSV a JSON** para optimizar la transferencia de datos entre backend y frontend.  
- **JSON** es ligero, fácil de manejar y adecuado para aplicaciones web modernas.

---

## 🖱️ **Funciones del Frontend (botones.js)**

1. **Carga de Jugadas Iniciales**  
   - Solicitud a `/api/primeras-jugadas` para llenar la tabla de jugadas iniciales.

2. **Mostrar Win Rate**  
   - Solicitud a `/api/winrate` con las jugadas seleccionadas, generando un gráfico de barras.

3. **Mostrar Incremento**  
   - Solicitud a `/api/incremento` según el intervalo de ELO seleccionado, generando un gráfico circular.

4. **Visualizar Cantidad de Jugadores**  
   - Solicitud a `/api/cantidad-jugadores`, generando un gráfico de barras.

---

## 💡 **Integrantes**
- Mauricio Perez
- Joshua Leon
- Francisco Henriquez
- Franco Ugarte

---

## 📜 **Licencia**
Este proyecto se distribuye bajo la licencia MIT.  
Consulta el archivo `LICENSE` para más información. 