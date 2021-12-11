# beginning hours
hours = int(input("Beginning (Hours): "))

# beginning minutes
mins = int(input("Beginning (Minutes): "))

# duration minutes
duration = int(input("Duration (Minutes): "))

''' To get the hours of the total time duration, we add our beginning minutes and our duration.
After adding it together we // 60 because there's 60 minutes in 1 hour. Then we % 24 because
there's 24 hours in a day. Finally we add our beginning hours to the hours computed before.'''
end_hours =  str(((hours + (mins + duration)//60)%24))

'''To better understand, this is a break down of what happened: 
mins (17) + duration (59) = 76 
hours (76) // 60 (60 minutes in 1 hour) = 1
hours (1) % 24 (24 hours in a day) = 1
hours (1) + 12 (1 hour + our beginning hours) = 13

that's why our end_hours became 13
'''

'''To get the minutes of the total time duration, we add our beginning minutes and our duration then
% 60 because there's 60 minutes in 1 hour'''
end_mins = str((mins + duration) % 60)

'''To better understand, this is a break down of what happened:
mins (17) + duration (59) = 76
mins (76) % 60 (60 minutes in 1 hour) = 16

that's why our end_mins became 16
'''
# format the end result to look more representable
print("The total time duration is", end_hours + ":"+ end_mins)
