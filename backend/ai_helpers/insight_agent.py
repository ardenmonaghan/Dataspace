import duckdb
import os
from db_helpers.db_services import get_dataset_by_id
from openai import OpenAI
import dotenv

# Currently use 
dotenv.load_dotenv()

class InsightAgent:
    def __init__(self, dataset_id: str):
        self.dataset_id = dataset_id

    def run_query(self, query: str):
        client = OpenAI()

        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {"role": "system", "content": "you are saying hello to someone, make a greeting"},
                {"role": "user", "content": query}
            ]
        )
        return response.choices[0].message.content


if __name__ == "__main__":
    print(get_dataset_by_id("123"))
    print(InsightAgent("123").run_query("Hello, how are you?"))

# python3 -m ai_helpers.insight_agent

## Dataset metadata
# - dataset_id: abc-123
# - upload_type: csv
# - raw_byte_size: 1024000
# - tables: creditcard (1 table)

## Schema
# Table: creditcard
# - Time (BIGINT)
# - V1 (DOUBLE)
# - Class (BIGINT)
# ...

## Sample rows (first 100)
# Time,V1,V2,...,Class
# 0,-1.3598,-0.07278,...,0
# ...

# System: "System: “You are a data analyst. Given the dataset metadata, schema, and sample rows below, write a short overview: what the dataset is about, what the main columns mean, and 2–3 brief insights from the sample."

# Use Amazon Bedrock for data privacy
