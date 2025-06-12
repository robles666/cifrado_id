# 🔐 Detector de Tipo de Cifrado

Este es un software en Python con interfaz gráfica (GUI) que permite identificar de forma automatizada el tipo de cifrado o codificación que puede tener un archivo. Es útil para análisis forense, seguridad informática, criptografía básica o simplemente para estudiar patrones en archivos cifrados.

## 📦 Características principales

- Detección de:
  - Base64
  - Cifrado César / Vigenère
  - Cifrado XOR simple (1 byte)
  - Texto ASCII plano
  - Cifrado fuerte (entropía alta)
  - AES en modo ECB (bloques repetidos)
- Cálculo de **entropía de Shannon** del archivo.
- Interfaz gráfica intuitiva con `tkinter`.
- Exportación del análisis como archivo `.txt`.

## 🖥️ Requisitos

- Python 3.6 o superior
- No requiere librerías externas (usa solo librerías estándar)

## 🚀 Cómo usar

1. Clona o descarga este repositorio.
2. Ejecuta el archivo principal:

```bash
python detector_gui.py
