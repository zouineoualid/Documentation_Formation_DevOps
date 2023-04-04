iteration = 0
ep_min = 0.0001
ep_feuille = 400
while ep_min < ep_feuille:
    iteration += 1
    ep_min *= 2

print(iteration)
print(ep_min)

#solution à l'envers (on déplie)
it = 0
ep_min= 0.0001
ep_feuille = 400
while ep_feuille >= ep_min:
    ep_feuille /= 2 
    it += 1

print(it)
print(ep_feuille)