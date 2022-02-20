
# The idea:
# 1. Find the sum of all numbers from 0 to n in the list. 
    # 1.1 Calculate the sum of all numbers from 0 to n in the list with formula:
    # n * (n + 1) / 2
    # Time complexity: O(1)
# 2. Find the sum of all numbers in the missing list.
    # 2.1 Find the sum of all numbers in the missing list with built-in function:
    # sum(arr)
    # Time complexity: O(n)
# 3. Find the difference between the two sums.
# 4. Return the difference. The difference is the missing number.

#Time complexity: O(1) and O(n) => O(n)

def missing_number(arr) -> int:
    """Find the missing number in a list of numbers."""
    n = len(arr)
    return int(n*(n + 1)/2 - sum(arr)) 

if __name__ == "__main__":
    array = [0,1,2,3,4]
    print("The missing number: ", missing_number(array))