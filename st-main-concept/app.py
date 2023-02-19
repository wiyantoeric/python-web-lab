import streamlit as st
import pandas as pd
import numpy as np

data_count = 100
random_data = np.array([i*0.1 + np.random.randn() for i in range (data_count)])

chart_data = pd.DataFrame(
        random_data,
        columns=['Random Value'],
        dtype=float,
    )

st.sidebar.header("Random value line chart")
st.sidebar.caption("17 Feb 2023")

st.line_chart(chart_data)
with st.expander("See explanation"):
    st.write("Random value chart")