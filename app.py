import streamlit as st
import numpy as np
import pandas as pd

view = [100,150,30]
st.write('# view')
st.write('## paw')
view
st.write('## Bar chart')
st.bar_chart(view)



uploaded_file = st.file_uploader("greengas")
if uploaded_file is  not None:
    bytes_data = uploaded_file.getvalue()
    st.write(bytes_data)
    Stringio = StringIo(uploaded_file.getvalue().decode("utf-8"))
    st.write(Stringio)
    string_data = Stringio.read()
    st.write(string_data)
    dataframe = pd.read_csv(uploaded_file)
    st.write(dataframe)
    
