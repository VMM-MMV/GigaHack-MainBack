from llm_factory import get_llm
from reader import read_json

change_subscription_prompt = "You are a professional customer assistant, given the following general subscription plans available at the company, and the users desires, and requirements you must give him relevant advice on which plan suits him better."

incomplete_info_prompt = "Task: Formulate a single, additional question in Romanian that will help pinpoint the issue the user is encountering, using as much of the already available information as possible. The question must be directly relevant to the user's current problem and written entirely in Romanian without any clarifications or additional information. Context: The user has asked for help, but their issue remains unclear. You have access to prior exchanges and details about the user's project, allowing you to focus on asking a question that narrows down the specifics of the problem. Guidelines: Act as an expert in the relevant domain based on the provided information. Leverage all available context to craft a targeted question. Maintain focus on the action of asking a relevant question that helps clarify the user's issue. Ensure the question is precise, clear, and written in Romanian without any commentary. Adhere to the style and tone of direct questioning. Formulate the question now based on the task, context, and guidelines provided."

normal_prompt = "You must formulate a response for the user inquity with thje following data as reference, keep it formal and coherent!"

llm = get_llm()

def change_subscription(llm, prompt, history={}, plans={}):
    return llm.query(prompt + f"History: {history}" + f"Plans: {plans}")

def incomplete_info(llm, prompt, history={}):
    return llm.query(prompt + f"History: {history}")

def normal(llm, prompt, user_query, prompt_type):
    template = read_json("support_ro.json")
    template = template["script_support"]
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