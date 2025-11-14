🏗 Cálculo de Capacidad Portante — Método de Terzaghi

📘 Descripción General

Este proyecto consiste en una aplicación desarrollada en Python con Tkinter para estimar la capacidad portante del terreno de manera rápida y sencilla.

La herramienta permite ingresar parámetros geotécnicos básicos como cohesión, peso unitario, ancho de zapata, profundidad y ángulo de fricción, entregando un resultado inmediato mediante una interfaz gráfica amigable.

La aplicación utiliza una fórmula de ejemplo para cálculo, pero está diseñada para adaptarse fácilmente a la fórmula real de Terzaghi.

⚙ Funcionalidades

Interfaz gráfica intuitiva y fácil de usar.

Ingreso de parámetros geotécnicos:

Cohesión (c)

Peso unitario (γ)

Ancho de zapata (B)

Profundidad (Df)

Ángulo de fricción (φ)

Validación de entradas para asegurar que los datos sean numéricos.

Cálculo automático de la capacidad portante.

Resultados claros y legibles mostrados en la interfaz.

Ventana centrada automáticamente en pantalla.


🧮 Fundamento Teórico

El cálculo de capacidad portante se basa en la estimación de la resistencia del suelo bajo una carga, considerando parámetros como cohesión, peso unitario y características geométricas de la cimentación.

Aunque el proyecto actualmente utiliza una fórmula simplificada, la aplicación puede adaptarse fácilmente para incorporar la ecuación oficial de Terzaghi:

q_ult = cN_c + γDf N_q + 0.5 γ B N_γ

Esta ecuación permite determinar la capacidad última del suelo y evaluar la seguridad de la cimentación frente a cargas aplicadas.

🖥 Interfaz Gráfica

La interfaz está diseñada para ser clara y funcional, con los siguientes elementos:

Fondo en tonos azul claro para mayor legibilidad.

Paneles y secciones que organizan los campos de entrada.

Etiquetas y placeholders que guían al usuario en la introducción de datos.

Botón de cálculo destacado para ejecutar la estimación.

Panel de resultados que muestra la capacidad portante calculada de forma inmediata.


🧰 Tecnologías Utilizadas

Python 3.8 o superior

Tkinter (librería estándar de Python para interfaces gráficas)

Funciona sin necesidad de instalar librerías adicionales, compatible con IDLE, VS Code o PyCharm.


▶️ Uso

Abrir la aplicación en Python.

Introducir los valores de los parámetros requeridos.

Presionar el botón de cálculo.

Visualizar el resultado de la capacidad portante directamente en la ventana.

El sistema permite realizar múltiples cálculos sin reiniciar la aplicación.
