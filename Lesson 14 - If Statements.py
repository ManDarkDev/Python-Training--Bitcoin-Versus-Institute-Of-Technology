#Do the right thing. It's easy to be a bad person. Try something different. 
is_rich = True
is_poppin = True
is_poor = False

if is_rich or is_poppin:
    print("You'd rather be rich than famous")
elif is_rich and not (is_poppin):
    print("You gotta bag")
elif not (is_rich) and is_poppin:
    print("You need to monetize your popularity")
else:
    print("You'd rather be famous and broke!")

#NawFR



