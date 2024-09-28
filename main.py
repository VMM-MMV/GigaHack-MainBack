from api import make_request
from json_handler import get_keys_from_file
from similarity import find_most_similar

data = {
    "query": "Wai puli tu teai ahuit disi la mini rutaru nu merji"
}

class_type = make_request("/classify", data)

types = get_keys_from_file('support_ro.json', depth=2)
types.remove("script_support")
types.append("DONT KNOW")

print(class_type)

validated_type, _ = find_most_similar(class_type, types)

print(validated_type)

# print(response)