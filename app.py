import streamlit as st
import cv2
import numpy as np
from PIL import Image
from detector import detect_changes
from streamlit_image_zoom import image_zoom

st.set_page_config(page_title="SatDetect", layout="centered")

st.title("🌍 SatDetect: Satellite Image Change Analyzer")

st.markdown("Upload **two satellite images** of the same region (different years), and this tool will detect, label, and display changes.")

uploaded1 = st.file_uploader("📤 Upload First Image (Old)", type=["jpg", "jpeg", "png"])
uploaded2 = st.file_uploader("📤 Upload Second Image (New)", type=["jpg", "jpeg", "png"])

if uploaded1 and uploaded2:
    img1 = Image.open(uploaded1).convert("RGB")
    img2 = Image.open(uploaded2).convert("RGB")

    img1_np = np.array(img1)
    img2_np = np.array(img2)

    result_img, diff_map, binary_mask, change_percent, results = detect_changes(img1_np, img2_np)

    st.subheader("📸 Side-by-Side Image Comparison")
    col1, col2 = st.columns(2)

    with col1:
        st.markdown("**🕰️ Old Image**")
        img1_bgr = cv2.cvtColor(img1_np, cv2.COLOR_RGB2BGR)
        image_zoom(img1_bgr)

    with col2:
        st.markdown("**🆕 New Image**")
        img2_bgr = cv2.cvtColor(img2_np, cv2.COLOR_RGB2BGR)
        image_zoom(img2_bgr)

    st.subheader("🧠 Change Detection Result")
    st.image(result_img, caption=f"📍 Changes Detected – Area Changed: {change_percent:.2f}%", use_container_width=True)

else:
    st.info("Please upload both satellite images to continue.")
