from socket import *

target = str(input("Enter the target (IP or Domain name): ")) #Getting the target name or ip from the user input
port_list=[]

def port_speci(): #function for user to specify their choice of scanning method, i.e one port, sequence of ports, ranges of ports
    print("Port specifications options are\n1. one port\n2. sequence of ports (23,56,5443)\n3. range of ports (10-100)")
    user_input = input("Enter your choice number: ")
    if user_input == "1":
        options=int(input("Enter the port number to scan: "))
        port_list.append(options)
    if user_input == "2":
        options=str(input("Enter the port numbers to scan: " ))
        str_list=options.split(",")
        for i in str_list:
            j=int(i)
            port_list.append((j))
        
    if user_input == "3":
        options=str(input("Enter the port numbers range to scan: "))
        str_list=options.split("-")
        a=int(str_list[0])
        b=int(str_list[1])+1
        c=list(range(a,b))
        port_list.extend(c)
   
        


def converter():
    test=target.split(".")
    x=test[0].isalpha() #help to determine wheather the user entered ip address or domain name
    global target_ip #declared as global because it has to be accessable outside of the functions also 

    if x == 1: #1 as TRUE, 0 as FALSE
        try:
            target_ip = gethostbyname(target)
            print("IP Address for",target,":", target_ip)
        except:
            print("Unknown host") #Throws this if the user entered a wrong domain name or unreachable domain name
    else:
        target_ip=target
        print("IP Address:", target_ip) 
    


def portscan(target_ip,port):
            sock = socket(AF_INET, SOCK_STREAM)     #no need to write as "socket.AF_INET" because socket is imported as *
            status = sock.connect_ex((target_ip,port))
            if (status == 0):
                print("{+} "+ str(port) + " is Open")
            else:
                print("{+} "+ str(port) + " is Closed")
            sock.close()

converter()
port_speci()

for port in port_list:
    portscan(target_ip,port)

