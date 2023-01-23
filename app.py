import streamlit as st
import tensorflow as tf
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

view = [100,150,30]
st.write('# view')
st.write('## paw')
view
st.write('## Bar chart')
st.bar_chart(view)



data = pd.read_excel("C:\\Users\\jason\\OneDrive\\바탕 화면\\1학년\\교과목\\수학\\ddim excel복사본.xlsx")
x_data = []
y_data = []
for i, rows in data.iterrows():
    x_data.append( rows['greengas'])
for i, rows in data.iterrows():
    y_data.append( rows['electric'])

data = {'greengas':x_data,
        'electric':y_data}
chart_data = pd.DataFrame(data, columns = ['greengas','electric'])

st.write('# greengas&electric')
st.line_chart(chart_data)
