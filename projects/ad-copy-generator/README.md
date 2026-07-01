# Ad Copy Generator

A Streamlit app that generates professional ad copy using Claude AI. Enter a product, audience, and tone, and get three ready-to-use ad variants in seconds.

---

## Overview

This project started as a local LLM experiment using TinyLlama and later Gemma-2b, both of which struggled to follow prompt instructions and produce usable ad copy. The final version upgrades to the Claude API, which reliably follows structured output formatting and produces professional results.

The app is built for any product or service, not tied to a single brand, making it a general-purpose ad generation tool.

---

## Features

- Product, audience, features, and promotion input fields
- Tone selection (Professional, Casual, Funny, Inspirational, Urgent, Minimalist)
- Platform selection (Facebook, Instagram, Email, LinkedIn, Google Search Ad)
- Generates 3 ad variants per request, each with a headline, body, and CTA
- Download button to save generated copy as a text file
- Custom styled UI

---

## Tech Stack

- Python
- Streamlit
- Anthropic API (Claude Haiku)
- python-dotenv

---

## How to Run

Clone the repository and install dependencies:

```bash
git clone https://github.com/NewManRising/the-builder-forge
cd ad-copy-generator
pip install -r requirements.txt
```

Create a `.env` file in the project root and add your Anthropic API key:

```
ANTHROPIC_API_KEY=your_key_here
```

Run the app:

```bash
streamlit run app/ad_gen.py
```

---

## Folder Structure

```text
ad-copy-generator/
│
├── notebooks/
│   └── bikeease_genai_ad.ipynb   # Early prompt engineering with local LLMs
│
├── app/
│   ├── ad_gen.py                 # Streamlit app
│   └── styles.css                # Custom UI styling
│
├── .env.example
├── .gitignore
├── README.md
└── requirements.txt
```

---

## Future Improvements

- Add a regenerate button without needing to resubmit the full form
- Save generation history within a session
- Compare output across multiple LLMs side by side
- Add character count per variant for platform-specific limits
