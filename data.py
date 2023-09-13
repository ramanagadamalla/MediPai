import pandas as pd

# Define the data as a list of dictionaries
data = [
    {"Question": "What is fever?", "Answer": "Fever is an elevated body temperature, often a sign of an underlying infection or illness."},
    {"Question": "What causes fever?", "Answer": "Fever can be caused by various factors, including infections (bacterial, viral, or fungal), inflammatory conditions, and certain medications."},
    {"Question": "What is the normal body temperature?", "Answer": "The normal body temperature for adults is typically around 98.6°F (37°C), but it can vary slightly from person to person."},
    {"Question": "How is body temperature measured?", "Answer": "Body temperature can be measured orally, rectally, under the armpit, or using ear or forehead thermometers."},
    {"Question": "What are the common symptoms of fever?", "Answer": "Common symptoms of fever include a high body temperature, chills, sweating, headache, muscle aches, fatigue, and a feeling of general discomfort."},
    {"Question": "Is fever always a sign of illness?", "Answer": "No, fever can also be a response to non-infectious factors such as heatstroke, dehydration, or certain inflammatory conditions."},
    {"Question": "When should I seek medical attention for fever?", "Answer": "You should seek medical attention if you have a high fever (above 103°F or 39.4°C), persistent fever, severe headache, difficulty breathing, chest pain, or other concerning symptoms."},
    {"Question": "How is fever treated at home?", "Answer": "Home treatment for fever often includes rest, staying hydrated, and taking over-the-counter fever-reducing medications like acetaminophen or ibuprofen."},
    {"Question": "Can fever be contagious?", "Answer": "Fever itself is not contagious, but the underlying cause of the fever, such as a viral infection, can be contagious."},
    {"Question": "What is a fever reducer?", "Answer": "A fever reducer is a medication that helps lower body temperature and relieve fever-related symptoms."},
    {"Question": "Is it necessary to treat every fever with medication?", "Answer": "Not necessarily. Fever is a natural response to infection and can help the body fight off the illness. Treatment with medication is often based on the severity of symptoms and comfort level."},
    {"Question": "Can a fever be a sign of a serious illness?", "Answer": "Yes, a fever can be a symptom of various serious illnesses, including bacterial infections, sepsis, and autoimmune diseases. It's essential to identify the underlying cause."},
    {"Question": "What is the difference between a low-grade fever and a high fever?", "Answer": "A low-grade fever is generally considered to be a body temperature slightly above the normal range but below 100.4°F (38°C). A high fever is typically above 103°F (39.4°C)."},
    {"Question": "What should I eat when I have a fever?", "Answer": "It's essential to stay hydrated and eat light, easily digestible foods like broth-based soups, plain rice, applesauce, and bananas. Avoid heavy or spicy foods."},
    {"Question": "Can fever be a side effect of vaccines?", "Answer": "Yes, low-grade fever can be a common side effect of some vaccines. It is usually temporary and not a cause for concern."},
    {"Question": "How can I prevent fever?", "Answer": "Fever prevention often involves maintaining good hygiene, getting vaccinated, practicing safe food handling, and avoiding close contact with individuals who have contagious illnesses."},
    {"Question": "Is it safe to give a cold bath to reduce fever?", "Answer": "No, giving a cold bath is not recommended for fever reduction. It can cause shivering and make the fever worse. Instead, use lukewarm water for a sponge bath if necessary."},
    {"Question": "Can fever occur without any other symptoms?", "Answer": "Yes, in some cases, fever may be the only symptom of an underlying illness, especially in mild viral infections."},
    {"Question": "What is the purpose of sweating during a fever?", "Answer": "Sweating during a fever is the body's way of cooling down and regulating temperature. It helps dissipate excess heat."},
    {"Question": "Can fever be a sign of COVID-19?", "Answer": "Yes, fever is one of the common symptoms of COVID-19, along with other respiratory symptoms like cough and shortness of breath."}


]

# Create a DataFrame from the data
df = pd.DataFrame(data)

# Save the DataFrame to a CSV file
df.to_csv("data.csv", index=True)

# print("Data has been written to heart_disease_dataset.csv.")
