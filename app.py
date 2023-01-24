import streamlit as st
import numpy as np
import pandas as pd

view = [100,150,30]
st.write('# view')
st.write('## paw')
view
st.write('## Bar chart')
st.bar_chart(view)



uploaded_files = st.file_uploader("Choose a CSV file", accept_multiple_files=True)
for uploaded_file in uploaded_files:
    bytes_data = uploaded_file.read()
    st.write("filename:", uploaded_file.name)
    st.write(bytes_data)
