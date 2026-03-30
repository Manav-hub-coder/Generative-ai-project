import streamlit as st
import requests
import pandas as pd
import plotly.express as px

st.title("GenAI BI Copilot")

query = st.text_input("Ask your data question:")

if st.button("Run Query"):
    response = requests.post("http://localhost:8000/query", json={"question": query})
    print(response.status_code)
    print(response.text)
    result = response.json()

    st.subheader("Generated SQL")
    st.code(result['sql'])

    df = pd.DataFrame(result['data'])
    st.subheader("Data")
    st.dataframe(df)

    if not df.empty:
        fig = px.bar(df, x=df.columns[0], y=df.columns[1])
        st.plotly_chart(fig)

    st.subheader("Insights")
    st.write(result['insights'])