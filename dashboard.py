import streamlit as st
import pandas as pd
import numpy as np

st.title("dashboard title")
st.header("section header")
st.subheader("subsection")
st.write("markdown, numbers, dataframes, floats, strs")
st.markdown("**Hole** _hole_ 'code'")

name = st.text("Mode Name")
options =st.selectbox("Choose a model", ["CNN", "YOLO", "diffusion"])
threshold = st.slider("Confidence threshold", 0.0, 1.0, 1.5)
run_button = st.button("Run Inference")

df = pd.DataFrame(np.random.randn(20,3), columns=["a", "b", "c"])
st.dataframe(df)
st.line_chart(df)