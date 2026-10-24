"""
IIUC Central Library Curriculum, Course Catalog & Physical Shelf Coordinates Dataset
Covers all official faculties and departments of International Islamic University Chittagong (IIUC).
"""

import hashlib
import json
import os
from typing import Dict, List, Any

# Official IIUC Departments grouped by Faculty and assigned Central Library Floor & Zone
IIUC_DEPARTMENTS: Dict[str, Dict[str, Any]] = {
    "CSE - Computer Science & Engineering": {
        "code": "CSE",
        "faculty": "Faculty of Science & Engineering (FSE)",
        "floor_no": "Floor 3",
        "zone": "Science & Engineering Wing (North)",
        "shelf_prefix": "CSE-S",
    },
    "CCE - Computer & Communication Engineering": {
        "code": "CCE",
        "faculty": "Faculty of Science & Engineering (FSE)",
        "floor_no": "Floor 3",
        "zone": "Science & Engineering Wing (North-East)",
        "shelf_prefix": "CCE-S",
    },
    "EEE - Electrical & Electronic Engineering": {
        "code": "EEE",
        "faculty": "Faculty of Science & Engineering (FSE)",
        "floor_no": "Floor 3",
        "zone": "Science & Engineering Wing (East)",
        "shelf_prefix": "EEE-S",
    },
    "ETE - Electronic & Telecommunication Engineering": {
        "code": "ETE",
        "faculty": "Faculty of Science & Engineering (FSE)",
        "floor_no": "Floor 3",
        "zone": "Science & Engineering Wing (South-East)",
        "shelf_prefix": "ETE-S",
    },
    "CE - Civil Engineering": {
        "code": "CE",
        "faculty": "Faculty of Science & Engineering (FSE)",
        "floor_no": "Floor 3",
        "zone": "Science & Engineering Wing (West)",
        "shelf_prefix": "CE-S",
    },
    "PHARM - Pharmacy": {
        "code": "PHARM",
        "faculty": "Faculty of Science & Engineering (FSE)",
        "floor_no": "Floor 3",
        "zone": "Life Sciences & Pharmacy Corner",
        "shelf_prefix": "PHM-S",
    },
    "BBA - Business Administration": {
        "code": "BBA",
        "faculty": "Faculty of Business Studies (FBS)",
        "floor_no": "Floor 2",
        "zone": "Business & Management Hall (West)",
        "shelf_prefix": "BBA-S",
    },
    "FIN - Finance": {
        "code": "FIN",
        "faculty": "Faculty of Business Studies (FBS)",
        "floor_no": "Floor 2",
        "zone": "Business & Banking Hall (East)",
        "shelf_prefix": "FIN-S",
    },
    "EB - Economics & Banking": {
        "code": "EB",
        "faculty": "Faculty of Social Science (FSS)",
        "floor_no": "Floor 2",
        "zone": "Social Science & Economics Wing",
        "shelf_prefix": "EB-S",
    },
    "LAW - Department of Law": {
        "code": "LAW",
        "faculty": "Faculty of Law (FLAW)",
        "floor_no": "Floor 2",
        "zone": "Jurisprudence & Legal Archive",
        "shelf_prefix": "LAW-S",
    },
    "ELL - English Language & Literature": {
        "code": "ELL",
        "faculty": "Faculty of Arts & Humanities (FAE)",
        "floor_no": "Floor 1",
        "zone": "Humanities & Literature Gallery (North)",
        "shelf_prefix": "ELL-S",
    },
    "ALL - Arabic Language & Literature": {
        "code": "ALL",
        "faculty": "Faculty of Arts & Humanities (FAE)",
        "floor_no": "Floor 1",
        "zone": "Arabic & Middle Eastern Studies Hall",
        "shelf_prefix": "ALL-S",
    },
    "QSIS - Qur'anic Sciences & Islamic Studies": {
        "code": "QSIS",
        "faculty": "Faculty of Shari'ah & Islamic Studies (FSIS)",
        "floor_no": "Floor 4",
        "zone": "Tafsir & Qur'anic Research Wing",
        "shelf_prefix": "QSI-S",
    },
    "DIS - Da'wah & Islamic Studies": {
        "code": "DIS",
        "faculty": "Faculty of Shari'ah & Islamic Studies (FSIS)",
        "floor_no": "Floor 4",
        "zone": "Da'wah & Comparative Religion Wing",
        "shelf_prefix": "DIS-S",
    },
    "SHIS - Science of Hadith & Islamic Studies": {
        "code": "SHIS",
        "faculty": "Faculty of Shari'ah & Islamic Studies (FSIS)",
        "floor_no": "Floor 4",
        "zone": "Hadith & Sunnah Archive",
        "shelf_prefix": "SHI-S",
    },
    "CGED - Center for General Education (URC)": {
        "code": "URC",
        "faculty": "Center for General Education (CGED)",
        "floor_no": "Floor 1",
        "zone": "General & Compulsory URC Reference Zone",
        "shelf_prefix": "URC-S",
    },
}

SEMESTERS: List[str] = [
    "1st Semester",
    "2nd Semester",
    "3rd Semester",
    "4th Semester",
    "5th Semester",
    "6th Semester",
    "7th Semester",
    "8th Semester",
]

