#List all consonants in the word 
# “ to access our personalized programs, webinars and live events so you can start to heal your attachment style and improve all your relationships.”

word = 'to access our personalized programs, webinars and live events so you can start to heal your attachment style'
conS = " ",'a', 'e', 'i', 'o', 'u', ',' 

consOnant = [c for c in word if c  not in conS ]
print(consOnant)
print(len(consOnant))

