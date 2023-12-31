import inflect  # To handle plurals
import requests  # To connect to a recipe API
from naomi import plugin

class RecipeManagerPlugin(plugin.SpeechHandlerPlugin):
    def __init__(self, *args, **kwargs):
        super(RecipeManagerPlugin, self).__init__(*args, **kwargs)
        # Initialize ingredient list and API endpoint
        self.ingredients = [
            "onions",
            "tomatoes",
            "garlic",
            "pasta",
            "cheese",
            "chicken",
            "rice",
            "beans",
            "lettuce",
            "carrots",
            "potatoes",
            "broccoli",
            "spinach",
            "milk",
            "eggs",
            "flour",
            "sugar",
            "butter",
            "oil"
        ]
        self.recipes = {
            "tomato_onion_garlic_recipe": {
                "ingredients": ["onions", "tomatoes", "garlic"],
                "instructions": "Saute onions and garlic. Add tomatoes and cook until soft. Serve with pasta."
            },
            "simple_pasta": {
                "ingredients": ["pasta", "tomato sauce", "cheese"],
                "instructions": "Boil pasta. Mix with tomato sauce and top with cheese."
            },
            "chicken_pasta": {
                "ingredients": ["pasta", "chicken", "tomato sauce"],
                "instructions": "Cook chicken and pasta separately. Mix with tomato sauce."
            },
            "cheesy_garlic_bread": {
                "ingredients": ["garlic", "bread", "cheese"],
                "instructions": "Spread garlic and cheese on bread. Toast until cheese melts."
            }
        }
        # Modify the API endpoint to point to Edamam's Recipe API
        self.recipe_api_endpoint = "https://api.edamam.com/api/recipes/v2"  # Edamam API endpoint

        # Edamam API specific parameters (you may need an API key)
        self.api_app_id = "d1a764d0"
        self.api_app_key = "137d78b7bf384c229a95ba117feefd55"

    def intents(self):
        return {
            "AddIngredientIntent": {
                "locale": {
                    "en-US": {
                        "keywords": {
                            "Ingredient": ["ingredient", "add", "include"],
                        }
                    }
                },
                "action": self.add_ingredient
            },
            "FindRecipeIntent": {
                "locale": {
                    "en-US": {
                        "keywords": {
                            "Recipe": ["recipe", "make", "cook"],
                        }
                    }
                },
                "action": self.find_recipe
            }
        }

    def add_ingredient(self, msg):
        ingredient = msg.data.get("Ingredient", "").lower()
        if ingredient:
            # Handle plurals using inflect library
            p = inflect.engine()
            singular = p.singular_noun(ingredient)
            if singular:
                ingredient = singular  # Convert to singular if plural
            self.ingredients.append(ingredient)
            self.speak(f"Added {ingredient} to your ingredients list.")

    def find_recipe(self, msg):
        if not self.ingredients:
            self.speak("Your ingredients list is empty. You can add ingredients by saying 'Add [ingredient].'")
            return

        # Connect to a recipe API to fetch recipes based on ingredients
        try:
            response = requests.get(self.recipe_api_endpoint, params={"ingredients": ",".join(self.ingredients)})
            if response.status_code == 200:
                api_recipes = response.json().get("recipes", [])
                if api_recipes:
                    recipe_list = ", ".join(api_recipes)
                    self.speak(f"You can make: {recipe_list}")
                else:
                    self.speak("No API recipes found with your ingredients.")
            else:
                self.speak("Failed to retrieve recipes from the API. Please try again later.")
        except Exception as e:
            self.speak("An error occurred while fetching recipes from the API. Please try again later.")

        # Check if there are matching recipes in your own recipes
        matching_recipes = [name for name, recipe_data in self.recipes.items() if all(ingredient in self.ingredients for ingredient in recipe_data["ingredients"])]
        
        if matching_recipes:
            recipe_list = ", ".join(matching_recipes)
            self.speak(f"From your own recipes, you can make: {recipe_list}")
        else:
            self.speak("Sorry, no matching recipes found in your own recipes.")

