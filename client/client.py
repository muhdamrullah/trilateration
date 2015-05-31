import json
import requests
from urlparse import urlparse
from triangulate import triangulate

signalPower = 0
def pullApi(macAddress, ipAddress):
    http = 'http://'
    uri = '/todo/api/v1.0/tasks/'
    target = urlparse(http + ipAddress + uri + macAddress) #Combines uri and MAC address into a single line
    url = target.geturl() #Combines into a usable url function
    response = requests.get(url)
    data = response.json
    rawData =  data['Face']['power']
    return rawData

def enterMAC(str, ipstr):
    rawData = pullApi(str, ipstr) #Use the function pullApi to extract rawData
    SignalStrength = 80 + int(rawData)
    SignalPower = "{0:0.1f}".format(SignalStrength)
    return SignalPower
   
if __name__ == '__main__':
    MAC_default = raw_input("Enter the MAC Address: ");
    IP_first = raw_input("Enter the 1st IP Address: ");
    IP_second = raw_input("Enter the 2nd IP Address: ");
    SignalPower = enterMAC(MAC_default, IP_first)
    Signal1 = float(SignalPower)
    SignalPower = enterMAC(MAC_default, IP_second)
    Signal2 = float(SignalPower)

    coordinates = triangulate([(0.0, 0.0, Signal1), (25.0, 0.0, Signal2), (50.0, 0.0, 10.0)])
    #print Signal1
    #print Signal2
    print coordinates
#    str_second = raw_input("Enter the Mac Address: ");
#    ipstr_second = raw_input("Enter the IP Address: ");
#    pullApi(str_second, ipstr_second)
#    Signal2 = 80 + int(rawData)
#    print Signal2
