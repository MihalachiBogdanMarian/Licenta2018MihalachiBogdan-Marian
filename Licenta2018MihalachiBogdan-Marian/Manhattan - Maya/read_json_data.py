import json

data = open(r"C:\Users\Bidi\eclipse-workspace\Manhattan\manhattan_results.json", "rt").read()
d = json.loads(data)
planeDimension = d["planeDimension"]
longestPath = d["longestPath"]
curves = d["curves"]
