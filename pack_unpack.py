# Packing data
def pack(*nums):
    print(f'Received arguments: {nums}')
    # print(f'First argument: {nums[0]}')
    # print(f'Second argument: {nums[1]}')
    # print(f'Third argument: {nums[2]}')


pack(1, 2, 3)


# Unpacking data
def unpack(a, b, c):
    print(f'Unpacked arguments: {a}, {b}, {c}')


num = [1, 2, 3]
unpack(*num)


# Dictionary issue, only the keys are unpacked/packed
'''
d = dict(name='Bryan', age=46, pet='Cat')
print('Packing dictionary')
pack(*d)

print('Unpacking dictionary')
unpack(*d)  # Answer: Unpacked arguments: name, age, pet
'''


# Packing a dictionary
def pack_dict(**nums):
    print(f'Received keyword arguments: {nums}')


pack_dict(name='Bryan', age=46, pet='Cats')


# Unpacking a dictionary
def unpack_dict(name, age, pet):
    print(f'Unpacked arguments: name: {name}, age: {age}, pet: {pet}')


d = dict(name='Bryan', age=46, pet='Cat')
unpack_dict(**d)
