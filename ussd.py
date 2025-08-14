balance=float(input("Enter your balance here: "))
print("*432# for balance and *312# for data")
ussd= input("Enter USSD here: ")
if ussd=="*432#":
    print(f"Your account balance is: {balance:.2f}")
elif ussd=="*312#":
    print('''Welcome to data bundles
    1. Daily plans
    2. Weekly plans 
    3. Monthly plans''')
#operations for daily plan
    data_plan=input("Enter an option's number: ")
    if data_plan =="1":
        print('''Here are the daily plans
        1. #100 for 100mb
        2. #300 for 1gb
        3. #1000 for 4.2gb''')
        data_bundle = input("Pick a bundle ")
        if data_bundle =="1" and balance>=100:
            balance-=100
            print(f"You have received 100mb and your account balance is {balance:.2f}")
        elif data_bundle =="2" and balance>=300:
            balance-=300
            print(f"You have received 1gb and your account balance is {balance:.2f}")
        elif data_bundle=="3" and balance>=1000:
            balance-=1000
            print(f"You have received 4.2gb and your account balance is {balance:.2f}")
        elif data_bundle=="1" and balance<100:
            print("Transaction failed due to insufficient balance")
        elif data_bundle=="2" and balance<300:
            print("Transaction failed due to insufficient balance")
        elif data_bundle=="3" and balance<1000:
            print("Transaction failed due to insufficient balance")
        else:
            print("Invalid operation")
            #operations for weekly plan
    elif data_plan =="2":
        print('''Here are the weekly plans
        1. #1,000 for 2gb
        2. #1,500 for 5gb
        3. #2,000 for 15gb''')
        data_bundle = input("Pick a bundle ")
        if data_bundle=="1" and balance>=1000:
            balance-=1000
            print(f"You have received 2gb and your account balance is {balance:.2f}")
        elif data_bundle =="2" and balance>=1500:
            balance-=1500
            print(f"You have received 5gb and your account balance is {balance:.2f}")
        elif data_bundle =="3" and balance>=2000:
            balance-=2000
            print(f"You have received 15gb and your account balance is {balance:.2f}")
        elif data_bundle=="1" and balance<1000:
            print("Transaction failed due to insufficient balance")
        elif data_bundle=="2" and balance<1500:
            print("Transaction failed due to insufficient balance")
        elif data_bundle=="3" and balance<2000:
            print("Transaction failed due to insufficient balance")
        else:
            print("invalid operation")
        #operations for monthly plan
    elif data_plan =="3":
        print('''Here are the monthly plans
        1. 2,000 for 10gb
        2. 5,000 for 20gb
        3. 10,000 for 80gb''')
        data_bundle = input("Pick a bundle ")
        if data_bundle=="1" and balance>=2000:
            balance-=2000
            print(f"You have received 10gb and your account balance is {balance:.2f}")
        elif data_bundle =="2" and balance>=5000:
              balance-=5000
              print(f"You have received 20gb and your account balance is {balance:.2f}")
        elif data_bundle =="3" and balance>=10000:
              balance-=10000
              print(f"You have received 80gb and your account balance is {balance:.2f}")
        elif data_bundle=="1" and balance<2000:
             print("Transaction failed due to insufficient balance")
        elif data_bundle=="2" and balance<5000:
             print("Transaction failed due to insufficient balance")
        elif data_bundle=="3" and balance<10000:
             print("Transaction failed due to insufficient balance")
        else:
            print("Invalid operation")
    else:
        print("Invalid operation")
else:
    print("That USSD is not supported")
