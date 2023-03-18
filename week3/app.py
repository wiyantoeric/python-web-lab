import streamlit as st
import pandas as pd
import numpy as np

# Text input
labelInput = st.text_input('Label')

# Access input value with session state
# st.text_input('Your name', key='name')
# st.session_state.name

# Number input
numberInput = st.number_input('Number')

# Show inputted label and number if both are not null
if (numberInput and labelInput):
    st.write(f"{labelInput} : {numberInput+10}")
