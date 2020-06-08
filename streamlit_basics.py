import streamlit as st
import datetime
import time
import pandas as pd
import numpy as np


# title
st.title('Streamlit Basics')

# header
st.header('header')
st.subheader('subheader')

# text
st.text('regular text')

# markdown
st.markdown('## markdown text')

# color text
st.success('Success!')

# misc
st.info('Info')

st.warning('Warning!')

st.error('Error code: ')

st.exception('Name not defined')

# sidebars
st.sidebar.header('Sidebar')
st.sidebar.text('table of content')


# widgets

# checkbox
st.checkbox('yes/no')

# radio buttion
st.radio('yes/no', ('yes', 'no'))

# select box
selected = st.selectbox('select', ['yes', 'no', 'dont know'])
st.write('option selected: ', selected)

# multiselect
st.multiselect('select shape: ', ('Square', 'Triangle', 'Circle'))

# slider
st.slider('Select number between 1 and 10: ', 1, 10)

# text input
st.text_input('Input text here: ', 'type here')

# date
st.date_input('The date is ', datetime.datetime.now())

# time input
st.time_input('The time is ', datetime.time())


# progress bar
bar = st.progress(0)
for i in range(100):
    time.sleep(0.01)
    bar.progress(i+1)

# display data
# single line code
st.code('import pandas as pd')

# section code
with st.echo():
    import pandas as pd
    import numpy as np 
    import datetime as dt 
    import matplotlib.pyplot as plt 
    import seaborn as sns


# plots
arr = np.random.normal(1, 1, size=100)
plt.hist(arr, bins=20)
st.pyplot()

# dataframe
df = pd.DataFrame(np.random.randn(5, 5), columns=('col_%d' % i for i in range(5)))
st.dataframe(df)

# table()
st.table(df)


