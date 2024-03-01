import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st
from babel.numbers import format_currency
import matplotlib.ticker as ticker
sns.set(style='dark')
st.set_page_config(layout="wide")

day_df = pd.read_csv('main_data.csv')

total_sum_by_month_df = day_df.groupby(by=["weekday"]).agg({
    "casual" : "sum",
    "registered" : "sum",
    "cnt" : "sum",
})
total_2011_df = day_df.loc[day_df['yr'] == 0]
total_sum_by_month_2011_df = total_2011_df.groupby(by=["weekday"]).agg({
    "casual" : "sum",
    "registered" : "sum",
    "cnt" : "sum",
})
total_2012_df = day_df.loc[day_df['yr'] == 1]
total_sum_by_month_2012_df = total_2012_df.groupby(by=["weekday"]).agg({
    "casual" : "sum",
    "registered" : "sum",
    "cnt" : "sum",
})
days = ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday']
total_sum_by_month_df.index = total_sum_by_month_df.index.map(lambda x: days[x])
total_sum_by_month_2011_df.index = total_sum_by_month_2011_df.index.map(lambda x: days[x])
total_sum_by_month_2012_df.index = total_sum_by_month_2012_df.index.map(lambda x: days[x])

total_sum_by_weather = day_df.groupby(by="weathersit").agg({
    "cnt" : "sum"
})
total_sum_by_weather = total_sum_by_weather._append({'cnt': 0}, ignore_index=True)
weather = ['Clear', 'Mist + Cloudy', 'Light Snow', 'Heavy Rain']
total_sum_by_weather.index = total_sum_by_weather.index.map(lambda x: weather[x])

total_2011_df = day_df.loc[day_df['yr'] == 0]
total_sum_by_month_2011_df = total_2011_df.groupby(by=["weekday"]).agg({
    "casual" : "sum",
    "registered" : "sum",
    "cnt" : "sum",
})
total_2011_by_weather_df = day_df.loc[day_df['yr'] == 0]
total_2011_by_weather_df = total_2011_by_weather_df.groupby(by="weathersit").agg({
    "cnt" : "sum"
})
total_2011_by_weather_df = total_2011_by_weather_df._append({'cnt': 0}, ignore_index=True)
weather = ['Clear', 'Mist + Cloudy', 'Light Snow', 'Heavy Rain']
total_2011_by_weather_df.index = total_2011_by_weather_df.index.map(lambda x: weather[x])

total_2012_by_weather_df = day_df.loc[day_df['yr'] == 1]
total_2012_by_weather_df = total_2012_by_weather_df.groupby(by="weathersit").agg({
    "cnt" : "sum"
})
total_2012_by_weather_df = total_2012_by_weather_df._append({'cnt': 0}, ignore_index=True)
weather = ['Clear', 'Mist + Cloudy', 'Light Snow', 'Heavy Rain']
total_2012_by_weather_df.index = total_2012_by_weather_df.index.map(lambda x: weather[x])

st.header('Dicoding Project Dashboard 🚴 :)')
col1, col2 = st.columns([2,6])
st.subheader('Daily Riders')
with col1:
    year = st.selectbox(
        label="Select Year",
        options=('2011 & 2012', '2011', '2012')
    )

col1, col2, col3 = st.columns(3)

with col1:
    if year == '2011 & 2012':
        total = total_sum_by_month_df["cnt"].sum()
    elif year == '2011':
        total = total_sum_by_month_2011_df["cnt"].sum()
    else:
        total = total_sum_by_month_2012_df["cnt"].sum()
    st.metric("Total Riders", value=total)

with col2:
    if year == '2011 & 2012':
        total = total_sum_by_month_df["casual"].sum()
    elif year == '2011':
        total = total_sum_by_month_2011_df["casual"].sum()
    else:
        total = total_sum_by_month_2012_df["casual"].sum()
    st.metric("Total Casual Riders", value=total)
    
with col3:
    if year == '2011 & 2012':
        total = total_sum_by_month_df["registered"].sum()
    elif year == '2011':
        total = total_sum_by_month_2011_df["registered"].sum()
    else:
        total = total_sum_by_month_2012_df["registered"].sum()
    st.metric("Total Registered Riders", value=total)

col1, col2, col3 = st.columns(3)

if year == '2011 & 2012':
    with col1:
        plt.figure(figsize=(10, 5))
        plt.plot(total_sum_by_month_df.index, total_sum_by_month_df["cnt"], marker='o', linewidth=2, color="#72BCD4")
        plt.title("Daily Rider ({})".format(year), loc="center", fontsize=20)
        plt.xticks(fontsize=10)
        plt.yticks(fontsize=10)
        plt.xlabel('Day')
        plt.ylabel('Amount')
        plt.legend(["Total"])
        plt.grid(True)
        st.pyplot(plt)
    with col2:
        plt.figure(figsize=(10, 5))
        plt.plot(total_sum_by_month_df.index, total_sum_by_month_df["casual"], marker='o', linewidth=2, color="#72BCD4")
        plt.title("Daily Casual Rider ({})".format(year), loc="center", fontsize=20)
        plt.xticks(fontsize=10)
        plt.yticks(fontsize=10)
        plt.xlabel('Day')
        plt.ylabel('Amount')
        plt.legend(["Casual"])
        plt.grid(True)
        st.pyplot(plt)
    with col3:
        plt.figure(figsize=(10, 5))
        plt.plot(total_sum_by_month_df.index, total_sum_by_month_df["registered"], marker='o', linewidth=2, color="#72BCD4")
        plt.title("Daily Registered Rider ({})".format(year), loc="center", fontsize=20)
        plt.xticks(fontsize=10)
        plt.yticks(fontsize=10)
        plt.xlabel('Day')
        plt.ylabel('Amount')
        plt.legend(["Registered"])
        plt.grid(True)
        st.pyplot(plt)
