import math
import tkinter as tk
from tkinter import messagebox

# ------------------------------------------
# Funciones de cálculo
# ------------------------------------------
def factores_capacidad_portante(phi):
    """Calcula los factores Nc, Nq y Nγ según el ángulo de fricción φ (en grados)."""
    phi_rad = math.radians(phi)
    if phi == 0:
        return 5.7, 1.0, 0.0  # valores típicos para suelo puramente cohesivo
    Nq = math.exp(math.pi * math.tan(phi_rad)) * (math.tan(math.radians(45) + phi_rad / 2))**2
    Nc = (Nq - 1) / math.tan(phi_rad)
    N_gamma = 2 * (Nq + 1) * math.tan(phi_rad)
    return Nc, Nq, N_gamma


def capacidad_portante(c, gamma, B, Df, phi):
    """Calcula la capacidad portante última (qult) y admisible (qadm)."""
    Nc, Nq, N_gamma = factores_capacidad_portante(phi)
    q_ult = c * Nc + gamma * Df * Nq + 0.5 * gamma * B * N_gamma
    FS = 3  # factor de seguridad típico
    q_adm = q_ult / FS
    return q_ult, q_adm


# ------------------------------------------
# Función que se ejecuta al presionar el botón
# ------------------------------------------
def calcular():
    try:
        c = float(entry_c.get())
        gamma = float(entry_gamma.get())
        B = float(entry_B.get())
        Df = float(entry_Df.get())
        phi = float(entry_phi.get())

        q_ult, q_adm = capacidad_portante(c, gamma, B, Df, phi)

        label_resultado.config(
            text=f"Capacidad portante última: {q_ult:.2f} kPa\n"
                 f"Capacidad portante admisible (FS=3): {q_adm:.2f} kPa",
            fg="darkblue"
        )
    except ValueError:
        messagebox.showerror("Error", "Por favor, ingrese valores numéricos válidos.")


# ------------------------------------------
# Interfaz gráfica (Tkinter)
# ------------------------------------------
ventana = tk.Tk()
ventana.title("Cálculo de Capacidad Portante - Terzaghi")
ventana.geometry("400x400")
ventana.resizable(False, False)
ventana.config(bg="#e6f2ff")

# Título
tk.Label(ventana, text="Cálculo de Capacidad Portante del Suelo",
         font=("Arial", 13, "bold"), bg="#e6f2ff").pack(pady=10)

# Campos de entrada
frame = tk.Frame(ventana, bg="#e6f2ff")
frame.pack()

labels = ["Cohesión c (kPa):", "Peso unitario γ (kN/m³):",
          "Ancho zapata B (m):", "Profundidad Df (m):",
          "Ángulo de fricción φ (°):"]

entries = []

for texto in labels:
    tk.Label(frame, text=texto, font=("Arial", 10), bg="#e6f2ff").pack(anchor="w", pady=3)
    e = tk.Entry(frame, width=20)
    e.pack(pady=2)
    entries.append(e)

entry_c, entry_gamma, entry_B, entry_Df, entry_phi = entries

# Botón calcular
tk.Button(ventana, text="Calcular", command=calcular,
          bg="#4da6ff", fg="white", font=("Arial", 11, "bold"),
          width=15).pack(pady=10)

# Resultado
label_resultado = tk.Label(ventana, text="", font=("Arial", 11, "bold"),
                           bg="#e6f2ff", justify="center")
label_resultado.pack(pady=15)

# Inicia la ventana
ventana.mainloop()
