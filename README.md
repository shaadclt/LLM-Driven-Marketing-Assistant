# LLM-Driven Marketing Campaign Assistant

## Overview

This project is a Streamlit-based application that utilizes a language model (LLM - Language Model) to assist in generating marketing content for different age groups. The application allows users to input a product, select a marketing task (e.g., writing sales copy, creating a tweet, or writing a product description), and choose a target audience age group (Kids, Adults, or Senior Citizens).

## Features

- **Dynamic Content Generation:** The application dynamically generates marketing content using a language model tailored to specific age groups.
- **Example-Based Templates:** Examples are provided for each age group to guide the content generation process.
- **Streamlit Interface:** The user interacts with the application through a user-friendly Streamlit interface.

## Getting Started

### Prerequisites

- Python 
- Install the required packages by running: `pip install -r requirements.txt`

### Usage

1. Clone the repository:

   ```bash
   git clone https://github.com/shaadclt/LLM-Driven-Marketing-Campaign-Assistant.git
   ```

2. Navigate to the project directory:

   ```bash
   cd LLM-Driven-Marketing-Campaign-Assistant
   ```

3. Set up your environment variable:

   Update the values in the '**.env**' file, especially the **'GOOGLE_API_KEY'** required for the GooglePalm language model.

4. Run the application:

   ```bash
   streamlit run app.py
   ```

5. Access the application in your web browser at [http://localhost:8501](http://localhost:8501).


