#!/usr/bin/env/python #for python v3
#!/usr/bin/env/python3 #for python v3
#! python3 

"""
    the python shebang at the start of each python file we create is the directive that tells the OS how to handle this specefic file
    however the shebang line is not mandatory but its a common practice to inclute this at the start of our file and it allows us to run this as an executable.
"""
import updateCheck
import subprocess
import re

updateCheck

print("[+] =============================================================================================================== [+]")
print("[+] script name : EttherForge.py")
print("[+] @auther == happy-kitty0821 on github [+]")
print("[+] this script is just for educational and testing purposes [+]")
print("[+] this script doesnot gurantees 100% working rate and anonimity [+]")
print("[+] the users must ust this script on their own risk [+]")
print("[+] if you agree to the terms and conditions please type y or yes and press enter [+]")
print("[+] Please note that changing the MAC address of a network interface may have legal and ethical implications [+]")
print("[+] it's important to ensure you have proper authorization to do so [+]")
print("[+]                                       EtherForge v0.0.001 beta  [+]") 
print("[+] ================================================================================================================ [+]")

print("")
print("[+] if you've read and agreed to the terms and conditions please type 'y'or 'yes' to use this script [+]")

confirmation = input("-->>> ").lower
if confirmation == "y" or confirmation == "yes":
    
    #Get the available network interfaces
    
    result = subprocess.run(['ifconfig'], capture_output=True, text=True)
    print(result.stdout)
    
    print("[+] Please select the interface you want to change the MAC address of:    [+]")
    print("[+] MAC address format: XX:XX:XX:XX:XX:XX, where X is a hexadecimal digit [+]")
    interfaceChoice = input("[+] -->> ")
    
    #Validate and prompt for a new MAC address
    
    while True:
        CustomMacAddress = input("[+] Enter the new MAC address: ")
        
        if re.match(r'^([0-9A-Fa-f]{2}:){5}[0-9A-Fa-f]{2}$', CustomMacAddress):
            break
        
        else:
            print("[+] Invalid MAC address format. Please try again. [+]")
    
    #Change the MAC address of the selected interface
    
    subprocess.run(['ifconfig', interfaceChoice, 'hw', 'ether', CustomMacAddress])
    
    #finally putting the interface back online or enabling it
    
    subprocess.run(["ifconfig", interfaceChoice, "up"])
    
else:
    print("[+] imvalid input [+]") 
    print(" [+] exitinggg....[+]")