# Recipe Manager Plugin for Project Naomi

The Recipe Manager Plugin is an extension for Project Naomi, a Python-based personal assistant framework. This plugin provides the functionality to manage ingredients and find recipes based on the ingredients you have. You can add ingredients to your list and then ask Naomi what recipes you can make with those ingredients.

## Usage

### Adding Ingredients

To add ingredients to your list, use the following command:

- "Add [ingredient]" - For example, "Add one apple" will add "apple" to your ingredients list.

### Finding Recipes

To find recipes based on the ingredients you have, use the following command:

- "What can I make" - Naomi will search for recipes that can be made with the ingredients you've added.

## Installation

1. Create a directory for the Recipe Manager Plugin within your Naomi plugins directory. For example, create a directory named `recipe_manager`.

2. Inside the `recipe_manager` directory, create a Python file, e.g., `recipe_plugin.py`, and add the code provided in the plugin.

## Configuration

There is no additional configuration required for this plugin. It automatically initializes an empty ingredients list when you start Naomi.

## Example Usage

Here are some examples of how to use the Recipe Manager Plugin:

- **Adding Ingredients:**
  - "Add one apple" - This command adds "apple" to your ingredients list.
  - "Add two cups of flour" - You can specify quantities and units for ingredients.

- **Finding Recipes:**
  - "What can I make" - Naomi will search for recipes based on your available ingredients and provide a list of recipes that can be made.

## Customization

You can customize this plugin by replacing the sample recipes and ingredients in the code with your own data. You can also extend the plugin's functionality to include features like removing ingredients, handling quantities, and managing a more extensive recipe database.

## License

This plugin is provided under the MIT License. See the `LICENSE` file in your Naomi installation for details.

## Author

- Joe Graham

Feel free to expand and customize this documentation to suit your specific needs.