# Core curated courses & books for featured departments + automatic generator for all 8 semesters across all 16 departments
CURATED_COURSES: Dict[str, Dict[str, List[Dict[str, Any]]]] = {
    "CSE": {
        "1st Semester": [
            {
                "course_code": "CSE-1121",
                "course_title": "Structured Programming Language (C)",
                "books": [
                    {
                        "title": "Programming in ANSI C (8th Edition)",
                        "author": "E. Balagurusamy",
                        "edition": "8th Ed",
                        "role": "Primary Textbook",
                        "floor_no": "Floor 3",
                        "shelf_no": "CSE-S01",
                        "row_no": 2,
                        "col_no": 3,
                        "copies_available": 14,
                        "topics": ["C Syntax", "Loops", "Arrays", "Pointers", "Functions", "File I/O"],
                        "exam_tip_en": "Ch 1-5 for Midterm; Pointers, Structures & File Handling (Ch 9-12) for Final.",
                        "exam_tip_bn": "মিডটার্মের জন্য অধ্যায় ১-৫ এবং ফাইনালের জন্য পয়েন্টার ও স্ট্রাকচার (অধ্যায় ৯-১২) সবচেয়ে গুরুত্বপূর্ণ।",
                    },
                    {
                        "title": "Teach Yourself C (3rd Edition)",
                        "author": "Herbert Schildt",
                        "edition": "3rd Ed",
                        "role": "Reference Book",
                        "floor_no": "Floor 3",
                        "shelf_no": "CSE-S01",
                        "row_no": 2,
                        "col_no": 4,
                        "copies_available": 9,
                        "topics": ["Control Statements", "Data Types", "Pointers", "Standard Library"],
                        "exam_tip_en": "Great step-by-step practice exercises for 1st-semester lab quizzes.",
                        "exam_tip_bn": "ল্যাব কুইজ এবং বেসিক প্রোগ্রামিং অনুশীলনের জন্য এই বইটির উদাহরণগুলো খুব সহজ।",
                    },
                ],
            },
            {
                "course_code": "MAT-1101",
                "course_title": "Differential and Integral Calculus",
                "books": [
                    {
                        "title": "Calculus: Early Transcendentals (10th Edition)",
                        "author": "Howard Anton, Irl Bivens, Stephen Davis",
                        "edition": "10th Ed",
                        "role": "Primary Textbook",
                        "floor_no": "Floor 3",
                        "shelf_no": "CSE-S02",
                        "row_no": 1,
                        "col_no": 2,
                        "copies_available": 11,
                        "topics": ["Limits", "Derivatives", "Definite Integrals", "Maxima & Minima"],
                        "exam_tip_en": "Focus on exercise problems in Ch 2, 3, and 5—directly mirrored in IIUC mid/final papers.",
                        "exam_tip_bn": "অধ্যায় ২, ৩ এবং ৫-এর অনুশীলনীর অংকগুলো IIUC-এর পরীক্ষায় সরাসরি কমন আসে।",
                    }
                ],
            },
        ],
        "2nd Semester": [
            {
                "course_code": "CSE-1221",
                "course_title": "Object Oriented Programming (C++ / Java)",
                "books": [
                    {
                        "title": "Object-Oriented Programming with C++ (8th Edition)",
                        "author": "E. Balagurusamy",
                        "edition": "8th Ed",
                        "role": "Primary Textbook",
                        "floor_no": "Floor 3",
                        "shelf_no": "CSE-S02",
                        "row_no": 3,
                        "col_no": 1,
                        "copies_available": 12,
                        "topics": ["Classes & Objects", "Constructors", "Inheritance", "Polymorphism", "Operator Overloading"],
                        "exam_tip_en": "Classes & Constructors for Midterm; Inheritance, Virtual Functions & Templates for Final.",
                        "exam_tip_bn": "ক্লাস ও কনস্ট্রাক্টর মিডটার্মের জন্য এবং ইনহেরিট্যান্স ও পলিমরফিজম ফাইনালের জন্য পড়ুন।",
                    },
                    {
                        "title": "Java: The Complete Reference (12th Edition)",
                        "author": "Herbert Schildt",
                        "edition": "12th Ed",
                        "role": "Reference Book",
                        "floor_no": "Floor 3",
                        "shelf_no": "CSE-S02",
                        "row_no": 3,
                        "col_no": 2,
                        "copies_available": 7,
                        "topics": ["OOP Principles", "Exception Handling", "Multithreading", "Collections"],
                        "exam_tip_en": "Best reference for Java GUI project and exception handling questions.",
                        "exam_tip_bn": "জাভা প্রজেক্ট এবং এক্সসেপশন হ্যান্ডলিং বোঝার জন্য সেরা রেফারেন্স বই।",
                    },
                ],
            },
            {
                "course_code": "CSE-1223",
                "course_title": "Discrete Mathematics",
                "books": [
                    {
                        "title": "Discrete Mathematics and Its Applications (8th Edition)",
                        "author": "Kenneth H. Rosen",
                        "edition": "8th Ed",
                        "role": "Primary Textbook",
                        "floor_no": "Floor 3",
                        "shelf_no": "CSE-S02",
                        "row_no": 4,
                        "col_no": 5,
                        "copies_available": 15,
                        "topics": ["Propositional Logic", "Set Theory", "Mathematical Induction", "Graph Theory", "Trees"],
                        "exam_tip_en": "Ch 1 (Logic & Proofs) and Ch 10-11 (Graphs & Trees) carry over 60% of exam marks.",
                        "exam_tip_bn": "লজিক (অধ্যায় ১) এবং গ্রাফ থিওরি ও ট্রি (অধ্যায় ১০-১১) থেকে পরীক্ষায় সবচেয়ে বেশি প্রশ্ন আসে।",
                    }
                ],
            },
        ],
        "3rd Semester": [
            {
                "course_code": "CSE-2321",
                "course_title": "Data Structures",
                "books": [
                    {
                        "title": "Schaum's Outline of Data Structures with C",
                        "author": "Seymour Lipschutz",
                        "edition": "International Ed",
                        "role": "Primary Textbook",
                        "floor_no": "Floor 3",
                        "shelf_no": "CSE-S03",
                        "row_no": 2,
                        "col_no": 4,
                        "copies_available": 18,
                        "topics": ["Arrays", "Linked Lists", "Stacks", "Queues", "Binary Trees", "Graphs", "Sorting"],
                        "exam_tip_en": "The #1 must-have book for IIUC 3rd Semester. Every algorithm dry-run in exams comes from Lipschutz.",
                        "exam_tip_bn": "৩য় সেমিস্টারের সবচেয়ে জরুরি বই। স্ট্যাক, কিউ, লিংকড লিস্ট ও বাইনারি ট্রির সব অ্যালগরিদম এখান থেকে আসে।",
                    },
                    {
                        "title": "Data Structures Using C (2nd Edition)",
                        "author": "Reema Thareja",
                        "edition": "2nd Ed",
                        "role": "Reference Book",
                        "floor_no": "Floor 3",
                        "shelf_no": "CSE-S03",
                        "row_no": 2,
                        "col_no": 5,
                        "copies_available": 8,
                        "topics": ["Linked Lists", "AVL Trees", "Hashing", "Heaps"],
                        "exam_tip_en": "Contains clean C code implementations for lab assignments and viva.",
                        "exam_tip_bn": "ল্যাব অ্যাসাইনমেন্ট এবং ভাইভার জন্য সি কোডগুলো খুব পরিষ্কারভাবে দেওয়া আছে।",
                    },
                ],
            },
            {
                "course_code": "CSE-2323",
                "course_title": "Digital Logic Design",
                "books": [
                    {
                        "title": "Digital Design: With an Introduction to the Verilog HDL (6th Edition)",
                        "author": "M. Morris Mano, Michael D. Ciletti",
                        "edition": "6th Ed",
                        "role": "Primary Textbook",
                        "floor_no": "Floor 3",
                        "shelf_no": "CSE-S03",
                        "row_no": 4,
                        "col_no": 2,
                        "copies_available": 13,
                        "topics": ["Boolean Algebra", "K-Map", "Combinational Circuits", "Flip-Flops", "Counters"],
                        "exam_tip_en": "K-Map simplification (Ch 3) and Counters/Registers (Ch 5-6) are guaranteed exam questions.",
                        "exam_tip_bn": "কে-ম্যাপ (অধ্যায় ৩) এবং ফ্লিপ-ফ্লপ/কাউন্টার (অধ্যায় ৫-৬) পরীক্ষার জন্য ১০০% গুরুত্বপূর্ণ।",
                    }
                ],
            },
        ],
        "4th Semester": [
            {
                "course_code": "CSE-2421",
                "course_title": "Computer Algorithms",
                "books": [
                    {
                        "title": "Introduction to Algorithms (CLRS - 4th Edition)",
                        "author": "Thomas H. Cormen, Charles E. Leiserson, Ronald L. Rivest, Clifford Stein",
                        "edition": "4th Ed",
                        "role": "Primary Textbook",
                        "floor_no": "Floor 3",
                        "shelf_no": "CSE-S04",
                        "row_no": 1,
                        "col_no": 3,
                        "copies_available": 10,
                        "topics": ["Asymptotic Notation", "Divide & Conquer", "Dynamic Programming", "Greedy", "Shortest Paths"],
                        "exam_tip_en": "Master Theorem, LCS/Knapsack (DP), and Dijkstra/Bellman-Ford from CLRS are core exam staples.",
                        "exam_tip_bn": "মাস্টার থিওরেম, ডাইনামিক প্রোগ্রামিং (LCS, Knapsack) এবং গ্রাফ অ্যালগরিদম পড়ার জন্য মূল বই।",
                    },
                    {
                        "title": "Computer Algorithms / C++ (2nd Edition)",
                        "author": "Ellis Horowitz, Sartaj Sahni, Sanguthevar Rajasekaran",
                        "edition": "2nd Ed",
                        "role": "Reference Book",
                        "floor_no": "Floor 3",
                        "shelf_no": "CSE-S04",
                        "row_no": 1,
                        "col_no": 4,
                        "copies_available": 9,
                        "topics": ["Backtracking", "N-Queens", "Branch and Bound", "NP-Completeness"],
                        "exam_tip_en": "Easier step-by-step trace tables for Backtracking and Branch & Bound than CLRS.",
                        "exam_tip_bn": "ব্যাকট্র্যাকিং এবং ব্রাঞ্চ অ্যান্ড বাউন্ড অংশটি এই বই থেকে পড়া অনেক সহজ।",
                    },
                ],
            },
            {
                "course_code": "CSE-2423",
                "course_title": "Database Management Systems (DBMS)",
                "books": [
                    {
                        "title": "Database System Concepts (7th Edition)",
                        "author": "Abraham Silberschatz, Henry F. Korth, S. Sudarshan",
                        "edition": "7th Ed",
                        "role": "Primary Textbook",
                        "floor_no": "Floor 3",
                        "shelf_no": "CSE-S04",
                        "row_no": 3,
                        "col_no": 6,
                        "copies_available": 14,
                        "topics": ["ER Diagrams", "Relational Algebra", "SQL", "Normalization (1NF-BCNF)", "Transactions"],
                        "exam_tip_en": "ER Diagram + SQL queries for Midterm; Normalization (3NF/BCNF) & ACID Transactions for Final.",
                        "exam_tip_bn": "ইআর ডায়াগ্রাম ও SQL মিডটার্মের জন্য এবং নরমালাইজেশন (BCNF) ও ট্রানজেকশন ফাইনালের জন্য পড়ুন।",
                    }
                ],
            },
        ],
        "5th Semester": [
            {
                "course_code": "CSE-3521",
                "course_title": "Operating Systems",
                "books": [
                    {
                        "title": "Operating System Concepts (10th Edition - Dinosaur Book)",
                        "author": "Abraham Silberschatz, Peter Baer Galvin, Greg Gagne",
                        "edition": "10th Ed",
                        "role": "Primary Textbook",
                        "floor_no": "Floor 3",
                        "shelf_no": "CSE-S05",
                        "row_no": 2,
                        "col_no": 2,
                        "copies_available": 11,
                        "topics": ["Process Scheduling", "Threads", "Deadlocks (Banker's Algorithm)", "Paging & Virtual Memory"],
                        "exam_tip_en": "CPU Scheduling (Ch 5) & Deadlocks (Ch 8) for Midterm; Page Replacement (FIFO/LRU/Optimal) for Final.",
                        "exam_tip_bn": "সিপিইউ শিডিউলিং ও ডেডলক মিডটার্মের জন্য এবং পেজ রিপ্লেসমেন্ট অ্যালগরিদম ফাইনালের জন্য সবচেয়ে গুরুত্বপূর্ণ।",
                    }
                ],
            },
            {
                "course_code": "CSE-3523",
                "course_title": "Compiler Design",
                "books": [
                    {
                        "title": "Compilers: Principles, Techniques, and Tools (2nd Edition - Dragon Book)",
                        "author": "Alfred V. Aho, Monica S. Lam, Ravi Sethi, Jeffrey D. Ullman",
                        "edition": "2nd Ed",
                        "role": "Primary Textbook",
                        "floor_no": "Floor 3",
                        "shelf_no": "CSE-S05",
                        "row_no": 4,
                        "col_no": 1,
                        "copies_available": 8,
                        "topics": ["Lexical Analysis", "FIRST & FOLLOW", "LL(1) & LR Parsing", "Syntax-Directed Translation"],
                        "exam_tip_en": "Practice FIRST/FOLLOW sets, Left Recursion elimination, and CLR/LALR parsing tables from Ch 2 & 4.",
                        "exam_tip_bn": "লেফট রিকার্শন, FIRST ও FOLLOW সেট এবং পার্সিং টেবিল তৈরির অংকগুলো ভালো করে অনুশীলন করুন।",
                    }
                ],
            },
        ],
        "6th Semester": [
            {
                "course_code": "CSE-3621",
                "course_title": "Computer Networks",
                "books": [
                    {
                        "title": "Data Communications and Networking (5th Edition)",
                        "author": "Behrouz A. Forouzan",
                        "edition": "5th Ed",
                        "role": "Primary Textbook",
                        "floor_no": "Floor 3",
                        "shelf_no": "CSE-S06",
                        "row_no": 1,
                        "col_no": 5,
                        "copies_available": 16,
                        "topics": ["OSI & TCP/IP Models", "IPv4 Subnetting", "Error Detection (CRC)", "Routing Protocols"],
                        "exam_tip_en": "CRC error detection and IPv4 Subnetting/VLSM problems are guaranteed in Midterm/Final exams.",
                        "exam_tip_bn": "ওএসআই মডেল, সিআরসি (CRC) এবং আইপি সাবনেটিং (VLSM) অংক পরীক্ষার জন্য অপরিহার্য।",
                    }
                ],
            },
            {
                "course_code": "CSE-3623",
                "course_title": "Artificial Intelligence",
                "books": [
                    {
                        "title": "Artificial Intelligence: A Modern Approach (4th Edition)",
                        "author": "Stuart Russell, Peter Norvig",
                        "edition": "4th Ed",
                        "role": "Primary Textbook",
                        "floor_no": "Floor 3",
                        "shelf_no": "CSE-S06",
                        "row_no": 3,
                        "col_no": 4,
                        "copies_available": 9,
                        "topics": ["BFS/DFS", "A* Search", "Minimax & Alpha-Beta Pruning", "First-Order Logic"],
                        "exam_tip_en": "A* Heuristic search trace and Alpha-Beta Pruning game trees (Ch 3-5) appear every semester.",
                        "exam_tip_bn": "এ-স্টার (A*) সার্চ এবং আলফা-বিটা প্রুনিং ট্রি প্রতি সেমিস্টারের পরীক্ষায় আসে।",
                    }
                ],
            },
        ],
        "7th Semester": [
            {
                "course_code": "CSE-4721",
                "course_title": "Software Engineering & Information System Design",
                "books": [
                    {
                        "title": "Software Engineering: A Practitioner's Approach (9th Edition)",
                        "author": "Roger S. Pressman, Bruce R. Maxim",
                        "edition": "9th Ed",
                        "role": "Primary Textbook",
                        "floor_no": "Floor 3",
                        "shelf_no": "CSE-S07",
                        "row_no": 2,
                        "col_no": 3,
                        "copies_available": 10,
                        "topics": ["Agile & Scrum", "SDLC Models", "UML Diagrams", "Black-Box & White-Box Testing"],
                        "exam_tip_en": "SDLC comparison, Use-Case/DFD diagrams, and Cyclomatic Complexity testing are high-weight topics.",
                        "exam_tip_bn": "এসডিএলসি মডেল, ইউএমএল ডায়াগ্রাম এবং সফটওয়্যার টেস্টিং (Cyclomatic Complexity) ভালো করে পড়ুন।",
                    }
                ],
            }
        ],
        "8th Semester": [
            {
                "course_code": "CSE-4821",
                "course_title": "Machine Learning & Pattern Recognition",
                "books": [
                    {
                        "title": "Hands-On Machine Learning with Scikit-Learn, Keras, and TensorFlow (3rd Edition)",
                        "author": "Aurélien Géron",
                        "edition": "3rd Ed",
                        "role": "Primary Textbook",
                        "floor_no": "Floor 3",
                        "shelf_no": "CSE-S08",
                        "row_no": 5,
                        "col_no": 2,
                        "copies_available": 7,
                        "topics": ["Linear Regression", "SVM", "Decision Trees", "Neural Networks", "CNN"],
                        "exam_tip_en": "Great for both 8th-semester theory exams and final year thesis implementation.",
                        "exam_tip_bn": "ফাইনাল ইয়ার থিসিস এবং মেশিন লার্নিং থিওরি ও কোডিংয়ের জন্য সবচেয়ে কার্যকর বই।",
                    }
                ],
            }
        ],
    },
    "EEE": {
        "1st Semester": [
            {
                "course_code": "EEE-1101",
                "course_title": "Electrical Circuits I (DC)",
                "books": [
                    {
                        "title": "Fundamentals of Electric Circuits (7th Edition)",
                        "author": "Charles K. Alexander, Matthew N.O. Sadiku",
                        "edition": "7th Ed",
                        "role": "Primary Textbook",
                        "floor_no": "Floor 3",
                        "shelf_no": "EEE-S01",
                        "row_no": 1,
                        "col_no": 2,
                        "copies_available": 20,
                        "topics": ["Ohm's Law", "KCL & KVL", "Nodal & Mesh Analysis", "Thevenin & Norton Theorems"],
                        "exam_tip_en": "Solve worked examples of Mesh/Nodal (Ch 3) and Superposition/Thevenin (Ch 4) from Sadiku.",
                        "exam_tip_bn": "সাদিকুর বইয়ের অধ্যায় ৩ (নডাল ও মেশ) এবং অধ্যায় ৪ (থেভেনিন ও নর্টন)-এর উদাহরণগুলো শতভাগ জরুরি।",
                    }
                ],
            }
        ],
        "2nd Semester": [
            {
                "course_code": "EEE-1201",
                "course_title": "Electrical Circuits II (AC)",
                "books": [
                    {
                        "title": "Introductory Circuit Analysis (13th Edition)",
                        "author": "Robert L. Boylestad",
                        "edition": "13th Ed",
                        "role": "Primary Textbook",
                        "floor_no": "Floor 3",
                        "shelf_no": "EEE-S02",
                        "row_no": 2,
                        "col_no": 4,
                        "copies_available": 15,
                        "topics": ["Sinusoids & Phasors", "AC Power Analysis", "Three-Phase Circuits", "Resonance"],
                        "exam_tip_en": "Phasor diagrams and Balanced Three-Phase Y-Delta calculations are key for Finals.",
                        "exam_tip_bn": "ফেজর ডায়াগ্রাম এবং থ্রি-ফেজ সার্কিটের অংকগুলো ফাইনালের জন্য ভালো করে অনুশীলন করুন।",
                    }
                ],
            }
        ],
        "3rd Semester": [
            {
                "course_code": "EEE-2301",
                "course_title": "Electronic Devices & Circuits I",
                "books": [
                    {
                        "title": "Electronic Devices and Circuit Theory (11th Edition)",
                        "author": "Robert L. Boylestad, Louis Nashelsky",
                        "edition": "11th Ed",
                        "role": "Primary Textbook",
                        "floor_no": "Floor 3",
                        "shelf_no": "EEE-S03",
                        "row_no": 3,
                        "col_no": 3,
                        "copies_available": 17,
                        "topics": ["PN Junction Diode", "Clippers & Clampers", "BJT Biasing", "MOSFET Amplifiers"],
                        "exam_tip_en": "Clipper/Clamper wave shapes for Midterm; BJT DC/AC small-signal re-model for Final.",
                        "exam_tip_bn": "ডায়োড ক্লিপর/ক্ল্যাম্পার মিডটার্মের জন্য এবং BJT ও MOSFET বায়াসিং ফাইনালের জন্য পড়ুন।",
                    }
                ],
            }
        ],
    },
    "BBA": {
        "1st Semester": [
            {
                "course_code": "ACT-1101",
                "course_title": "Principles of Accounting",
                "books": [
                    {
                        "title": "Accounting Principles (14th Edition)",
                        "author": "Jerry J. Weygandt, Paul D. Kimmel, Donald E. Kieso",
                        "edition": "14th Ed",
                        "role": "Primary Textbook",
                        "floor_no": "Floor 2",
                        "shelf_no": "BBA-S01",
                        "row_no": 1,
                        "col_no": 3,
                        "copies_available": 19,
                        "topics": ["Journal Entries", "Ledger", "Trial Balance", "Adjusting Entries", "Financial Statements"],
                        "exam_tip_en": "Complete Accounting Cycle & Worksheet (Ch 1-4) is mandatory for Midterm.",
                        "exam_tip_bn": "জাবেদা, খতিয়ান, রেওয়ামিল এবং আর্থিক বিবরণী (অধ্যায় ১-৪) পরীক্ষার জন্য আবশ্যিক।",
                    }
                ],
            }
        ],
        "2nd Semester": [
            {
                "course_code": "MKT-1201",
                "course_title": "Principles of Marketing",
                "books": [
                    {
                        "title": "Principles of Marketing (18th Edition)",
                        "author": "Philip Kotler, Gary Armstrong",
                        "edition": "18th Ed",
                        "role": "Primary Textbook",
                        "floor_no": "Floor 2",
                        "shelf_no": "BBA-S02",
                        "row_no": 2,
                        "col_no": 5,
                        "copies_available": 16,
                        "topics": ["Marketing Mix (4Ps)", "Consumer Behavior", "Segmentation (STP)", "Branding Strategy"],
                        "exam_tip_en": "STP Strategy and 4Ps case examples from Kotler are directly asked in IIUC exams.",
                        "exam_tip_bn": "মার্কেটিং মিক্স (4Ps) এবং ক্রেতা আচরণ অধ্যায়গুলো কেস স্টাডির জন্য খুব গুরুত্বপূর্ণ।",
                    }
                ],
            }
        ],
    },
}

