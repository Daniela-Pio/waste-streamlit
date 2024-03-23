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
 st.warning('Select the desired waste bin and you will receive information about the recycling process.')


# Load data
data = pd.DataFrame({
    'Mülltonne': ['Black bin', 'Yellow bin', 'Organic bin', 'Glass container', 'Paper container'],
    'Plastic': [0, 48, 0, 0, 0],
    'Problematic substances': [1, 0, 0, 0, 0],
    'Residual waste': [32.60, 28, 0, 0, 0],
    'Recyclable material': [27.60, 10, 0, 0, 0],
    'Composite': [0, 10, 0, 0, 0],
    'Organic waste': [39.30, 27.6, 100, 0, 0],
    'Metals': [0, 14, 0, 0, 0]
})

# Input widgets
## Bin selection
waste_type = st.selectbox('Select Trash bin', data['Mülltonne'])

if waste_type not in ['Organic bin', 'Glass container', 'Paper container']:
    selected_data = data[data['Mülltonne'] == waste_type].melt(var_name='Components', value_name='Procent')

    # Filter out rows where Procent is equal to zero
    selected_data = selected_data[selected_data['Procent'] != 0]

    if not selected_data.empty:
        # Display chart
        chart = alt.Chart(selected_data).mark_bar().encode(
            x='Procent:Q',
            y='Components:N'
        ).properties(
            width=600,
            height=400
        )

        st.altair_chart(chart)


#Infotext
if waste_type == 'Black bin':
 st.write("The waste from the black garbage can is incinerated in a waste incineration plant - only a small proportion goes to mechanicalbiogical.")
elif waste_type == 'Yellow bin':
 st.write("The plastic waste from the yellow garbage can is recycled and reused. Only 31% of the plastic waste generated ends up in the recycling yard, resulting in 509 kilotons of new raw material. Composite waste produces 125 kilotons of new raw material and the reprocessing of metals produces 250 kilotons of new raw material. Everything that was sorted incorrectly is incinerated.")
elif waste_type == 'Organic bin':
 st.write("The organic waste from the brown garbage can is turned into compost in composting plants as a substitute for mineral fertilizer.")
elif waste_type == 'Glass container':
  st.write("The used glass is sorted and reused to produce new raw materials approx. 84% of the used glass is reused.")
elif waste_type == 'Paper container':
  st.write("The waste paper and cardboard is used to produce new raw materials approx. 77%.")
