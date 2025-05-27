
# 🧠 Real-Time Emotion, Gender & Age Detection Dashboard

A real-time computer vision dashboard that detects **emotions**, **gender**, and **age** from live webcam input using **Streamlit**, **OpenCV**, **FER**, and **DeepFace**. The app supports **multi-face detection**, draws **bounding boxes**, tracks **FPS**, includes **start/stop streaming**, **theme toggling**, and a **snapshot capture feature** — all in an interactive browser-based UI.

![App Preview](demo.gif) <!-- Replace with your actual GIF or screenshot path -->

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
git clone https://github.com/yourusername/emotion-detection-dashboard.git
cd emotion-detection-dashboard
```

2. **(Optional) Create a virtual environment**

```bash
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
```

3. **Install dependencies**

```bash
pip install -r requirements.txt
```

---

## ▶️ Run the App

Launch the app using Streamlit:

```bash
streamlit run dashboard.py
```

Then visit [http://localhost:8501](http://localhost:8501) in your browser.

---

## 📋 Requirements

```
streamlit
opencv-python
fer
deepface
tensorflow
mtcnn
```

Install manually if needed:

```bash
pip install streamlit opencv-python fer deepface tensorflow mtcnn
```

---

## 📸 Demo & Snapshots

You can record the app with [Kap](https://getkap.co/) or [Screen Studio](https://screen.studio) and convert to GIF using [ezgif.com](https://ezgif.com).

Use `📸 Snapshot` inside the app to save the current frame.

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

**Your Name**  
🔗 [LinkedIn](https://linkedin.com/in/yourprofile) • 🐦 [Twitter](https://twitter.com/yourhandle) • 🌐 [Portfolio](https://yourwebsite.com)

---

## 🤝 Contributions

Contributions and suggestions are welcome via [Pull Requests](https://github.com/yourusername/emotion-detection-dashboard/pulls).

---

## 🛡 License

This project is licensed under the **MIT License**. See the `LICENSE` file for details.
