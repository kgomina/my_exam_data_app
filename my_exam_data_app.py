import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

st.sidebar.markdown("## User Input Features")

# Saisie du nombre de pages à scraper
num_pages = st.sidebar.number_input("Pages indexes", min_value=1, max_value=10, value=3, step=1)
st.sidebar.write(f"Vous avez saisi {num_pages} pages.")

# Options disponibles
option = st.sidebar.selectbox(
    "Options",
    ("Scrape data using selenium", "Download scraped data", "Dashboard of the data", "Fill the form")
)

st.markdown("<h1 style='text-align: center; color: black;'>My_exam_data_app</h1>", unsafe_allow_html=True)

st.markdown("""
This app allows you to download scraped data on Houses and lands from Dakarvente
* **Python libraries:** base64, pandas, streamlit, matplotlib, seaborn
* **Data source:** [Dakarvente](https://dakarvente.com/annonces-categorie-appartements-vendre-61.html).
""")

# Fonction de loading des données
def load_(dataframe, title, key):
    if st.button(title, key):
        st.subheader('Display data dimension')
        st.write(f'Data dimension: {dataframe.shape[0]} rows and {dataframe.shape[1]} columns.')
        st.dataframe(dataframe)

# Charger les données 
load_(pd.read_csv('data/Dakarventenet1.csv'), 'Données nettoyées url1', '1')
load_(pd.read_csv('data/Dakarventenet2.csv'), 'Données nettoyées url2', '2')
load_(pd.read_csv('data/Dakarventenet3.csv'), 'Données nettoyées url3', '3')
load_(pd.read_csv('data/dakar_vente_scrap1.csv'), 'Données non nettoyées url1', '4')
load_(pd.read_csv('data/dakar_vente_scrap2.csv'), 'Données non nettoyées url2', '5')
load_(pd.read_csv('data/dakar_vente_scrap3.csv'), 'Données non nettoyées url3', '6')

# Section Dashboard
if option == "Dashboard of the data":
    st.markdown("## Dashboard des Données")
    data = pd.read_csv('data/Dakarventenet1.csv')
    if not data.empty:
        st.write("### Aperçu des données")
        st.dataframe(data.head())

        st.write("### Distribution des prix")
        fig, ax = plt.subplots()
        sns.histplot(data['prix'], bins=20, kde=True, ax=ax)
        st.pyplot(fig)

        st.write("### Nombre d'annonces par adresse")
        fig, ax = plt.subplots()
        sns.countplot(x='adresse', data=data, ax=ax)
        plt.xticks(rotation=45)
        st.pyplot(fig)
    else:
        st.write("Aucune donnée disponible pour le tableau de bord.")

# Formulaire d'évaluation de l'application
if option == "Fill the form":
    st.markdown("## Donnez votre avis sur l'application")
    avis = st.text_area("Comment trouvez-vous l'application ?")
    note = st.slider("Notez l'application (1-5)", 1, 5, 3)
    if st.button("Soumettre l'avis"):
        st.success("Merci pour votre retour !")







 


