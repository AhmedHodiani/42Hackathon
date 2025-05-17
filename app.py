from transformers import pipeline

classifier = pipeline("sentiment-analysis")


res = classifier("hello hi my name is Ahmed")


print(res)
