"""
IIUC Smart Library Book Tagger & Exact Shelf Locator
Powered by Open-Source Gemma 4 E2B (via Ollama)

Top 2 Core Features:
1. Visual Book Scanner & Identifier: Capture or upload an image of ANY book -> Gemma 4 E2B identifies the book,
   tags its IIUC Department, Semester & Course, and shows its exact Floor, Shelf, Row, and Column.
2. Remote Course Book Finder & Shelf Locator: A student outside the library selects Department -> Semester -> Course
   and gets required textbooks + exact Floor No, Shelf No, Row No, and Column No with an interactive 2D Shelf Grid.
"""

import hashlib
import streamlit as st

from iiuc_library_data import (
    IIUC_DEPARTMENTS,
    SEMESTERS,
    FULL_CATALOG,
    get_all_books_flat,
)
from gemma_engine import (
    DEFAULT_MODEL_NAME,
    DEFAULT_OLLAMA_URL,
    check_ollama_status,
    identify_book_from_image,
    generate_custom_course_advice,
)

st.set_page_config(
    page_title="IIUC Smart Library Book Tagger & Locator",
    page_icon="📚",
    layout="wide",
    initial_sidebar_state="collapsed",
)

# Custom CSS for full multi-device responsiveness, clean badges, location cards, and visual shelf matrix
st.markdown(
    """
    <style>
    /* Viewport & base responsiveness */
    html, body, [data-testid="stAppViewContainer"] {
        max-width: 100vw;
        overflow-x: hidden;
    }

    /* Fluid page container padding */
    .block-container {
        padding-top: 2rem !important;
        padding-bottom: 3.5rem !important;
        padding-left: clamp(0.75rem, 3vw, 3rem) !important;
        padding-right: clamp(0.75rem, 3vw, 3rem) !important;
        max-width: 1300px;
    }

    /* Prevent text elements from overflowing */
    h1, h2, h3, h4, h5, h6, p, span, div {
        overflow-wrap: break-word;
        word-wrap: break-word;
    }

    /* Hero Banner */
    .main-banner {
        background: linear-gradient(135deg, #0f5132 0%, #198754 100%);
        color: white;
        padding: clamp(1rem, 2.5vw, 1.6rem) clamp(1rem, 3vw, 1.8rem);
        border-radius: 14px;
        margin-bottom: 1.2rem;
        box-shadow: 0 4px 14px rgba(15, 81, 50, 0.18);
    }
    .main-banner h1 {
        margin: 0;
        font-size: clamp(1.2rem, 3vw, 1.85rem);
        font-weight: 800;
        color: #ffffff;
        line-height: 1.25;
    }
    .main-banner p {
        margin: 0.4rem 0 0 0;
        font-size: clamp(0.85rem, 1.8vw, 1rem);
        opacity: 0.94;
        line-height: 1.45;
    }

    /* Responsive 4-Box Coordinate Grid */
    .coord-grid {
        display: grid;
        grid-template-columns: repeat(4, 1fr);
        gap: 12px;
        margin: 0.75rem 0;
        width: 100%;
    }
    .coord-box {
        background: #f8fafc;
        border: 2px solid #198754;
        border-radius: 12px;
        padding: 0.8rem 0.5rem;
        text-align: center;
        box-shadow: 0 2px 6px rgba(0,0,0,0.04);
        display: flex;
        flex-direction: column;
        justify-content: center;
        min-height: 78px;
    }
    .coord-label {
        font-size: clamp(0.68rem, 1.4vw, 0.78rem);
        text-transform: uppercase;
        letter-spacing: 0.04em;
        color: #475569;
        font-weight: 700;
        line-height: 1.2;
    }
    .coord-value {
        font-size: clamp(1.05rem, 2.2vw, 1.3rem);
        font-weight: 800;
        color: #0f5132;
        margin-top: 0.25rem;
        line-height: 1.2;
    }

    /* Tag Pills with flex container */
    .tag-pill-container {
        display: flex;
        flex-wrap: wrap;
        gap: 6px;
        margin: 0.4rem 0 0.6rem 0;
    }
    .tag-pill {
        display: inline-flex;
        align-items: center;
        padding: 0.25rem 0.65rem;
        border-radius: 999px;
        font-size: clamp(0.72rem, 1.5vw, 0.84rem);
        font-weight: 700;
        line-height: 1.3;
    }
    .pill-dept { background: #dcfce7; color: #166534; }
    .pill-sem  { background: #dbeafe; color: #1e40af; }
    .pill-crs  { background: #fef3c7; color: #92400e; }
    .pill-role { background: #f3e8ff; color: #6b21a8; }

    /* Department Summary Strip */
    .dept-summary-banner {
        display: flex;
        flex-wrap: wrap;
        gap: 0.5rem 1.2rem;
        background: #f1f5f9;
        border: 1px solid #cbd5e1;
        border-radius: 10px;
        padding: 0.7rem 1rem;
        margin: 0.8rem 0 1.2rem 0;
        align-items: center;
    }
    .dept-summary-item {
        font-size: clamp(0.82rem, 1.8vw, 0.92rem);
        color: #334155;
    }

    /* Visual Shelf Grid Card */
    .shelf-grid-card {
        background: #ffffff;
        border: 1px solid #e2e8f0;
        border-radius: 12px;
        padding: clamp(8px, 2vw, 14px);
        margin-top: 0.5rem;
        box-shadow: 0 1px 4px rgba(0,0,0,0.04);
        width: 100%;
    }
    .shelf-grid-title {
        font-weight: 700;
        font-size: clamp(0.78rem, 1.8vw, 0.9rem);
        color: #1e293b;
        margin-bottom: 6px;
        line-height: 1.3;
    }
    .shelf-grid-scroll-wrap {
        width: 100%;
        overflow-x: auto;
        -webkit-overflow-scrolling: touch;
        padding-bottom: 4px;
    }
    .shelf-grid-table {
        width: 100%;
        min-width: 280px;
        border-collapse: separate;
        border-spacing: 5px;
    }
    .shelf-cell {
        border: 1px solid #cbd5e1;
        border-radius: 6px;
        padding: 6px 3px;
        text-align: center;
        font-size: clamp(0.66rem, 1.4vw, 0.75rem);
        background: #f1f5f9;
        color: #64748b;
        white-space: nowrap;
    }
    .shelf-cell-active {
        border: 2px solid #15803d;
        border-radius: 6px;
        padding: 6px 3px;
        text-align: center;
        font-size: clamp(0.7rem, 1.5vw, 0.8rem);
        font-weight: 800;
        background: #22c55e;
        color: #ffffff;
        box-shadow: 0 0 10px rgba(34, 197, 94, 0.55);
        white-space: nowrap;
    }

    /* Ask Gemma button spacing container */
    .ask-btn-spacer {
        height: 1.75rem;
    }

    /* Responsive Tabs */
    div[data-baseweb="tab-list"] {
        gap: 6px !important;
        overflow-x: auto !important;
        scrollbar-width: thin;
        -webkit-overflow-scrolling: touch;
        border-bottom: 2px solid #e2e8f0;
        padding-bottom: 4px;
    }
    div[data-baseweb="tab"] {
        padding: 8px 12px !important;
        font-size: clamp(0.8rem, 1.8vw, 0.92rem) !important;
        font-weight: 600 !important;
        white-space: normal !important;
        text-align: center !important;
    }

    /* Touch Targets & Buttons */
    div[data-testid="stButton"] button {
        min-height: 42px;
        font-size: clamp(0.85rem, 1.8vw, 0.95rem) !important;
        border-radius: 8px !important;
    }

    /* Breakpoint: Tablets & below (<= 900px) */
    @media (max-width: 900px) {
        .coord-grid {
            grid-template-columns: repeat(2, 1fr);
            gap: 10px;
        }
    }

    /* Breakpoint: Mobile screens (<= 768px) */
    @media (max-width: 768px) {
        /* Stack multi-column horizontal blocks vertically */
        div[data-testid="stHorizontalBlock"] {
            flex-direction: column !important;
            gap: 0.9rem !important;
        }
        div[data-testid="stHorizontalBlock"] > div[data-testid="column"] {
            width: 100% !important;
            min-width: 100% !important;
            flex: 1 1 100% !important;
        }

        /* Hide desktop spacer on mobile */
        .ask-btn-spacer {
            display: none !important;
            height: 0 !important;
        }

        /* Full width touch-friendly controls */
        div[data-testid="stSelectbox"], 
        div[data-testid="stTextInput"],
        div[data-testid="stRadio"],
        div[data-testid="stFileUploader"] {
            width: 100% !important;
        }
    }

    /* Breakpoint: Small Mobile Phones (<= 480px) */
    @media (max-width: 480px) {
        .block-container {
            padding-top: 1rem !important;
            padding-bottom: 2rem !important;
            padding-left: 0.6rem !important;
            padding-right: 0.6rem !important;
        }
        .coord-grid {
            grid-template-columns: repeat(2, 1fr);
            gap: 8px;
        }
        .coord-box {
            padding: 0.55rem 0.35rem;
            min-height: 68px;
        }
        .shelf-grid-table {
            border-spacing: 3px;
        }
        .shelf-cell, .shelf-cell-active {
            padding: 5px 2px;
        }
    }
    </style>
    """,
    unsafe_allow_html=True,
)


