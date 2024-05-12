
from LLMGit.Prompting.groq import Grok

def test_grok_llm_call_works():
    groq = Grok('wwww.grok.come')
    assert groq.__call__('what is height of everest') != 'not implemented yet'