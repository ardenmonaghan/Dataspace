import duckdb
import os
from db_helpers.db_services import get_sample_rows
from db_helpers.db_metadata import get_dataset_by_id
from openai import OpenAI
import logging
import dotenv

# Currently use 
dotenv.load_dotenv()

class InsightAgent:
    def __init__(self, dataset_id: str):
        self.dataset_id = dataset_id
        self.dataset = None
        self.sample_rows = None
        self.system_prompt = None

    def run_simple_query(self, query: str):
        client = OpenAI()

        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {"role": "system", "content": "you are saying hello to someone, make a greeting"},
                {"role": "user", "content": query}
            ]
        )
        return response.choices[0].message.content

    def retrieve_dataset(self):
        '''
        Retrieve the metadata of the dataset from the database.
        '''
        # dataset object is returned from this call. 
        dataset = get_dataset_by_id(self.dataset_id)
        self.dataset = dataset
        return dataset

    def retrieve_sample_rows(self, table_name: str):
        '''
        Retrieve the sample rows of the dataset from the database.
        '''

        if table_name is None:
            raise ValueError("No table name provided.")

        if table_name not in self.dataset.tables:
            raise ValueError(f"Table {table_name} not found in the dataset.")

        sample_rows = get_sample_rows(self.dataset, 10, table_name)
        self.sample_rows = sample_rows

        return sample_rows

    def format_rows(sample_rows: list[dict[str, any]]) -> str:
        '''
        format rows is a function that formats the sample rows into a string.
        '''

        lines = []

    def build_system_prompt(self):
        '''
        build_system_prompt is a function that builds the system prompt for the agent to retrieve the insight of the data
        Args:
            None
        Returns:
            str - The system prompt for the agent.
        '''
        system_prompt = f"""
        System: “You are a data analyst. Given the dataset metadata, schema, and sample rows below, 
        write a short overview: what the dataset is about, what the main columns mean, 
        and 2–3 brief insights from the sample.

        ## Dataset metadata:
        - dataset_id: {self.dataset.dataset_id}
        - upload_type: {self.dataset.upload_type}
        - raw_byte_size: {self.dataset.raw_byte_size}
        - tables: {", ".join(self.dataset.tables)}

        ## Schema:
        {self.dataset.schema}

        ## Sample rows:
        {self.sample_rows}
        """

        print(system_prompt)
        self.system_prompt = system_prompt

    def run_agent(self):

        client = OpenAI()
        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {"role": "system", "content": self.system_prompt},
                {"role": "user", "content": "Write a short overview of what the dataset is about, what the main columns mean, and 2–3 brief insights from the sample."}
            ]
        )
        return response.choices[0].message.content

    def run_full_agent(self, dataset_id: str, table_name: str):

        self.retrieve_dataset(dataset_id)
        self.retrieve_sample_rows(table_name)
        self.build_system_prompt()
        return self.run_agent()

if __name__ == "__main__":
    # insight_agent = InsightAgent("d2808899-d2ab-405c-82e0-3e34c5517913")

    # insight_agent.retrieve_dataset()
    # insight_agent.retrieve_sample_rows("ins_feat")
    # insight_agent.build_system_prompt()

    response = InsightAgent("d2808899-d2ab-405c-82e0-3e34c5517913").run_full_agent("d2808899-d2ab-405c-82e0-3e34c5517913", "ins_feat")


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

# Use Amazon Bedrock for data privacy
