# 🌍 SatDetect – City Change Detector Using Satellite Imagery

Welcome to **SatDetect**, a simple yet powerful tool for detecting **landscape changes** between two satellite images of the same region. Whether you're tracking urban development, environmental impact, or deforestation, SatDetect helps you **visualize and understand changes over time** with just two image uploads.

🔗 **GitHub Repository:** [Mehboob786/CityChangeDetector](https://github.com/Mehboob786/CityChangeDetector)

---

## ✨ Features

- 🖼️ **Side-by-side Image Comparison**  
  Compare past and present satellite images interactively.

- 🔍 **Automatic Change Detection**  
  Highlights areas with visual differences and labels the change type.

- 🧠 **Smart Change Classification**  
  Detects:
  - 🌳 Vegetation Loss
  - 💧 Water Body Change
  - 🏗️ New Construction

- 📊 **Change Percentage Report**  
  Quickly see how much of the area has changed.

- 🔎 **Zoomable View**  
  Zoom in to inspect fine details using `streamlit-image-zoom`.

---

## 🚀 How to Use

1. **Clone the Repository**
   ```bash
   git clone https://github.com/Mehboob786/CityChangeDetector.git
   cd CityChangeDetector
   ```

2. **Install Dependencies**
   Make sure you have Python 3.7+ installed. Then run:
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the App**
   ```bash
   streamlit run app.py
   ```

4. **Upload Your Images**  
   - First Image: older satellite photo of the region  
   - Second Image: newer satellite photo of the same region

   The app will detect and highlight the changes between the two images.

---

## 🧠 How It Works

- The two uploaded images are resized and converted to grayscale.
- A pixel-by-pixel difference is computed.
- Changes are isolated using thresholding and contours.
- Each detected change is classified based on dominant color:
  - Green → Vegetation Loss
  - Blue → Water Change
  - Gray/Neutral → Construction

---

## 📦 Tech Stack

- **Streamlit** – for interactive web app
- **OpenCV** – for image processing
- **NumPy** – for array manipulation
- **PIL** – for image handling
- **streamlit-image-zoom** – for zoom functionality

---

## 📁 Project Structure

```
CityChangeDetector/
│
├── app.py              # Streamlit frontend app
├── detector.py         # Core change detection logic
├── requirements.txt    # Python dependencies
└── README.md           # Project documentation
```

---

## 📸 Sample Use Case

Imagine you have two satellite images of a city – one from 2020 and one from 2024. Upload both, and SatDetect will:

- Highlight newly constructed buildings
- Show where water bodies have shrunk or shifted
- Detect areas where vegetation has been removed

---

## 💡 Future Improvements

- Support for larger image sizes
- AI-based advanced classification
- Exportable reports in PDF
- Integration with Google Earth Engine or Mapbox

---

## 🙌 Contributing

Have ideas or want to improve the model? Pull requests are welcome!  
Let’s build smarter, greener cities together.

---

## 🧑‍💻 Author

**Mehboob Ahmad**  
GitHub: [@Mehboob786](https://github.com/Mehboob786)

---

## 📃 License

This project is licensed under the MIT License. See [LICENSE](LICENSE) for details.
