import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.title("天气数据仪表板 - Temperature / Humidity / Rainfall")

# 读取数据
df = pd.read_csv("weather.csv")
df["date"] = pd.to_datetime(df["date"])

# 数据预览
st.subheader("数据预览")
st.dataframe(df.head())

# 选择年份
years = df["date"].dt.year.unique()
year = st.selectbox("选择年份", years)

filtered = df[df["date"].dt.year == year]

# 温度图
st.subheader(f"{year} 年气温变化")
fig1, ax1 = plt.subplots(figsize=(10, 4))
ax1.plot(filtered["date"], filtered["temperature_2m_mean"])
ax1.set_xlabel("Date")
ax1.set_ylabel("Temperature (°C)")
st.pyplot(fig1)

# 湿度图
st.subheader(f"{year} 年湿度变化")
fig2, ax2 = plt.subplots(figsize=(10, 4))
ax2.plot(filtered["date"], filtered["relativehumidity_2m_mean"])
ax2.set_xlabel("Date")
ax2.set_ylabel("Humidity (%)")
st.pyplot(fig2)

# 降雨量图
st.subheader(f"{year} 年降雨量")
fig3, ax3 = plt.subplots(figsize=(10, 4))
ax3.bar(filtered["date"], filtered["precipitation_sum"])
ax3.set_xlabel("Date")
ax3.set_ylabel("Rainfall (mm)")
st.pyplot(fig3)
