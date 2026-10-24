# 📚 IIUC Smart Library — AI Book Tagger & 2D Shelf Locator

[![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=Streamlit&logoColor=white)](https://streamlit.io)
[![Python 3.11+](https://img.shields.io/badge/Python-3.11%2B-blue?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![Ollama Cloud / Local](https://img.shields.io/badge/AI-Ollama%20%2F%20Gemma%204-black?style=for-the-badge&logo=ollama&logoColor=white)](https://ollama.com)
[![GitHub Repository](https://img.shields.io/badge/GitHub-IIUC--Smart--Library-181717?style=for-the-badge&logo=github&logoColor=white)](https://github.com/flucloxin500/IIUC-Smart-Library)

An intelligent, AI-powered smart library assistance system built specifically for the **International Islamic University Chittagong (IIUC)** central library. 

This application bridges physical library exploration and digital curriculum browsing using vision-capable **Gemma 4** models (via Ollama Cloud or local Ollama). It empowers students to instantly identify any textbook from a photo, tag its academic course, pinpoint its exact physical location on an interactive **2D visual shelf grid**, and get personalized curriculum study guidance.

---

## 🌟 Key Features

### 1. 📷 Visual Book Scanner & Academic Tagger
- **Camera Capture & Upload:** Snap a photo using your laptop/phone camera or upload JPG, PNG, or WebP cover images.
- **Gemma Vision Engine:** Automatically reads book titles, authors, and edition details without hallucinating non-book objects (distinguishes covers from faces or random objects).
- **Catalogue Mapping:** Correlates the recognized title with the IIUC library catalogue to identify:
  - 🏛️ **Faculty & Department** (e.g., *CSE, EEE, Pharmacy, BBA, Law, English, CGED*)
  - 🎓 **Semester** (Semesters 1 through 8)
  - 📘 **Course Code & Title** (e.g., *CSE-2311: Data Structures*)
  - 📦 **Real-time Availability & Copies**

### 2. 📍 Interactive 2D Visual Shelf Locator
- **Exact Coordinates:** Pinpoints the book’s physical location:
  - **Floor Level:** (e.g., *Floor 2 — Engineering & Technology Wing*)
  - **Shelf Number:** (e.g., *Shelf #12*)
  - **Row Level:** (e.g., *Row 3*)
  - **Column Position:** (e.g., *Column 4*)
- **Visual Matrix:** Renders an intuitive 4-tier interactive shelf matrix highlighting the exact slot where the book is physically stocked.

### 3. 🔍 Remote Course Book Finder
- Students outside the campus library can select:
  $$\text{Department} \longrightarrow \text{Semester} \longrightarrow \text{Course}$$
- Instantly view all recommended core textbooks and reference manuals, complete with physical shelf coordinates for when they visit campus.

### 4. 🧠 Personalized AI Study Assistant
- Powered by `gemma4:31b` / `gemma4:e2b`.
- Provides tailored study advice, foundational chapter roadmaps, and conceptual tips based on the selected course curriculum and textbook.

### 5. 📱 Responsive & Aesthetic UI
- Built with a modern, glassmorphic design system tailored for all screens (mobile phones, tablets, laptops, and ultra-wide displays).
- Instant health checks for AI API reachability and fallback to manual catalogue search if AI services are unavailable.

---

## 🏛️ IIUC Academic Coverage

The system indexes courses and textbooks across **16 Departments** and **6 Faculties + CGED**:

| Faculty | Covered Departments |
| :--- | :--- |
| **Faculty of Science & Engineering (FSE)** | CSE, EEE, CCE, Civil Engineering, Pharmacy |
| **Faculty of Business Studies (FBS)** | BBA, Economics & Banking (EB) |
| **Faculty of Law (FL)** | Department of Law |
| **Faculty of Social Sciences & Arts (FSA)** | English Language & Literature (ELL), Arabic Language & Literature (ALL) |
| **Faculty of Shari'ah & Islamic Studies (FSIS)** | Quranic Sciences & Islamic Studies (QSIS), Da'wah & Islamic Studies (DIS), Hadith & Islamic Studies (HIS) |
| **Faculty of General Education** | Center for General Education (CGED) Core Courses |

---

## 🛠️ Tech Stack & Architecture

- **Frontend & App Framework:** [Streamlit](https://streamlit.io/) (Python)
- **AI Inference:** [Ollama Cloud](https://ollama.com/) (`gemma4:31b`) / Local Ollama (`gemma4:e2b`)
- **Image Processing:** [Pillow (PIL)](https://python-pillow.org/)
- **Catalog Matching:** Python `SequenceMatcher` algorithm with strict threshold validation to avoid false positives
- **Styling:** Custom fluid CSS with CSS Grid & Flexbox, responsive typography, and mobile touch-friendly controls

---

## 📂 Project Structure

```text
IIUC-Smart-Library/
├── .streamlit/
│   ├── config.toml           # Streamlit theme & UI styling options
│   └── secrets.toml          # Private API keys & backend configuration (Git-ignored)
├── app.py                    # Main Streamlit web application & UI layout
├── gemma_engine.py           # Gemma Vision API handler & JSON parser
├── iiuc_library_data.py      # Department, course & shelf catalog database
├── secrets.example.toml      # Reference template for configuration secrets
├── requirements.txt          # Python package dependencies
├── DEPLOY.md                 # Deployment & cloud configuration manual
└── README.md                 # Comprehensive project documentation
```

---

## 🚀 Quick Start (Local Setup)

### Prerequisites
- Python 3.10, 3.11, or 3.12 installed.
- Git installed.
- *(Optional for offline AI)* [Ollama](https://ollama.com/) installed locally with `ollama pull gemma4:e2b`.

### 1. Clone the Repository
```bash
git clone https://github.com/flucloxin500/IIUC-Smart-Library.git
cd IIUC-Smart-Library
```

### 2. Set Up a Virtual Environment
```bash
# Windows (PowerShell)
python -m venv .venv
.venv\Scripts\Activate.ps1

# macOS / Linux
python3 -m venv .venv
source .venv/bin/activate
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### 4. Configure Secrets

Create a file named `.streamlit/secrets.toml`:

```toml
# For Ollama Cloud (Recommended)
OLLAMA_BACKEND = "cloud"
OLLAMA_MODEL = "gemma4:31b"
OLLAMA_API_KEY = "your_ollama_cloud_api_key_here"

# OR For Local Ollama
# OLLAMA_BACKEND = "local"
# OLLAMA_MODEL = "gemma4:e2b"
# OLLAMA_BASE_URL = "http://localhost:11434"
```

> 💡 **Tip:** Obtain your free Ollama Cloud API Key at [ollama.com/settings/keys](https://ollama.com/settings/keys).

### 5. Launch the Application
```bash
python -m streamlit run app.py
```
Open **`http://localhost:8501`** in your browser.

---

## ☁️ Deploying on Streamlit Community Cloud

Deploy in under 2 minutes:

1. Push your latest code to your GitHub repository:
   ```bash
   git push origin main
   ```
2. Navigate to **[share.streamlit.io](https://share.streamlit.io/)** and sign in with GitHub.
3. Click **"New app"** and configure:
   - **Repository:** `flucloxin500/IIUC-Smart-Library`
   - **Branch:** `main`
   - **Main file path:** `app.py`
4. Click **Advanced settings...**:
   - Select **Python 3.11** or **3.12**.
   - In the **Secrets** section, paste:
     ```toml
     OLLAMA_BACKEND = "cloud"
     OLLAMA_MODEL = "gemma4:31b"
     OLLAMA_API_KEY = "YOUR_OLLAMA_API_KEY"
     ```
5. Click **Deploy!** 🚀

Detailed deployment notes and troubleshooting are available in [`DEPLOY.md`](DEPLOY.md).

---

## 🔒 Security Best Practices

- Never commit `.streamlit/secrets.toml` or active API credentials to public repositories.
- Keep `.streamlit/secrets.toml` listed inside `.gitignore`.
- If an API key is ever accidentally pushed, revoke it immediately at [ollama.com/settings/keys](https://ollama.com/settings/keys) and issue a fresh one.

---

## 🤝 Contributing

Contributions to expand catalogue data, add 3D shelf visualizers, or integrate university barcode scanners are welcome!

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

---

## 📄 License & Acknowledgments

- Developed for **IIUC Library & Academic Community**.
- Powered by Google Gemma Models via Ollama API.
- Distributed under the **MIT License**.