# Department-specific template courses so EVERY department (all 16) and EVERY semester (1-8) has rich, realistic courses and shelf locations
DEPT_COURSE_TEMPLATES: Dict[str, List[tuple]] = {
    "CCE": [
        ("CCE-1101", "Introduction to Computer & Communication Systems", "Data and Computer Communications", "William Stallings"),
        ("CCE-1201", "Object Oriented Programming & Data Structures", "Data Structures and Algorithm Analysis in C++", "Mark Allen Weiss"),
        ("CCE-2301", "Digital Communication & Coding Theory", "Modern Digital and Analog Communication Systems", "B.P. Lathi"),
        ("CCE-2401", "Computer Networks & Routing Switching", "Computer Networking: A Top-Down Approach", "James F. Kurose, Keith W. Ross"),
        ("CCE-3501", "Microprocessors & Embedded Systems", "The 8086 Microprocessor: Programming & Interfacing", "Kenneth J. Ayala"),
        ("CCE-3601", "Wireless & Mobile Communication", "Wireless Communications: Principles and Practice", "Theodore S. Rappaport"),
        ("CCE-4701", "Cryptography & Network Security", "Cryptography and Network Security", "William Stallings"),
        ("CCE-4801", "Cloud Computing & IoT Architecture", "Internet of Things: A Hands-On Approach", "Arshdeep Bahga, Vijay Madisetti"),
    ],
    "ETE": [
        ("ETE-1101", "Basic Electrical & Electronic Engineering", "Principles of Electric Circuits", "Thomas L. Floyd"),
        ("ETE-1201", "Signals and Linear Systems", "Signals and Systems (2nd Edition)", "Alan V. Oppenheim, Alan S. Willsky"),
        ("ETE-2301", "Analog & Digital Communication", "Communication Systems (5th Edition)", "Simon Haykin"),
        ("ETE-2401", "Electromagnetic Fields & Waves", "Elements of Electromagnetics", "Matthew N.O. Sadiku"),
        ("ETE-3501", "Digital Signal Processing (DSP)", "Digital Signal Processing: Principles, Algorithms", "John G. Proakis"),
        ("ETE-3601", "Optical Fiber Communications", "Optical Fiber Communications (5th Edition)", "Gerd Keiser"),
        ("ETE-4701", "Microwave & Antenna Engineering", "Antenna Theory: Analysis and Design", "Constantine A. Balanis"),
        ("ETE-4801", "5G Cellular & Satellite Communications", "Satellite Communications (4th Edition)", "Timothy Pratt"),
    ],
    "CE": [
        ("CE-1101", "Analytic Mechanics & Engineering Drawing", "Vector Mechanics for Engineers: Statics", "Ferdinand P. Beer, E. Russell Johnston"),
        ("CE-1201", "Surveying & Levelling", "Surveying: Vol. 1 & 2", "B.C. Punmia"),
        ("CE-2301", "Mechanics of Solids I", "Strength of Materials (4th Edition)", "Andrew Pytel, Ferdinand L. Singer"),
        ("CE-2401", "Fluid Mechanics & Hydraulics", "Fluid Mechanics with Engineering Applications", "Robert L. Daugherty"),
        ("CE-3501", "Design of Concrete Structures I", "Design of Concrete Structures (15th Edition)", "Arthur H. Nilson"),
        ("CE-3601", "Geotechnical & Foundation Engineering", "Principles of Geotechnical Engineering", "Braja M. Das"),
        ("CE-4701", "Transportation & Highway Engineering", "Traffic and Highway Engineering", "Nicholas J. Garber"),
        ("CE-4801", "Environmental & Water Resources Engineering", "Water Supply and Sanitary Engineering", "G.S. Birdie"),
    ],
    "PHARM": [
        ("PHM-1101", "Inorganic & Physical Pharmacy I", "Martin's Physical Pharmacy and Pharmaceutical Sciences", "Patrick J. Sinko"),
        ("PHM-1201", "Organic Pharmacy & Medicinal Chemistry", "Organic Chemistry (12th Edition)", "T.W. Graham Solomons"),
        ("PHM-2301", "Human Physiology & Anatomy", "Guyton and Hall Textbook of Medical Physiology", "John E. Hall"),
        ("PHM-2401", "Pharmacognosy & Phytochemistry", "Trease and Evans' Pharmacognosy", "William Charles Evans"),
        ("PHM-3501", "Pharmacology & Therapeutics I", "Goodman & Gilman's The Pharmacological Basis of Therapeutics", "Laurence L. Brunton"),
        ("PHM-3601", "Pharmaceutical Technology & Dosage Forms", "Aulton's Pharmaceutics: The Design and Manufacture of Medicines", "Michael E. Aulton"),
        ("PHM-4701", "Biopharmaceutics & Pharmacokinetics", "Applied Biopharmaceutics & Pharmacokinetics", "Leon Shargel"),
        ("PHM-4801", "Clinical Pharmacy & Hospital Practice", "Clinical Pharmacy and Therapeutics", "Roger Walker"),
    ],
    "FIN": [
        ("FIN-1101", "Introduction to Finance & Banking", "Principles of Managerial Finance (16th Edition)", "Chad J. Zutter, Scott B. Smart"),
        ("FIN-1201", "Financial Accounting & Reporting", "Intermediate Accounting (17th Edition)", "Donald E. Kieso"),
        ("FIN-2301", "Corporate Finance", "Fundamentals of Corporate Finance (13th Edition)", "Stephen A. Ross, Randolph W. Westerfield"),
        ("FIN-2401", "Islamic Banking & Finance Operations", "An Introduction to Islamic Finance", "Mufti Muhammad Taqi Usmani"),
        ("FIN-3501", "Investment Analysis & Portfolio Management", "Investments (12th Edition)", "Zvi Bodie, Alex Kane, Alan J. Marcus"),
        ("FIN-3601", "Financial Markets & Institutions", "Financial Markets and Institutions (9th Edition)", "Frederic S. Mishkin"),
        ("FIN-4701", "International Financial Management", "International Financial Management (14th Edition)", "Jeff Madura"),
        ("FIN-4801", "Derivatives & Risk Management", "Options, Futures, and Other Derivatives", "John C. Hull"),
    ],
    "EB": [
        ("EB-1101", "Principles of Microeconomics", "Principles of Microeconomics (9th Edition)", "N. Gregory Mankiw"),
        ("EB-1201", "Principles of Macroeconomics", "Macroeconomics (10th Edition)", "N. Gregory Mankiw"),
        ("EB-2301", "Mathematical Economics", "Fundamental Methods of Mathematical Economics", "Alpha C. Chiang"),
        ("EB-2401", "Islamic Economics & Central Banking", "Islamic Economics: Theory and Practice", "M.A. Mannan"),
        ("EB-3501", "Basic Econometrics", "Basic Econometrics (5th Edition)", "Damodar N. Gujarati"),
        ("EB-3601", "International Trade & Finance", "International Economics: Theory and Policy", "Paul R. Krugman, Maurice Obstfeld"),
        ("EB-4701", "Development Economics & Bangladesh Economy", "Economic Development (13th Edition)", "Michael P. Todaro, Stephen C. Smith"),
        ("EB-4801", "Commercial Bank Management & Basel Norms", "Bank Management & Financial Services", "Peter S. Rose"),
    ],
    "LAW": [
        ("LAW-1101", "Jurisprudence & Legal Theory", "Salmond on Jurisprudence (12th Edition)", "P.J. Fitzgerald"),
        ("LAW-1201", "Law of Contract & Tort", "Law of Contract", "Avtar Singh"),
        ("LAW-2301", "Constitutional Law of Bangladesh", "The Constitution of the People's Republic of Bangladesh", "Mahmudul Islam"),
        ("LAW-2401", "Islamic Jurisprudence (Usul al-Fiqh) & Muslim Family Law", "Principles of Islamic Jurisprudence", "Mohammad Hashim Kamali"),
        ("LAW-3501", "Law of Evidence & Limitation", "The Evidence Act, 1872: Principles and Digest", "M. Monir"),
        ("LAW-3601", "Code of Civil Procedure (CPC) & Specific Relief", "The Code of Civil Procedure, 1908", "DF Mulla"),
        ("LAW-4701", "Penal Code & Code of Criminal Procedure (CrPC)", "The Penal Code, 1860 & CrPC Commentary", "Zahirul Huq"),
        ("LAW-4801", "Public International Law & Human Rights", "International Law (9th Edition)", "Malcolm N. Shaw"),
    ],
    "ELL": [
        ("ELL-1101", "Introduction to Poetry & Drama", "The Norton Anthology of English Literature", "Stephen Greenblatt"),
        ("ELL-1201", "Introduction to Prose & Fiction", "Aspects of the Novel", "E.M. Forster"),
        ("ELL-2301", "Romantic Poetry", "English Romantic Poetry: An Anthology", "Harold Bloom"),
        ("ELL-2401", "Introduction to Linguistics & Phonetics", "The Study of Language (8th Edition)", "George Yule"),
        ("ELL-3501", "Elizabethan & Jacobean Drama (Shakespeare)", "The Arden Shakespeare Complete Works", "William Shakespeare"),
        ("ELL-3601", "Victorian & Modern Literature", "The Victorian Age in Literature", "G.K. Chesterton"),
        ("ELL-4701", "Literary Criticism & Theory", "Beginning Theory: An Introduction to Literary and Cultural Theory", "Peter Barry"),
        ("ELL-4801", "English Language Teaching (ELT) & SLA", "Approaches and Methods in Language Teaching", "Jack C. Richards, Theodore S. Rodgers"),
    ],
    "ALL": [
        ("ALL-1101", "Functional Arabic Grammar (An-Nahw)", "An-Nahw al-Wadih fi Qawa'id al-Lughah al-Arabiyyah", "Ali al-Jarim, Mustafa Amin"),
        ("ALL-1201", "Arabic Morphology (As-Sarf) & Composition", "Shadha al-Arf fi Fann as-Sarf", "Ahmad al-Hamlawi"),
        ("ALL-2301", "Classical Arabic Prose & Pre-Islamic Poetry", "Tarikh al-Adab al-Arabi", "Shawqi Dayf"),
        ("ALL-2401", "Rhetoric & Prosody (Al-Balaghah)", "Al-Balaghah al-Wadihah", "Ali al-Jarim"),
        ("ALL-3501", "Qur'anic & Prophetic Eloquence", "I'jaz al-Qur'an", "Al-Baqillani"),
        ("ALL-3601", "Modern Arabic Literature & Novel", "Modern Arabic Literature", "M.M. Badawi"),
        ("ALL-4701", "Arabic-English-Bangla Translation Studies", "A Dictionary of Modern Written Arabic", "Hans Wehr"),
        ("ALL-4801", "Applied Linguistics & Arabic Pedagogy", "Al-Arabiyyah Bayna Yadayk (Complete Series)", "Dr. Abdur Rahman Ibn Ibrahim Al-Fawzan"),
    ],
    "QSIS": [
        ("QSI-1101", "Ulum al-Qur'an (Sciences of the Qur'an)", "Mabahith fi Ulum al-Qur'an", "Manna al-Qattan"),
        ("QSI-1201", "Principles of Tafsir (Usul at-Tafsir)", "An Introduction to the Principles of Tafseer", "Ibn Taymiyyah"),
        ("QSI-2301", "Analytical Study of Surah Al-Baqarah & Aal-Imran", "Tafsir Ibn Kathir (Abridged English/Arabic)", "Hafiz Ibn Kathir"),
        ("QSI-2401", "Tafsir al-Ayat al-Ahkam (Legal Verses)", "Rawa'i al-Bayan Tafsir Ayat al-Ahkam", "Muhammad Ali al-Sabuni"),
        ("QSI-3501", "History of Tafsir Literature & Schools", "At-Tafsir wal-Mufassirun", "Dr. Muhammad Husayn adh-Dhahabi"),
        ("QSI-3601", "Scientific & Thematic Tafsir (Tafsir Mawdu'i)", "Al-Madkhal ila at-Tafsir al-Mawdu'i", "Dr. Abdul Sattar Fathallah"),
        ("QSI-4701", "Qira'at & Tajweed Sciences", "Al-Itqan fi Ulum al-Qur'an", "Jalal al-Din al-Suyuti"),
        ("QSI-4801", "Contemporary Issues in Qur'anic Thought", "Fi Zilal al-Qur'an (Selected Volumes)", "Sayyid Qutb"),
    ],
    "DIS": [
        ("DIS-1101", "Principles & Methodology of Da'wah (Usul ad-Da'wah)", "Al-Madkhal ila Ilm ad-Da'wah", "Muhammad Abu al-Fath al-Bayanuni"),
        ("DIS-1201", "Sirah of the Prophet (PBUH) & Da'wah Movements", "Ar-Raheeq Al-Makhtum (The Sealed Nectar)", "Safiur Rahman Mubarakpuri"),
        ("DIS-2301", "Islamic Aqeedah & Theology", "Kitab at-Tawhid & Sharh al-Aqeedah at-Tahawiyyah", "Ibn Abi al-Izz"),
        ("DIS-2401", "Comparative Study of World Religions", "Muqaranat al-Adyan (Comparative Religion)", "Dr. Ahmad Shalabi"),
        ("DIS-3501", "History of Islamic Civilization & Culture", "As-Sirah an-Nabawiyyah: Durus wa Ibar", "Dr. Mustafa as-Siba'i"),
        ("DIS-3601", "Communication, Media & Oratory in Da'wah", "Islamic Da'wah: Theory and Practice", "Sohirin Mohammad Solihin"),
        ("DIS-4701", "Contemporary Ideologies & Intellectual Challenges", "Islam at the Crossroads", "Muhammad Asad"),
        ("DIS-4801", "Social Welfare & NGO Management in Islam", "Al-Qaradawi on Fiqh of Zakah", "Yusuf al-Qaradawi"),
    ],
    "SHIS": [
        ("SHI-1101", "Mustalah al-Hadith (Principles of Hadith Classification)", "Taysir Mustalah al-Hadith", "Dr. Mahmud at-Tahhan"),
        ("SHI-1201", "History & Compilation of Sunnah", "As-Sunnah wa Makanatuha fi at-Tashri al-Islami", "Dr. Mustafa as-Siba'i"),
        ("SHI-2301", "Study of Sahih al-Bukhari & Sahih Muslim", "Fath al-Bari bi-Sharh Sahih al-Bukhari", "Ibn Hajar al-Asqalani"),
        ("SHI-2401", "Hadith al-Ahkam (Legal Traditions)", "Subul as-Salam Sharh Bulugh al-Maram", "Imam as-San'ani"),
        ("SHI-3501", "Ilm al-Jarh wa at-Ta'dil (Narrator Criticism)", "Taqrib at-Tahdhib", "Ibn Hajar al-Asqalani"),
        ("SHI-3601", "Study of Sunan Abu Dawud, Tirmidhi, Nasa'i & Ibn Majah", "Tuhfat al-Ahwadhi bi-Sharh Jami at-Tirmidhi", "Al-Mubarakpuri"),
        ("SHI-4701", "Takhrij al-Hadith & Chain Verification", "Usul at-Takhrij wa Dirasat al-Asanid", "Dr. Mahmud at-Tahhan"),
        ("SHI-4801", "Defense of Sunnah & Orientalist Critiques", "Studies in Early Hadith Literature", "Dr. Muhammad Mustafa Al-Azami"),
    ],
    "URC": [
        ("URED-1101", "Basic Teachings of Islam", "Islami Jibon Dhara (Islamic Way of Life)", "CGED Publication, IIUC"),
        ("URED-1201", "Sciences of Qur'an and Hadith (Compulsory)", "Introduction to Ulum al-Qur'an & Hadith", "CGED Editorial Board, IIUC"),
        ("URED-2301", "Introduction to Political Thought & Social Behavior", "Islamic Worldview & Ethics", "CGED Publication, IIUC"),
        ("URED-2401", "Life and Teachings of the Prophet Muhammad (PBUH)", "Ar-Raheeq Al-Makhtum (IIUC Student Edition)", "Safiur Rahman Mubarakpuri"),
        ("URED-3501", "History of the Emergence of Independent Bangladesh", "History of Bangladesh: 1947-1971", "Dr. Abu Md. Delwar Hossain"),
        ("URED-3601", "Bangladesh Studies & Socio-Economic Development", "Economy and Society of Bangladesh", "CGED Reference Series, IIUC"),
        ("URED-4701", "Professional Ethics & Moral Philosophy", "Ethics in Islam and Modern Professions", "CGED Publication, IIUC"),
        ("URED-4801", "Arabic for Daily & Academic Communication", "Al-Arabiyyah Li-Tullab al-Jami'ah", "IIUC Language Institute"),
    ],
    "EEE_EXTRA": [
        ("EEE-2401", "Electrical Machines I (Transformers & Motors)", "Electric Machinery Fundamentals (5th Edition)", "Stephen J. Chapman"),
        ("EEE-3501", "Power System Analysis I", "Elements of Power System Analysis (4th Edition)", "William D. Stevenson"),
        ("EEE-3601", "Control Systems I", "Modern Control Engineering (5th Edition)", "Katsuhiko Ogata"),
        ("EEE-4701", "Power Electronics & Industrial Drives", "Power Electronics: Circuits, Devices, and Applications", "Muhammad H. Rashid"),
        ("EEE-4801", "Renewable Energy & Smart Grid Systems", "Renewable and Efficient Electric Power Systems", "Gilbert M. Masters"),
    ],
    "BBA_EXTRA": [
        ("BBA-2301", "Organizational Behavior & HRM", "Organizational Behavior (18th Edition)", "Stephen P. Robbins, Timothy A. Judge"),
        ("BBA-2401", "Business Statistics & Quantitative Analysis", "Statistical Techniques in Business & Economics", "Douglas A. Lind"),
        ("BBA-3501", "Cost and Managerial Accounting", "Managerial Accounting (17th Edition)", "Ray H. Garrison, Eric W. Noreen"),
        ("BBA-3601", "Operations & Supply Chain Management", "Operations Management (14th Edition)", "William J. Stevenson"),
        ("BBA-4701", "Strategic Management & Business Policy", "Strategic Management: Concepts and Cases", "Fred R. David"),
        ("BBA-4801", "Entrepreneurship & SME Development", "Entrepreneurship: Successfully Launching New Ventures", "Bruce R. Barringer"),
    ],
}


