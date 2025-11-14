import tkinter as tk

# Crear ventana principal
ventana = tk.Tk()
ventana.title("Cálculo de Capacidad Portante - Terzaghi")
ventana.configure(bg="#e6f2ff")

# ----- FRAME PRINCIPAL -----
frame = tk.Frame(ventana, bg="#e6f2ff", padx=20, pady=20)
frame.pack()

# ----- ETIQUETAS Y CAMPOS DE ENTRADA -----
labels = [
    "Cohesión c (kPa):",
    "Peso unitario γ (kN/m³):",
    "Ancho zapata B (m):",
    "Profundidad Df (m):",
    "Ángulo de fricción φ (°):"
]

entries = []

for texto in labels:
    tk.Label(frame, text=texto, font=("Arial", 10, "bold"), bg="#e6f2ff").pack(anchor="w", pady=3)
    e = tk.Entry(frame, width=25, font=("Arial", 10))
    e.pack(pady=3)
    entries.append(e)

entry_c, entry_gamma, entry_B, entry_Df, entry_phi = entries

# ----- FUNCIÓN DE CÁLCULO -----
def calcular():
    try:
        c = float(entry_c.get())
        gamma = float(entry_gamma.get())
        B = float(entry_B.get())
        Df = float(entry_Df.get())
        phi = float(entry_phi.get())

        # Ejemplo simple (aquí puedes poner tu fórmula real)
        q_ult = c + gamma * Df + B * phi
        label_resultado.config(text=f"Capacidad portante estimada: {q_ult:.2f} kPa")

    except ValueError:
        label_resultado.config(text="⚠ Por favor, ingresa valores numéricos válidos.")

# ----- BOTÓN CALCULAR -----
tk.Button(
    ventana,
    text="Calcular",
    command=calcular,
    bg="#4da6ff",
    fg="white",
    font=("Arial", 11, "bold"),
    width=15
).pack(pady=15)

# ----- RESULTADO -----
label_resultado = tk.Label(
    ventana,
    text="",
    font=("Arial", 11, "bold"),
    bg="#e6f2ff",
    justify="center"
)
label_resultado.pack(pady=10)

# ----- AJUSTAR Y CENTRAR VENTANA -----
ventana.update_idletasks()
ancho = ventana.winfo_width()
alto = ventana.winfo_height()
x = (ventana.winfo_screenwidth() // 2) - (ancho // 2)
y = (ventana.winfo_screenheight() // 2) - (alto // 2)
ventana.geometry(f"+{x}+{y}")

# Ejecutar ventana
ventana.mainloop()
