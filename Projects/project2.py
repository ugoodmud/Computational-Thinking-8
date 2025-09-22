waffles_points = 0 
pancakes_points = 0 


answer = input ("witch is better A) waffles or B) pancakes?")
if answer =="A": 
     waffles_points += 1 
elif answer == "B":
     pancakes_points += 1


answer = input("what animal is more useful? A) Dogs or B) cats")
if asnwer == "A": 
     dog_points += 1 
elif answer == "B": 
     cat_points += 1 


answer = input("what food is more tasty? A) steak or B) chicken")
if asnwer == "A": 
     steak_points += 1 
elif answer == "B": 
     chicken_points += 1 


answer = input("what is the more addicting? A) TikTok or B) YouTube")
if asnwer == "A": 
     TikTok_points += 1 
elif answer == "B": 
     YouTube_points += 1 


answer = input("what is the most poplar color? A) blue or B) pink")
if answer == "A" and blue_points > 3:
     print ("its blue!!!!")
     blue_points += 1 