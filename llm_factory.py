from reader import get_config
from GroqLLM import GroqLLM
from ServerLLM import ServerLLM

def get_llm(llm=None):
    if llm == None:
        llm = get_config("llm")
    llm = llm.lower()

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
