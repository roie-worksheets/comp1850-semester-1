# Week 1.2, Session 2: Task 6
def get_number(text, type=int):
    try:
        return type(input(text))
    except ValueError:
        print("Invalid value entered")
        return get_number(text, type)

# Step 1
temperature = get_number("Enter the machine's temperature in ºC: ")
pressure = get_number("Enter the machine's pressure in PSI: ")
op_status = get_number("Enter the machine's status (0, 1): ")

unsafe_temp = False
unsafe_pressure = False

match temperature:
    case t if t > 80:
        unsafe_temp = True
    case t if 50 < t < 80:
        print("Machine's temperature is within safe limits.")
    case t if t < 50:
        print("Machine temperature is low and no further action is required.")

match pressure:
    case t if t > 100:
        unsafe_pressure = True
    case t if 70 < t < 100:
        print("Machine's pressure is stable.")
    case t if t < 70:
        print("Machine pressure is low and no further action is required.")

if op_status == 1:
    if unsafe_temp:
        print("Machine's temperature is too high, shut it down.")
    elif unsafe_pressure:
        print("Machine's pressure is too high, maintenance recommended.")
    else:
        print("Machine is operating normally.")
else:
    print("Machine is not running so no immediate action is needed.")
