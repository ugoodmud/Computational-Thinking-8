cat_points = 0 
dog_points = 0 


answer = input ("witch is better A) waffles or B) pancakes?")
if answer =="A": 
     waffles_points += 1 
elif answer == "B":
     pancakes_points += 1


answer = input ("what animal is more useful? A) Dogs or B) cats")
if answer == "A": 
     dog_points += 1 
elif answer == "B": 
     cat_points += 1 


answer = input ("what food is more tasty? A) steak or B) chicken")
if answer == "A": 
     dog_points += 1 
elif answer == "B": 
     cat_points += 1 


answer = input ("what is the more addicting? A) TikTok or B) YouTube")
if answer == "A": 
     dog_points += 1 
elif answer == "B": 
     cat_points += 1 


answer = input ("what is the most poplar color? A) blue or B) pink")
if answer == "A" and dog_points < 2:
     print ("your a dog person!!!!")   

     answer = input ("what is cuter? (A puppies (B kittens")
if answer == "B" and dog_points < 2: 
     print ("your a cat person!!")