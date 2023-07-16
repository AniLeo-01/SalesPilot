# SalesPilot🚀💹

A sales assistant chatbot giving recommendation to different sales transcription based on the sales objection using GPT-3.5 model.

### Installation

1. Clone the github repository.
2. Create a database in Postgresql and copy the credentials to the ``.env.staging`` file under environments in api

   ```
   DB_URL=postgresql+asyncpg://<USER>:<PASSWORD>@localhost:5432/<DATABASE_NAME>
   ```
3. Start the uvicorn server

   ```
   uvicorn api.main:app --workers 1 --host 0.0.0.0 --port 8000
   ```
4. In another terminal, start the streamlit server

   ```
   streamlit run Get_Recommendations.py
   ```
