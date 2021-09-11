## belajar list comprehension

# contoh tanpa menggunakan list comprehension
print('Tanpa List Comprehension'.center(50, '='))
kuadrat = [] # tipe data list
for i in range(1, 5):
    kuadrat.append(i**2)
print(kuadrat)
print('')


# contoh dengan menggunakan list comprehension
print('Dengan List Comprehension'.center(50, '='))
kuadrat2 = [i**2 for i in range(1, 5)]
print(kuadrat2)
print('')


# contoh dengan menggunakan list comprehension
print('Dengan List Comprehension'.center(50, '='))
sisaBagi5 = [i**2 % 5 for i in range(1, 20)]
print(sisaBagi5)

