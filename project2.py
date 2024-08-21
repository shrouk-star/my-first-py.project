def translator ( pharse):
    translation= ""
    for letter in pharse:
       if letter in "aiuoe":
           translation=translation + "g"
       else: translation = translation + letter
       
    return translation 
print(translator (input (" enter a pharse")))