###################################################
#              Generador de leads                 #
# V.2.0.0 //25 04 2025//                          #
# Desplegado con streamlit                        #
# Agentes impulsados con OpenAI                   #
# Desarrollador: Sergio Emiliano López Bautista   #
###################################################


# ------------------------- Requerimentos y librerías -------------------------------
import io
import os
import time
import codecs
import streamlit as st
from dotenv import load_dotenv, find_dotenv
from openai import OpenAI

# --------------------------- Seteadores ----------------------------------------------
st.set_page_config(page_title="Estudio de mercado", layout="wide")

#dotenv_path = find_dotenv()
#load_dotenv(dotenv_path, override=True)
#client = OpenAI(api_key = os.getenv("OPENAI_API_KEY"))
client = OpenAI(api_key = st.secrets["OPENAI_API_KEY"])

st.title("Estudio de mercado")

# --------------------------- Funciones -----------------------------------------------
def agente(tema):
    try:
        agente = client.responses.create(
        model= "gpt-4.1",
        input= f"Necesito un estudio de mercado acerca de {tema}"
        )
        return agente.output_text
    except Exception as e:
        st.error(f"Error: {str(e)}")
        return None

def maquina_de_escribir(respuesta):
    for word in respuesta.split(" "):
        yield word + " "
        time.sleep(0.02)

def instrucciones():
    with codecs.open("instrucciones.txt", "r", encoding="utf-8") as f:
        fi = f.read()
    file = fi.split('\n')
    for linea in file:
        st.markdown(linea)

# -------------------------------- Interfaz (MAIN)-------------------------------------

st.header("Dale, mano")
tema = st.text_input("De qué tema buscas información")

if st.button("investigar"):
    if tema:
        with st.spinner("investigando..."):
            st.markdown("### Vista previa de la información")
            st.markdown(agente(tema))
            #st.write_stream(maquina_de_escribir(agente(tema)))