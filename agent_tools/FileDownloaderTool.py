import requests
import os
from llama_index.core.tools import FunctionTool

BASE_API_URL = "https://agents-course-unit4-scoring.hf.space" 

def download_file(task_id: str, file_name: str) -> str:
    """
    Downloads a file for a given task_id from the GAIA API.
    Args:
        task_id (str): The ID of the task to download the file for.
        file_name (str): The name to save the file as.
    Returns:
        str: The local path to the downloaded file.
    """

    print(f"Attempting to download file for task: {task_id}")

    # 1. Construct the full URL for the file endpoint.
    file_url = f"{BASE_API_URL}/files/{task_id}"

    # 2. Define the local directory to save downloads.
    download_dir = "downloads"
    os.makedirs(download_dir, exist_ok=True)

    # 3. Construct the full local path for the file.
    local_filepath = os.path.join(download_dir, file_name)

    # 4. Make a GET request to the file_url.
    try:
        response = requests.get(file_url, timeout=20)
        # This will raise an exception for bad status codes (like 404).
        response.raise_for_status() 

        # 5. Save the content of the response to the local file.
        with open(local_filepath, 'wb') as f:
            f.write(response.content)

        print(f"Successfully downloaded file to: {local_filepath}")
        
        # 6. Return the local file path.
        return local_filepath

    except requests.exceptions.RequestException as e:
        error_message = f"Failed to download file for task {task_id}. Error: {e}"
        print(error_message)
        return error_message


# Wrapper function to create the tool
def get_downloader_tool() -> FunctionTool:
    return FunctionTool.from_defaults(
        fn=download_file,
        name="file_downloader",
        description="A tool to download files associated with a specific task ID. Use this when a question mentions an image, audio file, or other document."
    )