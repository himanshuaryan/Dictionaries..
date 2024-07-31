states = ("Andhra Pradesh","Arunachal Pradesh","Assam","Bihar","Chhattisgarh","Goa","Gujarat","Haryana","Himachal Pradesh","Jharkhand","Karnataka","Kerala","Madhya Pradesh","Maharashtra","Manipur ","Meghalaya","Mizoram","Nagaland ","Odisha","Punjab","Rajasthan","Sikkim","Tamil Nadu","Telengana","Tripura","Uttarakhand","Uttar Pradesh","West Bengal")

cos  = ("Amaravati","Itanagar","Dispur","Patna","Raipur","Panaji","Gandhinagar","Chandigarh","Shimla","Ranchi","Bangalore","Thiruvananthapuram","Bhopal","Mumbai","Imphal","Shillong","Aizawl","Kohima","Bhubaneswar","Chandigarh","Jaipur","Gangtok","Chennai","Hyderabad","Agartala","Dehradun", "Lucknow","Kolkata")

unTerr =("Andaman And Nicobar Islands","Chandigarh","Dadra And Nagar Haveli And Daman And Diu","Delhi","Jammu And Kashmir","Ladakh","Lakshadweep",
"Puducherry")

cout = ("Port Blair", "Chandigarh", "Daman","New Delhi", "Srinagar", "Leh", "Kavaratti", "Puducherry")

stateswithcapital = dict(zip(states,cos))
utwithcapital = dict(zip(unTerr,cout))

def state(key):
    """Enter the correct name of state, union territory or it's capital, let system display about it.."""
    if key in stateswithcapital.keys():
        return stateswithcapital.get(key)
    elif key in utwithcapital.keys():
        return utwithcapital.get(key)

def Capital(d, value):
        for s, c in d.items():
            if c == value:
                return s
        return None          

print(f"""{"by @himanshuaryan".center(117)}
{"States and Union Territory and their Capital".center(65)}
\n{state.__doc__}\n""")

press = input("Do you want show Indian states or union territory with their capital (Yes or No) : ").title()
if press == "Yes":
    state_or_ut = input("\tState or Union Territory : ").title()
    
    if state_or_ut == "State":
        for st, cap in stateswithcapital.items(): # displya each state with its capital
            print(f"\n    State   : {st}")
            print(f"    Capital : {cap}")
        also = input("\nAlso show Union Territories (Yes or No) : ").title() 
        if also == "Yes":
                for ut, cap in utwithcapital.items():
                    print(f"\n    U.T.   : {ut}")
                    print(f"    Capital : {cap}")
                    
    elif state_or_ut == "Union Territory":
        for ut, cap in utwithcapital.items(): # display each union territory with its capital
            print(f"\n    U.T.   : {ut}")
            print(f"   Capital : {cap}")
        also = input("\nAlso show states (Yes or No) : ").title() 
        if also == "Yes":
                for st, cap in stateswithcapital.items():
                    print(f"\n    State   : {st}")
                    print(f"    Capital : {cap}")


name = input("\n\nEnter the place name : ").title()

print(" ")

while (name not in states) or (name not in unTerr) :
    if name in utwithcapital.keys():
        print("\n",state.__doc__)
        cap = f"{name} is an Union Territory of INDIA.              \n{state(name)} is the capital of {name}."
        print(cap)
        break
    elif name in stateswithcapital.keys():
        cap = f"{name} is a state of INDIA.                               \n{state(name)} is the capital of {name}."
        print(cap)
        break
    elif (name in utwithcapital.values()):
        un_trt= Capital(utwithcapital, name)
        print(f"{name} is the capital of {un_trt}.")
        break
    elif (name in stateswithcapital.values()):
        State = Capital(stateswithcapital, name)
        print(f"{name} is the capital of {State}.")    
        break
    else:
        print("Please Enter correct name.")
        name = input("Enter the state name : ").title()
