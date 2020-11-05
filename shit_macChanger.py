import subprocess 

interface = wlan0
print("[$]-Changing MAC addr for " + interface)

subprocess.call("ifconfig wlan0 down", shell=True)
subprocess.call("ifconfig wlan0 hw ether 00:33:22:44:55", shell=True)
subprocess.call("ifconfig wlan0 up", shell=True)
