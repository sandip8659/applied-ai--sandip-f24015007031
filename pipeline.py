from transformers import pipeline
classifier =pipeline("sentiment-analysis")
result = classifier("I hate my self.")
print(result)
                                                   