import streamlit as s
import pandas as p
import numpy as n
from datetime import time, datetime

s.header("Select Box")

option = s.selectbox(
    label="cars",
    options=['BMW', "Toyota", "Hyundai"],
    index=2
)

s.write(f"You choose {option}")