import streamlit as st
import nltk
from transformers import pipeline
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

#Download necessary NLTK data
nltk.download('punkt')
nltk.download('stopwords')

#Load a pre trained Hugging Face model
chatbot = pipeline("text-generation",model='distilgpt2')

#Define healthcare-specific response logic
def healthcare_chatbot(user_input):
    #Simple rule-based keywords to responses.
    if "syntoms" in user_input:
        return("I am an AI Chatbot, please consult a doctor for accurate advice.")
    elif "Appointment" in user_input:
        return("Would you like to schedule an appointment with a doctor ? ")
    elif "Medication" in user_input:
        return("It's important to take the prescribed medicines regularly as per the doctors advice.")
    else:
        #For other inputs,use the hugging face model to generate the response
        response = chatbot(user_input,max_length=500,num_return_sequences=1)
        #specifies the maximum length of the generated text response,including the input and generated tokens
        #If set to 3,the model generates three different possible responses,based on the given input
        return response[0]['generated_text']

#Steramlit web app interface
def main():
    #Set up the web app title and input area
    st.title("Healthcare Assistant Chatbot")

    #Display a simple text input for the queries
    user_input = st.text_input("How can I assist you today???")

    #Display chatbot response
    if st.button("Submit"):
        if user_input:
            st.write("User:  ",user_input)
            with st.spinner("Processing your query................This may take a while.........."):
                response = healthcare_chatbot(user_input)
            st.write("Healthcare Assistant : ",response)
            print(response)
        else:
            st.write("Please Enter a message to get a response.")

main()

