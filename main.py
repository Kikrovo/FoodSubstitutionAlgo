from DISS.FoodSubstitutionAlgo.recipe_modifier import SubstitutionAlgorithm
from food_data_fetcher import FoodDataFetcher

api_key = "MM1YcWHeSeJXrp7PwPooOXIRReY4SbvStyIuq0qP"
food_data_fetcher = FoodDataFetcher(api_key)

# Initialize substitution algorithm with the food data fetcher
substitution_algorithm = SubstitutionAlgorithm(food_data_fetcher)

# Sample recipes, values are in grams
recipes = {
    "Chicken Salad": {
        "chicken breast": 200,
        "spinach": 100,
        "avocado": 50,
        "milk": 30
    },
    "Stir-fry": {
        "tofu": 150,
        "spinach": 100,
        "cauliflower": 200,
        "coconut oil": 20
    },
    "Egg Breakfast": {
        "egg": 150,
        "spinach": 50,
        "bacon": 50
    }
}

# User Input Example
dietary_preference = input("Enter your dietary preference (keto, high-protein, low-calorie): ").lower()
recipe_name = input("Enter the recipe name (e.g., Chicken Salad, Stir-fry, Egg Breakfast): ")

# Modify the recipe based on the user's dietary preference
modified_recipe = substitution_algorithm.modify_recipe_for_diet(recipe_name, dietary_preference, recipes)
print(f"Modified Recipe for {recipe_name}: {modified_recipe}")