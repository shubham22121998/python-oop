def change(strng):
    print("id before calling the method",id(strng))
    strng=strng
    print("id after calling the methed",id(strng))

s1=(1,2,3)
change(s1)