def _build_complete_catalog() -> Dict[str, Dict[str, List[Dict[str, Any]]]]:
    """Builds a complete 16-department x 8-semester catalog with deterministic Floor, Shelf, Row, and Column coordinates."""
    catalog: Dict[str, Dict[str, List[Dict[str, Any]]]] = {}

    for dept_label, dept_meta in IIUC_DEPARTMENTS.items():
        code = dept_meta["code"]
        catalog[code] = {}
        curated_semesters = CURATED_COURSES.get(code, {})

        for sem_idx, sem_name in enumerate(SEMESTERS, start=1):
            if sem_name in curated_semesters:
                catalog[code][sem_name] = curated_semesters[sem_name]
                continue

            # Check extra templates for EEE and BBA or department templates
            if code == "EEE" and sem_idx >= 4:
                item = DEPT_COURSE_TEMPLATES["EEE_EXTRA"][sem_idx - 4]
            elif code == "BBA" and sem_idx >= 3:
                item = DEPT_COURSE_TEMPLATES["BBA_EXTRA"][sem_idx - 3]
            elif code in DEPT_COURSE_TEMPLATES:
                item = DEPT_COURSE_TEMPLATES[code][sem_idx - 1]
            else:
                item = (
                    f"{code}-{sem_idx}101",
                    f"{code} Core Course ({sem_name})",
                    f"Standard {code} Textbook ({sem_name})",
                    "IIUC Academic Press",
                )

            course_code, course_title, book_title, book_author = item
            shelf_no = f"{dept_meta['shelf_prefix']}0{sem_idx}"
            row_no = ((sem_idx - 1) % 5) + 1
            col_no = ((sem_idx * 2 - 1) % 6) + 1

            catalog[code][sem_name] = [
                {
                    "course_code": course_code,
                    "course_title": course_title,
                    "books": [
                        {
                            "title": book_title,
                            "author": book_author,
                            "edition": "Latest IIUC Syllabus Edition",
                            "role": "Primary Textbook",
                            "floor_no": dept_meta["floor_no"],
                            "shelf_no": shelf_no,
                            "row_no": row_no,
                            "col_no": col_no,
                            "copies_available": 6 + (sem_idx % 9),
                            "topics": [
                                f"{course_title} Fundamentals",
                                "Midterm Core Concepts",
                                "Analytical Problem Solving",
                                "Final Exam Case Studies",
                            ],
                            "exam_tip_en": f"Core textbook recommended by IIUC {code} faculty for {course_code} ({sem_name}).",
                            "exam_tip_bn": f"IIUC {code} বিভাগের {sem_name}-এর ({course_code}) মিডটার্ম ও ফাইনাল পরীক্ষার মূল পাঠ্যবই।",
                        },
                        {
                            "title": f"IIUC {course_code} Past Questions & Solution Guide",
                            "author": f"IIUC {code} Seminar Library Committee",
                            "edition": "2025-2026 Revised",
                            "role": "Reference & Past Paper Guide",
                            "floor_no": dept_meta["floor_no"],
                            "shelf_no": shelf_no,
                            "row_no": row_no,
                            "col_no": (col_no % 6) + 1,
                            "copies_available": 5,
                            "topics": [
                                "Solved Midterm Papers",
                                "Solved Final Papers",
                                "Chapter-wise Short Questions",
                            ],
                            "exam_tip_en": f"Contains previous 5 semesters of IIUC question patterns for {course_title}.",
                            "exam_tip_bn": f"বিগত ৫ সেমিস্টারের প্রশ্ন ও সমাধান অনুশীলনের জন্য এই গাইডটি অত্যন্ত সহায়ক।",
                        },
                    ],
                }
            ]

    return catalog


