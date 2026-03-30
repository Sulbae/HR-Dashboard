# Proyek Pertama: Menyelesaikan Permasalahan Human Resources

## Business Understanding

Jaya Jaya Maju merupakan salah satu perusahaan multinasional yang telah berdiri sejak tahun 2000. Perusahaan telah memiliki lebih dari 1000 karyawan yang tersebar di seluruh penjuru negeri. Walaupun telah menjadi menjadi perusahaan yang cukup besar, Jaya Jaya Maju masih cukup kesulitan dalam mengelola karyawan. Hal ini berimbas tingginya attrition rate (rasio jumlah karyawan yang keluar dengan total karyawan keseluruhan) hingga lebih dari 10%. Untuk mencegah hal ini semakin parah, manajer departemen HR ingin meminta bantuan untuk mengidentifikasi berbagai faktor yang mempengaruhi tingginya attrition rate tersebut. Selain itu, ia juga perlu business dashboard untuk membantunya memonitori berbagai faktor tersebut.

### Permasalahan Bisnis

Berdasarkan permasalahan bisnis yang telah dijelaskan, maka fokus utama pada proyek ini adalah membuat dashboard sebagai platform monitoring metrik-metrik penting untuk kebutuhan analisis faktor-faktor yang memiliki pengaruh signifikan terhadap attrition rate. Perusahaan perlu menyusun strategi yang tepat untuk dapat menjaga produktivitas tetap stabil dan meningkatkan efisiensi kinerja para karyawannya. 

Berikut pertanyaan bisnis yang diharapkan dapat terjawab melalui proyek ini.
* Bagaimana pengaruh Salary terhadap tingkat Attrition?
* Bagaimana pengaruh Pengalaman Kerja terhadap tingkat Attrition?
* Bagaimana pengaruh Kepuasan/Kenyamanan Kerja terhadap tingkat Attrition?
* Apa saja 10 faktor yang paling berpengaruh signifikan terhadap tingginya attration rate?
* Bagaimana strategi yang harus dijalankan oleh tim HR dalam mengelola karyawannya agar bisa menahan Attration Rate tetap rendah?

### Cakupan Proyek

1) Pengolahan dan Persiapan Data
2) Eksplorasi dan Analisis Data
3) Pembuatan Dashboard
4) Rekomendasi

### Persiapan

Sumber data: [Jaya Jaya Maju Dataset](https://raw.githubusercontent.com/Sulbae/HR-Dashboard/refs/heads/main/employee_data.csv)

Setup environment:

1. Buat lingkungan virtual
    * 
    ```
    python -m venv env
    ```
2. Aktifkan lingkungan virtual
    * 
    ```

    ```
3. Install dependensi
    * menggunakan `requirements.txt`
    ```
    pip install -r requirements.txt
    ```

Pengolahan dan Persiapan Data


Eksplorasi dan Analisis Data


## Business Dashboard

Dashboard berisi informasi mengenai ringkasan metrik-metrik penting dan visualisasi data yang diperlukan dalam kegiatan monitoring terhadap berbagai aspek yang berkaitan dengan kondisi pengelolaan sumber daya manusia (talent) perusahaan seperti berikut:
1) Total Karyawan
    - Deskripsi: Jumlah seluruh karyawan yang terdata.
    - Kegunaan: Memberikan informasi mengenai besaran jumlah karyawan yang sedang/telah dikelola perusahaan.
2) Total Attrition
    - Deskripsi: Jumlah karyawan yang telah berhenti/diberhentikan dan tercatat pada database.
    - Kegunaan: Menjadi indikator tinggi-rendahnya tingkat pergantian karyawan (Attrition Rate).
3) Rata-rata Usia (Avg. Age)
    - Deskripsi: Usia rata-rata karyawan secara keseluruhan.
    - Kegunaan: Usia rata-rata dapat menjadi indikator dalam analisis demografi personel tim khususnya dalam monitoring komposisi tim hingga perencanaan promosi dan/atau suksesi.
