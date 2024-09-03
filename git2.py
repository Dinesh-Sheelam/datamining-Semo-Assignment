# Create the list
my_list = [1225, 4986, 6789, 7890, 2345, 6783, 0987, 1234, 8765, 3456]

# I. Iterate using a for loop
print("I. For loop:")
for item in my_list:
    print(item, end=" ")
print()

# II. Iterate using for loop and range
print("\nII. For loop with range:")
for i in range(len(my_list)):
    print(my_list[i], end=" ")
print()

# III. List Comprehension
print("\nIII. List Comprehension:")
squared_list = [x**2 for x in my_list]
print(squared_list)

# IV. Enumerate
print("\nIV. Enumerate:")
for index, value in enumerate(my_list):
    print(f"Index: {index}, Value: {value}")

# V. Iter function and next function
print("\nV. Iter and next functions:")
iter_list = iter(my_list)
for _ in range(5):  # Print first 5 elements
    print(next(iter_list), end=" ")
print()

# VI. Map function
print("\nVI. Map function:")
mapped_list = list(map(lambda x: x * 2, my_list))
print(mapped_list)

# VII. Using zip
print("\nVII. Using zip:")
for item1, item2 in zip(my_list[:5], my_list[5:]):
    print(f"{item1} - {item2}")

# VIII. Using NumPy Module
print("\nVIII. Using NumPy:")
import numpy as np
np_array = np.array(my_list)
print("Mean:", np.mean(np_array))
print("Standard Deviation:", np.std(np_array))