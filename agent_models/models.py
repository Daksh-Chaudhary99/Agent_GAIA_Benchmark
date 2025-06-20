import os
from llama_index.llms.nebius import NebiusLLM
from llama_index.llms.huggingface_api import HuggingFaceInferenceAPI
from openai import OpenAI

# NebiusAI API Key
os.environ["NEBIUS_API_KEY"] = ""

# Model config variable
llm_Id = "Qwen/Qwen2.5-32B-Instruct"

def get_language_model():
    '''Initializes and returns the LLM for Agent's core functionality'''
    return NebiusLLM(api_key=os.getenv("NEBIUS_API_KEY"), model=llm_Id) # To use HuggingFaceInferenceAPI -> return HuggingFaceInferenceAPI(model_name=llm_Id)

def get_vision_model_client():
    '''Initializes and returns the vision model for analyzing images'''
    
    return OpenAI(
        api_key=os.getenv("NEBIUS_API_KEY"),
        base_url="https://api.studio.nebius.com/v1/"
    )