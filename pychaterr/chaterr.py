import inspect
import os
import re
import sys
import traceback

import openai
from openai import ChatCompletion

from rich.console import Console
from rich.markdown import Markdown



openai.api_key = os.getenv("OPENAPI_API_KEY")

PYCHATERR_RE = re.compile("^(import pychaterr|from pychaterr import .*)$", re.MULTILINE)

PROMPT = """
You are a chatbot, act as an instructor, teaching errors in Python code to beginners.
I will give you code and exceptions and you will provide explanations and solutions.
Reply in Markdown with Python code blocks.
"""


def chat_exception_hook(type, value, tb):
    """Exception hook.

    Args:
        type (type): Exception type
        value (Exception): Exception instance
        tb (Traceback): Traceback object
    """
    stack_call = "".join(traceback.format_tb(tb))
    code = PYCHATERR_RE.sub("", inspect.getsource(tb))

    response = ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {
                "role": "system",
                "content": PROMPT,
            },
            {
                "role": "user",
                "content": f"{stack_call} {code}",
            },
        ],
    )

    result = [choice.message.content for choice in response.choices]

    console = Console()
    content = Markdown("".join(result))
    console.print(content)


def setup_handler():
    """Setup general exception handler and enable ChatGTP error processing."""
    if sys.excepthook != chat_exception_hook:
        sys.excepthook = chat_exception_hook