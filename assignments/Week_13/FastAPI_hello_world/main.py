from fastapi import FastAPI
app = FastAPI()


from transformers import pipeline
sentiment_model = pipeline("sentiment-analysis")

#sentiment_query_sentence = get_random_comment("Hello World")
#sentiment = sentiment_model(sentiment_query_sentence)
#print(f"Sentiment test: {sentiment_query_sentence} == {sentiment})

from pydantic import BaseModel

class PredictionRequest(BaseModel):
  query_string: str


@app.post("/my-endpoint")
def my_endpoint(request: PredictionRequest):
  # YOUR CODE GOES HERE 
  return sentiment_model(request.query_string) 

@app.get("/health")
def health():
    return "Service is online."
