import streamlit as st

st.title(':blue[Find the largest among of 3 Numbers]')

n1 = st.number_input(':green[Enter a number]')

n2 = st.number_input(':green[Enter the second number]')

n3 = st.number_input(':green[Enter the third number]')

if n1 >= n2 and n1 >= n3:
    ans = n1
elif n2 >= n3 and n2 >= n1:
    ans = n2
else:
    ans = n3

if st.button(":red[Submit]"):
    st.write(':orange[_The Greatest of the 3 numbers you\'ve inputed is:_]', ans)