elif year == '2011':
    with col1:
        plt.figure(figsize=(10, 5))
        plt.plot(total_sum_by_month_2011_df.index, total_sum_by_month_2011_df["cnt"], marker='o', linewidth=2, color="#72BCD4")
        plt.title("Daily Rider ({})".format(year), loc="center", fontsize=20)
        plt.xticks(fontsize=10)
        plt.yticks(fontsize=10)
        plt.xlabel('Day')
        plt.ylabel('Amount')
        plt.legend(["Total"])
        plt.grid(True)
        st.pyplot(plt)
    with col2:
        plt.figure(figsize=(10, 5))
        plt.plot(total_sum_by_month_2011_df.index, total_sum_by_month_2011_df["casual"], marker='o', linewidth=2, color="#72BCD4")
        plt.title("Daily Casual Rider ({})".format(year), loc="center", fontsize=20)
        plt.xticks(fontsize=10)
        plt.yticks(fontsize=10)
        plt.xlabel('Day')
        plt.ylabel('Amount')
        plt.legend(["Casual"])
        plt.grid(True)
        st.pyplot(plt)
    with col3:
        plt.figure(figsize=(10, 5))
        plt.plot(total_sum_by_month_2011_df.index, total_sum_by_month_2011_df["registered"], marker='o', linewidth=2, color="#72BCD4")
        plt.title("Daily Registered Rider ({})".format(year), loc="center", fontsize=20)
        plt.xticks(fontsize=10)
        plt.yticks(fontsize=10)
        plt.xlabel('Day')
        plt.ylabel('Amount')
        plt.legend(["Registered"])
        plt.grid(True)
        st.pyplot(plt)
else:
    with col1:
        plt.figure(figsize=(10, 5))
        plt.plot(total_sum_by_month_2012_df.index, total_sum_by_month_2012_df["cnt"], marker='o', linewidth=2, color="#72BCD4")
        plt.title("Daily Rider ({})".format(year), loc="center", fontsize=20)
        plt.xticks(fontsize=10)
        plt.yticks(fontsize=10)
        plt.xlabel('Day')
        plt.ylabel('Amount')
        plt.legend(["Total"])
        plt.grid(True)
        st.pyplot(plt)
    with col2:
        plt.figure(figsize=(10, 5))
        plt.plot(total_sum_by_month_2012_df.index, total_sum_by_month_2012_df["casual"], marker='o', linewidth=2, color="#72BCD4")
        plt.title("Daily Casual Rider ({})".format(year), loc="center", fontsize=20)
        plt.xticks(fontsize=10)
        plt.yticks(fontsize=10)
        plt.xlabel('Day')
        plt.ylabel('Amount')
        plt.legend(["Casual"])
        plt.grid(True)
        st.pyplot(plt)
    with col3:
        plt.figure(figsize=(10, 5))
        plt.plot(total_sum_by_month_2012_df.index, total_sum_by_month_2012_df["registered"], marker='o', linewidth=2, color="#72BCD4")
        plt.title("Daily Registered Rider ({})".format(year), loc="center", fontsize=20)
        plt.xticks(fontsize=10)
        plt.yticks(fontsize=10)
        plt.xlabel('Day')
        plt.ylabel('Amount')
        plt.legend(["Registered"])
        plt.grid(True)
        st.pyplot(plt)



st.subheader('Riders During Different Weather Conditions')
col1, col2, col3 = st.columns(3)

with col1:
    fig, ax = plt.subplots()
    sns.barplot(
        y=total_sum_by_weather["cnt"],
        x=total_sum_by_weather.index,
        ax=ax
    )
    ax.yaxis.set_major_formatter(ticker.FuncFormatter(lambda x, pos: '{:,.0f}'.format(x)))
    ax.set_xlabel('Weather')
    ax.set_ylabel('Count')
    ax.set_title('Rider count during Weather (2011 & 2012)')
    plt.grid(True)
    st.pyplot(fig)
with col2:
    fig, ax = plt.subplots()
    sns.barplot(
        y=total_2011_by_weather_df["cnt"],
        x=total_2011_by_weather_df.index,
        ax=ax
    )
    ax.yaxis.set_major_formatter(ticker.FuncFormatter(lambda x, pos: '{:,.0f}'.format(x)))
    ax.set_xlabel('Weather')
    ax.set_ylabel('Count')
    ax.set_title('Rider count during Weather (2011)')
    plt.grid(True)
    st.pyplot(fig)
with col3:
    fig, ax = plt.subplots()
    sns.barplot(
        y=total_2012_by_weather_df["cnt"],
        x=total_2012_by_weather_df.index,
        ax=ax
    )
    ax.yaxis.set_major_formatter(ticker.FuncFormatter(lambda x, pos: '{:,.0f}'.format(x)))
    ax.set_xlabel('Weather')
    ax.set_ylabel('Count')
    ax.set_title('Rider count during Weather (2012)')
    plt.grid(True)
    st.pyplot(fig)