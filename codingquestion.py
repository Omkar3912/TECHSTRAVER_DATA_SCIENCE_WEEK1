def list_operations():
    # Create a list
    my_list = [1, 2, 3, 4, 5]
    print(f"Original List: {my_list}")

    # Append to the list
    my_list.append(6)
    print(f"List after appending 6: {my_list}")

    # Reverse the list
    my_list.reverse()
    print(f"Reversed List: {my_list}")

    # Delete the list
    del my_list
    print("List deleted")

def dict_operations():
    # Create a dictionary
    my_dict = {'a': 1, 'b': 2, 'c': 3}
    print(f"Original Dictionary: {my_dict}")

    # Append to the dictionary
    my_dict['d'] = 4
    print(f"Dictionary after adding key 'd': {my_dict}")

    # Reverse the dictionary (Note: this reverses the insertion order for Python 3.7+)
    reversed_dict = dict(reversed(list(my_dict.items())))
    print(f"Reversed Dictionary: {reversed_dict}")

    # Delete the dictionary
    del my_dict
    print("Dictionary deleted")

def set_operations():
    # Create a set
    my_set = {1, 2, 3, 4, 5}
    print(f"Original Set: {my_set}")

    # Append to the set
    my_set.add(6)
    print(f"Set after adding 6: {my_set}")

    # Reverse the set (Note: sets are unordered, so this concept doesn't apply directly)
    reversed_set = set(sorted(my_set, reverse=True))
    print(f"Reversed Set (by sorting): {reversed_set}")

    # Delete the set
    del my_set
    print("Set deleted")

def tuple_operations():
    # Create a tuple
    my_tuple = (1, 2, 3, 4, 5)
    print(f"Original Tuple: {my_tuple}")

    # Append to the tuple (create a new tuple)
    my_tuple = my_tuple + (6,)
    print(f"Tuple after appending 6: {my_tuple}")

    # Reverse the tuple (create a new tuple)
    reversed_tuple = my_tuple[::-1]
    print(f"Reversed Tuple: {reversed_tuple}")

    # Delete the tuple
    del my_tuple
    print("Tuple deleted")

# Execute the functions
print("List Operations:")
list_operations()
print("\nDictionary Operations:")
dict_operations()
print("\nSet Operations:")
set_operations()
print("\nTuple Operations:")
tuple_operations()
