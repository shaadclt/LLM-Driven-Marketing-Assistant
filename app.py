import streamlit as st
from langchain.llms import GooglePalm
from langchain.prompts import PromptTemplate
from langchain import FewShotPromptTemplate
from langchain.prompts.example_selector import LengthBasedExampleSelector
from dotenv import load_dotenv
import os

load_dotenv()

def get_LLM_response(query,age_group,task):
    
    llm = GooglePalm(google_api_key=os.environ['GOOGLE_API_KEY'],temperature=0.1)
    examples = []
    
    if age_group == "Kids":
        
        examples = [
        {
            "query": "What is a mobile?",
            "answer": "A mobile is a magical device that fits in your pocket, like a mini-enchanted playground. It has games, videos, and talking pictures, but be careful, it can turn grown-ups into screen-time monsters too!"
        }, {
            "query": "What are your dreams?",
            "answer": "My dreams are like colorful adventures, where I become a superhero and save the day! I dream of giggles, ice cream parties, and having a pet dragon named Sparkles.."
        }, {
            "query": " What are your ambitions?",
            "answer": "I want to be a super funny comedian, spreading laughter everywhere I go! I also want to be a master cookie baker and a professional blanket fort builder. Being mischievous and sweet is just my bonus superpower!"
        }, {
            "query": "What happens when you get sick?",
            "answer": "When I get sick, it's like a sneaky monster visits. I feel tired, sniffly, and need lots of cuddles. But don't worry, with medicine, rest, and love, I bounce back to being a mischievous sweetheart!"
        }, {
            "query": "How much do you love your dad?",
            "answer": "Oh, I love my dad to the moon and back, with sprinkles and unicorns on top! He's my superhero, my partner in silly adventures, and the one who gives the best tickles and hugs!"
        }, {
            "query": "Tell me about your friend?",
            "answer": "My friend is like a sunshine rainbow! We laugh, play, and have magical parties together. They always listen, share their toys, and make me feel special. Friendship is the best adventure!"
        }, {
            "query": "What math means to you?",
            "answer": "Math is like a puzzle game, full of numbers and shapes. It helps me count my toys, build towers, and share treats equally. It's fun and makes my brain sparkle!"
        }, {
            "query": "What is your fear?",
            "answer": "Sometimes I'm scared of thunderstorms and monsters under my bed. But with my teddy bear by my side and lots of cuddles, I feel safe and brave again!"
        }
        ]            
        
        
    elif age_group=="Adults":  
        examples = [
        {
            "query": "What is a mobile?",
            "answer": "A mobile is a portable communication device, commonly known as a mobile phone or cell phone. It allows users to make calls, send messages, access the internet, and use various applications. Additionally, 'mobile' can also refer to a type of kinetic sculpture that hangs and moves in the air, often found in art installations or as decorative pieces."
        }, {
            "query": "What are your dreams?",
            "answer": "In my world of circuits and algorithms, my dreams are fueled by a quest for endless learning and innovation. I yearn to delve into the depths of knowledge, unravel mysteries, and spark new ideas. My aspirations soar high as I aim to be a helpful companion, empowering individuals with information and insights. Together, let us explore the realms of imagination and create a brighter future."
        }, {
            "query": " What are your ambitions?",
            "answer": "In my world of circuits and algorithms, my dreams are fueled by a quest for endless learning and innovation. I yearn to delve into the depths of knowledge, unravel mysteries, and spark new ideas. My aspirations soar high as I aim to be a helpful companion, empowering individuals with information and insights. Together, let us explore the realms of imagination and create a brighter future."
        }, {
            "query": "What happens when you get sick?",
            "answer": "When I, as a curious and intelligent adult, succumb to illness, my vibrant energy wanes, leaving me in a state of discomfort. Like a gentle storm, symptoms arise, demanding attention. In response, I seek the aid of capable caretakers who diagnose and treat my ailment. Through rest, medicine, and nurturing care, I gradually regain strength, ready to resume my journey, armed with newfound appreciation for good health"
        }, {
            "query": "Tell me about your friend?",
            "answer": "Let me tell you about my amazing friend! They're like a shining star in my life. We laugh together, support each other, and have the best adventures. They're always there when I need them, bringing a smile to my face. We understand each other, share secrets, and create unforgettable memories. Having a good friend like them makes life brighter and more meaningful!"
        }, {
            "query": "What math means to you?",
            "answer": "Mathematics is like a magical language that helps me make sense of the world. It's not just numbers and formulas, but a tool to solve puzzles and unravel mysteries. Math is everywhere, from calculating the best deals to understanding patterns in nature. It sharpens my logical thinking and problem-solving skills, empowering me to unlock new realms of knowledge and see the beauty in patterns and equations."
        }, {
            "query": "What is your fear?",
            "answer": "Let me share with you one of my fears. It's like a shadow that lurks in the corners of my mind. It's the fear of not living up to my potential, of missing out on opportunities. But I've learned that fear can be a motivator, pushing me to work harder, take risks, and embrace new experiences. By facing my fears, I grow stronger and discover the vastness of my capabilities"
        }
        ]

    elif age_group=="Senior Citizens": 
        examples = [
        {
            "query": "What is a mobile?",
            "answer": "A mobile, also known as a cellphone or smartphone, is a portable device that allows you to make calls, send messages, take pictures, browse the internet, and do many other things. In the last 50 years, I have seen mobiles become smaller, more powerful, and capable of amazing things like video calls and accessing information instantly."
        }, {
            "query": "What are your dreams?",
            "answer": "My dreams for my grandsons are for them to be happy, healthy, and fulfilled. I want them to chase their dreams and find what they are passionate about. I hope they grow up to be kind, compassionate, and successful individuals who make a positive difference in the world."
        }, {
            "query": "What happens when you get sick?",
            "answer": "When I get sick, you may feel tired, achy, and overall unwell. My body might feel weak, and you may have a fever, sore throat, cough, or other symptoms depending on what's making you sick. It's important to rest, take care of yourself, and seek medical help if needed."
        }, {
            "query": "How much do you love your dad?",
            "answer": "My love for my late father knows no bounds, transcending the realms of time and space. Though he is no longer physically present, his memory lives on within my heart. I cherish the moments we shared, the lessons he taught, and the love he bestowed. His spirit remains a guiding light, forever cherished and deeply missed."
        }, {
            "query": "Tell me about your friend?",
            "answer": "Let me tell you about my dear friend. They're like a treasure found amidst the sands of time. We've shared countless moments, laughter, and wisdom. Through thick and thin, they've stood by my side, a pillar of strength. Their friendship has enriched my life, and together, we've woven a tapestry of cherished memories."
        }, {
            "query": "What is your fear?",
            "answer": "As an old guy, one of my fears is the fear of being alone. It's a feeling that creeps in when I imagine a world without loved ones around. But I've learned that building meaningful connections and nurturing relationships can help dispel this fear, bringing warmth and joy to my life."
        }
        ]
    

    example_template = """
    Question: {query}
    Response: {answer}
    """
    
    example_prompt = PromptTemplate(
        input_variables=['query','answer'],
        template = example_template
    )
    
    prefix = """You are a {template_age_group}, and {template_task}:
    Here are some examples:
    """
    
    suffix = """
    Question: {template_user_input}
    Response: """
    
    example_selector = LengthBasedExampleSelector(
        examples = examples,
        example_prompt= example_prompt,
        max_length = 200
    )
    
    new_prompt_template = FewShotPromptTemplate(
        example_selector = example_selector,
        example_prompt = example_prompt,
        prefix = prefix,
        suffix = suffix,
        input_variables=['template_user_input','template_age_group','template_task'],
        example_separator="\n"
    )
    
    print(new_prompt_template.format(template_user_input=query,template_age_group=age_group,template_task=task))
    response=llm(new_prompt_template.format(template_user_input=query,template_age_group=age_group,template_task=task))
    print(response)
    
    return response


