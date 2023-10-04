import streamlit as st
import os
import shutil
from zipfile import ZipFile
import tempfile

def rename_files(folder_path, new_prefix):
    for filename in os.listdir(folder_path):
        if filename.startswith("synthese_taxe_apprentissage_"):
            new_name = f"{new_prefix}_{filename.split('_')[2]}_2023.xlsx"
            os.rename(
                os.path.join(folder_path, filename),
                os.path.join(folder_path, new_name)
            )

st.title("Renommage des fichiers Excel")

uploaded_files = st.file_uploader("Téléchargez les fichiers Excel", accept_multiple_files=True)

new_prefix = st.text_input("Nouvelle préfixe:", value="22-EDF")

if uploaded_files and new_prefix:
    with tempfile.TemporaryDirectory() as temp_dir:
        for uploaded_file in uploaded_files:
            with open(os.path.join(temp_dir, uploaded_file.name), "wb") as f:
                f.write(uploaded_file.getbuffer())
        rename_files(temp_dir, new_prefix)
        # Créer un fichier zip pour le dossier modifié
        shutil.make_archive("renamed_files", 'zip', temp_dir)
        st.download_button(
            label="Téléchargez le dossier renommé",
            data=open("renamed_files.zip", "rb"),
            file_name="renamed_files.zip"
        )
