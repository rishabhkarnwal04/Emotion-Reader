# -*- coding: utf-8 -*-
"""dashboard

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1wWr8xiORUV3Kh-3QitzlL0bcb37xA7ny
"""

import streamlit as st
import cv2
from deepface import DeepFace
import numpy as np
import tempfile
import os
import time
from datetime import datetime

# ---------------------- Streamlit UI Setup ----------------------
st.set_page_config(page_title="Real-time Emotion Detection", layout="wide")
st.markdown("## 🎭 Real-time Emotion Detection")
st.markdown("### Using DeepFace + OpenCV (Multi-face)")
theme = st.toggle("🌗 Toggle Dark Mode", value=True)

if theme:
    st.markdown('<style>body{background-color:#0e1117;color:white;}</style>', unsafe_allow_html=True)
else:
    st.markdown('<style>body{background-color:white;color:black;}</style>', unsafe_allow_html=True)

start_button = st.button("▶️ Start Camera")
stop_button = st.button("⏹ Stop Camera")
snapshot_button = st.button("📸 Take Snapshot")

frame_placeholder = st.empty()
fps_placeholder = st.empty()

# ---------------------- Helper Functions ----------------------
def detect_and_annotate(frame, detector_backend="opencv"):
    try:
        result = DeepFace.analyze(
            frame,
            actions=["emotion", "age", "gender"],
            detector_backend=detector_backend,
            enforce_detection=False,
            silent=True
        )
        if not isinstance(result, list):
            result = [result]
        for face in result:
            x, y, w, h = face["region"]["x"], face["region"]["y"], face["region"]["w"], face["region"]["h"]
            cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
            label = f"{face['dominant_emotion']} | {face['gender']} | {int(face['age'])}"
            cv2.putText(frame, label, (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 0), 2)
    except Exception as e:
        cv2.putText(frame, "No face detected", (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)
    return frame

# ---------------------- Camera Stream ----------------------
cap = None
frame = None
start_time = None
fps = 0

if start_button:
    cap = cv2.VideoCapture(0)
    start_time = time.time()
    frame_count = 0

    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            st.error("Failed to grab frame.")
            break

        frame = cv2.flip(frame, 1)
        frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

        annotated_frame = detect_and_annotate(frame_rgb)

        frame_count += 1
        elapsed = time.time() - start_time
        fps = frame_count / elapsed
        cv2.putText(annotated_frame, f"FPS: {fps:.2f}", (10, annotated_frame.shape[0] - 10),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 255, 0), 2)

        frame_placeholder.image(annotated_frame, channels="RGB", use_column_width=True)
        fps_placeholder.markdown(f"🎥 **FPS**: `{fps:.2f}`")

        if stop_button:
            cap.release()
            break

        if snapshot_button:
            ts = datetime.now().strftime("%Y%m%d_%H%M%S")
            filename = f"snapshot_{ts}.png"
            filepath = os.path.join(tempfile.gettempdir(), filename)
            cv2.imwrite(filepath, cv2.cvtColor(annotated_frame, cv2.COLOR_RGB2BGR))
            with open(filepath, "rb") as file:
                btn = st.download_button("📥 Download Snapshot", file, file_name=filename)
            snapshot_button = False

if stop_button and cap:
    cap.release()
    st.warning("Camera stopped.")