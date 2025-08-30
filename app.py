import streamlit as st
import hashlib

def get_file_hash(file):
    hash_obj = hashlib.sha1()
    for chunk in iter(lambda: file.read(4096), b""):
        hash_obj.update(chunk)
    file.seek(0)
    return hash_obj.hexdigest()

st.title("PDF Compare Tool")
file1 = st.file_uploader("Upload first PDF", type="pdf")
file2 = st.file_uploader("Upload second PDF", type="pdf")

if file1 and file2:
    hash1 = get_file_hash(file1)
    hash2 = get_file_hash(file2)
    if hash1 == hash2:
        st.success("PDFs are identical.")
    else:
        st.error("PDFs are different.")
