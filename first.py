import streamlit as st
import pandas as pd
from streamlit_pandas_profiling import st_profile_report

st.header('`streamlit_pandas_profiling`')

df = pd.read_csv('https://raw.githubusercontent.com/Opensourcefordatascience/Data-sets/master/automotive_data.csv')

pr = df.profile_report()
st_profile_report(pr)