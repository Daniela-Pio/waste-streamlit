import streamlit as st
import numpy as np
import pandas as pd
import altair as alt

# Page title
st.set_page_config(page_title='Waste dedication', page_icon='🗑️')
st.title('🗑️ Waste dedication')

with st.expander('About this app'):
st.markdown('What can this app do?')
st.info('This app gives you information about the composition of the contents of the waste bins and the further processing of the waste.')
st.markdown('How to use the app?')
st.warning('Select the desired waste bin and you will receive the desired information.')


# Load data
data = pd.DataFrame({
'Mülltonne': ['Schwarze Tonne', 'Gelbe Tonne', 'Braune Tonne'],
'Plastik': [70, 90, 0],
'Papier': [20, 0, 10],
'Restmüll': [10, 0, 10],
'Wasser': [0, 10, 0],
'Organische Abfälle': [0, 0, 80]
})

# Input widgets
## Bin selection
waste_type = st.selectbox('Select Trash bin', data['Mülltonne'])

selected_data = data[data['Mülltonne'] == waste_type].melt(var_name='Bestandteil', value_name='Prozent')



# Display chart
chart = alt.Chart(selected_data).mark_bar().encode(
x='Prozent:Q',
y='Bestandteil:N'
).properties(
width=600,
height=400
)

st.altair_chart(chart)

#Infotext
if waste_type == 'Schwarze Tonne':
st.write("Der Müll aus der schwarzen Tonne wird in einer Müllverbrennungsanlage verbrannt.")
elif waste_type == 'Gelbe Tonne':
st.write("Der Plastikmüll aus der gelben Tonne wird recycelt und wiederverwendet.")
elif waste_type == 'Braune Tonne':
