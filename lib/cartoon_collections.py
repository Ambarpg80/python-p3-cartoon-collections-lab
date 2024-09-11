def roll_call_dwarves(names):
    for name in names:
        print(f"{names.index(name)+1}. {name}")
    

def summon_captain_planet(planet_call):
     title_case = [f"{call.title()}!" for call in planet_call]
     return title_case

def long_planeteer_calls(calls):
    over_four = [len(call) > 4 for call in calls]
    return any(over_four)
        

def find_the_cheese(ingredients):
    if ("cheddar" or "gouda" or "camembert") in ingredients:
        return ("cheddar" or "gouda" or "camembert")
