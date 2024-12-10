#Using max() and min() function display the maximum and minimum of 5 Random numbers.

import random  

random_numbers = [random.randint(1, 100) for _ in range(5)]

print("Random numbers:", random_numbers)

print("Maximum number:", max(random_numbers))
print("Minimum number:", min(random_numbers))