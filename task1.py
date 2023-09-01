jumbled_superheroes = ['DocTor_StranGe', 'SpidErman', 'Moon_knigHt', 'caPtain_ameriCa', 'HulK']

indices = []
decoded_names = []

for i, names in enumerate(jumbled_superheroes):
    indices.append(i)
    names = names.replace('_', ' ').lower()
    decoded_names.append(names)
length_lambda = lambda x: len(x) #function defined
name_lengths = list(map(length_lambda, decoded_names))
indices.sort(key=lambda index: name_lengths[index])
print("Phase 5 kickoff list : ")
d=0
for j in indices:
    print(f'{d+1}. {decoded_names[j].title()}')
    d=d+1
    