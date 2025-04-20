import streamlit as st
import random

st.set_page_config(page_title="Microbiologi Pangan - Encyclopedia", layout="wide")
st.title("🧫 Microbiologi Pangan - Encyclopedia")

mode = st.sidebar.selectbox("Pilih Mode", ["Library", "Petri Panic"])

# Data 30 mikroorganisme
library_data = [
    {"nama": "Salmonella enterica", "familia": "Enterobacteriaceae", "deskripsi": "Batang Gram-negatif, motil, tidak membentuk spora.", "sejarah": "Ditemukan oleh Dr. Daniel E. Salmon, USA, 1885.", "makanan_terkait": "Daging ayam mentah, telur mentah.", "alasan_makanan": "Sering mencemari daging unggas dan telur melalui pencernaan hewan.", "penanganan": "Antibiotik dan hidrasi intensif.", "pencegahan": "Masak daging dan telur sampai matang sempurna."},
    {"nama": "Escherichia coli O157:H7", "familia": "Enterobacteriaceae", "deskripsi": "Batang Gram-negatif, motil.", "sejarah": "Diidentifikasi sebagai patogen makanan tahun 1982, USA.", "makanan_terkait": "Daging sapi mentah, sayuran mentah.", "alasan_makanan": "Kontaminasi feses saat penyembelihan.", "penanganan": "Perawatan suportif, hindari antibiotik pada kasus parah.", "pencegahan": "Masak daging dengan suhu aman, cuci sayuran."},
    {
        "nama": "Campylobacter jejuni",
        "familia": "Campylobacteraceae",
        "deskripsi": "Spiral atau kurva, Gram-negatif, mikroaerofilik.",
        "sejarah": "Diidentifikasi pada 1972 sebagai patogen makanan.",
        "makanan_terkait": "Daging unggas mentah, susu tidak dipasteurisasi.",
        "alasan_makanan": "Biasa terdapat pada usus unggas dan mentransfer ke daging.",
        "penanganan": "Rehidrasi, kadang antibiotik seperti azitromisin.",
        "pencegahan": "Masak ayam sampai matang dan cuci peralatan masak."
    },
    {
        "nama": "Staphylococcus aureus",
        "familia": "Staphylococcaceae",
        "deskripsi": "Kokus Gram-positif, non-motil, membentuk racun enterotoksin.",
        "sejarah": "Dikenal sebagai penyebab keracunan makanan sejak awal abad ke-20.",
        "makanan_terkait": "Krim, daging olahan, salad kentang.",
        "alasan_makanan": "Racun diproduksi saat pertumbuhan bakteri pada makanan.",
        "penanganan": "Istirahat dan hidrasi; racun resisten panas.",
        "pencegahan": "Simpan makanan pada suhu aman dan hindari kontaminasi."
    },
    {
        "nama": "Bacillus cereus",
        "familia": "Bacillaceae",
        "deskripsi": "Bentuk batang, Gram-positif, aerob dan menghasilkan spora.",
        "sejarah": "Dikenal menyebabkan keracunan makanan sejak 1950-an.",
        "makanan_terkait": "Nasi, pasta, kentang.",
        "alasan_makanan": "Spora tahan panas tumbuh saat penyimpanan makanan buruk.",
        "penanganan": "Gejala ringan, sering sembuh sendiri.",
        "pencegahan": "Simpan makanan panas atau dingin, jangan di suhu ruang."
    },
    {
        "nama": "Clostridium botulinum",
        "familia": "Clostridiaceae",
        "deskripsi": "Batang Gram-positif, anaerob, membentuk spora dan neurotoksin.",
        "sejarah": "Ditemukan pada akhir abad ke-19 oleh Emile van Ermengem.",
        "makanan_terkait": "Makanan kaleng rumah, daging fermentasi.",
        "alasan_makanan": "Kondisi anaerob dalam makanan kaleng mendukung pertumbuhan.",
        "penanganan": "Antitoksin dan rawat inap darurat.",
        "pencegahan": "Sterilisasi makanan kaleng dengan benar."
    },
    {
        "nama": "Shigella spp.",
        "familia": "Enterobacteriaceae",
        "deskripsi": "Batang kecil, Gram-negatif, tidak motil.",
        "sejarah": "Ditemukan oleh Kiyoshi Shiga tahun 1897.",
        "makanan_terkait": "Sayur mentah, makanan yang terkontaminasi tangan.",
        "alasan_makanan": "Menyebar lewat rute fecal-oral, sangat menular.",
        "penanganan": "Hidrasi dan antibiotik bila parah.",
        "pencegahan": "Cuci tangan, kebersihan saat pengolahan makanan."
    },
    {
        "nama": "Vibrio cholerae",
        "familia": "Vibrionaceae",
        "deskripsi": "Bentuk koma, Gram-negatif, motil dengan flagela tunggal.",
        "sejarah": "Ditemukan oleh Filippo Pacini pada 1854.",
        "makanan_terkait": "Air minum dan makanan laut mentah.",
        "alasan_makanan": "Makanan laut dapat tercemar air terkontaminasi.",
        "penanganan": "Oralit dan antibiotik dalam kasus berat.",
        "pencegahan": "Sterilisasi air dan masak makanan laut matang."
    },
    {
        "nama": "Clostridium perfringens",
        "familia": "Clostridiaceae",
        "deskripsi": "Gram-positif, batang pendek, anaerob, membentuk spora.",
        "sejarah": "Ditemukan tahun 1892 oleh William Welch.",
        "makanan_terkait": "Daging, kuah daging, makanan besar.",
        "alasan_makanan": "Tumbuh saat makanan besar disimpan tidak benar.",
        "penanganan": "Gejala ringan, istirahat dan cairan cukup.",
        "pencegahan": "Hindari penyimpanan makanan dalam suhu bahaya."
    },
    {
        "nama": "Norovirus",
        "familia": "Caliciviridae",
        "deskripsi": "Virus RNA kecil, tidak beramplop, sangat menular.",
        "sejarah": "Wabah pertama kali tercatat di Norwalk, Ohio, tahun 1972.",
        "makanan_terkait": "Kerang mentah, makanan olahan oleh tangan terinfeksi.",
        "alasan_makanan": "Menyebar lewat feses dan muntah pasien.",
        "penanganan": "Rehidrasi, biasanya sembuh sendiri.",
        "pencegahan": "Cuci tangan dan sanitasi permukaan."
    },
    {
        "nama": "Rotavirus",
        "familia": "Reoviridae",
        "deskripsi": "Virus RNA ganda, bentuk seperti roda.",
        "sejarah": "Ditemukan tahun 1973 oleh Ruth Bishop.",
        "makanan_terkait": "Makanan/minuman terkontaminasi feses.",
        "alasan_makanan": "Menular lewat rute fecal-oral, sering terjadi pada anak-anak.",
        "penanganan": "Oralit, kadang rawat inap untuk bayi.",
        "pencegahan": "Vaksinasi dan sanitasi."
    },
    {
        "nama": "Hepatitis A Virus",
        "familia": "Picornaviridae",
        "deskripsi": "Virus RNA kecil, tidak beramplop.",
        "sejarah": "Diketahui sebagai penyebab hepatitis pada 1970-an.",
        "makanan_terkait": "Kerang mentah, makanan tercemar air limbah.",
        "alasan_makanan": "Menyebar lewat feses ke makanan.",
        "penanganan": "Istirahat dan pengawasan hati.",
        "pencegahan": "Vaksinasi dan hindari makanan mentah."
    },
    {
        "nama": "Yersinia enterocolitica",
        "familia": "Enterobacteriaceae",
        "deskripsi": "Batang pendek Gram-negatif, motil pada suhu rendah.",
        "sejarah": "Ditemukan pada tahun 1939 oleh A. Schleifstein.",
        "makanan_terkait": "Daging babi, susu mentah.",
        "alasan_makanan": "Tumbuh baik di suhu kulkas, umum di hewan ternak.",
        "penanganan": "Biasanya sembuh sendiri, kadang antibiotik.",
        "pencegahan": "Masak makanan dengan suhu tepat dan pasteurisasi susu."
    },
    {
        "nama": "Enterobacter sakazakii (Cronobacter)",
        "familia": "Enterobacteriaceae",
        "deskripsi": "Batang Gram-negatif, fakultatif anaerob.",
        "sejarah": "Diidentifikasi sebagai patogen neonatus pada 1980-an.",
        "makanan_terkait": "Susu formula bubuk bayi.",
        "alasan_makanan": "Dapat mencemari bubuk saat produksi atau penyimpanan.",
        "penanganan": "Antibiotik dan dukungan intensif untuk bayi.",
        "pencegahan": "Gunakan air panas untuk membuat susu formula."
    },
    {
        "nama": "Aspergillus flavus",
        "familia": "Trichocomaceae",
        "deskripsi": "Jamur penghasil aflatoksin, koloni kekuningan.",
        "sejarah": "Dikenal sejak 1800-an sebagai kontaminan pangan.",
        "makanan_terkait": "Kacang tanah, jagung.",
        "alasan_makanan": "Tumbuh di bahan yang disimpan lembap.",
        "penanganan": "Buang makanan terkontaminasi.",
        "pencegahan": "Simpan kering, hindari kerusakan saat panen."
    },
    {
        "nama": "Penicillium expansum",
        "familia": "Trichocomaceae",
        "deskripsi": "Jamur penghasil patulin, koloni biru kehijauan.",
        "sejarah": "Dikenal sebagai jamur pembusuk apel.",
        "makanan_terkait": "Buah apel dan buah lunak lainnya.",
        "alasan_makanan": "Masuk lewat luka di permukaan buah.",
        "penanganan": "Buang buah busuk, jangan konsumsi.",
        "pencegahan": "Simpan buah dingin dan utuh."
    },
    {
        "nama": "Fusarium spp.",
        "familia": "Nectriaceae",
        "deskripsi": "Jamur penghasil mikotoksin, koloni putih hingga merah muda.",
        "sejarah": "Dikenal sejak abad ke-19 di gandum.",
        "makanan_terkait": "Sereal, jagung, gandum.",
        "alasan_makanan": "Infeksi tanaman saat panen dan penyimpanan buruk.",
        "penanganan": "Hindari konsumsi, monitoring regulasi mikotoksin.",
        "pencegahan": "Simpan kering, rotasi tanaman."
    },
    {
        "nama": "Alternaria alternata",
        "familia": "Pleosporaceae",
        "deskripsi": "Jamur hitam pekat dengan spora besar.",
        "sejarah": "Dikenal sebagai jamur pembusuk buah dan sayur.",
        "makanan_terkait": "Tomat, kentang, biji-bijian.",
        "alasan_makanan": "Tumbuh saat penyimpanan lembap dan luka buah.",
        "penanganan": "Buang bahan makanan terkontaminasi.",
        "pencegahan": "Kontrol kelembapan penyimpanan."
    },
    {
        "nama": "Saccharomyces cerevisiae",
        "familia": "Saccharomycetaceae",
        "deskripsi": "Ragi berbentuk bulat, kuning krem.",
        "sejarah": "Digunakan sejak ribuan tahun lalu dalam fermentasi.",
        "makanan_terkait": "Roti, bir, anggur.",
        "alasan_makanan": "Digunakan sebagai mikroba fermentasi.",
        "penanganan": "Umumnya tidak berbahaya, kecuali infeksi oportunistik.",
        "pencegahan": "Pengawasan higienis di industri fermentasi."
    },
    {
        "nama": "Candida albicans",
        "familia": "Saccharomycetaceae",
        "deskripsi": "Ragi oval, sering ditemukan di tubuh manusia.",
        "sejarah": "Dikenal sebagai penyebab kandidiasis sejak awal abad ke-20.",
        "makanan_terkait": "Jarang pada makanan, lebih umum pada infeksi manusia.",
        "alasan_makanan": "Kontaminasi silang dari manusia ke makanan.",
        "penanganan": "Antijamur sistemik.",
        "pencegahan": "Sanitasi pekerja makanan."
    },
    {
        "nama": "Rhizopus stolonifer",
        "familia": "Mucoraceae",
        "deskripsi": "Jamur roti hitam dengan spora gelap.",
        "sejarah": "Dikenal sejak lama sebagai jamur pembusuk.",
        "makanan_terkait": "Roti, buah-buahan lunak.",
        "alasan_makanan": "Tumbuh cepat pada makanan kaya karbohidrat.",
        "penanganan": "Buang makanan terkontaminasi.",
        "pencegahan": "Simpan dalam tempat kering dan dingin."
    },
    {
        "nama": "Pseudomonas fluorescens",
        "familia": "Pseudomonadaceae",
        "deskripsi": "Batang Gram-negatif, motil, fluoresens biru-hijau.",
        "sejarah": "Dikenal sebagai pembusuk produk susu.",
        "makanan_terkait": "Susu, daging, ikan.",
        "alasan_makanan": "Tumbuh pada suhu dingin, menyebabkan bau tak sedap.",
        "penanganan": "Buang produk terkontaminasi.",
        "pencegahan": "Simpan suhu dingin dan proses cepat."
    },
    {
        "nama": "Aeromonas hydrophila",
        "familia": "Aeromonadaceae",
        "deskripsi": "Batang Gram-negatif, motil, sering ditemukan di air tawar.",
        "sejarah": "Dikenal sebagai patogen air sejak pertengahan abad ke-20.",
        "makanan_terkait": "Ikan, makanan laut mentah.",
        "alasan_makanan": "Dapat mencemari air tempat hidup ikan.",
        "penanganan": "Antibiotik dan perawatan medis.",
        "pencegahan": "Masak makanan laut matang sempurna."
    },
    {
        "nama": "Mycobacterium avium",
        "familia": "Mycobacteriaceae",
        "deskripsi": "Batang tahan asam, tumbuh lambat.",
        "sejarah": "Ditemukan sebagai patogen air dan makanan sejak 1980-an.",
        "makanan_terkait": "Air minum, produk susu.",
        "alasan_makanan": "Tumbuh di biofilm sistem air.",
        "penanganan": "Antibiotik kombinasi jangka panjang.",
        "pencegahan": "Perawatan sistem air dan pasteurisasi."
    },
    {
        "nama": "Helicobacter pylori",
        "familia": "Helicobacteraceae",
        "deskripsi": "Spiral, Gram-negatif, tumbuh di lambung manusia.",
        "sejarah": "Ditemukan oleh Barry Marshall dan Robin Warren, 1982.",
        "makanan_terkait": "Air dan makanan terkontaminasi.",
        "alasan_makanan": "Menyebar lewat makanan atau air tidak bersih.",
        "penanganan": "Antibiotik dan penghambat asam lambung.",
        "pencegahan": "Kebersihan makanan dan sanitasi air."
    },
    {
        "nama": "Micrococcus luteus",
        "familia": "Micrococcaceae",
        "deskripsi": "Kokus Gram-positif, koloni kuning terang.",
        "sejarah": "Dikenal sebagai flora normal kulit, kontaminan makanan potensial.",
        "makanan_terkait": "Produk susu, daging.",
        "alasan_makanan": "Kontaminasi selama pemrosesan.",
        "penanganan": "Jarang patogenik, hanya untuk imunokompromais.",
        "pencegahan": "Higiene dalam proses makanan."
    },
    {
        "nama": "Geotrichum candidum",
        "familia": "Dipodascaceae",
        "deskripsi": "Jamur putih, membentuk miselium halus.",
        "sejarah": "Digunakan dalam pembuatan keju dan dikenal sebagai pembusuk.",
        "makanan_terkait": "Keju, susu, buah.",
        "alasan_makanan": "Tumbuh pada produk susu dan buah yang lembap.",
        "penanganan": "Buang makanan terkontaminasi.",
        "pencegahan": "Simpan dalam suhu dingin dan kering."
    },
    {
        "nama": "Acinetobacter baumannii",
        "familia": "Moraxellaceae",
        "deskripsi": "Coccobacilli Gram-negatif, non-motil.",
        "sejarah": "Muncul sebagai patogen rumah sakit, juga kontaminan makanan.",
        "makanan_terkait": "Sayur mentah, daging.",
        "alasan_makanan": "Tahan desinfektan, mencemari lingkungan dapur.",
        "penanganan": "Antibiotik tergantung resistensi.",
        "pencegahan": "Sanitasi dan pengolahan makanan higienis."
    },
    {
        "nama": "Serratia marcescens",
        "familia": "Enterobacteriaceae",
        "deskripsi": "Batang Gram-negatif, koloni merah muda.",
        "sejarah": "Pertama kali dikenal karena pigmentasi unik pada abad ke-19.",
        "makanan_terkait": "Produk susu, roti, makanan tinggi pati.",
        "alasan_makanan": "Pigmentasi tumbuh pada makanan lembap dan manis.",
        "penanganan": "Antibiotik jika menyebabkan infeksi.",
        "pencegahan": "Simpan makanan kering dan tertutup."
    }
]

