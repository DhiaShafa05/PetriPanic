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
    "Listeria monocytogenes": {
        "Description": "Listeria monocytogenes adalah bakteri Gram-positif yang dapat tumbuh pada suhu rendah, seperti dalam makanan yang disimpan dalam lemari es.",
        "History": "Ditemukan pada tahun 1929 oleh E.G.D. Lister, namun baru dikenal lebih luas sebagai patogen pada tahun 1980-an.",
        "Source": "Produk susu yang tidak dipasteurisasi, daging olahan, makanan siap saji yang disimpan pada suhu yang salah.",
        "Symptoms": "Demam, nyeri otot, dan dalam kasus berat, listeriosis yang dapat menyebabkan keguguran pada wanita hamil, serta infeksi pada orang dengan sistem kekebalan tubuh yang lemah.",
        "Prevention": "Menghindari makanan yang tidak dipasteurisasi, memasak makanan hingga suhu internal yang tepat, serta menjaga kebersihan tempat penyimpanan makanan.",
        "Handling": "Listeriosis membutuhkan pengobatan medis segera, biasanya dengan antibiotik."
    },
    "Clostridium botulinum": {
        "Description": "Clostridium botulinum adalah bakteri Gram-positif yang dapat menghasilkan racun botulinum yang sangat berbahaya bagi manusia.",
        "History": "Bakteri ini ditemukan oleh Emile van Ermengem pada tahun 1895.",
        "Source": "Makanan kalengan yang tidak dipasteurisasi, ikan, dan daging.",
        "Symptoms": "Penglihatan kabur, kesulitan menelan, kelemahan otot, kelumpuhan.",
        "Prevention": "Memasak makanan dengan benar, menjaga kebersihan dalam proses pengalengan.",
        "Handling": "Jika terpapar, segera konsultasikan dengan dokter untuk mendapatkan pengobatan dengan antitoksin botulinum."
    },
    "Campylobacter jejuni": {
        "Description": "Campylobacter jejuni adalah bakteri berbentuk spiral yang sering menjadi penyebab utama diare pada manusia.",
        "History": "Ditemukan pada tahun 1886 oleh Theodor Escherich.",
        "Source": "Daging ayam mentah, air yang terkontaminasi, susu tidak dipasteurisasi.",
        "Symptoms": "Diare, sakit perut, demam.",
        "Prevention": "Memasak daging ayam hingga matang sempurna, mencuci tangan dengan sabun setelah menangani makanan mentah.",
        "Handling": "Konsumsi cairan yang cukup dan istirahat. Jika gejala berat, konsultasikan dengan dokter."
    },
    "Vibrio cholerae": {
        "Description": "Vibrio cholerae adalah bakteri penyebab kolera yang ditularkan melalui air atau makanan yang terkontaminasi.",
        "History": "Ditemukan oleh Filippo Pacini pada tahun 1854.",
        "Source": "Air yang terkontaminasi, makanan yang terkontaminasi seperti sayuran, kerang.",
        "Symptoms": "Diare berat, dehidrasi parah, muntah.",
        "Prevention": "Menghindari konsumsi air dan makanan yang tidak terjamin kebersihannya, memasak makanan dengan benar.",
        "Handling": "Jika terpapar, segera konsultasikan dengan dokter untuk perawatan rehidrasi dan antibiotik."
    },
    "Staphylococcus aureus": {
        "Description": "Staphylococcus aureus adalah bakteri yang dapat menghasilkan racun yang menyebabkan keracunan makanan.",
        "History": "Ditemukan oleh Sir Alexander Ogston pada tahun 1880.",
        "Source": "Produk susu, daging yang tidak dipasteurisasi, makanan yang tidak disimpan dengan benar.",
        "Symptoms": "Mual, muntah, kram perut.",
        "Prevention": "Menyimpan makanan pada suhu yang tepat, menjaga kebersihan tangan dan alat masak.",
        "Handling": "Makan segera setelah disiapkan, dan hindari meninggalkan makanan pada suhu ruangan terlalu lama."
    },
    "Bacillus cereus": {
        "Description": "Bacillus cereus adalah bakteri yang dapat menyebabkan keracunan makanan dengan gejala diare atau muntah.",
        "History": "Ditemukan pada tahun 1887 oleh Ferdinand Cohn.",
        "Source": "Nasi dan makanan yang telah dimasak tetapi disimpan pada suhu kamar terlalu lama.",
        "Symptoms": "Muntah, diare, kram perut.",
        "Prevention": "Menyimpan makanan pada suhu yang benar, tidak membiarkan makanan yang dimasak terlalu lama pada suhu kamar.",
        "Handling": "Jika terpapar, biasanya gejalanya akan sembuh dengan sendirinya setelah beberapa jam."
    },
    "Shigella spp.": {
        "Description": "Shigella adalah bakteri penyebab disentri, infeksi usus yang menyebabkan diare berdarah.",
        "History": "Ditemukan pada tahun 1897 oleh Kiyoshi Shiga.",
        "Source": "Makanan dan air yang terkontaminasi, terutama sayuran dan buah yang tidak dicuci dengan baik.",
        "Symptoms": "Diare berdarah, kram perut, demam.",
        "Prevention": "Mencuci tangan setelah menggunakan toilet dan sebelum makan, mencuci sayuran dan buah dengan air yang bersih.",
        "Handling": "Jika terpapar, pastikan cukup cairan dan segera konsultasikan dengan dokter."
    },
    "Yersinia enterocolitica": {
        "Description": "Yersinia enterocolitica adalah bakteri yang menyebabkan penyakit enteritis, infeksi saluran pencernaan.",
        "History": "Ditemukan oleh Alexandre Yersin pada tahun 1889.",
        "Source": "Daging babi, produk susu yang tidak dipasteurisasi, air yang terkontaminasi.",
        "Symptoms": "Diare, demam, sakit perut.",
        "Prevention": "Memasak daging babi dengan suhu yang aman, mencuci tangan setelah menangani produk daging mentah.",
        "Handling": "Menghindari makanan yang terkontaminasi dan pastikan pengolahan makanan dilakukan dengan benar."
    },
    "Norovirus": {
        "Description": "Norovirus adalah virus yang dapat menyebabkan gastroenteritis, sering dikenal dengan keracunan makanan.",
        "History": "Ditemukan pada tahun 1972.",
        "Source": "Makanan yang terkontaminasi, air yang tidak bersih.",
        "Symptoms": "Mual, muntah, diare, kram perut.",
        "Prevention": "Mencuci tangan dengan sabun, memanaskan makanan dengan benar.",
        "Handling": "Jika terpapar, pastikan banyak minum air untuk mencegah dehidrasi dan istirahat yang cukup."
    },
    # Menambahkan mikroba lainnya sesuai kebutuhan
    # Add another 15 types of microbes here as needed.
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
    
    # Membuat petunjuk tanpa menyebutkan nama mikroba
    clue = microbes_data[correct_microbe]["Description"]
    source = microbes_data[correct_microbe]["Source"]

    # Membuat pertanyaan tanpa nama mikroba
    question = f"Microba ini adalah bakteri yang dapat menyebabkan infeksi usus pada manusia, terutama ditemukan pada {source}. Apa nama mikroba ini?"

    # Menampilkan pertanyaan
    st.subheader("Petunjuk:")
    st.write(question)

    # Input tebakan
    user_guess = st.text_input("Tebak nama mikroba:")

    # Jika pengguna menebak
    if user_guess:
        if user_guess.lower() == correct_microbe.lower():
            st.success(f"Selamat! Jawaban Anda benar. Mikroba yang dimaksud adalah **{correct_microbe}**.")
            st.subheader("Penjelasan:")
            st.write(f"{correct_microbe} adalah {microbes_data[correct_microbe]['Description']}")
            st.write(f"Sejarah Penemuan: {microbes_data[correct_microbe]['History']}")
            st.write(f"Sumber Kontaminasi: {microbes_data[correct_microbe]['Source']}")
            st.write(f"Gejala: {microbes_data[correct_microbe]['Symptoms']}")
            st.write(f"Pencegahan: {microbes_data[correct_microbe]['Prevention']}")
            st.write(f"Penanganan: {microbes_data[correct_microbe]['Handling']}")
        else:
            st.error(f"Tebakan Anda salah. Coba lagi!")
            st.write(f"Jawaban yang benar adalah **{correct_microbe}**.")
            st.subheader("Penjelasan:")
            st.write(f"{correct_microbe} adalah {microbes_data[correct_microbe]['Description']}")
            st.write(f"Sejarah Penemuan: {microbes_data[correct_microbe]['History']}")
            st.write(f"Sumber Kontaminasi: {microbes_data[correct_microbe]['Source']}")
            st.write(f"Gejala: {microbes_data[correct_microbe]['Symptoms']}")
            st.write(f"Pencegahan: {microbes_data[correct_microbe]['Prevention']}")
            st.write(f"Penanganan: {microbes_data[correct_microbe]['Handling']}")

# Menu utama aplikasi
st.sidebar.title("Menu")
menu = st.sidebar.radio("Pilih Seksi", ["Library", "Petri Panic"])

if menu == "Library":
    library_section()
elif menu == "Petri Panic":
    petri_panic_game()

