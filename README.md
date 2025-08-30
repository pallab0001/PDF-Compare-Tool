# 📄 PDF Comparison Tool
As part of my internship with SureProEd, I recently completed an exciting assignment.
A simple and efficient **PDF Comparison Tool** built with **Python** and **Streamlit** as part of my internship assignment at **SureProEd**.  
This app allows users to **compare two PDF documents** and check whether they are identical or have text differences.

---

## 🚀 Features
- ✅ Upload two PDF files
- ✅ Compare PDFs by **hash** and **content**
- ✅ Display whether the files are identical or different
- ✅ Lightweight and easy-to-use web interface built with Streamlit

---

## 🌐 Live Demo
🔗 [Click here to access the app](https://pdf-compare-tool.streamlit.app/)

---

## 📂 GitHub Repository
[https://github.com/YourUsername/pdf-compare-tool](https://github.com/pallab0001/PDF-Compare-Tool)

---

## 🛠 Tech Stack
- **Python**
- **Streamlit**
- **PyPDF (pypdf)** for PDF text extraction
- **hashlib** for hashing
- **difflib** for content difference

---

## ⚙️ Installation & Setup

1. **Clone the repository**
   ```bash
   git clone https://github.com/YourUsername/pdf-compare-tool.git
   cd pdf-compare-tool
2. **Create a virtual environment**
   ```bash
   python -m venv venv
   source venv/bin/activate      # For Mac/Linux
   venv\Scripts\activate         # For Windows
3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
4. **Run the app**
   ```bash
   streamlit run app.py
