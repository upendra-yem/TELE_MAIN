from llm_router import router_prompt
from query_trans import spell_correct, map_domain, rewrite_query
from openai import OpenAI, api_key
input_data = spell_correct(input_data)
input_data = map_domain(input_data)
rre_output = rewrite_query(input_data)
def route_query(input_data):
    client= OpenAI(api_key = api_key)
    response = client.chat.completions.create(
        model = "gpt-4o-mini",
        messages = [
            {"role": "system", "content": "You are an intelligent Query Router for an AI-powered Fleet Intelligence Platform."},
            {"role": "user", "content": router_prompt.format(input_data=input_data)}
        ]
    )
    return response
route_output = route_query(input_data)
def redirect_pipeline(input):
    if input['pipeline'] == "BOTH" and input['sql_query'] != "null" and input['rag_query'] != "null":
        pass    
    elif input['pipeline'] == "NL2SQL" and input['sql_query'] != "null":
        #call NL2SQL Pipeline in schema_rag folder
        pass
    elif input['pipeline'] == "RAG" and input['rag_query'] !="null":
        #call rag pipeline in advisory_rag folder
        pass
redirect_pipeline(route_output) 





