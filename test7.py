n = int(input("Enter the number:"))
if(n>0):
    def countstrings(n, start):
        if n == 0:
            return 1
        cnt = 0
        for i in range(start, 5):
            cnt += countstrings(n - 1, i)
        return cnt
    def countVowelStrings(n):
        return countstrings(n, 0)
    print(countVowelStrings(n))
else:
    print("Not valid")
