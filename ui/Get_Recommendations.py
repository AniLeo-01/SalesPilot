import streamlit as st
import requests

st.set_page_config(
    page_title="SalesPilot",
    page_icon="🚀",
)

st.title("SalesPilot🚀💹")

def fetch_recommendation(openai_key: str, query: str):
    params = {
        "user_data": {
            "chatgpt_api_key": openai_key
        },
        "input_data": {
            "query": query
        }
    }

    response = requests.post(url = 'http://127.0.0.1:8000/query', json=params)
    if response.status_code == 200:
        json_response = response.json()
        if json_response:
            return json_response['response']
    else:
        json_response = response.json()
        return json_response['detail']


st.header("User Credentials")
openai_api_key = st.text_input("OpenAI API Key", type="password")

st.header("Sales Transcript")
sales_transcript = st.text_area("Enter the Sales Transcript")
if st.button("Submit"):
    # Fetch the result and display the recommendation
    with st.spinner('Loading recommendation...'):
        recommendation = fetch_recommendation(openai_api_key, sales_transcript)
        st.text_area("Sales Recommendation", value=recommendation, height=100)

st.sidebar.success("Navigation Menu")


# Run the selected page

