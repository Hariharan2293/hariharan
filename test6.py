def maxArea(A, Len) :

    area = 0

    for i in range(Len) :

        for j in range(i + 1, Len) :

           

            # Calculating the max area

            area = max(area, min(A[j], A[i]) * (j - i))

    return area
 
# Driver code

b = [ 7,3 ]
len2 = len(b)

print(maxArea(b, len2))
