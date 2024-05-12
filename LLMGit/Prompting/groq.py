import functools
from typing import Any, Optional, Union
from dsp.modules.lm import LM

# TODO: Ideally, this takes the name of the index and looks up its port.


class Grok(LM):
    """Wrapper for the Grok Calls."""

    def __init__(
        self,
        url: str = "http://0.0.0.0",
        post_requests: bool = False,
    ):
        self.url = url

    # TODO: Implementation of abstractmethod from LM class 
    # See https://github.com/stanfordnlp/dspy/blob/61fd5ccd0307f54e48e4b09fbaf61b26cca0d63e/dsp/modules/google.py#L109 for an example
    def basic_request(self, prompt, **kwargs):
        pass

    def __call__(
        self, prompt:str
    ) :

        return "not implemented yet"