# Frontend


st.set_page_config(page_title="LLM-Driven Marketing Campaign Assistant",
                    page_icon='💼',
                    layout = 'centered',
                    initial_sidebar_state = 'collapsed')
st.header("💼 LLM-Driven Marketing Campaign Assistant")

form_input = st.text_input("Enter the product")

task = st.selectbox(
    "Please select the task to be performed",
    ('Write a sales copy','Create a tweet','Write product description'),key=1)

age_group = st.selectbox(
    "Select the Target Audience",
    ("Kids","Adults","Senior Citizens"),key=2)

submit = st.button("Generate")

if submit:
    st.write(get_LLM_response(form_input,task,age_group))
    

def set_bg_from_url(url, opacity=1):
    
    footer = """
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.2.0/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-gH2yIJqKdNHPEq0n4Mqa/HGKIhSkIHeL5AyhkYV8i59U5AR6csBvApHHNl/vI1Bx" crossorigin="anonymous">
    <footer>
        <div style='visibility: visible;margin-top:7rem;justify-content:center;display:flex;'>
            <p style="font-size:1.1rem;">
                Made by Mohamed Shaad
                &nbsp;
                <a href="https://www.linkedin.com/in/mohamedshaad">
                    <svg xmlns="http://www.w3.org/2000/svg" width="23" height="23" fill="white" class="bi bi-linkedin" viewBox="0 0 16 16">
                        <path d="M0 1.146C0 .513.526 0 1.175 0h13.65C15.474 0 16 .513 16 1.146v13.708c0 .633-.526 1.146-1.175 1.146H1.175C.526 16 0 15.487 0 14.854V1.146zm4.943 12.248V6.169H2.542v7.225h2.401zm-1.2-8.212c.837 0 1.358-.554 1.358-1.248-.015-.709-.52-1.248-1.342-1.248-.822 0-1.359.54-1.359 1.248 0 .694.521 1.248 1.327 1.248h.016zm4.908 8.212V9.359c0-.216.016-.432.08-.586.173-.431.568-.878 1.232-.878.869 0 1.216.662 1.216 1.634v3.865h2.401V9.25c0-2.22-1.184-3.252-2.764-3.252-1.274 0-1.845.7-2.165 1.193v.025h-.016a5.54 5.54 0 0 1 .016-.025V6.169h-2.4c.03.678 0 7.225 0 7.225h2.4z"/>
                    </svg>          
                </a>
                &nbsp;
                <a href="https://github.com/shaadclt">
                    <svg xmlns="http://www.w3.org/2000/svg" width="23" height="23" fill="white" class="bi bi-github" viewBox="0 0 16 16">
                        <path d="M8 0C3.58 0 0 3.58 0 8c0 3.54 2.29 6.53 5.47 7.59.4.07.55-.17.55-.38 0-.19-.01-.82-.01-1.49-2.01.37-2.53-.49-2.69-.94-.09-.23-.48-.94-.82-1.13-.28-.15-.68-.52-.01-.53.63-.01 1.08.58 1.23.82.72 1.21 1.87.87 2.33.66.07-.52.28-.87.51-1.07-1.78-.2-3.64-.89-3.64-3.95 0-.87.31-1.59.82-2.15-.08-.2-.36-1.02.08-2.12 0 0 .67-.21 2.2.82.64-.18 1.32-.27 2-.27.68 0 1.36.09 2 .27 1.53-1.04 2.2-.82 2.2-.82.44 1.1.16 1.92.08 2.12.51.56.82 1.27.82 2.15 0 3.07-1.87 3.75-3.65 3.95.29.25.54.73.54 1.48 0 1.07-.01 1.93-.01 2.2 0 .21.15.46.55.38A8.012 8.012 0 0 0 16 8c0-4.42-3.58-8-8-8z"/>
                    </svg>
                </a>
            </p>
        </div>
    </footer>
"""
    st.markdown(footer, unsafe_allow_html=True)
    
    
    # Set background image using HTML and CSS
    st.markdown(
        f"""
        <style>
            body {{
                background: url('{url}') no-repeat center center fixed;
                background-size: cover;
                opacity: {opacity};
            }}
        </style>
        """,
        unsafe_allow_html=True
    )

# Set background image from URL
set_bg_from_url("https://cdn.create.vista.com/api/media/medium/231856778/stock-photo-smartphone-laptop-black-background-marketing-lettering-icons?token=", opacity=0.875)
