spicy_foods = [
    {
        "name": "Green Curry",
        "cuisine": "Thai",
        "heat_level": 9,
    },
    {
        "name": "Buffalo Wings",
        "cuisine": "American",
        "heat_level": 3,
    },
    {
        "name": "Mapo Tofu",
        "cuisine": "Sichuan",
        "heat_level": 6,
    },
]

def get_names(spicy_foods):
    names = [n["name"] for n in spicy_foods]
    return names

def get_spiciest_foods(spicy_foods):
    heat = [n for n in spicy_foods if n["heat_level"] >= 5]
    return heat

def print_spicy_foods(spicy_foods):
    for food in spicy_foods:
            name = food["name"]
            cuisine = food["cuisine"]
            heat_level = food["heat_level"] 
            heat_level_str = "🌶" * heat_level
            print(f"{name} ({cuisine}) | Heat Level: {heat_level_str}")
    

def get_spicy_food_by_cuisine(spicy_foods, cuisine):
        for food in spicy_foods:
             if food["cuisine"] == cuisine:
                  return food
        
        
def print_spiciest_foods(spicy_foods):
    for food in spicy_foods:
         if food["heat_level"] > 5:
              name = food["name"]
              cuisine = food["cuisine"]
              heat_level = food["heat_level"]
              chili_peppers = "🌶" * heat_level
              print(f"{name} ({cuisine}) | Heat Level: {chili_peppers}")

def get_average_heat_level(spicy_foods):
    total_heat_value = 0
    for food in spicy_foods:
         total_heat_value += food['heat_level']
         average = total_heat_value / len(spicy_foods)
    return int(average)

def create_spicy_food(spicy_foods, spicy_food):
    spicy_foods.append(spicy_food)
    return spicy_foods

