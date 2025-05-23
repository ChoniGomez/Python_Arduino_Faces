# 🧠 Reconocimiento Facial con IA y Arduino

Este proyecto utiliza **Python**, **OpenCV** y **Arduino** para detectar rostros en tiempo real a través de una cámara web y controlar un dispositivo Arduino según la detección.

---

## 🚀 Funcionalidad

- Detecta rostros humanos mediante un modelo Haarcascade (OpenCV).
- Envía señales al puerto serie (`'A'` cuando hay rostro, `'B'` cuando no hay).
- Arduino puede actuar en consecuencia (encender un LED, mover un servo, etc.).

---

## 🛠️ Tecnologías y Versiones

| Componente     | Versión Recomendada |
|----------------|---------------------|
| **Python**     | 3.13+ (funciona desde 3.7 en adelante) |
| **OpenCV**     | `opencv-python` 4.9.0.80 o superior |
| **PySerial**   | `pyserial` 3.5 o superior |
| **Arduino IDE**| 1.8.x o Arduino IDE 2.x |
| **Placa Arduino** | Cualquier compatible con puerto serie (ej. Uno, Nano, Mega) |

---

## 📦 Instalación de Dependencias

```bash
pip install opencv-python
pip install pyserial
```

---

## 📁 Archivos necesarios

- `haarcascade_frontalface_default.xml`  
  Descargable desde el repositorio oficial de OpenCV:  
  [https://github.com/opencv/opencv/tree/master/data/haarcascades](https://github.com/opencv/opencv/tree/master/data/haarcascades)

---

## 🎥 Cómo Ejecutar el Proyecto

1. Conectá tu Arduino y abrí el monitor serie para asegurarte de que está en el **puerto COM correcto**.
2. Modificá la línea de conexión serial si es necesario:

```python
arduino = serial.Serial('COM8', 9600, timeout=1)
```

3. Ejecutá el script en la terminal con:

```bash
python detecta_rostro.py
```

4. Pulsá la tecla **ESC** para salir.

---

## 🔌 Ejemplo de Código Arduino

```cpp
void setup() {
  Serial.begin(9600);
  pinMode(13, OUTPUT);  // LED integrado
}

void loop() {
  if (Serial.available()) {
    char dato = Serial.read();
    if (dato == 'A') {
      digitalWrite(13, HIGH);
    } else if (dato == 'B') {
      digitalWrite(13, LOW);
    }
  }
}
```

---

## 🧪 Probado en

- **Windows 10 / 11**
- **Python 3.13.0**
- **Arduino Uno**
- **Webcam USB estándar**

---

## 📄 Licencia

Este proyecto es de código abierto bajo licencia MIT.
