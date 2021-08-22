def outfun():
    a=20
    def infun():
        nonlocal a
        a=30
        print("Value for b:",a)
    infun()
    print("Value for a:",a)
outfun()