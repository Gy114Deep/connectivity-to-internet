import csv  #checking private or public with #csv# file.
import ipaddress
def is_ip_private(ip_str):
    try:
        List=ipaddress.ip_address(ip_str.strip())
        if List.is_private:
            print("yes it is private".upper())
        else:
            print("No!it is PUBLIC")
    except ValueError:
        print("sorry! error".capitalize())
with open("type(csv).csv","r")as file:
    reader=csv.reader(file)
    for row in reader:
        ip_input=row[0],row[1]
        for ip in row:
            is_ip_private(ip)