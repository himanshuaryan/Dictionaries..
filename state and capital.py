states = ("Andhra Pradesh","Arunachal Pradesh","Assam","Bihar","Chhattisgarh","Goa","Gujarat","Haryana","Himachal Pradesh","Jharkhand","Karnataka","Kerala","Madhya Pradesh","Maharashtra","Manipur ","Meghalaya","Mizoram","Nagaland ","Odisha","Punjab","Rajasthan","Sikkim","Tamil Nadu","Telengana","Tripura","Uttarakhand","Uttar Pradesh","West Bengal")

cos  = ("Amaravati","Itanagar","Dispur","Patna","Raipur","Panaji","Gandhinagar","Chandigarh","Shimla","Ranchi","Bangalore","Thiruvananthapuram","Bhopal","Mumbai","Imphal","Shillong","Aizawl","Kohima","Bhubaneswar","Chandigarh","Jaipur","Gangtok","Chennai","Hyderabad","Agartala","Dehradun", "Lucknow","Kolkata")

unTerr =("Andaman and Nicobar Islands","Chandigarh","Dadra and Nagar Haveli and Daman & Diu","Delhi","Jammu & Kashmir","Ladakh","Lakshadweep",
"Puducherry")

cout = ("Port Blair", "Chandigarh", "Daman","Delhi", "Srinagar", "Leh", "Kavaratti", "Puducherry")

stateswithcapital = dict(zip(states,cos))
utwithcapital = dict(zip(unTerr,cout))

def state(place):
    """Enter the correct name of the state, let system display
it's capital."""
    if place in stateswithcapital.keys():
        return stateswithcapital.get(place)
    elif place in utwithcapital.keys():
        return utwithcapital.get(place)
    else:
        print('Enter correct name of state.')
    
print(f"""{"by @himanshuaryan".center(117)}
{"States and their Capital".center(60)}
\n{state.__doc__}\n""")

name = input("Enter the state name : ").title()

while (name not in states) or (name not in unTerr) :
    if name in unTerr:
        cap = f"{name} is an Union Territory of INDIA. \n{state(name)} is the capital of {name}."
        print(cap)
        break
    elif name in states:
        cap = f"{name} is a state of INDIA. \n{state(name)} is the capital of {name}."
        print(cap)
        break
    else:
        print("Please Enter correct name.")
        name = input("Enter the state name : ").title()