# --- MODE LIBRARY --- #
if mode == "Library":
    st.header("📚 Library")
    mikroba_pilihan = st.selectbox("Pilih Mikroorganisme", [m["nama"] for m in library_data])

    mikroba = next((m for m in library_data if m["nama"] == mikroba_pilihan), None)
    if mikroba:
        st.subheader(mikroba["nama"])
        st.markdown(f"**Familia:** {mikroba['familia']}")
        st.markdown(f"**Deskripsi Bentuk dan Warna:** {mikroba['deskripsi']}")
        st.markdown(f"**Sejarah Penemuan:** {mikroba['sejarah']}")
        st.markdown(f"**Terdapat pada Makanan:** {mikroba['makanan_terkait']}")
        st.markdown(f"**Alasan Ditemukan di Makanan Tersebut:** {mikroba['alasan_makanan']}")
        st.markdown(f"**Penanganan Jika Terpapar:** {mikroba['penanganan']}")
        st.markdown(f"**Cara Pencegahan:** {mikroba['pencegahan']}")

# --- MODE PETRI PANIC --- #
elif mode == "Petri Panic":
    st.header("🎮 Petri Panic")

    questions = [
        {
            "question": "Apa nama ilmiah dari bakteri yang sering ditemukan dalam daging ayam mentah dan menyebabkan diare parah?",
            "options": ["Salmonella enterica", "Lactobacillus acidophilus", "Penicillium roqueforti", "Escherichia coli", "Clostridium botulinum"],
            "answer": "Salmonella enterica",
            "explanation": "Salmonella enterica adalah bakteri penyebab umum diare dari daging ayam yang tidak matang."
        },
        {
            "question": "Mikroorganisme penghasil aflatoksin yang tumbuh pada kacang tanah adalah...",
            "options": ["Aspergillus flavus", "Candida albicans", "Rhizopus stolonifer", "Listeria monocytogenes", "Fusarium oxysporum"],
            "answer": "Aspergillus flavus",
            "explanation": "Aspergillus flavus menghasilkan aflatoksin yang bersifat karsinogenik dan sering ditemukan pada kacang-kacangan."
        },
        {
            "question": "Apa genus dari mikroba berbentuk spiral yang hidup di lambung dan menyebabkan gastritis?",
            "options": ["Helicobacter", "Staphylococcus", "Bacillus", "Micrococcus", "Pseudomonas"],
            "answer": "Helicobacter",
            "explanation": "Helicobacter pylori adalah bakteri spiral yang hidup di lambung manusia."
        },
        {
            "question": "Mikroorganisme apakah yang umum digunakan dalam pembuatan roti dan bir?",
            "options": ["Saccharomyces cerevisiae", "Escherichia coli", "Geotrichum candidum", "Mycobacterium avium", "Serratia marcescens"],
            "answer": "Saccharomyces cerevisiae",
            "explanation": "Saccharomyces cerevisiae adalah ragi yang digunakan untuk fermentasi dalam pembuatan roti dan bir."
        },
        {
            "question": "Jenis bakteri Gram-positif yang dapat menyebabkan botulisme makanan adalah...",
            "options": ["Clostridium botulinum", "Bacillus subtilis", "Listeria monocytogenes", "Staphylococcus epidermidis", "Yersinia enterocolitica"],
            "answer": "Clostridium botulinum",
            "explanation": "Clostridium botulinum menghasilkan toksin botulinum yang sangat beracun dan dapat menyebabkan botulisme."
        },
        {
            "question": "Penicillium expansum menghasilkan toksin berbahaya yang disebut...",
            "options": ["Patulin", "Aflatoksin", "Histamin", "Botulinum", "Ochratoksin"],
            "answer": "Patulin",
            "explanation": "Patulin adalah mikotoksin yang dihasilkan oleh Penicillium expansum, terutama pada apel busuk."
        },
        {
            "question": "Bakteri mana yang merupakan flora normal kulit namun bisa menjadi patogen oportunistik dalam makanan?",
            "options": ["Staphylococcus aureus", "Candida albicans", "Clostridium perfringens", "Geotrichum candidum", "Enterobacter sakazakii"],
            "answer": "Staphylococcus aureus",
            "explanation": "Staphylococcus aureus adalah flora normal kulit yang bisa menghasilkan enterotoksin jika mencemari makanan."
        },
        {
            "question": "Apa nama jamur yang menyebabkan roti menjadi berjamur hitam?",
            "options": ["Rhizopus stolonifer", "Aspergillus flavus", "Penicillium roqueforti", "Fusarium graminearum", "Mucor racemosus"],
            "answer": "Rhizopus stolonifer",
            "explanation": "Rhizopus stolonifer dikenal sebagai jamur roti hitam karena spora hitamnya."
        },
        {
            "question": "Bakteri yang menyebabkan listeriosis, terutama berbahaya bagi ibu hamil adalah...",
            "options": ["Listeria monocytogenes", "Salmonella typhi", "E. coli O157:H7", "Clostridium tetani", "Campylobacter jejuni"],
            "answer": "Listeria monocytogenes",
            "explanation": "Listeria monocytogenes bisa tumbuh di suhu rendah dan menyebabkan listeriosis yang berisiko bagi ibu hamil."
        },
        {
            "question": "Jamur penghasil mikotoksin pada gandum yang menyebabkan penyakit pada manusia adalah...",
            "options": ["Fusarium spp.", "Aspergillus niger", "Candida glabrata", "Saccharomyces cerevisiae", "Micrococcus luteus"],
            "answer": "Fusarium spp.",
            "explanation": "Fusarium menghasilkan mikotoksin seperti DON (vomitoksin) yang mencemari gandum dan biji-bijian."
        }
    ]

    score = 0
    for i, q in enumerate(questions, 1):
        st.markdown(f"**{i}. {q['question']}**")
        selected = st.radio(f"Jawaban Anda untuk nomor {i}:", q["options"], key=f"q{i}", index=None)
        if selected:
            if selected == q["answer"]:
                st.success("✅ Jawaban benar!")
                score += 1
            else:
                st.error(f"❌ Jawaban salah. Jawaban yang benar adalah **{q['answer']}**.")
                st.info(q["explanation"])

    st.markdown("---")
    st.markdown(f"### Skor akhir Anda: **{score} / {len(questions)}**")
