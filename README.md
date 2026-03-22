# 🎛️ Hand Gesture Volume Control

Control your system volume using just your hand! ✋
This project uses **Computer Vision + AI** to adjust volume in real-time based on the distance between your thumb and index finger.

---

## 🚀 Demo

<p align="center">
  <img src="https://raw.githubusercontent.com/Ujjwal15-coder/Hand-Gesture-Volume-Control/main/Screenshot%202026-03-22%20223024.png" width="600"/>
</p>

---

## 🧠 How It Works

* Detects hand landmarks using **MediaPipe**
* Calculates distance between **thumb & index finger**
* Maps distance to **system volume range**
* Controls volume using **Pycaw**
* Displays real-time **volume bar & status**

---

## 🛠️ Tech Stack

* 🐍 Python
* 👁️ OpenCV
* ✋ MediaPipe
* 🔊 Pycaw
* 📊 NumPy

---

## ⚙️ Features

* 🎯 Real-time hand tracking
* 🎚️ Smooth volume control
* 📏 Distance-based gesture detection
* 🟢 Live visual feedback
* ⚡ Fast and responsive system

---

## 📂 Project Structure

```
Hand-Gesture-Volume-Control/
│
├── volume_control_python.py   # Main script
├── README.md                  # Documentation
├── .gitignore
```

---

## 🧑‍💻 Installation

### 1. Clone the repository

```bash
git clone https://github.com/Ujjwal15-coder/Hand-Gesture-Volume-Control.git
cd Hand-Gesture-Volume-Control
```

### 2. Create virtual environment (optional)

```bash
python -m venv .venv
.venv\Scripts\activate
```

### 3. Install dependencies

```bash
pip install opencv-python mediapipe pycaw numpy
```

---

## ▶️ Run the Project

```bash
python volume_control_python.py
```

---

## 🎮 Controls

* ✋ Show your hand to webcam
* 🤏 Move fingers closer → Volume Down
* 🤏 Move fingers apart → Volume Up

---

## 🔮 Future Improvements

* 🎤 Voice + gesture control
* 📱 Web / mobile version
* 🎵 Media player controls
* 🎨 UI enhancements

---

## ⭐ Support

If you like this project:

* ⭐ Star this repo
* 🍴 Fork it
* 🤝 Contribute

---

## 👨‍💻 Author

**Ujjwal Shobhit**
🔗 https://github.com/Ujjwal15-coder
