from transformers import pipeline
classifier = pipeline(
    "text-classification",
    model="distilbert/distilbert-base-uncased-finetuned-sst-2-english"
)
print(classifier("This course is surprisingly useful!"))
