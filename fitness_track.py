# create a list of exercises
upper_push = ["Dips", "Push Ups"]
upper_pull = ["Rows", "Pull Ups"]
lower_body = ["Squats", "Deadlifts"]
abs_exercise = ["Knee Raises", "Leg Raises"]
# a function that asks for the exercise that you did
def exercise_choice():
    exercise = ""
    print("What did you work on today? Type anything other than the options presented to exit")
    print("A: upper body pushing movements")
    print("B: upper body pulling movements")
    print("C: lower body movements")
    print("D: Abs")
    choice = input("Enter your choice here: ")
    if choice.upper() == "A":
        print("Which one did you do?")
        print("A: " + upper_push[0])
        print("B: " + upper_push[1])
        second_choice = input("Enter your choice here: ")
        if second_choice.upper() == "A":
            exercise = upper_push[0]
        elif second_choice.upper() == "B":
            exercise = upper_push[1]
        else:
            print("Invalid choice")
    elif choice.upper() == "B":
        print("Which one did you do?")
        print("A: " + upper_pull[0])
        print("B: " + upper_pull[1])
        second_choice = input("Enter your choice here: ")
        if second_choice.upper() == "A":
            exercise = upper_pull[0]
        elif second_choice.upper() == "B":
            exercise = upper_pull[1]
        else:
            print("Invalid choice")
    elif choice.upper() == "C":
        print("Which one did you do?")
        print("A: " + lower_body[0])
        print("B: " + lower_body[1])
        second_choice = input("Enter your choice here: ")
        if second_choice.upper() == "A":
            exercise = lower_body[0]
        elif second_choice.upper() == "B":
            exercise = lower_body[1]
        else:
            print("Invalid choice")
    elif choice.upper() == "D":
        print("Which one did you do?")
        print("A: " + abs_exercise[0])
        print("B: " + abs_exercise[1])
        second_choice = input("Enter your choice here: ")
        if second_choice.upper() == "A":
            exercise = abs_exercise[0]
        elif second_choice.upper() == "B":
            exercise = abs_exercise[1]
        else:
            print("Invalid choice")
    else:
        print("Invalid choice")
    return exercise
# a function that asks for the date
def today_date():
    month = int(input("In a number, what is the month?: "))
    if month > 12 or month < 1:
        print("That is not a month")
        exit()
    day = int(input("In a number, what is today?: "))
    if day < 1 or day > 31:
        print("That is not a valid day")
        exit()
# check to make sure the date is valid for each month
    if month == 2 and day > 28:
        print("That is not a valid date")
        exit()
    elif month == 9 or month == 4 or month == 6 or month == 11 and day > 30:
        print("That is not a valid date")
        exit()
    date = (str(month) + "/" + str(day))
    return date
# a function that asks for the sets and reps
def set_reps():
    sets = input("How many sets did you do?: ")
    reps = input("How many reps did you do?: ")
    sets_reps = sets + "x" + reps
    return sets_reps
def main():
    # create the file
    file = open("workouts.txt","a+")
    # enter the date
    print("First, let's enter the date")
    file.write(today_date() + "\n")
    workout = True
    while workout is True:
        print("Now, let's enter your exercise")
        file.write(exercise_choice() + " ")
        print("Now the sets and reps")
        file.write(set_reps() + "\n")
        next_exercise = input("Did you do another exercise? Yes (Y) or No (N): ")
        if next_exercise.upper() == "N":
            workout = False

if __name__=="__main__":
    main()
