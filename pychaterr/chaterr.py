import inspect
import os
import sys
import traceback

import openai


# # TODO: remove api key
# openai.api_key = os.getenv("OPENAPI_API_KEY")

# response = openai.ChatCompletion.create(
#     model="gpt-3.5-turbo",
#     messages=[
#         {
#             "role": "system",
#             "content": "You are a chatbot",
#         },
#         {
#             "role": "user",
#             "content": "Why should DevOps engineer learn kubernetes?",
#         },
#     ],
# )

# result = ""
# for choice in response.choices:
#     result += choice.message.content


def chat_exception_hook(type, value, tb):
    """Exception hoook.

    Args:
        type (type): Exception type
        value (Exception): Exception instance
        traceback (Traceback): Traceback object
    """
    stack_call = "".join(traceback.format_tb(tb))
    code = inspect.getsource(tb)



def setup_handler():
    """Setup general exception handler and enable ChatGTP error processing."""
    if sys.excepthook != chat_exception_hook:
        sys.excepthook = chat_exception_hook