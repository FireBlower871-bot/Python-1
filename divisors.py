def divisors():
    print("Enter a Number.\nI shall give you all of the divisors of that number.")
    num = int(input())   
    for i in range(1,num +1):
        if(num % i == 0):
            print(i)
    
    choice = replay()
    
    if choice == "Y" or choice =="y":
        divisors()
    elif choice == "N" or choice == "n":
        print("I hope you got the right divisors!")
        return
    else:
        "Remember to type Y if you want to continue, or N if you don't."
        choices()

def replay():
    print("Do you want to go again? (Y is yes, N if no.)")
    choice = input()

    return choice

divisors() 
