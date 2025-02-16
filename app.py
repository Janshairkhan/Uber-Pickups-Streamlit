import streamlit as st
import pandas as pd
import numpy as np
import time

# Custom HTML & CSS for crazy styling
st.markdown(
    """
    <style>
    body {
        background-color: #f4f4f4;
    }
    .stTitle {
        color: #ff5733;
        font-size: 50px;
        font-weight: bold;
        text-align: center;
        text-shadow: 2px 2px 10px #ff0000;
    }
    .stSubheader {
        color: #33ff57;
        font-size: 30px;
        text-shadow: 2px 2px 5px #00ff00;
    }
    .stText {
        font-size: 20px;
        font-weight: bold;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# 🔥 Crazy Title
st.markdown('<h1 class="stTitle">🚖 Uber Pickups in NYC 🚖</h1>', unsafe_allow_html=True)

# 🎉 Animated Loading Text
loading_msg = st.empty()
for i in range(3):
    loading_msg.text(f"⏳ Loading data{'.' * (i + 1)}")
    time.sleep(0.5)
loading_msg.text("✅ Data Loaded!")

# 🛠️ Data Loading Function
DATE_COLUMN = 'date/time'
DATA_URL = ('https://s3-us-west-2.amazonaws.com/streamlit-demo-data/uber-raw-data-sep14.csv.gz')
st.balloons()
@st.cache_data
def load_data(nrows):
    data = pd.read_csv(DATA_URL, nrows=nrows)
    data.rename(lambda x: str(x).lower(), axis='columns', inplace=True)
    data[DATE_COLUMN] = pd.to_datetime(data[DATE_COLUMN])
    return data

data = load_data(10_000)

# 🎯 Funky Sidebar for Filters
st.sidebar.header("🎚️ Filters")
hour_to_filter = st.sidebar.slider('⏰ Select an Hour', 0, 23, 17)

# 🌈 Crazy Data Section
st.markdown('<h2 class="stSubheader">📜 Raw Data</h2>', unsafe_allow_html=True)
if st.checkbox('🧐 Show Raw Data'):
    st.dataframe(data.style.applymap(lambda x: "color: red" if isinstance(x, int) and x % 2 == 0 else "color: blue"))

# 📊 Pickup Histogram
st.markdown('<h2 class="stSubheader">📊 Pickups by Hour</h2>', unsafe_allow_html=True)
hist_values = np.histogram(data[DATE_COLUMN].dt.hour, bins=24, range=(0, 24))[0]
st.bar_chart(hist_values)

# 🗺️ NYC Map with Pickups
st.markdown('<h2 class="stSubheader">🌍 All Uber Pickups</h2>', unsafe_allow_html=True)
st.map(data)

# 🕵️‍♂️ Filtered Pickups by Hour
filtered_data = data[data[DATE_COLUMN].dt.hour == hour_to_filter]
st.markdown(f'<h2 class="stSubheader">🕒 Pickups at {hour_to_filter}:00</h2>', unsafe_allow_html=True)
st.map(filtered_data)

# 🎵 Add Some Sound Effects
st.markdown('<audio autoplay><source src="https://www.fesliyanstudios.com/play-mp3/387" type="audio/mp3"></audio>', unsafe_allow_html=True)

# 🎊 Crazy Footer
st.markdown("""
    <div style="text-align:center">
        <h3>🚀 Made with ❤️ in Streamlit</h3>
        <p>🔥🔥🔥🔥🔥</p>
    </div>
""", unsafe_allow_html=True)
