# Power Calculator

print("Create a function that takes voltage and current and returns the calculated power.")

def cal_power():
    voltage = int(input("Enter the Number of Voltage : "))
    current = int(input("Enter the Number of current : "))
    circuit_Power = (voltage*current)
    print("Calculated Circuit Power is -",str(circuit_Power))


cal_power()


# Program  not closed emmidately 

input("Please Click to Enter to End the Program ")