import streamlit as st
import pandas as pd
import requests

def delete_data_from_db(id: int):
    response = requests.delete(url = f'http://127.0.0.1:8000/query/{id}')
    if response.status_code == 200:
        json_response = response.json()
        if json_response:
            return json_response
    else:
        return None

st.header("Delete Data From History")
delete_id = st.number_input("Enter the ID to delete", min_value=1)
if st.button("Delete"):
    deleted_data = delete_data_from_db(delete_id)  # Delete data by ID
    if deleted_data:
        df = pd.DataFrame([deleted_data])
        df.set_index(keys = 'id', inplace=True)
        df.drop(columns=['modified_on', 'created_on'], inplace=True)
        st.table(df)
    else:
        st.write("ID does not exists!")
