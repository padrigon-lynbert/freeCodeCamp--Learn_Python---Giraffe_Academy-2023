Male = True; Tall = False
if Male and Tall: print("M, Tall") 
elif Male and not(Tall): print("M, !Tall")
elif not(Male) and Tall: print("F, Tall")
else: print("F, !Tall")