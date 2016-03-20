#### The Grid Search

- Given a 2D array of digits, try to find the occurrence of a given 2D pattern of digits. For example, consider the following 2D matrix:

     1234567890  
     0987654321  
     1111111111  
     1111111111  
     2222222222  
- Assume we need to look for the following 2D pattern:

     876543  
     111111  
     111111
- If we scan through the original array, we observe that the 2D pattern begins at the second row and the third column of the larger grid (the 8 in the second row and third column of the larger grid is the top-left corner of the pattern we are searching for).

- So, a 2D pattern of P digits is said to be present in a larger grid G, if the latter contains a contiguous, rectangular 2D grid of digits matching with the pattern P, similar to the example shown above.



For more details, please refer to https://www.hackerrank.com/challenges/the-grid-search