def render_shelf_grid_html(shelf_no: str, target_row: int, target_col: int, total_rows: int = 5, total_cols: int = 6) -> str:
    """Renders a responsive visual 2D bookshelf matrix highlighting the exact Row and Column slot."""
    html = [
        f"<div class='shelf-grid-card'>",
        f"<div class='shelf-grid-title'>"
        f"🗄️ Visual Rack Map — Shelf <code>{shelf_no}</code> (Row {target_row}, Col {target_col})</div>",
        "<div class='shelf-grid-scroll-wrap'>",
        "<table class='shelf-grid-table'>",
    ]
    for r in range(1, total_rows + 1):
        html.append("<tr>")
        for c in range(1, total_cols + 1):
            if r == int(target_row) and c == int(target_col):
                html.append(f"<td class='shelf-cell-active'>📍 R{r}•C{c}<br>BOOK HERE</td>")
            else:
                html.append(f"<td class='shelf-cell'>R{r}•C{c}</td>")
        html.append("</tr>")
    html.append("</table></div></div>")
    return "".join(html)


def render_location_coordinates(floor_no: str, shelf_no: str, row_no: int, col_no: int, zone: str = ""):
    """Renders the physical coordinate bar using a responsive 4-box CSS Grid (auto wraps 2x2 on mobile)."""
    grid_html = (
        f"<div class='coord-grid'>"
        f"<div class='coord-box'><div class='coord-label'>🏢 Floor No</div>"
        f"<div class='coord-value'>{floor_no}</div></div>"
        f"<div class='coord-box'><div class='coord-label'>🗄️ Shelf No</div>"
        f"<div class='coord-value'>{shelf_no}</div></div>"
        f"<div class='coord-box'><div class='coord-label'>📏 Row No (Top→Down)</div>"
        f"<div class='coord-value'>Row {row_no}</div></div>"
        f"<div class='coord-box'><div class='coord-label'>📍 Col No (Left→Right)</div>"
        f"<div class='coord-value'>Col {col_no}</div></div>"
        f"</div>"
    )
    st.markdown(grid_html, unsafe_allow_html=True)
    if zone:
        st.caption(f"🧭 **Library Zone:** {zone} • **Call Tag:** `IIUC-{shelf_no}-R{row_no}C{col_no}`")


