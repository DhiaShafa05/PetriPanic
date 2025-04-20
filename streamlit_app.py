import streamlit as st

# Data Mikroba (30 Jenis)
microbes_data = {
    "Salmonella": {
        "Description": "Salmonella adalah bakteri yang sering ditemukan dalam produk hewani seperti telur dan daging ayam.",
        "History": "Ditemukan oleh Theobald Smith pada tahun 1885.",
        "Source": "Telur, daging ayam, produk susu yang terkontaminasi.",
        "Symptoms": "Diare, demam, mual, kram perut.",
        "Prevention": "Memasak makanan hingga matang sempurna dan mencuci tangan secara menyeluruh.",
        "Handling": "Jika terinfeksi, minum banyak cairan dan berkonsultasilah dengan dokter."
    },
    "Escherichia coli (E. coli)": {
        "Description": "E. coli adalah bakteri yang biasanya ditemukan di usus manusia dan hewan.",
        "History": "Ditemukan pada tahun 1885 oleh Theodor Escherich.",
        "Source": "Daging mentah, sayuran mentah yang terkontaminasi.",
        "Symptoms": "Diare berdarah, sakit perut, demam.",
        "Prevention": "Memasak daging hingga suhu yang aman dan mencuci sayuran dengan benar.",
        "Handling": "Jika terinfeksi, segera konsultasikan dengan tenaga medis."
    },
    "Staphylococcus aureus": {
        "Description": "Staphylococcus aureus adalah bakteri yang dapat menghasilkan racun yang menyebabkan keracunan makanan.",
        "History": "Ditemukan oleh Alexander Ogston pada tahun 1880.",
        "Source": "Makanan yang terkontaminasi oleh bakteri ini, seperti produk daging, telur, atau makanan yang disimpan pada suhu yang tidak tepat.",
        "Symptoms": "Muntah, diare, kram perut.",
        "Prevention": "Menjaga suhu makanan tetap aman dan menghindari makanan yang telah terkontaminasi.",
        "Handling": "Jika terpapar, gejala biasanya akan hilang dalam beberapa jam. Namun, jika parah, segera cari perawatan medis."
    },
    "Listeria monocytogenes": {
        "Description": "Listeria monocytogenes adalah bakteri yang dapat menyebabkan penyakit serius seperti listeriosis.",
        "History": "Ditemukan pada tahun 1924 oleh E.G.D. Murray.",
        "Source": "Produk susu yang tidak dipasteurisasi, daging yang tidak dimasak dengan benar.",
        "Symptoms": "Demam, nyeri otot, sakit kepala, mual.",
        "Prevention": "Menghindari konsumsi produk susu yang tidak dipasteurisasi, memasak makanan dengan suhu yang aman.",
        "Handling": "Segera dapatkan pengobatan antibiotik jika terinfeksi, terutama jika hamil atau memiliki sistem kekebalan tubuh yang lemah."
    },
    "Campylobacter jejuni": {
        "Description": "Campylobacter jejuni adalah bakteri yang menyebabkan penyakit yang dikenal sebagai campylobacteriosis.",
        "History": "Ditemukan pada tahun 1972 oleh Bruce R. B. Bell.",
        "Source": "Daging ayam yang tidak dimasak dengan benar, susu mentah.",
        "Symptoms": "Diare, demam, mual, kram perut.",
        "Prevention": "Memasak daging ayam hingga matang sempurna dan mencuci tangan setelah menangani makanan mentah.",
        "Handling": "Biasanya sembuh dalam beberapa hari tanpa pengobatan, tetapi penting untuk menghindari dehidrasi."
    },
    "Bacillus anthracis": {
        "Description": "Bacillus anthracis adalah bakteri penyebab penyakit antraks yang bisa menular melalui kontak dengan produk hewan.",
        "History": "Ditemukan oleh Robert Koch pada tahun 1877.",
        "Source": "Produk hewani yang tidak dimasak dengan benar.",
        "Symptoms": "Demam, batuk, nyeri dada, sesak napas, dan pada beberapa kasus, infeksi kulit.",
        "Prevention": "Memasak daging hingga suhu internal yang aman, menghindari konsumsi produk hewani yang terkontaminasi.",
        "Handling": "Jika terpapar, segera dapatkan perawatan medis, biasanya dengan antibiotik."
    },
    "Aspergillus flavus": {
        "Description": "Aspergillus flavus adalah jamur yang dapat menghasilkan aflatoksin, sebuah toksin yang sangat berbahaya bagi manusia.",
        "History": "Ditemukan pada tahun 1943.",
        "Source": "Kacang tanah, jagung, produk biji-bijian yang disimpan dalam kondisi lembab.",
        "Symptoms": "Keracunan makanan, gangguan hati, bahkan kanker hati jika terpapar dalam jumlah besar.",
        "Prevention": "Menjaga makanan pada suhu yang kering dan sejuk, menghindari makanan yang telah terkontaminasi jamur.",
        "Handling": "Jika terpapar, hindari konsumsi makanan yang terkontaminasi dan konsultasikan dengan tenaga medis."
    },
    "Clostridium botulinum": {
        "Description": "Clostridium botulinum adalah bakteri yang menghasilkan racun botulinum yang dapat menyebabkan keracunan makanan.",
        "History": "Ditemukan pada tahun 1895 oleh Emile van Ermengem.",
        "Source": "Makanan kalengan yang tidak diproses dengan benar, produk hewani yang terkontaminasi.",
        "Symptoms": "Kelumpuhan otot, kesulitan bernapas, dan dalam kasus parah, kematian.",
        "Prevention": "Memasak makanan dengan benar dan memastikan produk kalengan diproses dengan suhu yang tepat.",
        "Handling": "Jika terinfeksi, segera periksakan diri ke dokter dan dapatkan pengobatan berupa antitoksin botulinum."
    },
    "Vibrio cholerae": {
        "Description": "Vibrio cholerae adalah bakteri penyebab kolera yang ditularkan melalui air dan makanan yang terkontaminasi.",
        "History": "Ditemukan pada tahun 1854 oleh Robert Koch.",
        "Source": "Air yang terkontaminasi, makanan laut yang tidak dimasak dengan baik.",
        "Symptoms": "Diare parah, dehidrasi, muntah.",
        "Prevention": "Menghindari konsumsi air yang tidak terjamin kebersihannya dan memastikan makanan laut dimasak dengan benar.",
        "Handling": "Jika terinfeksi, segera rehidrasi dan konsultasikan dengan dokter untuk pengobatan lebih lanjut."
    },
    "Shigella": {
        "Description": "Shigella adalah bakteri yang menyebabkan penyakit shigellosis, sering ditularkan melalui kontak langsung dengan feses yang terkontaminasi.",
        "History": "Ditemukan pada tahun 1897 oleh Kiyoshi Shiga.",
        "Source": "Makanan atau air yang terkontaminasi dengan feses.",
        "Symptoms": "Diare berdarah, kram perut, demam.",
        "Prevention": "Menjaga kebersihan tangan dan sanitasi yang baik.",
        "Handling": "Jika terinfeksi, minum banyak cairan dan segera konsultasikan dengan tenaga medis."
    },
    "Trichinella spiralis": {
        "Description": "Trichinella spiralis adalah parasit penyebab trichinosis yang dapat ditularkan melalui konsumsi daging yang tidak dimasak dengan benar.",
        "History": "Ditemukan pada tahun 1835 oleh Richard Owen.",
        "Source": "Daging babi atau produk daging yang tidak dimasak dengan baik.",
        "Symptoms": "Sakit perut, mual, demam, nyeri otot.",
        "Prevention": "Memasak daging hingga suhu yang aman untuk membunuh parasit.",
        "Handling": "Jika terinfeksi, pengobatan dengan obat anti-parasit dapat diberikan."
    },
    "Norovirus": {
        "Description": "Norovirus adalah virus yang dapat menyebabkan gastroenteritis atau infeksi saluran pencernaan.",
        "History": "Ditemukan pada tahun 1972.",
        "Source": "Makanan atau air yang terkontaminasi, serta kontak dengan orang yang terinfeksi.",
        "Symptoms": "Mual, muntah, diare, sakit perut.",
        "Prevention": "Menjaga kebersihan tangan, menghindari konsumsi makanan yang terkontaminasi.",
        "Handling": "Biasanya sembuh dalam beberapa hari tanpa pengobatan khusus, tetapi penting untuk tetap terhidrasi."
    },
    # Tambah 20 jenis mikroba lainnya
    "Bacillus cereus": {
        "Description": "Bacillus cereus adalah bakteri yang dapat menyebabkan keracunan makanan, terutama dari nasi yang tidak disimpan dengan baik.",
        "History": "Ditemukan pada tahun 1955.",
        "Source": "Nasi yang dimasak dan dibiarkan pada suhu kamar terlalu lama.",
        "Symptoms": "Mual, diare, kram perut.",
        "Prevention": "Menyimpan nasi di suhu yang aman dan tidak membiarkannya pada suhu kamar terlalu lama.",
        "Handling": "Jika terinfeksi, gejala biasanya hilang dalam beberapa jam tanpa perawatan medis."
    },
    "Yersinia enterocolitica": {
        "Description": "Yersinia enterocolitica adalah bakteri yang dapat menyebabkan yersiniosis.",
        "History": "Ditemukan pada tahun 1957.",
        "Source": "Daging babi, susu yang tidak dipasteurisasi, sayuran yang terkontaminasi.",
        "Symptoms": "Demam, diare, sakit perut.",
        "Prevention": "Memasak daging hingga matang dan menghindari konsumsi susu yang tidak dipasteurisasi.",
        "Handling": "Biasanya sembuh dalam waktu beberapa minggu, tetapi terkadang membutuhkan pengobatan antibiotik."
    },
    "Toxoplasma gondii": {
        "Description": "Toxoplasma gondii adalah parasit penyebab toksoplasmosis, terutama berbahaya bagi wanita hamil.",
        "History": "Ditemukan pada tahun 1908.",
        "Source": "Daging yang tidak dimasak dengan baik, terutama daging domba dan kucing yang terinfeksi.",
        "Symptoms": "Gejala flu, tetapi dapat menyebabkan masalah serius pada bayi yang terinfeksi dalam kandungan.",
        "Prevention": "Memasak daging dengan baik dan mencuci tangan setelah menangani hewan atau daging mentah.",
        "Handling": "Konsultasikan dengan dokter jika hamil dan terpapar parasit ini."
    },
    "Cryptosporidium": {
        "Description": "Cryptosporidium adalah parasit penyebab cryptosporidiosis, infeksi yang disebabkan oleh konsumsi air yang terkontaminasi.",
        "History": "Ditemukan pada tahun 1976.",
        "Source": "Air yang terkontaminasi dengan feses hewan atau manusia.",
        "Symptoms": "Diare, kram perut, demam.",
        "Prevention": "Menghindari konsumsi air yang tidak terjamin kebersihannya dan menjaga kebersihan."
    },
    "Vibrio parahaemolyticus": {
        "Description": "Vibrio parahaemolyticus adalah bakteri penyebab infeksi yang ditularkan melalui konsumsi makanan laut yang tidak dimasak dengan benar.",
        "History": "Ditemukan pada tahun 1951.",
        "Source": "Makanan laut mentah atau setengah matang.",
        "Symptoms": "Diare, muntah, demam.",
        "Prevention": "Memasak makanan laut hingga matang sempurna.",
        "Handling": "Jika terinfeksi, biasanya sembuh dengan sendirinya dalam beberapa hari."
    },
    "Clostridium perfringens": {
        "Description": "Clostridium perfringens adalah bakteri yang sering ditemukan pada makanan yang disimpan dalam suhu yang tidak aman.",
        "History": "Ditemukan pada tahun 1892.",
        "Source": "Daging yang terkontaminasi dan disimpan pada suhu yang tidak aman.",
        "Symptoms": "Diare, kram perut.",
        "Prevention": "Memasak dan menyimpan makanan dengan benar, menjaga suhu makanan."
    },
    "Helicobacter pylori": {
        "Description": "Helicobacter pylori adalah bakteri yang dapat menyebabkan tukak lambung atau infeksi pada sistem pencernaan.",
        "History": "Ditemukan pada tahun 1982 oleh Barry Marshall dan Robin Warren.",
        "Source": "Daging yang terkontaminasi, makanan yang terkontaminasi.",
        "Symptoms": "Nyeri ulu hati, mual, perut kembung.",
        "Prevention": "Menjaga kebersihan makanan dan air."
    },
    # ... Tambahkan sisa mikroba lainnya
}

