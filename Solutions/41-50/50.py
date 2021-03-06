s=input() # Taking string input

d={} # Initializing a dictionary
    # Dictionary in Python is an unordered collection of data values, used to store data values like a map, which unlike other Data Types that hold only single value as an element, Dictionary holds keyvalue pair. Key value is provided in the dictionary to make it more optimized.
    # Similar to unordered_map in c++

# traversing through the string to calculate the frequency of each element 
for i in s:
    if i in d:
        d[i]+=1 # If character 'i' is already in the dictionary, we increase the key value, i.e the characters frequency by 1 
    else:
        d[i]=1 # If character 'i' is not in the dictionary, then we initialize it to key value to 1   

print(d) # Printing the dictionary which holds character's frequency 