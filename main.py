from json_handler import get_keys_from_file
from similarity import find_most_similar
from llm_factory import get_llm
from type_llm_factory import *


def get_validated_type(llm, data):
    class_type = llm.query(data, "/classify")

    types = get_keys_from_file('support_ro.json', depth=2)
    types.remove("script_support")
    types.append("DONT KNOW")

    print(class_type)

    validated_type, _ = find_most_similar(class_type, types)

    print(validated_type)

    return validated_type

def get_user_sentiment(llm, data):
    return llm.query(data, "/sentiments")

llm = get_llm("server")
data = "Di si nu merji ruteru brat"


validated_type = get_validated_type(llm, data)
user_sentiment = get_user_sentiment(llm, data)

print(user_sentiment)
print(validated_type)

print(answer_based_on_type(data,"DONT KNOW"))

