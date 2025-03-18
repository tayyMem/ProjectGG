import streamlit as st
from transformers import T5ForConditionalGeneration, T5Tokenizer
import torch

repo_name = "TayyMem/ProjectGG_Testing3"

# Load model and tokenizer from Hugging Face
#ref for below https://docs.streamlit.io/get-started/tutorials/create-an-app
def model_load_function():
	tokenizer = T5Tokenizer.from_pretrained(repo_name)
	model = T5ForConditionalGeneration.from_pretrained(repo_name)
	# # Define the device
	# # If a GPU is available, it will use the GPU. Otherwise, it will use the CPU.
	device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
	return tokenizer, model, device
tokenizer, model, device = model_load_function()

st.divider() 
#st.caption("You can paste/write your sentence below.")

text = st.text_area("You can paste/write your sentence here for us to make correction.", value="", height=None, max_chars=None, key=None, help=None, on_change=None, args=None, kwargs=None, disabled=False, label_visibility="visible")

if st.button("**Let's begin checking!!**"):
    if text.strip():
        # Tokenizing input
        testing_input = tokenizer(text,max_length=256,truncation=True,padding=True,return_tensors='pt').to(device)

        # Generating correction
        testing_output = model.generate(input_ids= testing_input["input_ids"],attention_mask= testing_input["attention_mask"],max_length=256) # A way to predict data        

        # Decoding output
        corrected_sentences = tokenizer.decode(testing_output[0],skip_special_tokens=True) 
        st.write(f":red[**Your sentence is:**] {text}")
        st.write(f":green[**Correction is :**] :blue-background[{corrected_sentences}]")
        st.balloons()
    else:
        st.warning("Please enter a sentence to correct.")
