# Student Academic Status Prediction

## Project Description

project ini dibuat untuk membuat model machine learning classification yang digunakan untuk memprediksi status akademik student. status akademik student pada dataset ini dibagi menjadi 3 yaitu graduate, dropout, dan enrolled.

project ini menggunakan beberapa informasi dari student seperti data pada saat pendaftaran, kondisi pembayaran tuition fee, umur saat enrollment, nilai, dan data akademik semester pertama dan semester kedua.

## Dataset

dataset yang digunakan pada project ini adalah "data.csv".

setelah dataset dibaca, terdapat 4424 baris dan 37 kolom. kolom "target" digunakan sebagai target yang akan diprediksi.

target pada dataset terdiri dari:

- Graduate
- Dropout
- Enrolled

sebelum digunakan, nama kolom pada dataset dirapihin terlebih dahulu supaya lebih gampang digunakan pada proses selanjutnya. beberapa proses yang dilakukan yaitu menghapus spasi, mengubah nama kolom menjadi lowercase, mengganti spasi menjadi underscore, dan memperbaiki typo pada kolom `nationality`.

## Objective

project ini dibuat untuk:

- melihat gambaran kondisi akademik student dari dataset yang digunakan
- melihat beberapa faktor yang berkaitan dengan status akademik student melalui EDA
- menyiapkan data supaya bisa digunakan untuk proses machine learning
- membuat model classification untuk memprediksi status akademik student
- menggunakan model yang sudah dibuat pada data baru melalui model inference

## Project Flow

### 1. Data Loading

pada bagian ini dataset `data.csv` dibaca menggunakan pandas. karena dataset menggunakan separator `;`, maka separator tersebut ditentukan pada saat membaca dataset.

setelah itu dilakukan pengecekan jumlah baris dan kolom, nama kolom, tipe data, missing value, duplicate data, dan jumlah data pada masing-masing target.

### 2. Exploratory Data Analysis

pada bagian EDA dilakukan eksplorasi untuk melihat kondisi data dan hubungan beberapa feature dengan status akademik student.

visualisasi digunakan supaya pola pada data lebih gampang dilihat dan dibandingkan antara student dengan status **Graduate**, **Dropout**, dan **Enrolled**.

### 3. Feature Engineering

pada bagian ini feature dan target dipisahkan terlebih dahulu.

`X` berisi feature yang digunakan untuk modeling, sedangkan `y` berisi kolom `target`.

setelah itu data dibagi menjadi train-set dan test-set dengan perbandingan **80% train-set dan 20% test-set**. pembagian data menggunakan `stratify=y` supaya proporsi masing-masing target tetap terjaga.

feature kemudian dipisahkan menjadi feature kategorikal dan numerikal karena preprocessing yang digunakan pada kedua jenis feature berbeda.

### 4. Modeling

setelah data selesai dipersiapkan, data digunakan untuk proses modeling classification. model kemudian dievaluasi untuk melihat performanya dalam memprediksi status akademik student.

### 5. Model Inference

model terbaik yang sudah disimpan digunakan kembali pada notebook inference untuk mencoba prediksi pada data yang tidak digunakan pada proses training maupun testing.

## Libraries

library utama yang digunakan pada project ini yaitu:

- pandas
- matplotlib
- seaborn
- scikit-learn

## How to Run

1. pastikan file dataset `data.csv` berada pada folder yang sama dengan notebook.
2. install library yang dibutuhkan.
3. buka notebook `P1M2_Syauqiya_Hasna.ipynb` menggunakan Jupyter Notebook atau VS Code.
4. jalankan notebook dari bagian import libraries sampai selesai secara berurutan.
5. untuk model inference, jalankan notebook `P1M2_Syauqiya_Hasna_inf.ipynb` setelah model sudah disimpan dari notebook modeling.


## File

```text
P1M2_Syauqiya_Hasna.ipynb
P1M2_Syauqiya_Hasna_inf.ipynb
data.csv
description.md
url.txt
deployment/
```

## Author

Syauqiya Hasna