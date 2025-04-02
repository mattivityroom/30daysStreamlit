import streamlit as st
import numpy as np
import pandas as pd
import altair as alt


st.header("st.write")

st.subheader("Display Text")
st.write("Hello world! 👾")

st.subheader("Display numbers")
st.write(1234)

st.subheader("Display DataFrame")
df = pd.DataFrame({
    'first column': [1,2,3,4],
    'second column': [10,20,30,40]
})
st.write(df)

st.subheader("Accept multiple arguments")
st.write('Bellow is data frame', df, 'Above is dataframe')

st.subheader("Display Chart")
df2 = pd.DataFrame(
    np.random.randn(5, 3),
    columns=['a', 'b', 'c'])
c = alt.Chart(df2).mark_circle().encode(
    x='a', y='b', size='c', color='c', tooltip=['a', 'b', 'c'])
st.write(c)