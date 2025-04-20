import streamlit as st

import streamlit as st
import random

# Data mikroba (informasi yang sudah ditambahkan lebih lengkap)
microbes_data = {
    "Salmonella enterica": {
        "Description": "Salmonella enterica adalah bakteri Gram-negatif berbentuk batang yang dapat menyebabkan infeksi usus pada manusia.",
        "History": "Ditemukan oleh Theobald Smith pada tahun 1885.",
        "Source": "Daging ayam mentah, telur mentah, susu tidak dipasteurisasi.",
        "Symptoms": "Diare, demam, kram perut, muntah.",
        "Prevention": "Memasak daging hingga matang sempurna, mencuci tangan dan peralatan masak setelah kontak dengan produk hewani mentah.",
        "Handling": "Jika terpapar, minum banyak cairan dan segera hubungi dokter jika gejala berat muncul."
    },
    "Escherichia coli (E. coli)": {
        "Description": "Escherichia coli (E. coli) adalah bakteri Gram-negatif yang biasanya ditemukan di usus manusia dan hewan.",
        "History": "Ditemukan oleh Theodor Escherich pada tahun 1885.",
        "Source": "Daging sapi kurang matang, sayuran yang terkontaminasi, air yang terkontaminasi.",
        "Symptoms": "Diare berdarah, kram perut, muntah.",
        "Prevention": "Memasak daging hingga suhu internal yang aman, mencuci sayuran dan buah dengan air mengalir, menghindari konsumsi air yang tidak terjamin kebersihannya.",
        "Handling": "Konsumsi cairan yang cukup dan konsultasikan dengan tenaga medis jika gejala berlangsung lebih dari dua hari."
    },
    # Tambahkan data mikroba lainnya sesuai kebutuhan...
}

# Fungsi untuk seksi "Library"
def library_section():
    st.title('🍽️ Library - Ensiklopedia Mikroorganisme dalam Makanan')
    st.markdown("""
    Di sini Anda bisa mengetahui berbagai mikroba yang ditemukan dalam makanan serta informasi terkait gejala infeksi, penanganan, dan pencegahan.
    Pilih mikroba di bawah untuk melihat detail informasi.
    """)
    
    # Sidebar untuk memilih mikroba
    microbe_choice = st.sidebar.selectbox('Pilih Mikroba', list(microbes_data.keys()))

    # Menampilkan informasi mikroba yang dipilih
    microbe = microbes_data[microbe_choice]

    st.header(f"🔬 {microbe_choice}")
    st.subheader("Deskripsi:")
    st.write(microbe["Description"])

    st.subheader("Sejarah Penemuan:")
    st.write(microbe["History"])

    st.subheader("Sumber Kontaminasi:")
    st.write(microbe["Source"])

    st.subheader("Gejala Infeksi:")
    st.write(microbe["Symptoms"])

    st.subheader("Pencegahan dan Penanganan:")
    st.write(microbe["Prevention"])

    st.subheader("Penanganan jika Terpapar:")
    st.write(microbe["Handling"])

# Fungsi untuk seksi "Petri Panic" (game tebak-tebakan mikroba)
def petri_panic_game():
    st.title("🎮 Petri Panic - Tebak Mikroba")
    st.markdown("""
    Selamat datang di game **Petri Panic**! 
    Anda akan diberikan petunjuk tentang mikroba yang ada dalam makanan. Tebak nama mikroba tersebut!
    """)
    
    # Memilih mikroba secara acak
    microbes_list = list(microbes_data.keys())
    correct_microbe = random.choice(microbes_list)
    clue = microbes_data[correct_microbe]["Description"]

    # Memulai game
    st.subheader("Petunjuk:")
    st.write(clue)

    user_guess = st.text_input("Tebak nama mikroba:")

    if user_guess.lower() == correct_microbe.lower():
        st.success("Selamat! Jawaban Anda benar.")
    elif user_guess != "":
        st.error("Tebakan Anda salah. Coba lagi!")

# Menu utama aplikasi
st.sidebar.title("Menu")
menu = st.sidebar.radio("Pilih Seksi", ["Library", "Petri Panic"])

if menu == "Library":
    library_section()
elif menu == "Petri Panic":
    petri_panic_game()

