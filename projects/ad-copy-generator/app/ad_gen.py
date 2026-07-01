import os
import anthropic
import streamlit as st
from pathlib import Path
from dotenv import load_dotenv

load_dotenv()


client = anthropic.Anthropic(api_key=os.getenv("MY_KEY"))


# Page Configuration
st.set_page_config(page_title="Ad Copy Generator",
                   page_icon=":fire:", layout="centered")


def load_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)


css_path = Path(__file__).parent / "styles.css"
load_css(css_path)

st.title(":fire: Ad Copy Generator :fire:")
st.caption("Generate professional ad copy for your product or service using AI!")


# Input Form
st.subheader("Enter your product or service details:", divider="gray")

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


# Creating The Function
def generate_ad(product, audience, features, discount, tone, platform):
    prompt = f"""You are the world's best marketing copywriter.

Generate a {tone.lower()} ad for the following product or service for {audience}.

Product / Service: {product}
Key Features: {features}
Discount: {discount if discount else 'None'}
Platform: {platform}


Write exactly 3 ad variants using the AIDA method. Each variant must follow this structure:

VARIANT 1:
HEADLINE:
BODY:
CTA:

VARIANT 2:
HEADLINE:
BODY:
CTA:

VARIANT 3:
HEADLINE:
BODY:
CTA:

Keep each variant concise and appropriate for {platform}. No placeholders, no extra commentary."""

    response = client.messages.create(
        model="claude-haiku-4-5",
        max_tokens=1000,
        messages=[{"role": "user", "content": prompt}]

    )
    return response.content[0].text


if st.button("Generate", type="primary"):
    if not product or not audience or not features:
        st.warning("Please fill in all required fields.")
    else:
        with st.spinner("Please Be Patient, Generating Your Ad... "):
            result = generate_ad(product, audience, features,
                                 discount, tone, platform)
            st.success("Ad copy generated successfully!")
            st.subheader("Here are your generated ads:")
            st.text(result)

            st.download_button(
                label="Download Your Ads",
                data=result,
                file_name="ad_copy.txt",
                mime="text/plain"
            )
