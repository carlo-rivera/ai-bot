from litellm import completion

def llm_call(model: str, messages: list):
    return completion(model=model, messages=messages, num_retries=2)