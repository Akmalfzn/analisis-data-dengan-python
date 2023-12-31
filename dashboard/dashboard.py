import pandas as pd
import streamlit as st
import seaborn as sns
import matplotlib.pyplot as plt


# Set style seaborn
sns.set(style='dark')

# Menyiapkan data dfday
dfday = pd.read_csv("https://raw.githubusercontent.com/Akmalfzn/analisis-data-dengan-python/main/data/day.csv")
dfday.head()

# Menghapus beberapa kolom yang tidak diperlukan pada table day
drop_col = ['instant', 'windspeed']

for i in dfday.columns:
  if i in drop_col:
    dfday.drop(labels=i, axis=1, inplace=True)


# Mengubah angka menjadi keterangan
dfday['season'] = dfday['season'].map({
    1: 'Spring', 2: 'Summer', 3: 'Fall', 4: 'Winter'
})
dfday['mnth'] = dfday['mnth'].map({
    1: 'Jan', 2: 'Feb', 3: 'Mar', 4: 'Apr', 5: 'May', 6: 'Jun',
    7: 'Jul', 8: 'Aug', 9: 'Sep', 10: 'Oct', 11: 'Nov', 12: 'Dec'
})
dfday['weekday'] = dfday['weekday'].map({
    0: 'Sun', 1: 'Mon', 2: 'Tue', 3: 'Wed', 4: 'Thu', 5: 'Fri', 6: 'Sat'
})
dfday['weathersit'] = dfday['weathersit'].map({
    1: 'Clear/Partly Cloudy',
    2: 'Misty/Cloudy',
    3: 'Light Snow/Rain',
    4: 'Severe Weather'
})

# Menyiapkan daily_rent_df
def create_daily_rent_df(df):
    daily_rent_df = df.groupby(by='dteday').agg({
        'cnt': 'sum'
    }).reset_index()
    return daily_rent_df

# Menyiapkan daily_casual_rent_df
def create_daily_casual_rent_df(df):
    daily_casual_rent_df = df.groupby(by='dteday').agg({
        'casual': 'sum'
    }).reset_index()
    return daily_casual_rent_df

# Menyiapkan daily_registered_rent_df
def create_daily_registered_rent_df(df):
    daily_registered_rent_df = df.groupby(by='dteday').agg({
        'registered': 'sum'
    }).reset_index()
    return daily_registered_rent_df
    
# Menyiapkan season_rent_df
def create_season_rent_df(df):
    season_rent_df = df.groupby(by='season')[['registered', 'casual']].sum().reset_index()
    return season_rent_df

# Menyiapkan monthly_rent_df
def create_monthly_rent_df(df):
    monthly_rent_df = df.groupby(by='mnth').agg({
        'cnt': 'sum'
    })
    ordered_mnths = [
        'Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun',
        'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'
    ]
    monthly_rent_df = monthly_rent_df.reindex(ordered_mnths, fill_value=0)
    return monthly_rent_df

# Menyiapkan weather_rent_df
def create_weather_rent_df(df):
    weather_rent_df = df.groupby(by='weathersit').agg({
        'cnt': 'sum'
    })
    return weather_rent_df


# Membuat komponen filter
min_date = pd.to_datetime(dfday['dteday']).dt.date.min()
max_date = pd.to_datetime(dfday['dteday']).dt.date.max()
 
with st.sidebar:
    st.image("https://raw.githubusercontent.com/Akmalfzn/analisis-data-dengan-python/main/dashboard/bikerent.png")
    
    # Mengambil start_date & end_date dari date_input
    start_date, end_date = st.date_input(
        label='Rentang Waktu',
        min_value= min_date,
        max_value= max_date,
        value=[min_date, max_date]
    )

main_df = dfday[(dfday['dteday'] >= str(start_date)) & 
                (dfday['dteday'] <= str(end_date))]

# Menyiapkan berbagai dataframe
daily_rent_df = create_daily_rent_df(main_df)
daily_casual_rent_df = create_daily_casual_rent_df(main_df)
daily_registered_rent_df = create_daily_registered_rent_df(main_df)
season_rent_df = create_season_rent_df(main_df)
monthly_rent_df = create_monthly_rent_df(main_df)
weather_rent_df = create_weather_rent_df(main_df)

# Membuat Dashboard secara lengkap

# Membuat judul
st.header('Dashboard Rental Sepeda 🚲')

# Membuat jumlah penyewaan harian
st.subheader('Sewa Harian')
col1, col2, col3 = st.columns(3)

with col1:
    daily_rent_casual = daily_casual_rent_df['casual'].sum()
    st.metric('Pengguna Biasa', value= daily_rent_casual)

with col2:
    daily_rent_registered = daily_registered_rent_df['registered'].sum()
    st.metric('Pengguna Terdaftar', value= daily_rent_registered)
 
with col3:
    daily_rent_total = daily_rent_df['cnt'].sum()
    st.metric('Total Pengguna', value= daily_rent_total)


# Membuah jumlah penyewaan berdasarkan kondisi cuaca
st.subheader('Penyewaan Berdasarkan Cuaca')

fig, ax = plt.subplots(figsize=(16, 8))

colors=["tab:blue", "tab:orange", "tab:green"]

sns.barplot(
    x=weather_rent_df.index,
    y=weather_rent_df['cnt'],
    ax=ax
)

for index, row in enumerate(weather_rent_df['cnt']):
    ax.text(index, row + 1, str(row), ha='center', va='bottom', fontsize=12)

ax.set_xlabel(None)
ax.set_ylabel(None)
ax.tick_params(axis='x', labelsize=20)
ax.tick_params(axis='y', labelsize=15)
st.pyplot(fig)


# Membuat jumlah penyewaan berdasarkan season
st.subheader('Penyewaan Berdasarkan Musim')

fig, ax = plt.subplots(figsize=(16, 8))

sns.barplot(
    x='season',
    y='registered',
    data=season_rent_df,
    label='Registered',
    color='tab:blue',
    ax=ax
)

sns.barplot(
    x='season',
    y='casual',
    data=season_rent_df,
    label='Casual',
    color='tab:orange',
    ax=ax
)

for index, row in season_rent_df.iterrows():
    ax.text(index, row['registered'], str(row['registered']), ha='center', va='bottom', fontsize=12)
    ax.text(index, row['casual'], str(row['casual']), ha='center', va='bottom', fontsize=12)

ax.set_xlabel(None)
ax.set_ylabel(None)
ax.tick_params(axis='x', labelsize=20, rotation=0)
ax.tick_params(axis='y', labelsize=15)
ax.legend()
st.pyplot(fig)

# Membuat jumlah penyewaan bulanan
st.subheader('Penyewaan Berdasarkan Bulan')
fig, ax = plt.subplots(figsize=(24, 8))
ax.plot(
    monthly_rent_df.index,
    monthly_rent_df['cnt'],
    marker='o', 
    linewidth=2,
    color='tab:blue'
)

for index, row in enumerate(monthly_rent_df['cnt']):
    ax.text(index, row + 1, str(row), ha='center', va='bottom', fontsize=12)

ax.tick_params(axis='x', labelsize=25, rotation=45)
ax.tick_params(axis='y', labelsize=20)
st.pyplot(fig)

st.caption('Copyright (C) Muhammad Akmal Fauzan 2023')