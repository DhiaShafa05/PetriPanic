import streamlit as st

# Judul Halaman
st.title("Petri Panic🦠🍕")
st.write("Berikut adalah 20 jenis mikroorganisme yang umum ditemukan dalam makanan, baik yang bermanfaat maupun berbahaya.")

# Path folder gambar
image_folder = "images"

# Daftar mikroba
mikroba_list = [
    {"nama": "Saccharomyces cerevisiae", "deskripsi": "Ragi untuk fermentasi roti dan alkohol.", "file": "saccharomyces_cerevisiae.jpg"},
    {"nama": "Lactobacillus bulgaricus", "deskripsi": "Bakteri penghasil yoghurt.", "file": "lactobacillus_bulgaricus.jpg"},
    {"nama": "Streptococcus thermophilus", "deskripsi": "Bekerja sama dengan Lactobacillus dalam yoghurt.", "file": "streptococcus_thermophilus.jpg"},
    {"nama": "Rhizopus oligosporus", "deskripsi": "Jamur utama dalam pembuatan tempe.", "file": "rhizopus_oligosporus.jpg"},
    {"nama": "Neurospora sitophila", "deskripsi": "Jamur untuk membuat oncom.", "file": "neurospora_sitophila.jpg"},
    {"nama": "Acetobacter xylinum", "deskripsi": "Digunakan untuk membuat nata de coco.", "file": "acetobacter_xylinum.jpg"},
    {"nama": "Aspergillus oryzae", "deskripsi": "Jamur untuk fermentasi kecap dan miso.", "file": "aspergillus_oryzae.jpg"},
    {"nama": "Lactobacillus acidophilus", "deskripsi": "Probiotik yang baik untuk pencernaan.", "file": "lactobacillus_acidophilus.jpg"},
    {"nama": "Bifidobacterium bifidum", "deskripsi": "Probiotik dalam usus manusia.", "file": "bifidobacterium_bifidum.jpg"},
    {"nama": "Penicillium roqueforti", "deskripsi": "Jamur untuk keju biru.", "file": "penicillium_roqueforti.jpg"},
    {"nama": "Penicillium camemberti", "deskripsi": "Jamur untuk keju camembert.", "file": "penicillium_camemberti.jpg"},
    {"nama": "Clostridium botulinum", "deskripsi": "Penyebab botulisme, sangat beracun.", "file": "clostridium_botulinum.jpg"},
    {"nama": "Escherichia coli", "deskripsi": "Bakteri yang bisa menyebabkan diare parah.", "file": "escherichia_coli.jpg"},
    {"nama": "Salmonella enterica", "deskripsi": "Penyebab umum keracunan makanan.", "file": "salmonella_enterica.jpg"},
    {"nama": "Listeria monocytogenes", "deskripsi": "Berbahaya terutama untuk ibu hamil.", "file": "listeria_monocytogenes.jpg"},
    {"nama": "Vibrio cholerae", "deskripsi": "Penyebab kolera.", "file": "vibrio_cholerae.jpg"},
    {"nama": "Campylobacter jejuni", "deskripsi": "Penyebab umum gastroenteritis.", "file": "campylobacter_jejuni.jpg"},
    {"nama": "Bacillus cereus", "deskripsi": "Bisa mencemari makanan dan menyebabkan muntah.", "file": "bacillus_cereus.jpg"},
    {"nama": "Pseudomonas aeruginosa", "deskripsi": "Bisa tumbuh di makanan dan menyebabkan infeksi.", "file": "pseudomonas_aeruginosa.jpg"},
    {"nama": "Staphylococcus aureus", "deskripsi": "Menghasilkan racun yang menyebabkan keracunan.", "file": "staphylococcus_aureus.jpg"},
]

# Menampilkan mikroba satu per satu
for mikroba in mikroba_list:
    st.subheader(mikroba["nama"])
    st.write(mikroba["deskripsi"])

    image_path = os.path.join(image_folder, mikroba["file"])
    
    if os.path.exists(image_path):
        image = Image.open(image_path)
        st.image(image, use_column_width=True)
    else:
        st.warning(f"Gambar tidak ditemukan: {mikroba['file']}")
    
    st.markdown("---")

