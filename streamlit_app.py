import streamlit as s
import pandas as p
import numpy as n
from datetime import time, datetime

s.header('Line Chart')

chart_data = p.DataFrame(
    n.random.rand(3,3),
    columns=['a','b','c']
)

s.line_chart(chart_data)