import streamlit as st
import pandas as pd
import requests

def fetch_data_from_db():
    response = requests.get(url = 'http://127.0.0.1:8000/query')
    if response.status_code == 200:
        json_response = response.json()
        if json_response:
            return json_response
    else:
        return None



st.header("Data History")
data = fetch_data_from_db()  # Fetch data from the database
if data:
    # Display the table
    df = pd.DataFrame(data)
    df.set_index(keys = 'id', inplace=True)
    df.drop(columns=['modified_on', 'created_on'], inplace=True)
    st.table(df)
else:
    st.write("No history found!")


