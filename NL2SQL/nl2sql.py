from openai import OpenAI
from api.pipeline import call_sql_query
from nl2sql import nl2sql_prompt
client= OpenAI(api_key = api_key)
def call_sql_query(input, prompt):
    llm = client.chat.completions.create(
        model = "gpt-4o-mini",
        messages = [
            {"role": "system", "content": "You are an expert in generating MYSQL Query"},
            {"role": "user", "content": nl2sql_prompt.format(question = call_sql_query) }
        ]
    )
    
    response = llm.response
    