import streamlit as st
import pandas as pd
import numpy as np

# Create chart with random value
data_count = 100
random_data = np.array([i*0.1+np.random.randn() for i in range (data_count)])

chart_data = pd.DataFrame(
        random_data,
        columns=['Value'],
        dtype=float,
    )

# Render UI
st.header('Random Data Graph')
st.caption('Python web lecture assignment')
st.line_chart(chart_data)
