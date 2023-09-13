import csv

data = [
    ["Question", "Answer"],
    ["What is heart disease?", "Heart disease refers to a range of conditions that affect the heart's structure and function, often leading to cardiovascular problems."],
    ["What are the main types of heart disease?", "The main types of heart disease include coronary artery disease, congestive heart failure, arrhythmias, valvular heart disease, and congenital heart disease."],
    ["What are the leading risk factors for heart disease?", "Leading risk factors for heart disease include smoking, high blood pressure, high cholesterol, obesity, diabetes, and a family history of heart disease."],
    ["How does high blood pressure contribute to heart disease?", "High blood pressure can damage blood vessels, increasing the risk of atherosclerosis and heart disease."],
    ["What is cholesterol, and how does it affect heart health?", "Cholesterol is a fatty substance that can accumulate in arteries, narrowing them and leading to atherosclerosis, a common cause of heart disease."],
    ["What are the common symptoms of a heart attack?", "Common symptoms of a heart attack include chest pain or discomfort, shortness of breath, nausea, lightheadedness, and pain radiating to the arm, jaw, or back."],
    ["What is angina, and how is it related to heart disease?", "Angina is chest pain or discomfort caused by reduced blood flow to the heart muscle, often due to coronary artery disease."],
    ["Can heart disease be hereditary?", "Heart disease can have a hereditary component, and a family history of heart disease can increase an individual's risk."],
    ["What lifestyle changes can help prevent heart disease?", "Lifestyle changes like regular exercise, a heart-healthy diet, quitting smoking, managing stress, and limiting alcohol intake can help prevent heart disease."],
    ["What is the role of diet in heart disease prevention?", "A heart-healthy diet includes plenty of fruits, vegetables, whole grains, lean proteins, and limited saturated and trans fats."],
    ["How does physical activity impact heart health?", "Regular physical activity helps lower the risk of heart disease by improving cardiovascular health, reducing blood pressure, and managing weight."],
    ["What is the connection between smoking and heart disease?", "Smoking is a major risk factor for heart disease, as it damages blood vessels and contributes to the buildup of plaque in arteries."],
    ["What is coronary artery disease, and how does it develop?", "Coronary artery disease involves the narrowing or blockage of coronary arteries, usually due to the buildup of plaque."],
    ["What are the risk factors for atherosclerosis?", "Risk factors for atherosclerosis include smoking, high cholesterol, high blood pressure, diabetes, and a family history of the condition."],
    ["What is heart failure, and what are its symptoms?", "Heart failure occurs when the heart is unable to pump blood effectively, leading to symptoms like fatigue, shortness of breath, and fluid retention."],
    ["How is heart disease diagnosed?", "Heart disease is diagnosed through various tests, including electrocardiograms (ECGs or EKGs), stress tests, echocardiograms, and cardiac catheterizations."],
    ["What treatments are available for heart disease?", "Treatments for heart disease may include medications, lifestyle changes, angioplasty, stents, bypass surgery, and heart transplant in severe cases."],
    ["What is a cardiac catheterization, and when is it used?", "Cardiac catheterization is a procedure where a thin tube is inserted into the heart's blood vessels to diagnose and treat heart conditions."],
    ["Can heart disease be reversed through lifestyle changes?", "In some cases, heart disease can be managed and even reversed through lifestyle changes, such as diet modification, exercise, and medication."],
    ["What should I do in case of a suspected heart attack?", "In the case of a suspected heart attack, it is crucial to seek emergency medical attention immediately by calling 911 or the appropriate emergency number."],
]

# Define the file name
file_name = "data.csv"

# Write the data to the CSV file
with open(file_name, mode='w', newline='') as file:
    writer = csv.writer(file)
    writer.writerows(data)

print(f"Data has been written to {file_name}.")
