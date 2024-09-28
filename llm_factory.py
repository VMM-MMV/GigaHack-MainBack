from reader import get_sys_env
from GroqLLM import GroqLLM
from ServerLLM import ServerLLM

def get_llm(llm_name=None):
    llm = get_sys_env("LLM")
    llm = llm.lower()
    
    if llm_name != None:
        llm = llm_name.lower()

    match(llm):
        case "grok":
            return GroqLLM()
        case "server":
            return ServerLLM()
        case _:
            assert False, "Not impleemented"

if __name__ == "__main__":
    llm = get_llm()
    a = llm.query("What is the capital of Moldova")
    print(a)
