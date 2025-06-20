import pandas as pd
from llama_index.experimental.query_engine import PandasQueryEngine
from llama_index.core.tools import FunctionTool
from agent_models.models import get_language_model 

def analyze_spreadsheet(file_path: str, question: str) -> str:
    """
    Analyzes a spreadsheet (Excel/CSV) to answer a specific question about its data.
    This is a powerful tool for data analysis on structured files.
    Args:
        file_path (str): The local path to the .xlsx or .csv file.
        question (str): The question to ask about the data in the file.
    """
    print(f"Analyzing spreadsheet '{file_path}' for question: '{question}'")
    try:
        # Load the spreadsheet into a Pandas DataFrame
        df = pd.read_excel(file_path)
        
        # The PandasQueryEngine needs a LLM to translate natural language into Pandas commands.
        llm = get_language_model()
        
        # Create the query engine
        query_engine = PandasQueryEngine(df=df, llm=llm, verbose=True)
        
        # Ask the question and get the response
        response = query_engine.query(question)
        
        return str(response)

    except Exception as e:
        return f"Error analyzing spreadsheet: {e}"

# Wrapper function to create the LlamaIndex tool
def get_pandas_tool() -> FunctionTool:
    return FunctionTool.from_defaults(
        fn=analyze_spreadsheet,
        name="spreadsheet_analyzer",
        description="A tool to answer questions about data stored in a spreadsheet (.xlsx or .csv). It takes two arguments: the 'file_path' to the spreadsheet and the 'question' to ask about the data."
    )