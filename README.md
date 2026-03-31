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

    ```
    conda create --name penerapan-data-science python=3.10 -y
    ```
2. Aktifkan lingkungan virtual

    ```
    conda activate penerapan-data-science
    ```
3. Install dependensi

    ```
    conda install -r requirements.txt
    ```

Pengolahan dan Persiapan Data
``` 
Data Exploration
|---Karakteristik Data
|---Kelengkapan Data
|---Distribusi Data
Data Cleaning
|---Missing Value Handling
```
Eksplorasi dan Analisis Data
```
Analisis Korelasi Antar Variabel Data 
|---Observasi pengaruh Salary & Income terhadap Attrition Rate
|---Observasi pengaruh Pengalaman Kerja terhadap Attrition Rate
|---Observasi pengaruh Kepuasan/Kenyamanan Kerja terhadap Attrition Rate
```

## Business Dashboard

[Lihat Dashboard](https://lookerstudio.google.com/reporting/9b9a270a-81f3-4665-b0a8-41c93a1c8350)

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
    - Deskripsi: Menampilkan jumlah Attrition berdasarkan Monthly Rate yang telah dikelompokkan ke dalam level tertentu.
    - Kegunaan: Memberikan informasi mengenai distribusi Attrition karyawan yang tersebar dalam berbagai level gaji bulanan. Data ini digunakan untuk memahami pengaruh besaran gaji yang diterima terhadap tingkat Attrition karyawan.  
9) Percent Salary Hike Chart
    - Deskripsi: Menampilkan jumlah Attrition berdasarkan besaran Percent Salary Hike dalam satu tahun terakhir.
    - Kegunaan: Memberikan informasi besaran persentase kenaikan gaji bulanan dibandingkan dengan gaji sebelumnya. Data ini digunakan untuk memahami pengaruh besaran persentase kenaikan gaji terhadap tingkat Attrition karyawan.
10) Monthly Income Chart
    - Deskripsi: Menampilkan jumlah Attrition berdasarkan Monthly Income yang telah dikelompokkan ke dalam level tertentu.
    - Kegunaan: Memberikan informasi mengenai distribusi Attrition karyawan yang tersebar dalam berbagai level pendapatan total (gaji + pendapatan lain-lain) bulanan. Data ini digunakan untuk memahami pengaruh besaran pendapatan total bulanan yang mampu diperoleh terhadap tingkat Attrition karyawan.
11) Years at Company Chart
    - Deskripsi: Menampilkan jumlah Attrition berdasarkan Years at Company (Lama tahun telah bekerja di perusahaan Jaya Jaya Maju).
    - Kegunaan: Memberikan informasi mengenai distribusi Attrition karyawan yang tersebar sesuai dengan periode kerja di perusahaan. Data ini digunakan untuk memahami periode rata-rata kerja karyawan di perusahaan hingga akhirnya digantikan/berhenti.
12) Total Working Years Chart
    - Deskripsi: Menampilkan jumlah Attrition berdasarkan Total Working Years (total lama tahun pengalaman bekerja/profesional karir).
    - Kegunaan: Memberikan informasi mengenai distribusi Attrition karyawan yang tersebar sesuai dengan lama pengalaman karir/profesional. Data ini digunakan untuk memahami pengaruh total lama pengalaman kerja karyawan terhadap tingkat Attrition.
13) Num Companies Worked Chart
    - Deskripsi: Menampilkan jumlah Attrition berdasarkan Num Companies Worked (jumlah perusahaan yang sudah pernah disinggahi).
    - Kegunaan: Memberikan informasi mengenai distribusi Attrition karyawan yang tersebar sesuai dengan pengalaman karir/profesional yang ditunjukkan melalui seberapa banyak pengalaman kerja yang telah diperoleh sebelum akhirnya diterima di perusahaan Jaya Jaya Maju. Data ini digunakan untuk memahami pengaruh riwayat pengalaman kerja karyawan terhadap tingkat Attrition.
14) Job Ivolvement Chart
    - Deskripsi: Menampilkan jumlah Attrition berdasarkan Job Involvement (kesadaran akan perasaan atau jati diri dalam pekerjaan yang digeluti).
    - Kegunaan: Memberikan informasi mengenai distribusi Attrition karyawan yang tersebar sesuai dengan tingkat passion yang dirasakan karyawan terhadap tugas-tugas yang mereka emban sesuai role/peran masing-masing. Data ini digunakan untuk memahami pengaruh motivasi kerja karyawan terhadap tingkat Attrition.
15) Enviro Satisfaction Chart
    - Deskripsi: Menampilkan jumlah Attrition berdasarkan Environment Satisfaction (kepuasan karyawan terhadap lingkungan/budaya kerja perusahaan).
    - Kegunaan: Memberikan informasi mengenai distribusi Attrition karyawan yang tersebar sesuai dengan tingkat kepuasan karyawan yang dirasakan karyawan terhadap lingkungan kerja mereka. Data ini digunakan untuk memahami pengaruh kenyamanan kerja karyawan terhadap tingkat Attrition.
16) Job Satisfaction Chart
    - Deskripsi: Menampilkan jumlah Attrition berdasarkan Job Satisfaction (kepuasan karyawan akan tugas-tugas yang diberikan).
    - Kegunaan: Memberikan informasi mengenai distribusi Attrition karyawan yang tersebar sesuai dengan tingkat kepuasan yang dirasakan karyawan terhadap beban tugas-tugas yang diamanahkan kepada mereka. Data ini digunakan untuk memahami pengaruh kesesuaian ekspektasi kerja karyawan dengan fakta beban kerja nyata terhadap tingkat Attrition.

