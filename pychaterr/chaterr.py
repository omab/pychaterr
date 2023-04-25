import inspect
import os
import sys
import traceback

import openai


openai.api_key = os.getenv("OPENAPI_API_KEY")


def chat_exception_hook(type, value, tb):
    """Exception hoook.

    Args:
        type (type): Exception type
        value (Exception): Exception instance
        traceback (Traceback): Traceback object
    """
    stack_call = "".join(traceback.format_tb(tb))
    code = inspect.getsource(tb)

    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {
                "role": "system",
                "content": "You are a chatbot",
            },
            {
                "role": "user",
                "content": "Explain why this Python exception happens and propose a solution",
            },
            {
                "role": "user",
                "content": f"{stack_call} {code}",
            },
        ],
    )

    result = [choice.message.content for choice in response.choices]
    print("".join(result))


def setup_handler():
    """Setup general exception handler and enable ChatGTP error processing."""
    if sys.excepthook != chat_exception_hook:
        sys.excepthook = chat_exception_hook