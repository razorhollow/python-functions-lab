#----- CHALLENGE 1 -----#

def sum_to(int):
  counter = 0
  for num in range(int + 1):
    counter += num
  return counter

# print(sum_to(int(input('enter a number: '))))

#----- CHALLENGE 2 -----#

def largest(list):
  list.sort()
  return list[-1]

# list1 = [1,2,3,4,0]
# list2 = [10, 4, 2, 231, 91, 54]

# print (largest(list1))
# print (largest(list2))

#----- CHALLENGE 3 -----#

def occurrences(str1, str2):
  return str1.count(str2)

# print(occurrences('fleep floop', 'e'))   # returns 2
# print(occurrences('fleep floop', 'p'))   # returns 2
# print(occurrences('fleep floop', 'ee'))  # returns 1
# print(occurrences('fleep floop', 'fe'))  # returns 0

#----- CHALLENGE 4 -----#

def product(*args):
  product = 1
  for num in args:
    product *= num
  return product

# print(product(-1, 4)) # returns -4
# print(product(2, 5, 5)) # returns 50
# print(product(4, 0.5, 5)) # returns 10.0