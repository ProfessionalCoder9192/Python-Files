string =input("Write the word that you want to use:")
character =input("What character do you want to find in this word?:")
i=0
count=0
while(i<len(string)):

    if(string[i]== character):
        count = count + 1
    i = i+1

print("The total number of times that", character, "appeared was", count)