from random import randint
mass = []
for i in range (1,20):
   mass.append(randint(1,20))

for i in range(0, len(mass)):
   for j in range(len(mass)):
      if (mass[i] < mass[j]):
         Bufer = mass[i]
         mass[i] = mass[j]
         mass[j] = Bufer
print(mass)

for i in range(0, len(mass)):
   for j in range(len(mass)):
      if (mass[i] > mass[j]):
         Bufer = mass[i]
         mass[i] = mass[j]
         mass[j] = Bufer
print(mass)

