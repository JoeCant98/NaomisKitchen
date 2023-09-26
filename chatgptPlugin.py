from naomi import plugin

class RecipeManagerPlugin(plugin.SpeechHandlerPlugin):
    def __init__(self, *args, **kwargs):
        super(RecipeManagerPlugin, self).__init__(*args, **kwargs)
        self.ingredients = []

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

        # Define some sample recipes (you can replace this with your recipe data)
        recipes = {
            "recipe1": ["ingredient1", "ingredient2"],
            "recipe2": ["ingredient3", "ingredient4"],
            "recipe3": ["ingredient2", "ingredient5"],
        }

        available_recipes = []

        for recipe, ingredients in recipes.items():
            if all(ingredient in self.ingredients for ingredient in ingredients):
                available_recipes.append(recipe)

        if available_recipes:
            recipe_list = ", ".join(available_recipes)
            self.speak(f"You can make: {recipe_list}")
        else:
            self.speak("Sorry, you don't have enough ingredients to make any recipes.")