# Sidebar configuration
with st.sidebar:
    st.markdown(
        """
        <div style="display:flex; align-items:center; gap:10px; margin-bottom:1.2rem; padding-bottom:0.8rem; border-bottom:1px solid #e2e8f0;">
            <span style="font-size:1.6rem; line-height:1;">🏛️</span>
            <div>
                <h3 style="margin:0; font-size:1.15rem; font-weight:800; color:#0f5132;">IIUC Library Controls</h3>
                <span style="font-size:0.75rem; color:#64748b;">Model Settings & Info</span>
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )

    with st.expander("⚙️ Model Settings & Server URL", expanded=True):
        ollama_url = st.text_input("Ollama Server URL", value=DEFAULT_OLLAMA_URL)
        model_name = st.text_input("Ollama Model Tag", value=DEFAULT_MODEL_NAME)

        status = check_ollama_status(ollama_url)
        if status["online"]:
            st.success(f"🟢 Ollama Connected ({len(status['models'])} models)")
            if status["models"]:
                st.caption("Installed: " + ", ".join(status["models"][:5]))
        else:
            st.warning("Ollama is unavailable. Image recognition needs a working model connection; manual catalogue search remains available.")

    with st.expander("🏛️ Library Coverage & Info", expanded=False):
        st.info(
            f"**16 IIUC Departments** across **6 Faculties + CGED**\n\n"
            f"**8 Semesters** per Department\n\n"
            f"**{len(get_all_books_flat())}+ Pre-Tagged Books** with exact **Floor, Shelf, Row & Column** coordinates."
        )

# Top Header
st.markdown(
    """
    <div class="main-banner">
        <h1>📚 IIUC Smart Library Book Tagger & Exact Shelf Locator</h1>
        <p>Powered by Open-Source <b>Gemma 4 E2B (Multimodal AI)</b> • Snap any book to identify it, or find course books remotely with exact <b>Floor, Shelf, Row & Column</b> coordinates.</p>
    </div>
    """,
    unsafe_allow_html=True,
)

st.info("Prototype: catalogue courses, shelf locations and availability are sample data, not verified IIUC library records.")

# Two Main Feature Tabs
tab_scanner, tab_finder = st.tabs(
    [
        "📸 Feature 1: Snap / Upload Any Book (AI Book Identifier)",
        "🧭 Feature 2: Course Book Finder & Shelf Locator (All 16 Departments)",
    ]
)

# ==============================================================================
# FEATURE 1: SNAP OR UPLOAD ANY BOOK IMAGE -> IDENTIFY & LOCATE
# ==============================================================================
with tab_scanner:
    st.subheader("📸 Capture or Upload Any Book Cover / Page")
    st.write(
        "Take a photo of **any book** using your webcam/phone or upload an image. "
        "**Gemma 4 E2B** reads the cover, identifies the book, matches it to the right **IIUC Department, Semester & Course**, "
        "and gives you its exact **Floor No, Shelf No, Row No, and Column No**."
    )

    col_input, col_result = st.columns([1, 1.35], gap="large")

    with col_input:
        input_mode = st.radio(
            "Choose Image Input Method:",
            [
                "📁 Upload Book Image (JPG / PNG)",
                "📷 Live Camera Capture (Webcam / Phone)",
            ],
            horizontal=True,
        )

        image_bytes_to_analyze = None

        if input_mode == "📁 Upload Book Image (JPG / PNG)":
            uploaded = st.file_uploader("Upload a photo of a book cover or title page", type=["png", "jpg", "jpeg", "webp"])
            if uploaded is not None:
                image_bytes_to_analyze = uploaded.read()
                st.image(image_bytes_to_analyze, caption="Uploaded Book Image", use_container_width=True)

        elif input_mode == "📷 Live Camera Capture (Webcam / Phone)":
            cam_photo = st.camera_input("Point camera at book cover or title page")
            if cam_photo is not None:
                image_bytes_to_analyze = cam_photo.read()

        manual_hint = st.text_input(
            "Optional Text Hint (or type book title/topic if testing without a photo):",
            value="",
            placeholder="e.g., Introduction to Algorithms CLRS or Digital Logic Morris Mano",
        )

        analyze_btn = st.button("🔍 Identify Book & Locate Shelf with Gemma 4 E2B", type="primary", use_container_width=True)

    scan_key = hashlib.sha256(
        (image_bytes_to_analyze or b"")
        + repr((manual_hint, model_name, ollama_url, "validated-scanner-v2")).encode("utf-8")
    ).hexdigest()
    if st.session_state.get("scan_input_key") != scan_key:
        st.session_state.pop("last_scan_result", None)
        st.session_state["scan_input_key"] = scan_key

    with col_result:
        if analyze_btn:
            if not image_bytes_to_analyze and not manual_hint.strip():
                st.error("Please upload/capture a book image or enter a title/topic hint first.")
            else:
                with st.spinner("Gemma 4 E2B is reading the book image and mapping to IIUC Library coordinates..."):
                    result = identify_book_from_image(
                        image_bytes=image_bytes_to_analyze,
                        manual_hint=manual_hint,
                        model_name=model_name,
                        base_url=ollama_url,
                    )
                    st.session_state["last_scan_result"] = result

        if "last_scan_result" in st.session_state:
            res = st.session_state["last_scan_result"]
            if res.get("error"):
                st.warning(res["error"])
                with st.expander("Technical details"):
                    st.code(res.get("raw_model_response", ""))
            elif not res.get("catalog_match"):
                st.markdown(f"### {res['book_title']}")
                st.write(f"Author: {res['author']} | Edition: {res['edition']}")
                st.warning("Title read by Gemma, but no reliable catalogue match was found. Location and availability are unknown.")
                with st.expander("View model response"):
                    st.code(res.get("raw_model_response", ""))
            else:
                st.success(res["source"])
    
                st.markdown(f"### 📖 {res['book_title']}")
                st.write(f"**Author:** {res['author']}  |  **Edition:** {res['edition']}  |  **Copies in Library:** `{res['copies_available']}`")
    
                # Academic Tag Pills
                st.markdown(
                    f"<div class='tag-pill-container'>"
                    f"<span class='tag-pill pill-dept'>🏛️ Dept: {res['dept_code']}</span>"
                    f"<span class='tag-pill pill-sem'>🎓 {res['semester']}</span>"
                    f"<span class='tag-pill pill-crs'>📘 {res['course_code']}: {res['course_title']}</span>"
                    f"</div>",
                    unsafe_allow_html=True,
                )
    
                st.markdown("#### 📍 Sample catalogue location")
                render_location_coordinates(
                    floor_no=res["floor_no"],
                    shelf_no=res["shelf_no"],
                    row_no=res["row_no"],
                    col_no=res["col_no"],
                    zone=res.get("zone", ""),
                )
    
                # 2D Visual Shelf Grid
                st.markdown(
                    render_shelf_grid_html(
                        shelf_no=res["shelf_no"],
                        target_row=res["row_no"],
                        target_col=res["col_no"],
                    ),
                    unsafe_allow_html=True,
                )
    
                st.markdown("#### 🧠 Gemma 4 E2B Syllabus & Exam Guide")
                st.info(
                    f"**🇬🇧 English Study Tip:** {res['exam_tip_en']}\n\n"
                    f"**🇧🇩 বাংলা পরামর্শ:** {res['exam_tip_bn']}"
                )
    
                if res.get("detected_topics"):
                    st.write("**Key Covered Topics:** " + " • ".join([f"`{t}`" for t in res["detected_topics"]]))
    
                with st.expander("🔧 View Raw Gemma 4 E2B Model Output"):
                    st.code(res.get("raw_model_response") or "Matched via IIUC Catalog Engine", language="json")
        else:
            st.info("👈 Upload or capture a book image on the left and click **Identify Book & Locate Shelf** to see the full breakdown.")


# ==============================================================================
# FEATURE 2: REMOTE STUDENT COURSE BOOK FINDER + EXACT SHELF LOCATOR
# ==============================================================================
with tab_finder:
    st.subheader("🧭 Not in the Library? Find Your Course Books & Exact Shelf Coordinates")
    st.write(
        "Select your **Department**, **Semester**, and **Course** from anywhere (home, hall, or classroom). "
        "You'll immediately get the required textbooks along with their exact **Floor No, Shelf No, Row No, and Column No** "
        "so you can walk straight to the rack when you reach campus."
    )

    # 3-Step Selection Bar
    f_col1, f_col2, f_col3 = st.columns(3)

    with f_col1:
        selected_dept_label = st.selectbox(
            "1️⃣ Select Your Department (All 16 IIUC Depts):",
            options=list(IIUC_DEPARTMENTS.keys()),
            index=0,
        )
        dept_meta = IIUC_DEPARTMENTS[selected_dept_label]
        dept_code = dept_meta["code"]

    with f_col2:
        selected_semester = st.selectbox(
            "2️⃣ Select Your Semester:",
            options=SEMESTERS,
            index=2,  # Default to 3rd Semester for instant rich demo
        )

    courses_for_sem = FULL_CATALOG.get(dept_code, {}).get(selected_semester, [])
    course_labels = [f"{c['course_code']} — {c['course_title']}" for c in courses_for_sem]

    with f_col3:
        selected_course_idx = st.selectbox(
            "3️⃣ Select Your Course:",
            options=range(len(course_labels)),
            format_func=lambda idx: course_labels[idx],
        )

    selected_course = courses_for_sem[selected_course_idx]
    course_books = selected_course["books"]

    # Department & Floor Summary Strip
    st.markdown(
        f"<div class='dept-summary-banner'>"
        f"<div class='dept-summary-item'>🏛️ <b>Faculty:</b> {dept_meta['faculty']}</div>"
        f"<div class='dept-summary-item'>🏢 <b>Allocated Floor:</b> <code>{dept_meta['floor_no']}</code> ({dept_meta['zone']})</div>"
        f"<div class='dept-summary-item'>📚 <b>Books Found:</b> <b>{len(course_books)}</b> for <code>{selected_course['course_code']}</code></div>"
        f"</div>",
        unsafe_allow_html=True,
    )

    # Display Each Recommended Book with Floor, Shelf, Row, Column + Visual Rack Grid
    for idx, book in enumerate(course_books, start=1):
        with st.container(border=True):
            b_left, b_right = st.columns([1.35, 1], gap="large")

            with b_left:
                st.markdown(
                    f"<div class='tag-pill-container'>"
                    f"<span class='tag-pill pill-role'>⭐ {book['role']}</span>"
                    f"<span class='tag-pill pill-dept'>{dept_code} • {selected_semester}</span>"
                    f"<span class='tag-pill pill-crs'>{selected_course['course_code']}</span>"
                    f"</div>",
                    unsafe_allow_html=True,
                )
                st.markdown(f"### {idx}. {book['title']}")
                st.write(
                    f"**Author:** {book['author']}  |  **Edition:** {book['edition']}  |  "
                    f"**Available Copies:** `{book['copies_available']} copies`"
                )

                st.markdown("##### 📍 Exact Library Shelf Coordinates")
                render_location_coordinates(
                    floor_no=book["floor_no"],
                    shelf_no=book["shelf_no"],
                    row_no=book["row_no"],
                    col_no=book["col_no"],
                    zone=dept_meta["zone"],
                )

                st.markdown(
                    f"**🇬🇧 Exam Strategy:** {book['exam_tip_en']}  \n"
                    f"**🇧🇩 পরীক্ষার প্রস্তুতি:** {book['exam_tip_bn']}"
                )
                st.caption("**Key Syllabus Topics:** " + " • ".join(book["topics"]))

            with b_right:
                st.markdown(
                    render_shelf_grid_html(
                        shelf_no=book["shelf_no"],
                        target_row=book["row_no"],
                        target_col=book["col_no"],
                    ),
                    unsafe_allow_html=True,
                )

    # Interactive Gemma 4 E2B Course Advisor Box
    st.markdown("#### 🤖 Ask Gemma 4 E2B for Custom Topic / Exam Advice on This Course")
    q_col1, q_col2 = st.columns([3, 1])
    with q_col1:
        student_topic = st.text_input(
            "What topic or exam are you preparing for?",
            placeholder=f"e.g., Which book has easier examples for {selected_course['course_title']} midterm?",
        )
    with q_col2:
        st.markdown("<div class='ask-btn-spacer'></div>", unsafe_allow_html=True)
        ask_gemma_btn = st.button("✨ Ask Gemma 4 E2B", use_container_width=True)

    if ask_gemma_btn:
        with st.spinner("Gemma 4 E2B is preparing your personalized IIUC study & book pickup plan..."):
            advice = generate_custom_course_advice(
                dept_label=selected_dept_label,
                semester=selected_semester,
                course_code=selected_course["course_code"],
                course_title=selected_course["course_title"],
                student_topic_query=student_topic,
                books=course_books,
                model_name=model_name,
                base_url=ollama_url,
            )
            st.success("🎓 **Gemma 4 E2B Study & Library Pickup Plan:**")
            st.markdown(advice)