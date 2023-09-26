from naomi import plugin

class RecipeManagerPlugin(plugin.SpeechHandlerPlugin):
    def __init__(self, *args, **kwargs):
        super(RecipeManagerPlugin, self).__init__(*args, **kwargs)
        # Common ingredients
        self.ingredients = ["onions", "tomatoes", "garlic", "pasta", "cheese", "chicken"]
        # Common recipes
        self.recipes = {
            "tomato_onion_garlic_recipe": ["onions", "tomatoes", "garlic"],
            "simple_pasta": ["pasta", "tomato sauce", "cheese"],
            "chicken_pasta": ["pasta", "chicken", "tomato sauce"],
            "cheesy_garlic_bread": ["garlic", "bread", "cheese"]
        }

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
            self.ingredients.append(ingredient)
            self.speak(f"Added {ingredient} to your ingredients list.")

    def find_recipe(self, msg):
        if not self.ingredients:
            self.speak("Your ingredients list is empty. You can add ingredients by saying 'Add [ingredient].'")
            return

        available_recipes = []

        for recipe, ingredients in self.recipes.items():
            if all(ingredient in self.ingredients for ingredient in ingredients):
                available_recipes.append(recipe)

        if available_recipes:
            recipe_list = ", ".join(available_recipes)
            self.speak(f"You can make: {recipe_list}")
        else:
            self.speak("Sorry, you don't have enough ingredients to make any recipes.")
