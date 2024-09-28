from llm_factory import get_llm
from reader import read_json

change_subscription_prompt = ""

incomplete_info_prompt = ""

normal_prompt = ""

llm = get_llm()

def change_subscription(llm, prompt, history={}, plans={}):
    return llm.query(prompt + f"History: {history}" + f"Plans: {plans}")

def incomplete_info(llm, prompt, history={}):
    return llm.query(prompt + f"History: {history}")

def normal(llm, prompt, user_query, prompt_type):
    template = read_json("support_ro.json")
    answer_template = template[prompt_type]
    return llm.query(prompt + f"User Query: {user_query}" + f"Response Template: {answer_template}")

def answer_based_on_type(user_query, prompt_type):
    match(prompt_type):
        case "SCHIMB DE ABONAMENT":
            return change_subscription(llm, change_subscription_prompt, {}, {})
        case "DONT KNOW":
            return incomplete_info(llm, incomplete_info_prompt, {})
        case _:
            return normal(llm, normal_prompt, user_query, prompt_type)