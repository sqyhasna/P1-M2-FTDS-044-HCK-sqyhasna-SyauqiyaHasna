import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def fix_grade(value):
    value = str(value)

    if value.count('.') > 1:
        first_dot = value.find('.')
        value = value[:first_dot + 1] + value[first_dot + 1:].replace('.', '')

    return pd.to_numeric(value, errors='coerce')

def run():
    st.title('Student Academic Status Prediction')

    df = pd.read_csv('data.csv', sep=';')

    df.columns = df.columns.str.strip()
    df.columns = df.columns.str.lower()
    df.columns = df.columns.str.replace("'", "", regex=False)
    df.columns = df.columns.str.replace(r'[^a-z0-9]+', '_', regex=True)
    df.columns = df.columns.str.strip('_')
    df = df.rename(columns={'nacionality': 'nationality'})

    df['curricular_units_1st_sem_grade'] = (df['curricular_units_1st_sem_grade'].apply(fix_grade))
    df['curricular_units_2nd_sem_grade'] = (df['curricular_units_2nd_sem_grade'].apply(fix_grade))

    st.write('### Dataset')
    st.dataframe(df)

    st.write('### Distribusi Status Akademik')
    fig = plt.figure(figsize=(10, 5))
    sns.countplot(data=df, x='target')
    plt.title('distribusi status akademik')
    plt.xlabel('status akademik')
    plt.ylabel('jumlah student')
    st.pyplot(fig)

    st.write('status graduate punya jumlah paling banyak, sedangkan enrolled paling sedikit. perbedaannya cukup jelas, jadi dari awal sudah kelihatan kalau target mengalami ketidakseimbangan')

    st.write('### Distribusi Umur Saat Mendaftar')
    fig = plt.figure(figsize=(10, 5))
    sns.histplot(data=df, x='age_at_enrollment', bins=30, kde=True)
    plt.title('distibusi umur saat mendaftar')
    plt.xlabel('umur saat mendaftar')
    plt.ylabel('jumlah student')
    st.pyplot(fig)

    st.write('sebagian besar student mendaftar pada umur sekitar 18 sampai awal 20-an. distribusinya condong ke kanan karena masih ada student yang mendaftar di umur yang lebih tua, tapi jumlahnya semakin sedikit. jadi mayoritas data memang berasal dari student usia kuliah pada umumnya, tetapi tetap ada variasi usia yang cukup lebar')

    st.write('### Status Akademik Berdasarkan Pembayaran Tuition Fee')
    fig = plt.figure(figsize=(10, 5))
    sns.countplot(
        data=df,
        x='tuition_fees_up_to_date',
        hue='target'
    )
    plt.title('status akademik berdasarkan pembayaran tuition fee')
    plt.xlabel('pembayaran tuition fee')
    plt.ylabel('jumlah student')
    st.pyplot(fig)

    st.write('student dengan tuition fee yang "up to date" lebih banyak berada pada status graduate. sebaliknya, pada student yang pembayarannya tidak "up to date", jumlah dropout terlihat lebih dominan. dari grafik ini kelihatan kalau kondisi pembayaran punya hubungan dengan status akademik')

    st.write('### Status Akademik Berdasarkan Status Debtor')
    fig = plt.figure(figsize=(10, 5))
    sns.countplot(
        data=df,
        x='debtor',
        hue='target'
    )
    plt.title('status akademik berdasarkan status debtor')
    plt.xlabel('status debtor')
    plt.ylabel('jumlah student')
    st.pyplot(fig)

    st.write('pada student yang bukan "debtor", status Graduate paling dominan. sedangkan pada student yang punya status "debtor", jumlah Dropout terlihat lebih banyak. polanya searah dengan hasil tuition fee sebelumnya, yaitu kondisi finansial kelihatan cukup berkaitan dengan keberlanjutan studi. Feature debtor dan tuition_fees_up_to_date jadi cukup menarik untuk dipertahankan dalam modeling')

    st.write('### Status Akademik Berdasarkan Penerima Beasiswa')
    fig = plt.figure(figsize=(10, 5))
    sns.countplot(
        data=df,
        x='scholarship_holder',
        hue='target'
    )
    plt.title('status akademik berdasarkan penerima beasiswa')
    plt.xlabel('penerima beasiswa')
    plt.ylabel('jumlah student')
    st.pyplot(fig)

    st.write('student penerima beasiswa lebih banyak berada pada kelas graduate, sementara jumlah dropout-nya lebih sedikit. Pada student yang tidak menerima beasiswa, jumlah dropout terlihat lebih besar. hasil ini nunjukin kalau status beasiswa juga punya pola yang berbeda antar kelas target. walaupun begitu, beasiswa bukan satu-satunya faktor karena status akademik student tetap dipengaruhi oleh banyak feature lain')

    st.write('### Nilai Semester Pertama Berdasarkan Status Akademik')
    fig = plt.figure(figsize=(10, 5))
    sns.barplot(
        data=df,
        x='target',
        y='curricular_units_1st_sem_grade',
        estimator='median',
        errorbar=None
    )
    plt.title('jumlah mata kuliah lulus semester pertama berdasarkan status akademik')
    plt.xlabel('status akademik')
    plt.ylabel('jumlah mata kuliah lulus semester pertama')
    st.pyplot(fig)

    st.write('student dengan status graduate punya median nilai semester pertama yang lebih tinggi dibandingkan dropout dan Enrolled. sementara itu, kelompok dropout punya nilai yang lebih rendah. jadi performa akademik sejak semester pertama sudah kelihatan cukup membedakan ketiga status. ini juga masuk akal untuk dicek lebih lanjut pada feature importance karena nilai dan jumlah mata kuliah yang lulus muncul langsung selama proses studi')

    st.write('### Hubungan Nilai dan Mata Kuliah Lulus Semester Pertama')
    fig = plt.figure(figsize=(10, 6))
    sns.scatterplot(
        data=df,
        x='curricular_units_1st_sem_grade',
        y='curricular_units_1st_sem_approved',
        hue='target',
    )
    plt.title('hubungan nilai dan jumlah mata kuliah lulus semester pertama')
    plt.xlabel('nilai semester pertama')
    plt.ylabel('jumlah mata kuliah lulus semester pertama')
    st.pyplot(fig)

    st.write('secara umum, student dengan nilai semester pertama yang lebih baik juga cenderung punya lebih banyak mata kuliah yang lulus. titik Graduate lebih banyak muncul pada area nilai dan jumlah mata kuliah lulus yang lebih tinggi, sedangkan dropout lebih banyak muncul pada area yang lebih rendah. masih ada beberapa nilai yang terlihat jauh dari mayoritas data. Karena itu, pengecekan format data dan outlier tetap dilakukan sebelum modeling supaya nilai yang tidak wajar tidak langsung dianggap normal')

if __name__ == "__main__":
    run()
