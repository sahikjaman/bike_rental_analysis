import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load datasets
day = pd.read_csv('day.csv')
hour = pd.read_csv('hour.csv')

# Set page layout
st.set_page_config(page_title="Bike Sharing Analysis Dashboard", layout="wide")

# Header
st.title('Dashboard Analisis Penggunaan Sepeda')
st.markdown("""
Dashboard ini menyajikan analisis interaktif dari data peminjaman sepeda berdasarkan cuaca, waktu, dan tipe pengguna.
Pilih opsi di bawah ini untuk mengeksplorasi data lebih lanjut.
""")

# Sidebar for navigation
st.sidebar.title("Navigation")
selected_option = st.sidebar.selectbox('Pilih Analisis', ['Pengaruh Cuaca', 'Tren Jam Peminjaman'])

# Sidebar controls
st.sidebar.header('Kontrol Filter')
selected_analysis = st.sidebar.selectbox('Pilih Analisis:', 
                                         ['Penggunaan Berdasarkan Waktu', 'Penggunaan Berdasarkan Cuaca', 'Pengguna Kasual vs Terdaftar'])

# Visualization based on selected analysis
if selected_analysis == 'Penggunaan Berdasarkan Waktu':
    st.subheader('Penggunaan Sepeda Berdasarkan Jam dalam Sehari')
    # Visualisasi rata-rata penggunaan sepeda berdasarkan jam
    hourly_avg = hour.groupby('hr')['cnt'].mean().reset_index()

    # Plotting
    plt.figure(figsize=(10, 5))
    sns.lineplot(data=hourly_avg, x='hr', y='cnt', marker='o')
    plt.title('Rata-rata Penggunaan Sepeda per Jam')
    plt.xlabel('Jam')
    plt.ylabel('Rata-rata Jumlah Pengguna (cnt)')
    st.pyplot(plt)

elif selected_analysis == 'Penggunaan Berdasarkan Cuaca':
    st.subheader('Penggunaan Sepeda Berdasarkan Kondisi Cuaca')
    weather_group = day.groupby('weathersit')['cnt'].mean().reset_index()

    # Plotting
    plt.figure(figsize=(10, 5))
    sns.barplot(data=weather_group, x='weathersit', y='cnt', palette='viridis')
    plt.title('Rata-rata Penggunaan Sepeda Berdasarkan Kondisi Cuaca')
    plt.xlabel('Kondisi Cuaca')
    plt.ylabel('Rata-rata Jumlah Pengguna (cnt)')
    st.pyplot(plt)

elif selected_analysis == 'Pengguna Kasual vs Terdaftar':
    st.subheader('Perbandingan Pengguna Kasual dan Terdaftar')
    hourly_usage = hour.groupby('hr')[['casual', 'registered']].mean().reset_index()

    # Plotting
    plt.figure(figsize=(10, 5))
    sns.lineplot(data=hourly_usage, x='hr', y='casual', label='Casual', marker='o')
    sns.lineplot(data=hourly_usage, x='hr', y='registered', label='Registered', marker='o')
    plt.title('Rata-rata Penggunaan Sepeda per Jam (Kasual vs Terdaftar)')
    plt.xlabel('Jam')
    plt.ylabel('Rata-rata Jumlah Pengguna')
    plt.legend(title='Tipe Pengguna')
    st.pyplot(plt)