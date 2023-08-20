#3. Demonstrate use of List.

numbers = [1, 2, 3, 4, 5]

#List Functions
print(f'list sum function:: {sum(numbers)}')
print(f'list max function:: {max(numbers)}')
print(f'list min function:: {min(numbers)}')
print(f'any function:: {any([1,0,1,1,1,0])}')
print(f'All function:: {all([1,0,1,1,1,0])}')
#List Methods
cities = ["gadag", "delhi", "washington", "london", "seattle", "paris",
"washington"]
print(f'{cities}')
print(f'Count method:: {cities.count("seattle")}')
print(f'Index method:: {cities.index("washington")}')
cities.append('hubli')
print(f'Append method:: {cities}')
cities.reverse()
print(f'Reverse method:: {cities}')
cities.sort()
print(f'Sort method:: {cities}')
cities.pop()
print(f'Pop method:: {cities}')
cities.insert(1,'belagavi')
print(f'Inser method:: {cities}')
cities.remove("paris")
print(f'remove method:: {cities}')
more_cities=['bangalore','pune']
cities.extend(more_cities)
print(f'extend method:: {cities}')