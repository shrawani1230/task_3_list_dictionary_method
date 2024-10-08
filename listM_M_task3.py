# extend()
test = ['sugar','thyroid','heamoglobin','widal']
more_test = ['LFT','KFT']

test.extend(more_test)
print(test)

print('----------')



# pop

l3=['varsha','dipti','meena']
l3.pop(0)
print(f'l3={l3}')
print()
print
print('------')
print()

# clear
l4=['varsha','dipti','meena','swati']
l4.clear()
print(f'l4={l4}')
print()
print('------')
print()

# copy

l5 =[78,98,45,63,12,35]
x=l5.copy()
print(f'l5 = {l5}')
print()
print('------')
print()


# index 
fruits = ['kiwi','dragon','orange']
x=fruits.index("orange")
print(f'fruits{fruits}')


print('-----')
# values

bike={
    "brand": "bullet",
    "model": "royal",
    "year": 1988
}
x=bike.values()
print(x)


# difference
print('-------')
a= {'banana','kiwi','dragon'}
b= {'oppo','apple','redme'}
c= a.difference(b)
print(c)


#differnce_update

print('-------')


a= {'banana','kiwi','dragon'}
b= {'oppo','apple','redme'}
c= a.difference_update(b)
print(c)

# count
print('-----')


fruits = ['kiwi', 'dragon',' apple','apple']
count_apple=fruits.count('apple')
print(f'number of apples:{count_apple}')


print('----------------')

#### DICTIONARY METHOD



#fromkey


print('--------------')
a=('key1', 'key2','key3')
b=0
thisdict=dict.fromkeys(a,b)
print(f'thisdict{thisdict}')

# key

print('--------')
bike={
    "brand": "bullet",
    "model": "royal",
    "year": 1988
}
x=bike.keys()
print(x)


# popitem

print('----------')

bike={
    "brand": "bullet",
    "model": "royal",
    "year": 1988
}
x=bike.popitem()
print(x)

# setdefault

print('-----------')


bike={
    "brand": "bullet",
    "model": "royal",
    "year": 1988
}
x=bike.setdefault("model","ktm")
print(x)


