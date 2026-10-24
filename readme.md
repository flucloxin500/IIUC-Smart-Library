# IIUC Smart Library Book Tagger & Exact Shelf Locator

One line: An open-source multimodal AI tool powered by **Gemma 4 E2B** that identifies any textbook from a photo and helps IIUC students across all 16 departments find required course books with exact **Floor, Shelf, Row, and Column** coordinates.

## The problem

Students at International Islamic University Chittagong (IIUC) face two major library frustrations every semester:
1. **Unidentified or untagged books:** When someone shares a photo of a textbook cover or page in a class WhatsApp/Messenger group—or picks up a reference book in the seminar library—students don't know which exact IIUC course code or semester it covers, or where it sits in the Central Library.
2. **Wandering between library racks:** When a student is in their hall, at home in the city, or in class and needs a textbook for a specific course (e.g., *CSE 3rd Semester Data Structures* or *EEE 1st Semester Electrical Circuits I*), there is no easy tool that tells them both **which book to borrow** and its exact **Floor No, Shelf No, Row No, and Column No** before they walk into the library.

## The solution

**IIUC Smart Library Book Tagger & Exact Shelf Locator** solves both problems in one clean web interface built around **Gemma 4 E2B**:
- **Feature 1 — Visual Book Scanner & Identifier:** Capture a live camera photo or upload an image of any book cover or title page. Gemma 4 E2B reads the image, identifies the book title, author, and core topics, maps it to the right IIUC Department, Semester, and Course, and displays its exact physical library coordinates.
- **Feature 2 — Remote Course Book Finder & 2D Shelf Locator:** Students outside the library select their **Department (all 16 IIUC departments across 6 Faculties + CGED)**, **Semester (1st–8th)**, and **Course**. The app recommends the primary and reference textbooks, provides bilingual (English + Bangla) Midterm/Final study tips, and renders a visual **5×6 Bookshelf Rack Matrix** highlighting the exact **Floor No, Shelf No, Row No, and Column No**.

## How it works

- **Model(s) used:** **Gemma 4 E2B** (`gemma4:e2b` via [Ollama](https://ollama.com/library/gemma4) / [Google Gemma 4 Docs](https://ai.google.dev/gemma)) for multimodal vision book cover recognition, syllabus topic extraction, and bilingual study advice.
- **Tech stack:** Python, Streamlit (Frontend Web UI), Pillow (Image processing & demo cover generation), Ollama REST API (`/api/chat` multimodal endpoint).
- **Datasets (if any):** Custom synthetic sample dataset (`iiuc_library_data.py`) covering all 16 official IIUC departments (`CSE`, `CCE`, `EEE`, `ETE`, `CE`, `PHARM`, `BBA`, `FIN`, `EB`, `LAW`, `ELL`, `ALL`, `QSIS`, `DIS`, `SHIS`, `URC/CGED`) across Semesters 1–8 with realistic shelf coordinates.

## How to run it

1. Clone the repo:
   ```bash
   git clone https://github.com/<your-username>/iiuc-smart-library-tagger.git
   cd iiuc-smart-library-tagger
   ```
2. Install requirements and ensure Ollama is running with `gemma4:e2b`:
   ```bash
   pip install -r requirements.txt
   ollama run gemma4:e2b
   ```
3. Run the app:
   ```bash
   streamlit run app.py
   ```

## Screenshots / demo

- **Tab 1 (`📸 Feature 1`):** Upload or snap a photo of any book cover (or use the built-in 1-click sample book generator) to see Gemma 4 E2B identify the book and highlight its exact Floor, Shelf, Row, and Column.
- **Tab 2 (`🧭 Feature 2`):** Filter by any of the 16 IIUC Departments → Semester → Course to view recommended textbooks, bilingual exam strategies, and the highlighted 2D shelf matrix.

## What's not done yet

- Real-time barcode/RFID check-in integration with the physical IIUC Central Library circulation desk.
- Peer-to-peer student book lending notifications via Telegram.

## Credits

- Built solo during **Hacktoberfest Hack Day Chittagong x IEEE Computer Society IIUC SBC** organized by ML Bangladesh & Major League Hacking (MLH).
- Powered by Google's open-weight **Gemma 4 E2B** model running locally on Ollama.
