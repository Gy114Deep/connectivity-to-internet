import os #import os- Gives access to python to the operating system.
ip_input=(input(" your ip address is- "))
ip_list= ip_input.split(",")
if len(ip_list)>5:
    print("you give values out of limit😧")
    raise ValueError
else:print("go ahead")
for ip in ip_list:
        response=os.system(f"ping -n 1{ip}" 
            if os.name=='nt' else f"ping -c1{ip}")#for Window(nt) or Linux(posix).
        if response==0:
            print(f'{ip} is up ✔️') 
        else:
            print(f'{ip} is down ❌')
        import ipaddress
        def check_ip_type(ip):
            check_ip =ipaddress.ip_address(ip.strip())
            if check_ip.is_private:
                print("it is a private address")
        def check_ip_valid(ip):
            try:
                ipaddress.ip_address(ip.strip())
                print("valid")
            except:
                  print(f"not valid {ip}")
for ip in ip_list:
            check_ip_type
            check_ip_valid(ip)
