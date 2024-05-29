import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st
from babel.numbers import format_currency
sns.set(style='dark')

st.set_page_config(page_title="BB Analysis Dashboard")
st.header("BB Analysis Dashboard")


#Registered user graph
day_df = pd.read_csv("day_data.csv")
day_df['dteday'] = pd.to_datetime(day_df['dteday'])
st.dataframe(day_df)
col1, col2 = st.columns(2)
tab1, tab2 = st.tabs(["Registered User", "Casual user"])

with tab1:
    st.header("Registered User in 2011-2012")
    daily = day_df.resample(rule='M', on='dteday').agg({
        "instant": "nunique",
        "registered": "last"
    })
    daily.index = daily.index.strftime('%B %Y')
    daily = daily.reset_index()

    # Separate data for 2011 and 2012
    daily_2011 = daily[daily['dteday'].str.contains('2011')]
    daily_2012 = daily[daily['dteday'].str.contains('2012')]

    plt.figure(figsize=(20, 10)) 
    # Plot data for 2011
    plt.plot(daily_2011.index, daily_2011["registered"], marker='o', linewidth=2, color="#72BCD4", label='2011') 

    # Plot data for 2012
    plt.plot(daily_2012.index, daily_2012["registered"], marker='o', linewidth=2, color="#FFA500", label='2012') 

    plt.title("Number of Registered User per Month (2021-2022)", loc="center", fontsize=20) 
    plt.xticks(ticks=range(len(daily)), labels=daily["dteday"], rotation=45, fontsize=10) 
    plt.yticks(fontsize=10) 
    plt.legend()
    st.pyplot(plt)

#casual user graph
with tab2:
    st.header("Casual User in 2011 - 2012")
    daily = day_df.resample(rule='M', on='dteday').agg({
        "instant": "nunique",
        "casual": "last"
    })
    daily.index = daily.index.strftime('%B %Y')
    daily = daily.reset_index()

    # Separate data for 2011 and 2012
    daily_2011 = daily[daily['dteday'].str.contains('2011')]
    daily_2012 = daily[daily['dteday'].str.contains('2012')]

    plt.figure(figsize=(20, 10)) 
    # Plot data for 2011
    plt.plot(daily_2011.index, daily_2011["casual"], marker='o', linewidth=2, color="#72BCD4", label='2011') 

    # Plot data for 2012
    plt.plot(daily_2012.index, daily_2012["casual"], marker='o', linewidth=2, color="#FFA500", label='2012') 

    plt.title("Number of Casual User per Month (2021-2022)", loc="center", fontsize=20) 
    plt.xticks(ticks=range(len(daily)), labels=daily["dteday"], rotation=45, fontsize=10) 
    plt.yticks(fontsize=10) 
    plt.legend()
    st.pyplot(plt)
