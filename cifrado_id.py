import tkinter as tk
from tkinter import filedialog, messagebox
import base64
import math
import string
from collections import Counter

def calcular_entropia(data_bytes):
    if not data_bytes:
        return 0
    counter = Counter(data_bytes)
    total = len(data_bytes)
    return -sum((count/total) * math.log2(count/total) for count in counter.values())

def es_base64(data_str):
    try:
        base64.b64decode(data_str, validate=True)
        return True
    except Exception:
        return False

def parece_cesar(data_str):
    letras = [c for c in data_str if c.isalpha()]
    if not letras:
        return False
    frecuencias = Counter(letras)
    comunes = [l[0] for l in frecuencias.most_common(5)]
    return any(c.lower() in comunes for c in ['e', 't', 'a'])

def es_ascii(data_bytes):
    try:
        data_bytes.decode('ascii')
        return True
    except UnicodeDecodeError:
        return False

def detectar_xor_simple(data_bytes):
    for key in range(256):
        decoded = bytes(b ^ key for b in data_bytes)
        try:
            decoded.decode('ascii')
            if all(chr(b) in string.printable for b in decoded):
                return True, key
        except:
            continue
    return False, None

def identificar_cifrado_desde_archivo(path):
    with open(path, "rb") as f:
        data = f.read()

    entropia = calcular_entropia(data)
    resultado = f"Entropía: {entropia:.2f}\n"

    try:
        texto = data.decode('utf-8')
        if es_base64(texto):
            resultado += "→ Posible Base64\n"
        elif parece_cesar(texto):
            resultado += "→ Posible César o Vigenère\n"
    except:
        pass

    if es_ascii(data):
        resultado += "→ Texto ASCII sin cifrado\n"

    xor, clave = detectar_xor_simple(data)
    if xor:
        resultado += f"→ Cifrado XOR simple (clave: {clave})\n"

    if entropia > 7.5:
        resultado += "→ Probable cifrado fuerte (AES, etc.)\n"

    if "→" not in resultado:
        resultado += "→ No se pudo identificar el cifrado\n"

    return resultado

# Interfaz gráfica
def seleccionar_archivo():
    ruta = filedialog.askopenfilename()
    if ruta:
        resultado = identificar_cifrado_desde_archivo(ruta)
        messagebox.showinfo("Resultado del análisis", resultado)

root = tk.Tk()
root.title("Detector de tipo de cifrado")

tk.Label(root, text="Haz clic para seleccionar un archivo a analizar:").pack(pady=10)
tk.Button(root, text="Seleccionar archivo", command=seleccionar_archivo).pack(pady=10)

root.mainloop()
