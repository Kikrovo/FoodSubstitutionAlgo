from food_data_fetcher import FoodDataFetcher

class SubstitutionAlgorithm:
    def __init__(self, food_data_fetcher):
        self.food_data_fetcher = food_data_fetcher

    def calculate_nutrition(self, recipe):
        total_nutrients = {"calories": 0, "protein": 0, "fat": 0, "carbs": 0}
        ingredients = list(recipe.keys())
        ingredient_data = self.food_data_fetcher.fetch_food_data(ingredients)

        for ingredient, quantity in recipe.items():
            nutrient_data = ingredient_data.get(ingredient, {})
            if nutrient_data:
                for nutrient in total_nutrients:
                    total_nutrients[nutrient] += (nutrient_data.get(nutrient, 0) * quantity) / 100
        return total_nutrients

    def suggest_substitution(self, dietary_preference):
        substitutions = {
            "keto": {
                "brown rice": "cauliflower",  # Replace brown rice with cauliflower for low carbs
                "milk": "almond milk",  # Replace milk with almond milk (lower carbs)
                "bacon": "coconut oil",  # Keep bacon, but reduce processed meats with healthy fats
            },
            "high-protein": {
                "avocado": "chicken breast",  # Avocado is replaced with high-protein chicken breast
                "spinach": "egg",  # Spinach is replaced with egg to boost protein
                "cauliflower": "chicken breast",  # Cauliflower replaced with chicken for high-protein
            },
            "low-calorie": {
                "bacon": "spinach",  # Replace high-calorie bacon with spinach
                "chicken breast": "cauliflower",  # Replace chicken with cauliflower (lower calories)
                "avocado": "spinach",  # Avocado is high-calorie, so replace with spinach
            }
        }
        return substitutions.get(dietary_preference, {})

    def modify_recipe_for_diet(self, recipe_name, dietary_preference, recipes):
        recipe = recipes.get(recipe_name)
        if not recipe:
            return f"Recipe {recipe_name} not found."

        # Calculate original nutritional data
        original_nutrition = self.calculate_nutrition(recipe)
        print(f"Original Nutrition for {recipe_name}: {original_nutrition}")

        # Suggest ingredient substitutions based on dietary preference
        substitutions = self.suggest_substitution(dietary_preference)
        modified_recipe = recipe.copy()

        # Apply substitutions
        for ingredient, replacement in substitutions.items():
            if ingredient in modified_recipe:
                modified_recipe[replacement] = modified_recipe.pop(ingredient)

        # Calculate modified nutritional data
        modified_nutrition = self.calculate_nutrition(modified_recipe)
        print(f"Modified Nutrition for {recipe_name} ({dietary_preference}): {modified_nutrition}")

        # Return the modified recipe
        return modified_recipe