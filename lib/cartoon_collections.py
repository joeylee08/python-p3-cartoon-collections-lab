def roll_call_dwarves(dwarves_list):
    [print(f"{dwarves_list.index(dwarf) + 1}. {dwarf}") for dwarf in dwarves_list]

def summon_captain_planet(pcalls_list):
    return [f"{call.title()}!" for call in pcalls_list]

def long_planeteer_calls(long_pcalls_list):
    for call in long_pcalls_list:
        if len(call) > 4:
            return True
    return False

def find_the_cheese(cheese_list):
    cheeses = ['cheddar', 'gouda', 'camembert']
    for cheese in cheese_list:
        if cheese in cheeses:
            return cheese
    return None
