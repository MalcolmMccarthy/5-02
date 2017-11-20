'''
created by malcolm and roman
in november 2017
for ics3u
program takes the largest number from the array and returns it
'''

def array_function(array = []):
    for i in array:
        Max = max(array)
        return Max
a = [1, 2, 3, 4, 12]
max_value = array_function(a)
print'the highest number in the array is: ' 
print(max_value)
