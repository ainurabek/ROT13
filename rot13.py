def rot13(letters):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    upper_alph = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    out_letters = ""
    for i in letters:
        if i in alphabet:
            out_letters += alphabet[(alphabet.find(i)+13)]
        elif i in upper_alph:
            out_letters += upper_alph[(upper_alph.find(i)+13)]
        else:
            out_letters += i
       
    return out_letters

letters = input("Write any letters: ")
print(rot13(letters))
