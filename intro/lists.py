# Python list (array)
array = [5, 8, 1, -9, 4, 2]
print('original array', array, '\n')

array.sort()  # O(nlogn) in-place
print('sorted array', array, '\n')

array.append(90)  # O(1) average
print('insert at end', array, '\n')

array.insert(0, -90)  # O(n)
print('insert at front', array, '\n')

popped_element = array.pop()  # O(1) average
print('popped array', array)
print('popped_element', popped_element, '\n')

print('loop over values')
for item in array:
    item += 1
    print(item)
print('unchanged array', array, '\n')

# in case we need index of item. Useful when modifying
for i in range(len(array)):
    array[i] += 1

# modified array
print('modified array', array)
