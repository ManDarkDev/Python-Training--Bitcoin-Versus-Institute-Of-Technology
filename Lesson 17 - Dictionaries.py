#Dictionaries are a built-in data type that store key-value pairs. 
#They are unordered, mutable, and indexed by keys, which can be of any immutable type (like strings, numbers, or tuples)

'Bitcoin Mining Dictionary'

BitcoinTerminology = {
           "PSU": "Power Supply Unit",
           "HB": "Hashboard",
           "CB": "Control Board",
           "TH/s": "Terrahash per second",
           "IP": "IP Address",
           "SN": "Serial Number",
           "MAC": "Media Access Control Address", 
           "IT": "Information Technology"
           }

print(BitcoinTerminology["CB"]) #Prints out 'Control Board')
      
print(BitcoinTerminology.get("GPS", "Not a Valid Key")) #typing in the key(acronym) will print out what it really stands for. 

#Make sure you review your punctuation. It can totally mess up your code

