# import library

import streamlit as st
import openai
from streamlit_chat import message
from streamlit_option_menu import option_menu

st.set_page_config(
    page_title="Stellar",
    page_icon="⭐"
)

# Navigasi
selected = option_menu(None, ["Stellar", "About"], 
        icons=['house', "list-task"], 
        menu_icon="cast", default_index=0, orientation="horizontal",)

# Awal Content Chatbot 

# Cara memangil API dan Konfigurasi
openai.api_key = st.secrets["model"]

def generate_response(prompt):
	completions = openai.Completion.create(
		engine = "text-davinci-003", # Untuk menggunakan model 
		prompt = prompt,             # Untuk menghasilkan teks 
		max_tokens = 1024,           # Jumlah maksimum token (kata dan tanda baca)
		n = 1,                       # Jumlah tanggapan
		stop = None,                 # Untuk berhenti menghasilkan teks
		temperature = 0.5,           # Untuk mengontrol teks yang dihasilkan
	)
	message = completions.choices[0].text
	return message

# View ( "Tampilan Chatbot")
if selected == "Stellar":
 st.markdown("""# ⭐ Stellar
### Tanya Stellar

Hai, aku Stellar🙌

Kamu bisa panggil aku Sayang :see_no_evil:

Aku adalah asisten virtual **[Deval](https://devaldicaliesta.super.site/)** yang dibuat menggunakan **Model ChatGPT** yang dilatih oleh **[OpenAI](https://openai.com/blog/chatgpt/)**
Stellar bisa memberikanmu informasi apapun yang saat ini kamu butuhkan dan bisa jadi temen curhat
Kamu bisa mencari informasi dan teknologi yang digunakan di **ABOUT**.

""", True)

# Menyimpan obrolan chatbot
 if 'generated' not in st.session_state:
    st.session_state['generated'] = []

 if 'past' not in st.session_state:
    st.session_state['past'] = []

# Input Penguna 
 def get_text():
    input_text = st.text_input("Pertanyaan Saya: ","", key="input")
    return input_text 

# Respone Chatbot
 user_input = get_text()
   
 if user_input:
    output = generate_response(user_input)
    # Menyimpan output
    st.session_state.past.append(user_input)
    st.session_state.generated.append(output)

# Untuk menampilkan riwayat obrolan
 if st.session_state['generated']:

    for i in range(len(st.session_state['generated'])-1, -1, -1):
        message(st.session_state["generated"][i], key=str(i))
        message(st.session_state['past'][i], is_user=True, key=str(i) + '_user')
# Akhir Content Chatbot

# Awal Content About
if selected == "About":
    st.markdown("""# ⭐ Stellar
### Hallo Sahabat Stellar 🙌

Hai, Aku Stellar yang artinya bintang👋

Aku adalah asisten virtual **[Deval](https://devaldicaliesta.super.site/)** yang dibuat menggunakan **Model ChatGPT** yang dilatih oleh **[OpenAI](https://openai.com/blog/chatgpt/)**.
Stellar bisa memberikanmu informasi apapun yang saat ini kamu butuhkan dan bisa jadi temen curhat juga loh.
""", True)
    st.write("---")
    st.markdown("""
    ### Teknologi Yang Ada di Stellar ⭐
    Seperti yang telah disebutkan, **Stellar** merupakan chatbot yang dapat berkomunikasi dalam format percakapan dan dirancang untuk bisa berinteraksi selayaknya interaksi antar manusia🤗.       
    Pondasi dibalik teknologi chatbot sendiri adalah teknologi Artificial Intelligence (AI), 
    cabang ilmu komputer yang berkaitan dengan pemecahan masalah-masalah selayaknya manusia seperti berbicara, 
    memahami, ataupun berpikir🥳.

    Salah satu bidang dalam AI yang membuat chatbot dapat memproses bahasa alami manusia adalah Natural Language Processing (NLP). **Model ChatGPT** ini dapat digunakan tujuan yang beragam, seperti membuat obrolan otomatis di aplikasi percakapan, 
    membantu dalam pembuatan konten, atau bahkan membantu dalam penerjemahan berbagai bahasa dengan tingkat akurasi yang berbeda-beda untuk tiap bahasa.
    **Model ChatGPT** dilatih dengan menggunakan milyaran kalimat dari berbagai sumber, sehingga model ini dapat menangkap berbagai gaya bahasa dan konteks percakapan. 
    Selain itu, **Model ChatGPT** juga dapat dioptimalkan melalui **fine-tunning** dengan cara menambahkan data latih yang spesifik untuk tugas tertentu, sehingga hasilnya lebih akurat.

    **Model ChatGPT** ini masih memiliki batasan-batasan. **Model ChatGPT** tidak selalu dapat memberikan jawaban yang benar untuk pertanyaan yang bersifat subjektif, atau yang memerlukan pengetahuan yang spesifik dan up-to-date. 
    **Model ChatGPT** juga belum mampu memberikan informasi atau memahami konteks dari peristiwa setelah tahun 2021. 
    Selain itu, **Model ChatGPT** juga membutuhkan data latih yang cukup banyak untuk dapat berfungsi dengan baik.[Sumber](https://id.wikipedia.org/wiki/ChatGPT)
    
    **[Note] Stellar akan down kalau server OpenAI juga down**
    """, True)
# Akhir Content About

hide_st_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            header {visibility: hidden;}
            </style>
            """
st.markdown(hide_st_style, unsafe_allow_html=True)