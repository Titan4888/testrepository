#print("Do you wanna hear a quote ? ")
#answer = input()
#
#if answer == 'Yes' or answer == 'yes':
#    print("I think, therefore I am")
#    #Rene Descartes
#elif answer == 'No' or answer == 'no':
#    print("Fine.")
#else:
#    print("I don't Understand.")
    
print("Do you wanna hear a quote ? ")
answer = input()
affirmative_responses = ["yes","y"]
neg_responses = ["no","n"]

if answer.lower() in affirmative_responses:
    print("I think, therefore I am")
    #Rene Descartes
elif answer.lower() in neg_responses:
    print("Fine.")
else:
    print("I don't Understand.")