# Function untuk menampilkan halaman "Library"
def library_page():
    st.title("Food's Microorganism Encyclopedia")
    st.write("Selamat datang di ensiklopedia mikroorganisme pangan.")
    microbe_choice = st.selectbox("Pilih mikroba untuk mempelajari lebih lanjut:", list(microbes_data.keys()))
    st.write(f"**{microbe_choice}**")
    st.write(f"**Description**: {microbes_data[microbe_choice]['Description']}")
    st.write(f"**History**: {microbes_data[microbe_choice]['History']}")
    st.write(f"**Source**: {microbes_data[microbe_choice]['Source']}")
    st.write(f"**Symptoms**: {microbes_data[microbe_choice]['Symptoms']}")
    st.write(f"**Prevention**: {microbes_data[microbe_choice]['Prevention']}")
    st.write(f"**Handling**: {microbes_data[microbe_choice]['Handling']}")

# Soal untuk Mode Petri Panic (10 Soal Pilihan Ganda)
questions = [
    {
        "question": "Mikroba yang sering ditemukan dalam produk susu yang tidak dipasteurisasi dan dapat menyebabkan listeriosis adalah?",
        "options": ["Salmonella", "Listeria monocytogenes", "E. coli", "Campylobacter", "Staphylococcus aureus"],
        "answer": "Listeria monocytogenes",
        "explanation": "Listeria monocytogenes adalah bakteri yang dapat menyebabkan listeriosis, terutama pada ibu hamil dan individu dengan sistem kekebalan tubuh yang lemah."
    },
    {
        "question": "Mikroba yang menyebabkan keracunan makanan akibat konsumsi makanan laut yang tidak dimasak dengan benar adalah?",
        "options": ["Clostridium botulinum", "Vibrio cholerae", "Vibrio parahaemolyticus", "Escherichia coli", "Salmonella"],
        "answer": "Vibrio parahaemolyticus",
        "explanation": "Vibrio parahaemolyticus adalah bakteri yang sering ditemukan pada makanan laut mentah atau setengah matang dan dapat menyebabkan gastroenteritis."
    },
    {
        "question": "Mikroba yang dapat menghasilkan aflatoksin, yang berpotensi menyebabkan kanker hati adalah?",
        "options": ["Aspergillus flavus", "Clostridium perfringens", "Shigella", "Yersinia enterocolitica", "Staphylococcus aureus"],
        "answer": "Aspergillus flavus",
        "explanation": "Aspergillus flavus adalah jamur yang dapat menghasilkan aflatoksin, senyawa yang sangat berbahaya bagi manusia dan berisiko menyebabkan kanker hati."
    },
    {
        "question": "Bakteri penyebab diare berdarah dan sering ditemukan pada daging yang tidak dimasak sempurna adalah?",
        "options": ["Salmonella", "Campylobacter jejuni", "Staphylococcus aureus", "Bacillus cereus", "Listeria monocytogenes"],
        "answer": "Campylobacter jejuni",
        "explanation": "Campylobacter jejuni adalah bakteri yang dapat menyebabkan diare berdarah dan sering ditemukan pada daging ayam yang tidak dimasak dengan benar."
    },
    {
        "question": "Mikroba yang menyebabkan keracunan makanan akibat makanan yang terkontaminasi dengan racun yang dihasilkan oleh bakteri adalah?",
        "options": ["Staphylococcus aureus", "Escherichia coli", "Clostridium botulinum", "Salmonella", "Bacillus cereus"],
        "answer": "Staphylococcus aureus",
        "explanation": "Staphylococcus aureus menghasilkan racun yang menyebabkan keracunan makanan, terutama pada makanan yang disimpan dalam suhu yang salah."
    },
    {
        "question": "Mikroba yang dapat menyebabkan penyakit antraks pada manusia adalah?",
        "options": ["Bacillus anthracis", "Clostridium perfringens", "Campylobacter jejuni", "Vibrio cholerae", "Shigella"],
        "answer": "Bacillus anthracis",
        "explanation": "Bacillus anthracis adalah bakteri yang menyebabkan penyakit antraks pada manusia, dapat tertular melalui kontak dengan produk hewan."
    },
    {
        "question": "Bakteri yang menyebabkan penyakit kolera dan dapat ditularkan melalui air yang terkontaminasi adalah?",
        "options": ["Campylobacter jejuni", "Vibrio cholerae", "Listeria monocytogenes", "Escherichia coli", "Salmonella"],
        "answer": "Vibrio cholerae",
        "explanation": "Vibrio cholerae menyebabkan kolera yang ditularkan melalui konsumsi air yang terkontaminasi oleh feses manusia atau hewan."
    },
    {
        "question": "Mikroba yang menyebabkan infeksi lambung dan dapat menyebabkan tukak lambung adalah?",
        "options": ["Helicobacter pylori", "Shigella", "Bacillus cereus", "Campylobacter jejuni", "Aspergillus flavus"],
        "answer": "Helicobacter pylori",
        "explanation": "Helicobacter pylori adalah bakteri yang menyebabkan tukak lambung dan masalah pencernaan lainnya."
    },
    {
        "question": "Bakteri yang sering ditemukan pada makanan yang tidak disimpan dengan benar dan menyebabkan keracunan makanan adalah?",
        "options": ["Clostridium perfringens", "Listeria monocytogenes", "Campylobacter jejuni", "Escherichia coli", "Staphylococcus aureus"],
        "answer": "Clostridium perfringens",
        "explanation": "Clostridium perfringens adalah bakteri yang dapat menyebabkan keracunan makanan akibat pertumbuhan di makanan yang tidak disimpan dengan benar pada suhu yang salah."
    },
    {
        "question": "Mikroba yang dapat menyebabkan keracunan makanan serius dari makanan kalengan yang tidak diproses dengan benar adalah?",
        "options": ["Clostridium botulinum", "Staphylococcus aureus", "Vibrio cholerae", "E. coli", "Salmonella"],
        "answer": "Clostridium botulinum",
        "explanation": "Clostridium botulinum menghasilkan racun botulinum yang sangat berbahaya bagi manusia, terutama pada makanan kalengan yang tidak diproses dengan benar."
    },
]

# Function untuk menampilkan halaman "Petri Panic" (Game)
def petri_panic_page():
    st.title("Petri Panic Game!")
    score = 0
    for question in questions:
        st.write(question["question"])
        answer = st.radio("Pilih jawaban:", question["options"], key=question["question"])

        # Tampilan jawaban setelah memilih
        if st.button("Submit", key=f"submit_{question['question']}"):
            if answer == question["answer"]:
                score += 1
                st.markdown('<span style="color: green;">Jawaban Benar!</span>', unsafe_allow_html=True)
            else:
                st.markdown('<span style="color: red;">Jawaban Salah!</span>', unsafe_allow_html=True)
        
            st.write(f"Jawaban yang benar: {question['answer']}")
            st.write(f"Penjelasan: {question['explanation']}")
            st.write("------")

    st.write(f"Skor Anda: {score}/{len(questions)}")

# Main Menu
def main():
    st.title("Food's Microorganism Encyclopedia")
    page = st.sidebar.selectbox("Pilih Halaman", ["Library", "Petri Panic"])

    if page == "Library":
        library_page()
    elif page == "Petri Panic":
        petri_panic_page()

if __name__ == "__main__":
    main()
