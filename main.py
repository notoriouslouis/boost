import subprocess
import time
import webbrowser
import random
from random import randint
import os
import ipaddress

#setting DEF functions
def validate_ip_address(address):
    try:
        ip = ipaddress.ip_address(address)
        print("IP address {} is valid".format(address, ip))
    except ValueError:
        print("IP address {} is not valid".format(address))
        time.sleep(0.5)

        #typewriter text
        if select == 1:
            text = "Please restart the script and enter a valid IP"
        else:
            text = "Please restart the script and generate a new IP"
        #start text
        for c in text:  # for each character in each line
            print(
                c,
                end='')  # print a single character, and keep the cursor there.
            sys.stdout.flush()  # flush the buffer
            sleep(0.05)  # wait a little to make the effect look good.
        print('')
        time.sleep(1000)


#animated header
lines = ["Mixcloud Booster", "Version 2.0"]
from time import sleep
import sys

for line in lines:  # for each line of text (or each message)
    for c in line:  # for each character in each line
        print(c,
              end='')  # print a single character, and keep the cursor there.
        sys.stdout.flush()  # flush the buffer
        sleep(0.05)  # wait a little to make the effect look good.
    print('')
    time.sleep(0.5)  # line break (optional, could also be part of the message)

time.sleep(0.75)
#setting IP config
select = int(input("\n\tMENU \n\t1) custom IP \n\t2) random IP \n\t+ "))
if select == 1:
    ip_set = input("Please enter a IP to use: ")
    proxy = {"https": ip_set, "http": ip_set}
else:
    import random
    ip_change = int(
        input(
            "\n\tDo you want a new IP every Hit? \n\t1) yes \n\t2) no \n\t+ "))
    ip_set = ".".join(map(str, (random.randint(0, 255) for _ in range(4))))

time.sleep(1)

show = int(
    input(
        "\n\tIP history \n\t1) show ip usage history \n\t2) dont show ip usage history \n\t+ "
    ))

#opens history
with open('IP.history.txt') as f:
    time.sleep(2)
    ip_history = f.readlines()

if show == 1:
    time.sleep(1)
    print(ip_history)
    time.sleep(2)
    for i in range(0, 5):
        print("\n")
        time.sleep(0.1)
else:
    time.sleep(1)

time.sleep(1)
print("Saving IP, Please wait")
time.sleep(1)
f = open("IP.history.txt", "a")
f.write(ip_set + "\n")
print("IP: " + ip_set + " Has Been Saved To IP.history.txt")
f.close()

time.sleep(1)
print("Connecting to IP: " + ip_set)
for i in range(0, 3):
    print("Connecting .")
    time.sleep(0.25)
    print("Connecting . .")
    time.sleep(0.5)
    print("Connecting . . .")
    time.sleep(0.3)

time.sleep(1)

#check if IP works
validate_ip_address(ip_set)

time.sleep(2)

with open('url.txt') as f:
    url = str(f.readlines())
    print("found link:")
    time.sleep(0.5)
    print(url)
    print("\n")
time.sleep(1)
low = int(input("Enter minimum time to run in seconds: "))
time.sleep(1)
high = int(input("Enter maximum time to run in seconds: "))
time.sleep(1)
view = int(input("How many hit attempts do you want? "))
lowt = low * 60
hight = high * 60

for i in range(0, view):
    chrome_path = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s --incognito'

    webbrowser.get(chrome_path).open_new(url)
    randomnum = randint(low, high)
    time.sleep(randomnum)
    print("Attempting hit", i, "for", randomnum, "seconds")

    if select == 2:
        if ip_change == 1:
            ip_random = ".".join(
                map(str, (random.randint(0, 255) for _ in range(4))))
            time.sleep(0.5)
            print("Using new IP: " + ip_random)
            time.sleep(0.5)
            validate_ip_address(ip_random)
            time.sleep(5)

        else:
            time.sleep(0.5)
            print("using IP: " + ip_set)
    else:
        time.sleep(0.5)
        print("Used IP: " + ip_set)
    time.sleep(5)
print("Views have been sent")

time.sleep(2)

#scrape option
scrape = int(input("\n\tScrape IP \n\t1) yes \n\t2) no \n\t+ "))
if scrape == 1:
  amount = int(input("How many IP do you want: "))
  am1 = amount + 1
  for i in range(0, am1):
    scraper = ".".join(map(str, (random.randint(0, 255) for _ in range(4))))
    IP_list = str(amount)
    f = open(IP_list + "_IP.txt", "a")
    f.write(scraper + "\n")
    time.sleep(0.025)
    validate_ip_address(scraper)
  print("Scraped IP to IP_Scrape.txt")
