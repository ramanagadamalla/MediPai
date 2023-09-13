import pandas as pd
import nltk
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# read data from csv
data = pd.read_csv("data.csv")
# nltk.download("punkt")
# nltk.download("stopwords")
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
stop_words = set(stopwords.words("english"))
def preprocess_text(text):
    tokens = word_tokenize(text.lower())
    tokens = [token for token in tokens if token.isalnum() and token not in stop_words]
    return " ".join(tokens)
data['Question'] = data['Question'].apply(preprocess_text)
# TF-IDF Vectorization
vectorizer = TfidfVectorizer()
tfidf_matrix = vectorizer.fit_transform(data['Question'])
#  function to generate responses
def generate_response(user_input):
    user_input = preprocess_text(user_input)
    user_vector = vectorizer.transform([user_input])
    # cosine similarities b/w i/p and question data 
    cosine_similarities = cosine_similarity(user_vector, tfidf_matrix)
    #  index of the most similar question
    max_similarity_index = cosine_similarities.argmax()
    # Get the corresponding answer
    response = data['Answer'][max_similarity_index]
    return response
# Chat with bot

print("Bot: Hi there! How can I help you ")
while True:
    user_input = input("You: ")
    if user_input.lower() == "exit":
        print("Bot:Have a nice day!")
        break
    response = generate_response(user_input)
    print("Bot:", response)
