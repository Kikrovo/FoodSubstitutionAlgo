import requests

class FoodDataFetcher:
    def __init__(self, api_key):
        self.api_key = api_key
        self.target_nutrients = {
            "Energy": "calories",
            "Protein": "protein",
            "Total lipid (fat)": "fat",
            "Carbohydrate, by difference": "carbs"
        }

    def fetch_food_data(self, food_list):
        results = {}
        for food in food_list:
            params = {
                "query": food,
                "pageSize": 1,  # Fetch the top result
                "api_key": self.api_key
            }
            response = requests.get("https://api.nal.usda.gov/fdc/v1/foods/search", params=params)

            if response.status_code == 200:
                result = response.json()

                if "foods" in result and len(result["foods"]) > 0:
                    food_data = result["foods"][0]  # Get the first result
                    nutrients = {"calories": 0, "protein": 0, "fat": 0, "carbs": 0}

                    # Extract relevant nutrients
                    for nutrient in food_data.get("foodNutrients", []):
                        nutrient_name = nutrient.get("nutrientName")
                        if nutrient_name in self.target_nutrients:
                            nutrients[self.target_nutrients[nutrient_name]] = nutrient.get("value", 0)

                    results[food] = nutrients
                else:
                    print(f"No data found for {food}")
            else:
                print(f"Error fetching data for {food}: {response.status_code}, {response.reason}")

        return results