import streamlit as s

from datetime import time, datetime

s.header("s.Slider")

s.subheader('Slider')

age = s.slider('Ages?', 0, 100, 25)
s.write(f"I'm in {age} old")

s.subheader('Range slider')

values = s.slider(
     'Select a range of values',0, 10)
s.write('Values:', values)

s.subheader('Range time slider')

appointment = s.slider(
    'Schedule appointment',
    value=(time(11,30), time(12,45))
)
s.write(f"Your appoinment {appointment}")

s.subheader('Datetime slider')

start_time = s.slider(
     "When do you start?",
     value=datetime(2025, 12, 1, 0, 0 ),
     format="DD/MM/YY - hh:mm")
s.write("Start time:", start_time)