import sys
import inspect
import logging
from llama_index.core.agent import ReActAgent
from agent_models.models import get_language_model
from agent_tools.WebSearchTool import web_search_tools
from agent_tools.FileDownloaderTool import get_downloader_tool
from agent_tools.ImageReaderTool import get_image_interpreter_tool
from agent_tools.CalculatorTool import get_calculator_tool
from agent_tools.PandasTool import get_pandas_tool
from agent_prompts.SystemPrompt import gaia_system_prompt

#Logging
logging.basicConfig(stream=sys.stdout, level=logging.DEBUG)
logging.getLogger().addHandler(logging.StreamHandler(stream=sys.stdout))


# Agent Definition
class GaiaAgent:
    def __init__(self):
        # print(f"ReAct Agent signature--------------------------------------- \n {inspect.signature(ReActAgent.from_tools)} \n ReAct Agent signature--------------------------------------- \n" ) 
        list_of_search_tools = web_search_tools() 
        list_of_other_tools = [get_downloader_tool(), get_image_interpreter_tool(), get_calculator_tool(), get_pandas_tool()]
        
        self.llm = get_language_model()
        self.tools = list_of_search_tools + list_of_other_tools
        self.agent = ReActAgent.from_tools(tools=self.tools, llm=self.llm, context=gaia_system_prompt, verbose=True)

    async def __call__(self, question: str) -> str:
        response_object = self.agent.chat(question)
        full_response_text = str(response_object)

        final_answer_prefix = "FINAL ANSWER:"
        if final_answer_prefix in full_response_text:
            clean_answer = full_response_text.split(final_answer_prefix, 1)[1].strip()
            return clean_answer
        else:
            return full_response_text