
import streamlit as st 
import numpy as np 
import pandas as pd
from PIL import Image
import plotly.express as px
import plotly.figure_factory as ff
import requests
import re
import plotly.graph_objects as go
import io
import matplotlib.pyplot as plt
import streamlit.components.v1 as components
from graph_builder import *
#import tensorflow as tf
from streamlit_player import st_player

st.sidebar.caption('Wish to connect?')
st.sidebar.write('📧: maanharsh98@hotmail')

pdfFileObj = open('pdfs/CV - Harsh - 2014.pdf', 'rb')
st.sidebar.download_button('download resume',pdfFileObj,file_name='CV - Harsh - 2014.pdf',mime='pdf')
