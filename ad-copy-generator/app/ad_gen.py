import os
import anthropic
import streamlit as st
from dotenv import load_dotenv

load_dotenv()


client = anthropic.Anthropic(api_key=os.getenv("MY_KEY"))


# Page Configuration
st.set_page_config(page_title="Ad Copy Generator",
                   page_icon=":writing_hand:", layout="centered")

st.title(":fire: Ad Copy Generator :fire:")
st.caption("Generate professional ad copy for your product or service using AI!")


# Input Form
st.subheader("Enter your product or service details:", divider=True)

product = st.text_input("Product / Service",
                        placeholder="e.g. Electric bike rental")
audience = st.text_input(
    "Target Audience", placeholder="e.g. Urban commuters aged 25-40")
features = st.text_area("Features / Benefits",
                        placeholder="e.g. Lightweight, Eco-friendly, cost-effective, convenient")
discount = st.text_input("Promotion or Offer (optional)",
                         placeholder="e.g. 20% off first rental")
tone = st.selectbox("Tone", ["Professional", "Casual",
                    "Funny", "Inspirational", "Urgent", "Minimalist"])
platform = st.selectbox(
    "Platform", ["Facebook", "Instagram", "Email", "LinkedIn", "Google Search Ad"])
