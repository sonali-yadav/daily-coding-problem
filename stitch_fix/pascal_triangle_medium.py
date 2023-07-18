"""
Pascal's triangle is a triangular array of integers constructed with the following formula:

The first row consists of the number 1.
For each subsequent row, each element is the sum of the numbers directly above it, on either side.
For example, here are the first few rows:

    1
   1 1
  1 2 1
 1 3 3 1
1 4 6 4 1
Given an input k, return the kth row of Pascal's triangle.

Bonus: Can you do this using only O(k) space?

"""


def get_kth_row_of_pascal_triangle(k):
    row_value = 11 ** (k - 1)
    return list(map(int, str(row_value)))


def main():
    try:
        k = int(input("Enter value of k: "))
    except TypeError as ex:
        print("You have entered an incorrect value of k!")
    print(get_kth_row_of_pascal_triangle(k))


main()
