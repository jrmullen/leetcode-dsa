class Solution:
    def findAllRecipes(self, recipes: List[str], ingredients: List[List[str]], supplies: List[str]) -> List[str]:
        result = []

        # The `supplies` can all be cooked by default, so push them into the `can_cook` map with a value of `True`
        can_cook = { supply: True for supply in supplies } # Map recipe : T/F can cook value

        # Map each recipe's to its index so that its ingredients can easily be looked up
        recipe_idx = {recipe: idx for idx, recipe in enumerate(recipes)}

        def dfs(recipe):
            # Base case: if the recipe is already in the `can_cook` map, immediately return the result
            if recipe in can_cook:
                return can_cook[recipe]

            # Edge case: an ingredient does not exist in the initial recipe_idx map
            if recipe not in recipe_idx:
                return False
            
            # Add the `recipe` to the `can_cook` map with a defaulted False value
            can_cook[recipe] = False

            # Determine whether each ingredient for the recipe can be cooked. Ingredients can easily found using `recipe_idx` map
            for ingredient in ingredients[recipe_idx[recipe]]:
                if not dfs(ingredient): # If one of the ingredients cannot be cooked, exit immediately
                    return False
            
            # If all of the ingredients were able to be cooked, flag the `recipe` as cookable and return True
            can_cook[recipe] = True
            return can_cook[recipe]

        # DFS on each recipe in the list of `recipes` to determine if they can each be cooked
        for recipe in recipes:
            if dfs(recipe):
                result.append(recipe) # If the recipe can be cooked, add it to the `result` list
        
        return result
