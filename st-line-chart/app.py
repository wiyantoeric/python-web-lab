import streamlit as st
import pandas as pd
import numpy as np

st.set_page_config(
    page_title='Line Chart',
    page_icon21=None,
)

# Create chart with random value
data_count = 100
random_data = np.array([i*0.1 + np.random.randn() for i in range (data_count)])

chart_data = pd.DataFrame(
        random_data,
        columns=['Random Value'],
        dtype=float,
    )

# Render UI
st.header('Line Chart')
st.caption('Random data graph')
st.line_chart(chart_data)
