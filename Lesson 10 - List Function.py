#Make no mistake about it. People are followers. I actually have the guts to speak up for myself. 
lucky_numbers = [7, 644, 9253, 500, 100, 52] 

Super_Heroes = ["Superman","Superman", "Static Shock" , "Batman", "Hulk",]

Super_Heroes2 = Super_Heroes.copy()#makes a copy of original super_heroes variable

print(Super_Heroes2)

Super_Heroes.insert(1, "Storm") #added new superhero storm at index 1

Super_Heroes.remove("Batman") #removes batman from the list

Super_Heroes.pop() #removes last element from list

Super_Heroes.sort()

print(Super_Heroes)

print(Super_Heroes.index("Superman"))

print(Super_Heroes.count("Superman")) #will not count "superman" must be exact capitilization. Syntax is everything. 

Super_Heroes.clear() #clears list

print(Super_Heroes)

lucky_numbers.sort() #sorts numbers in ascending order 
lucky_numbers.reverse()#reverses numbers listed

print(lucky_numbers)

