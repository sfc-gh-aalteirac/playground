import streamlit as st

st.header('GO GO!')

if st.button('say hello'):
     st.write('why hello?')
else:
     st.write('goodbye')