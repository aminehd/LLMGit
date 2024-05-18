import functools
from typing import Any, Optional, Union
from dsp.modules.lm import LM
from dotenv import load_dotenv
from groq import Groq
import os

load_dotenv()

qroq_api_key = os.getenv("QROQ_API_KEY")

# TODO: Ideally, this takes the name of the index and looks up its port.


class Grok(LM):
    """Wrapper for the Grok Calls."""

    def __init__(
        self,
        url: str = "http://0.0.0.0",
        model: str = "llama3-8b-8192",
        post_requests: bool = False,
    ):
        self.url = url
        self.client = Groq(api_key=qroq_api_key)
        self.model = model

    # TODO: Implementation of abstractmethod from LM class 
    # See https://github.com/stanfordnlp/dspy/blob/61fd5ccd0307f54e48e4b09fbaf61b26cca0d63e/dsp/modules/google.py#L109 for an example
    def basic_request(self, prompt, **kwargs):
        pass

    def __call__(
        self, prompt:str
    ) :
        """Call Grok API with the given prompt."""
        # https://console.groq.com/docs/quickstart
        chat_completion = self.client.chat.completions.create(
            messages=[
                {
                    "role": "user",
                    "content": prompt,
                }
            ],
            model=self.model,
        )
        return chat_completion.choices[0].message.content
