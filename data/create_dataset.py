import fantasynames 
from random import sample

NUM_OF_NAMES = 50000

options = {
    "human": fantasynames.human, 
    "anglo": fantasynames.anglo, 
    "dwarf": fantasynames.dwarf, 
    "elf": fantasynames.elf, 
    "hobbit": fantasynames.hobbit, 
    "french": fantasynames.french
}

full_names = [options[''.join(sample(list(options.keys()), k=1))]().lower() for _ in range(NUM_OF_NAMES)]

names, surnames = [], []
for full_name in set(full_names):
    name_parts = full_name.split(" ") 
    names.append(name_parts[0])
    surnames.append(' '.join(name_parts[1:]))

with open("names.txt", "x") as f:
    for name in names:
        f.write(f"{name}\n")

with open("surnames.txt", "x") as f:
    for surname in surnames:
        f.write(f"{surname}\n")

with open("symbols.txt", "x") as f:
    f.write(f"{''.join(set(''.join(set(full_names))))}\n")
