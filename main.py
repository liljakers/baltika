from random import shuffle
spisog_omg = ['соль','мазик','картошечка']

triks = input('Введи ингредиент (хорош = стоп):')
while triks != 'хорош':
    if triks in spisog_omg:
        print('Этот ингредиент уже есть!')
    else: 
        spisog_omg.append(triks)

    triks = input('Введите ингредиент (хорош - стоп):')
    
spisog_blender = []
nums = int(input('Сколько месим ингредиентов:'))
for i in range (nums):
    shuffle(spisog_omg)
    spisog_blender.append(spisog_omg[0])
    spisog_omg.remove(spisog_omg[0])

print('Приготовь что-нибудь из:')
for i in range(nums):
    print(spisog_blender[i])