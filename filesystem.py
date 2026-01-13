# # #-----------To read data -----------#

# # f = open("data.txt" , "r")

# # msg = f.read()
# # print(msg)
# # f.close()

# # #--------To write data on file------------#

# # q = "That's the thing about books. They let you travel without moving your feet."

# # f = open("data.txt" , "w")
# # f.write(q)
# # f.close()


# # #-----------To append data ----------------#

# # q = "\nA book is a device to ignite the imagination."

# # f = open("data.txt" , "a")
# # f.write(q)
# # f.close()

# #------------With ----------------#

# with open("data.txt") as f:
#     text = f.read()
#     print(text)


# #--------

# with open("data.txt") as f:
#     text = f.read()
#     input = input("Search by author : ")
#     if(input in text):
#         print(f"{input} quote is in quote library")
#     else:
#         print(f"{input} quote is not in quote library")


#-------------------------

import random

def game():
    # new_score = 67
    new_score = random.randint(1 , 100)
    with open("text.txt" , "r") as f:
        old_score = f.read()
        if(old_score != ""):
            old_score = int(old_score)
        else:
            old_score = 0
    
    print(F"Your saved score is {old_score}")
    print(F"Your new score is {new_score}")

    if(new_score > old_score):
        with open("text.txt" , "w") as f :
            f.write(str(new_score))
            print(f"Your new score saved in file is {new_score}")


        



game()