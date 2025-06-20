import os
from typing import List
from llama_index.core.tools import FunctionTool
from llama_index.tools.tavily_research import TavilyToolSpec

def web_search_tools()->List[FunctionTool]:
    "Tool to search the web with Tavily (search + scraping)"

    os.environ["TAVILY_API_KEY"] = ""
    tavily_spec = TavilyToolSpec(api_key=os.getenv("TAVILY_API_KEY"))
    return tavily_spec.to_tool_list()