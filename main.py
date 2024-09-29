from flask import Flask, request, jsonify
from json_handler import get_keys_from_file
from similarity import find_most_similar
from llm_factory import get_llm
from type_llm_factory import answer_based_on_type
from CustomRedis import CustomRedis

app = Flask(__name__)
llm = get_llm("server")
redis = CustomRedis()

def get_validated_type(data):
    class_type = llm.query(data, "/classify")

    types = get_keys_from_file('support_ro.json', depth=2)
    types.remove("script_support")
    types.append("DONT KNOW")

    print(class_type)

    validated_type, _ = find_most_similar(class_type, types)

    print(validated_type)

    return validated_type

def get_user_sentiment(data):
    return llm.query(data, "/sentiments")

@app.route('/process', methods=['POST'])
def process_data():
    data = request.json.get('message')
    if not data:
        return jsonify({"error": "No message provided"}), 400

    validated_type = get_validated_type(data)
    user_sentiment = get_user_sentiment(data)

    llm_answer = answer_based_on_type(data, validated_type)
    # TODO: Add post-processing prompt with requirements from docx

    redis.set_cache("message", llm_answer)

    # TODO: If history out of bounds -> resume

    return jsonify({
        "type": validated_type,
        "sentiment": user_sentiment,
        "answer": llm_answer
    })

if __name__ == '__main__':
    app.run(debug=True)