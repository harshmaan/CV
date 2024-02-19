import streamlit as st
import numpy as np 
import pandas as pd
from PIL import Image
from streamlit_timeline import timeline
import plotly.express as px
import plotly.figure_factory as ff
import requests
import re
import io
import matplotlib.pyplot as plt
import streamlit.components.v1 as components
import tensorflow as tf

st.sidebar.caption('Wish to connect?')
st.sidebar.write('📧: maanharsh98@hotmail.com')
pdfFileObj = open('abc.pdf', 'rb')
st.sidebar.download_button('text_to_display',pdfFileObj,file_name='abc.pdf',mime='pdf')
