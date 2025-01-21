# Redefine the random_name function and generate JSON again
import random
import json

# Random name generators
# def random_name():
first_names = ["Alex", "Nina", "Oleg", "Ayna", "John", "Anastasia", "Ivan", "Leyla", "Michael", "Zarina"]
last_names = ["Smith", "Berdyev", "Ivanov", "Muratova", "Johnson", "Petrova", "Anderson", "Durdyeva", "Taylor", "Akhmedov"]
    # return random.choice(first_names), random.choice(last_names)

# Generate 20 samples
samples = []
for _ in range(10):
    first_name = first_names[_]
    last_name = last_names[_]
    samples.append({
        "name": f"{first_name} {last_name}",
        "name_tk": f"{first_name} {last_name}",  # Placeholder
        "name_en": f"{first_name} {last_name}",
        "name_ru": f"{first_name} {last_name}",  # Placeholder
        "surname": last_name,
        "surname_tk": last_name,  # Placeholder
        "surname_en": last_name,
        "surname_ru": last_name,  # Placeholder
        "description": f"{first_name} {last_name} is an experienced educator in Business Education.",
        "description_tk": f"{first_name} {last_name} Biznes Biliminde tejribeli mugallym.",  # Placeholder
        "description_en": f"{first_name} {last_name} is an experienced educator in Business Education.",
        "description_ru": f"{first_name} {last_name} опытный преподаватель в области бизнес-образования.",  # Placeholder
        "image": "",
        "major": "Business Education",
        "major_tk": "Biznes Bilim",
        "major_en": "Business Education",
        "major_ru": "Бизнес Образование"
    })

# Convert to JSON format
json_data = json.dumps(samples, indent=4, ensure_ascii=False)
print (json_data)

