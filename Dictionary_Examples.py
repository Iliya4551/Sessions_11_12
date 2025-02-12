d = {} #this is an empty dictionary
eng_to_spa = {"one": "uno", "two": "dos", "three": "tres"}
print(eng_to_spa)
eng_to_spa["i"] = "yo"
eng_to_spa["am"] = "soy"
eng_to_spa["spanish"] = "español"
print(eng_to_spa)
sentence = "i am spanish"
words = sentence.split()
for word in words:
    print(eng_to_spa[word])
eng_to_spa.update({"yes": "si", "no": "no"}) #this lets you update your dict. with a new dict.
print(eng_to_spa)
del eng_to_spa["no"] #that is how you remove a key/value from dict.
print(eng_to_spa)

print(eng_to_spa.popitem()) #popitem takes out the last item that was added. (not useful though because it is hard to know which is the last item you put.

print(eng_to_spa.pop("two")) #better to pop an item than popitem it because you specify the key

if "tree" in eng_to_spa:
    print(eng_to_spa["tree"])
else: #basically gives a command incase the "if" function doesn't work
    print("I don't know what that is blud")

print(eng_to_spa("tree", "unknown word"))

for key in eng_to_spa:
    print(f"{eng_to_spa[key]} means {key}")
