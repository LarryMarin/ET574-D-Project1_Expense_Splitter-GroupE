#add_expense function
#ask user for their name (make sure it is a valid name and not a number)
#ask the user to put a description of their expense (make sure it is a valid String and not numbers)
#to validate we can use try-except
#ask the user to input an amount

#all of this will be appended to a list in data.py
#we may need to use 2D list for all of this. in a 2D list we can store multiple lists inside. look at list2examples folder
#for 2D list examples

#view_all_expenses function
#we will print each item in the list (formatted correctly)
#we can use a for loop to go through the entire list
#since it is a 2D list we can use the index of the inner lists to print each item correctly
#ex list = [[1,2,3], [4,5,6]]
#in the for loop we can check the index for each item in the list [1,2,3] and print them out separately

#split_summary function:
#we ask the user to input the amount of people they want to split all the expenses in the list 
#this number will be used to divide the total expenses later

#we show the total of all expenses in the list:
#we can use a for loop to go through the outer list
#we check each inner list and check index 2 which will contain the expenses 
#the user inputs 3 things so we know the index is 0-2 and the third thing they entered was expense (which will be index 2)
#we can use format to print it out to 2 decimal places

#we can check the length of the outer list to get the number of expenses

#once we get the total expenses and the length of the outer list we can get the average
#avg = total_expenses / outerlist_length
#we can then use format to print it out to 2 decimal places

#while we go through the loop earlier to get the total expense we can check if the current expense is the highest expense every time and if it is save it.
#maybe we can use the max() function from lists? if not then we can manually check with an if statement

#lowest expense we can do the opposite of highest expense. check which is the lowest and save it. maybe we can use min() function from lists?

#for equal share we can divide the users input from earlier and divide total with it
#total_expenses / num_of_people