## Conclusion
Sesuai dengan hasil dari proyek ini, maka dapat disimpulkan bahwa:
1. Kompensasi Finansial merupakan Faktor Pendorong Utama Attrition
    * Karyawan dengan rasio kompensasi terhadap biaya hidup yang tidak seimbang (terutama yang menempuh jarak jauh dengan gaji yang relatif pas-pasan) memiliki kecenderungan lebih tinggi untuk resign. Dengan demikian, daya saing kompensasi dan pertimbangan biaya transportasi merupakan elemen kritis dalam keputusan retensi karyawan.
2. Masa Kerja dan Stabilitas Karir memiliki pengaruh yang signifikan terhadap Attrition Rate
    * Analisis terhadap NumCompaniesWorked, TotalWorkingYears, dan YearsAtCompany menunjukkan bahwa:
        - Karyawan dengan masa kerja kurang dari atau sama dengan 1 tahun merupakan segmen paling rentan terhadap Attrition (early-stage churn).
        - Karyawan dengan pengalaman kerja < 10 tahun dan riwayat perpindahan perusahaan yang cukup sering menunjukkan pola mobilitas karir yang cukup tinggi.
        - Sebaliknya, karyawan senior (masa kerja > 10 tahun atau dengan level jabatan yang tinggi) menunjukkan tingkat retensi yang lebih stabil.
3. Faktor Psikologis dan Lingkungan Kerja sebagai Pendorong Sekunder
    * Dapat dikatakan passion (JobInvolvement), lingkungan kerja (EnvironmentSatisfaction), dan kenyamanan dalam pekerjaan mereka (JobSatisfaction) memiliki korelasi moderat, tetapi konsisten terhadap attrition. Meskipun pengaruhnya tidak sekuat faktor-faktor lain. Aspek ini dapat menjadi faktor penguat yang akan mempercepat atau memperlambat keputusan resign, terutama ketika dikombinasikan dengan faktor ketidakpuasan terhadap kompensasi/benefit finansial.
4. Top 10 faktor yang berpengaruh signifikan terhadap Attration Rate
    * Berdasarkan hubungan pengaruh antar variabel yang telah dikalkulasi menggunakan metode perhitungan korelasi matrix. Aspek-aspek seperti DistanceFromHome, NumCompaniesWorked, MonthlyRate, PerformanceRating, dan PercentSalaryHike memiliki korelasi positif yang paling signifikan terhadap Attrition Karyawan dibandingkan dengan aspek-aspek lainnya. 
    * Menarik sekali bahwa PerfomanceRating memiliki korelasi positif terhadap Attrition. Beberapa alasan yang mungkin menjadi faktor penyebabnya antara lain:
        - Talent dengan performa tinggi seringkali memiliki nilai pasar (value) yang lebih kompetitif sehingga lebih mudah mendapat tawaran dari perusahaan lain.
        - Talent dengan performa tinggi memiliki ekspektasi promosi lebih cepat atau kenaikan gaji/kompensasi yang lebih tinggi. Jika ekspektasi tersebut tidak tercapai, maka dapat menjadi motivasi yang cukup kuat untuk pindah.
    * Sementara itu, aspek MonthlyIncome, StockOptionLevel, JobLevel, Age, TotalWorkingYears memiliki korelasi negatif yang paling signifikan terhadap Attrition Karyawan dibandingkan dengan aspek-aspek lainnya. Aspek Total Working Years dan Age biasanya saling berkaitan karena pada umumnya karyawan-karyawan yang sudah sangat senior memiliki peluang yang lebih rendah untuk berhenti/diberhentikan dari pekerjaannya karena berbagai alasan, misalnya sudah memiliki tanggungjawab yang besar atau sudah merasa nyaman dalam pekerjaannya. Hal ini sejalan dengan korelasi negatif yang ditunjukkan oleh aspek JobLevel, yang mana menandakan bahwa karyawan dengan level posisi yang lebih junior/rendah memiliki potensi Attrition yang lebih tinggi. 


### Rekomendasi Action Items (Optional)

Berdasarkan temuan-temuan tersebut, berikut adalah rekomendasi strategis yang potensial untuk diterapkan:

1. Menekan Angka Early-Stage Churn
    - Mengembangkan program mentorship yang sistematis dan terstruktur selama satu tahun pertama kerja yang dapat memberikan bimbingan profesional dan kepastian jenjang karir yang jelas.
2. Membuat Kebijakan Kompensasi yang Berbasis Data
    - Perusahaan harus bersedia memberikan kompensasi sesuai dengan beban kerja dan kebutuhan karyawan sehingga dapat terus memotivasi karyawan untuk dapat memiliki kinerja yang tinggi dan stabil.
3. Mempertahankan Talenta dengan Kinerja Tinggi
    - Memberikan penawaran benefit non-finansial lebih untuk para High Performer Talent seperti kepastian promosi dan kenaikan gaji yang adil.
4. Peningkatan Kualitas Lingkungan Kerja dan Engagement
    - Melakukan pengawasan rutin/berkala melalui riset internal terkait kesesuaian ekspektasi dan kebutuhan kerja karyawan dengan kondisi nyata di lapangan.
    - Mengembangkan lingkungan/budaya kerja yang dinamis berdasarkan hasil riset (tetapi tetap berprinsip pada visi dan misi perusahaan).