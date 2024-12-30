my_list =[9, 3, 3, 6]

#    print(num**2)


# comprehension list 
[print(x**2) for x in my_list]

paragraph = "create string type variables, I love Python"

#for sentance in paragraph.split(","):
   # print(sentance)
    #for word in sentance.split():
        #print(word)



[print(word) for sentance in paragraph.split(",") for word in sentance.split()]