4) Enviro Satisfaction Rate
    - Deskripsi: Tingkat kepuasan rata-rata karyawan terhadap kondisi lingkungan/budaya kerja perusahaan (Environment Satisfaction).
    - Kegunaan: Menjadi indikator awal dalam mengetahui tingkat kenyamanan perusahaan secara umum bagi seluruh karyawan.
5) Job Satisfaction Rate
    - Deskripsi: Tingkat kepuasan rata-rata karyawan terhadap pekerjaan yang diemban oleh mereka. 
    - Kegunaan: Menjadi indikator awal dalam mengetahui tingkat kesesuaian ekspektasi kerja karyawan dengan beban kerja nyata di kantor/lapangan. Informasi ini akan berguna sebagai early-warning dalam mendeteksi gejala burnout karyawan maupun pengelolaan organisasi yang tidak efisien.
6) Perfomance Rate
    - Deskripsi: Tingkat performa/kinerja rata-rata karyawan secara keseluruhan.
    - Kegunaan: Mengukur kinerja rata-rata karyawan dan sebagai tolak ukur awal yang menggambarkan tingkat produktivitas dari tenaga kerja perusahaan.
7) Rata-rata Pelatihan Yang Diikuti (Avg. Training (Last Year))
    - Deskripsi: Jumlah pelatihan rata-rata yang telah diikuti karyawan selama satu tahun terakhir.
    - Kegunaan: Menjadi indikator pembanding bagi metrik Performance Rate dalam mengukur tingkat produktivitas perusahaan. Jumlah pelatihan dapat menjadi nilai representatif dari besaran investasi yang telah perusahaan lakukan untuk memelihara kualitas talentanya, yakni melalui pemberian fasilitas kegiatan pelatihan bagi para karyawan.
8) Monthly Rate Chart
    - Deskripsi:
    - Kegunaan:
9) Percent Salary Hike Chart
    - Deskripsi:
    - Kegunaan:
10) Monthly Income Chart
    - Deskripsi:
    - Kegunaan:
11) Years at Company Chart
    - Deskripsi:
    - Kegunaan:
12) Total Working Years Chart
    - Deskripsi:
    - Kegunaan:
13) Num Companies Worked Chart
    - Deskripsi:
    - Kegunaan:
14) Job Ivolvement Chart
    - Deskripsi:
    - Kegunaan:
15) Enviro Satisfaction Chart
    - Deskripsi:
    - Kegunaan:
16) Job Satisfaction Chart
    - Deskripsi:
    - Kegunaan:

## Conclusion
Sesuai dengan hasil dari proyek ini, maka dapat disimpulkan bahwa:
1. Pengaruh Salary terhadap tingkat Attrition

2. Pengaruh Pengalaman Kerja terhadap tingkat Attrition

3. Pengaruh Kepuasan/Kenyamanan Kerja terhadap tingkat Attrition

4. Top 10 faktor yang berpengaruh signifikan terhadap Attration Rate


### Rekomendasi Action Items (Optional)

Untuk menekan agar angka Attration Rate tetap rendah, perusahaan harus mampu mengelola tingkat kepuasan dan kenyamanan kerja karyawan dengan berbagai cara, diantaranya:

    1. Memberikan insentif tambahan bagi karyawan dengan performa yang memadai atau melampaui target.
    2. Menawarkan peluang pengembangan karir yang jelas melalui kegiatan pelatihan yang terstruktur sesuai Job Role karyawan.
    3. Memberikan besaran gaji yang layak dan kompetitif sesuai dengan tanggung jawab kerja (Job Level) yang diberikan.
    4. Menyediakan layanan konsultasi kerja bagi para karyawan dengan gaya komunikasi yang bersifat kekeluargaan.
    5. Mendorong kolaborasi dan pengembangan tim melalui program mentorship.