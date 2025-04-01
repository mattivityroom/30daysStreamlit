import streamlit as st

st.header('button')

if st.button('Say hello', key='welcoming', use_container_width=True, type="primary"):
    st.write('Well, hello there')
else:
    st.write('Goodbye')

if st.button("Drop me", key='droping'):
    st.write("Dropped")
else:
    st.write("Not Dropped")