import streamlit as st

def valuta_candidato(esperienza, titolo_studio, competenze):
    if esperienza > 5:
        return "A"
    elif 3 <= esperienza <= 5:
        if titolo_studio == 0:
            return "B"
        elif titolo_studio >= 1:
            if competenze == 2:
                return "A"
            else:
                return "B"
    elif esperienza <= 2:
        if titolo_studio == 2:
            if competenze == 2:
                return "A"
            else:
                return "B"
        else:
            return "B"

# Interfaccia Streamlit
st.set_page_config(page_title="Valutazione Assunzione", page_icon="🧠")

st.title("🧑‍💼 Valutazione Candidato per Assunzione")

st.markdown("Inserisci le informazioni del candidato:")

esperienza = st.number_input("Anni di esperienza", min_value=0, max_value=50, step=1)

titolo_studio_label = {
    "Diploma": 0,
    "Laurea Triennale": 1,
    "Laurea Magistrale o superiore": 2
}
titolo_input = st.selectbox("Titolo di studio", list(titolo_studio_label.keys()))
titolo_studio = titolo_studio_label[titolo_input]

competenze_label = {
    "Scarse": 0,
    "Discrete": 1,
    "Eccellenti": 2
}
comp_input = st.selectbox("Competenze", list(competenze_label.keys()))
competenze = competenze_label[comp_input]

if st.button("Valuta"):
    risultato = valuta_candidato(esperienza, titolo_studio, competenze)
    if risultato == "A":
        st.success("✅ Il candidato è **Assunto (A)**")
    else:
        st.error("❌ Il candidato è **Respinto (B)**")
        
