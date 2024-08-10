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
           "MAC": "Media Access Control Address - a unique identifier assigned to network interfaces for communication on the physical network segment. It is represented in hexadecimal format, typically as six pairs of hexadecimal digits separated by colons or hyphens (e.g., 00:1A:2B:3C:4D:5E or 00-1A-2B-3C-4D-5E). Each pair represents 8 bits, so a MAC address is 48 bits (6 bytes) long.",
           "IT": "Information Technology -  a set of related fields that encompass computer systems, software, programming languages, and data and information processing, and storage",
           "API":"Application Programming Interface - a set of rules, protocols, and tools that enables software applications to communicate with each other, exchange data, and share functionality. It acts as an intermediary between different software systems, allowing them to interact and integrate seamlessly.",
           }

print(BitcoinTerminology["CB"]) #Prints out 'Control Board')
      
print(BitcoinTerminology.get("GPS", "Not a Valid Key")) #typing in the key(acronym) will print out what it really stands for. 

#Make sure you review your punctuation. It can totally mess up your code

