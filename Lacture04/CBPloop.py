#continue ไปวนต่อเลย
for letter in 'Narathip Rattanamanee':
    if letter == 'a' or letter == 'k':
        continue
    print ('current letter :', letter)
print()    
#หยุด เดี่ยว นี้
for letter in 'Uzumaki Naruto':
    if letter == 'a' or letter == 'k':
        break
    print ('current letter :', letter)
print()        
#ไปต่อ
for letter in 'Uchiha Sasuke':
    if letter == 'a' or letter == 'k':
        pass
    print ('current letter :', letter)