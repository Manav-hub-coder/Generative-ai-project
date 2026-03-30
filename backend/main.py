from fastapi import FastAPI
from pydantic import BaseModel
from sqlalchemy import create_engine, text
import pandas as pd
from llm_handler import generate_sql, generate_insights

app = FastAPI()

engine = create_engine("sqlite:///../database/data.db")

class QueryRequest(BaseModel):
    question: str

@app.post("/query")
def query_data(req: QueryRequest):
    sql_query = generate_sql(req.question)
    
    with engine.connect() as conn:
        result = conn.execute(text(sql_query))
        df = pd.DataFrame(result.fetchall(), columns=result.keys())

    insights = generate_insights(df)

    return {
        "sql": sql_query,
        "data": df.to_dict(orient="records"),
        "insights": insights
    }