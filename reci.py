'''
Recipy is a python based recipe tracker. The idea is that it will sort recipes
based on certain attributes such as time/food required/kitchen utencils etc.


class Recipe:
    def __init__(self, name, directions, ingredients, cookware, notes):
        self.name = name
        self.directions = directions
        self.ingredients = ingredients
        self.cookware = cookware
        self.notes = notes

    def print_rec(self):
        print(self.name + "\n" + self.directions + "\n" + self.ingredients + "\n"
        + self.cookware + "\n" + self.notes + "\n")

class Recipe_List:
    def __init__(self):
        self.recipes = []

    def add_recipe(self, name, directions, ingredients, cookware, notes):
        r = Recipe(name, directions, ingredients, cookware, notes)
        self.recipes.append(r)
    def print_recipe(self,name ):
        matches = [x for x in self.recipes if x.name == name]
        for x in matches:
            x.print_rec()
    def print_all_recipes(self):
        for x in self.recipes:
            x.print_rec()

    def count_recipes(self):
        print(len(self.recipes))



r = Recipe_List()
print("creating recipes")
r.add_recipe("boring","do stuff", "Onions \n peppers \n garlic", "pan", "test")
r.print_all_recipes()
print("finished")
'''

from flask import Flask, render_template
app = Flask(__name__)

@app.route("/")
def main():
    return render_template('index.html')

if __name__ == "__main__":
    app.run()