FULL_CATALOG = _build_complete_catalog()


def get_all_books_flat() -> List[Dict[str, Any]]:
    """Returns a flat list of all books across all departments & semesters for instant search/matching."""
    flat_books = []
    for dept_label, dept_meta in IIUC_DEPARTMENTS.items():
        code = dept_meta["code"]
        for sem_name, courses in FULL_CATALOG.get(code, {}).items():
            for course in courses:
                for book in course["books"]:
                    entry = dict(book)
                    entry["dept_code"] = code
                    entry["dept_label"] = dept_label
                    entry["faculty"] = dept_meta["faculty"]
                    entry["zone"] = dept_meta["zone"]
                    entry["semester"] = sem_name
                    entry["course_code"] = course["course_code"]
                    entry["course_title"] = course["course_title"]
                    flat_books.append(entry)
    return flat_books


def assign_Deterministic_Location(dept_code: str, semester: str, book_title: str) -> Dict[str, Any]:
    """
    If Gemma 4 E2B identifies a brand-new book from a photo that isn't in the static catalog yet,
    this assigns a consistent, realistic IIUC Central Library Floor, Shelf, Row, and Column coordinate.
    """
    matched_meta = None
    for _, meta in IIUC_DEPARTMENTS.items():
        if meta["code"].upper() == dept_code.upper():
            matched_meta = meta
            break
    if not matched_meta:
        matched_meta = IIUC_DEPARTMENTS["CSE - Computer Science & Engineering"]

    sem_num = 1
    for i in range(1, 9):
        if str(i) in str(semester):
            sem_num = i
            break

    digest = int(hashlib.md5(book_title.encode("utf-8")).hexdigest()[:6], 16)
    row_no = (digest % 5) + 1
    col_no = ((digest // 5) % 6) + 1
    shelf_no = f"{matched_meta['shelf_prefix']}0{sem_num}"

    return {
        "floor_no": matched_meta["floor_no"],
        "zone": matched_meta["zone"],
        "shelf_no": shelf_no,
        "row_no": row_no,
        "col_no": col_no,
    }