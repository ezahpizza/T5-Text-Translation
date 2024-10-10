import streamlit as st
import numpy as np
from transformers import AutoTokenizer, AutoModelForSeq2SeqLM
from transformers import pipeline
import torch

import warnings
warnings.filterwarnings('ignore')

checkpoint = "ezahpizza/translation_model"
tokenizer = AutoTokenizer.from_pretrained(checkpoint)
model = AutoModelForSeq2SeqLM.from_pretrained(checkpoint)

translator = pipeline("translation_en_to_es", model=model, tokenizer=tokenizer)

text = st.text_area('Enter text to translate: use the format \"translate English to Spanish: [your text]\"')
button = st.button("Translate")


if text and button :
    y_pred =  translator(text)
    st.write("Summary: ",y_pred[0]['translation_text'])