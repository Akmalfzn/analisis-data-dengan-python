# analisis-data-dengan-python
Menganalisis data bike rental menggunakan python dan memvisualisasi data pada dashboard menggunakan streamlit
![Dashboard Penyewaan Sepeda](https://raw.githubusercontent.com/Akmalfzn/analisis-data-dengan-python/main/Screenshot/Screenshot%201.png)

## Table of Contents
- [Overview](#overview)
- [Project Structure](#project-structure)
- [Installation](#installation)
- [Usage](#usage)

## Overview
Proyek ini merupakan proyek analisis dan visualisasi data yang berfokus pada data Bike Sharing. Ini mencakup kode untuk perselisihan data, analisis data eksplorasi (EDA), dan dasbor Streamlit untuk eksplorasi data interaktif. Proyek ini bertujuan untuk menganalisis data pada Bike Sharing Dataset.

## Project Structure
- `dashboard/`: Direktori ini berisi dashboard.py yang digunakan untuk membuat dashboard hasil analisis data.
- `data/`: Direktori yang berisi file data CSV mentah.
- `notebook.ipynb`: File ini digunakan untuk melakukan analisis data.
- `README.md`: File dokumentasi ini.

## Installation
1. Kloning repositori ini ke mesin lokal Anda:
```
git clone https://github.com/Akmalfzn/analisis-data-dengan-python.git
```
2. Buka direktori proyek
```
cd analisis-data-dengan-python
```
3. Instal paket Python yang diperlukan dengan menjalankan:
```
pip install -r requirements.txt
```

## Usage
1. **Data Wrangling**: Data wrangling scripts are available in the `notebook.ipynb` file to prepare and clean the data.

2. **Exploratory Data Analysis (EDA)**: Explore and analyze the data using the provided Python scripts. EDA insights can guide your understanding of Bike Sharing Dataset data patterns.

3. **Visualization**: Run the Streamlit dashboard for interactive data exploration:

```
cd analisis-data-dengan-python/dashboard
streamlit run dashboard.py
```
Access the dashboard in your web browser at `http://localhost:8501`.
