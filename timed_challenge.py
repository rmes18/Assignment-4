# Timed Challenge Question:
# Remove Duplicates (Keep Order)
# Return the values in the order they first appeared, without duplicates.
# Input: ["apple", "banana", "apple", "kiwi", "banana"]
# Output: ["apple", "banana", "kiwi"]

def remove_duplicates_keep_order(values):
    """
    Data Structure Choice: Set and List
    Justification: A set is used to track seen values with O(1) lookup time,
    while a list preserves the original order of elements. The algorithm runs
    in O(n) time with O(n) additional space.
    """
    seen = set()
    result = []

    for value in values:
        if value not in seen:
            seen.add(value)
            result.append(value)

    return result


# Test cases and edge cases
if __name__ == "__main__":
    print(remove_duplicates_keep_order(["apple", "banana", "apple", "kiwi", "banana"]))  # expected ['apple', 'banana', 'kiwi']
    print(remove_duplicates_keep_order([]))  # empty list
    print(remove_duplicates_keep_order(["a", "a", "a"]))  # all duplicates
    print(remove_duplicates_keep_order(["x", "y", "z"]))  # no duplicates


"""
Reflection:

For this timed challenge, I chose to use a combination of a set and a list. 
The set allowed me to efficiently track which values had already been seen.
The list was used to maintain the original order of elements, which is required by the problem. 
This combination made the solution both efficient and easy to understand.
The 30-minute time limit influenced my approach by encouraging me to select data structures I was already familiar with rather than attempting something more complex.
I focused on writing a clear and correct solution first, then added test cases for edge conditions such as empty input and repeated values. 
Under time pressure, I prioritized correctness and readability over the super small details.
One trade-off I made was using extra memory to store the set and result list, but this was acceptable because it simplified the logic and improved runtime performance. 
Overall, this challenge helped me practice choosing appropriate data structures quickly and writing efficient code under interview-like constraints.
"""
