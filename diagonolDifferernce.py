def fibCheck(n):
    if(n<=1):
        print(n)
    else:
        return fibCheck(n-1) + fibCheck(n-2)
    


fibCheck(10)