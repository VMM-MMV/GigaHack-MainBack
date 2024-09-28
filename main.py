from api import make_request

data = {
    "query": "Wai puli tu teai ahuit disi la mini rutaru nu merji"
}

response = make_request("/classify", data)
print(response)