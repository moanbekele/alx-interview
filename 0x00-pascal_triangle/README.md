# 0x00. Pascal's Triangle

### Create a function `def pascal_triangle(n):` that returns a list of lists of integers representing the Pascal’s triangle of n:

-   Returns an empty list if n <= 0
-   You can assume n will be always an integer

## Summary of what the code does:

1.  It initializes an empty list called triangle to store the rows of Pascal's triangle.
2.  The function checks if the input n is a positive integer. If not, it returns the empty triangle list.
3.  It uses nested loops to generate each row of Pascal's triangle. The outer loop iterates from `0` to `n-1`, representing the row index.
4.  Inside the outer loop, an empty list called line is created to represent the current row.
5.  The inner loop iterates from `0` to the current row index `(i)` and generates the elements of line.
6.  If the current column index `(j)` is either the leftmost column `(j == 0)` or the rightmost column `(j == i)`, the element is set to `1`.
7.  If the current column index is neither the leftmost nor the rightmost column, the element is calculated by summing the corresponding elements from the previous row `(i - 1)` of triangle.
8.  The generated line list is appended to the triangle list.
9.  After all rows are generated, the triangle list representing Pascal's triangle up to the `nth` row is returned.
10. In summary, this code allows you to generate Pascal's triangle up to a specified number of rows by calling the `pascal_triangle(n)` function.