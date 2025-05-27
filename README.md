
# 🧠 Real-Time Emotion, Gender & Age Detection Dashboard

A real-time computer vision dashboard that detects **emotions**, **gender**, and **age** from live webcam input using **Streamlit**, **OpenCV**, **FER**, and **DeepFace**. The app supports **multi-face detection**, draws **bounding boxes**, tracks **FPS**, includes **start/stop streaming**, **theme toggling**, and a **snapshot capture feature** — all in an interactive browser-based UI.

---

## 🚀 Features

- 🎥 Real-time webcam streaming via OpenCV
- 😊 Emotion recognition with [FER](https://github.com/justinshenk/fer)
- 👨‍👩 Gender and age prediction using [DeepFace](https://github.com/serengil/deepface)
- 🧠 Multi-face detection with bounding boxes
- ⚡ Live FPS performance display
- 🌗 Theme toggle (Light/Dark mode)
- 📸 Snapshot download button
- 🛑 Start and Stop stream control

---

## 📦 Tech Stack

| Component       | Technology      |
|----------------|-----------------|
| Frontend UI     | Streamlit       |
| Image Processing | OpenCV          |
| Emotion Model   | FER (MTCNN)     |
| Age/Gender Model| DeepFace        |
| Backend         | Python          |
| ML Framework    | TensorFlow      |

---

## 🔧 Installation

1. **Clone the repository**

```bash
git clone https://github.com/rishabhkarnwal04/emotion-reader.git
cd emotion-reader
```
---

2. **Install dependencies**

```bash
pip install -r requirements.txt
```

---

## ▶️ Run the App

Launch the app using Streamlit:

```bash
streamlit run dashboard.py
```

---

## 🧠 Model Details

| Model    | Task               | Notes                                |
|----------|--------------------|--------------------------------------|
| FER      | Emotion detection  | Uses CNN on cropped face with MTCNN  |
| DeepFace | Gender & Age       | Predicts using pretrained VGG-Face   |

All models are downloaded locally once used the first time.

---

## 📌 Troubleshooting

- **Laggy webcam feed?**  
  Add:
  ```python
  cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
  cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)
  ```
- **No face detected?**  
  Ensure you have good lighting and are facing the camera directly.

- **AVCaptureDeviceType warning (macOS only)?**  
  This is safe to ignore. It's a macOS system warning related to continuity camera fallback.

---

## 🙋 Author

**Rishabh Karnwal**  
🔗 [LinkedIn](https://www.linkedin.com/in/rishabh-karnwal-mujrk/) 

---

## THANK YOU 



