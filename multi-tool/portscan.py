from socket import *
import time
startTime = time.time()

banner = """
                                                
                                                
`7MMF'  `7MMF'                     `YMM'   `MP' 
  MM      MM                         VMb.  ,P   
  MM      MM  ,pP""Yq.       ,AM      `MM.M'    
  MMmmmmmmMM 6W'    `Wb     AVMM        MMb     
  MM      MM 8M      M8   ,W' MM      ,M'`Mb.   
  MM      MM YA.    ,A9 ,W'   MM     ,P   `MM.  
.JMML.  .JMML.`Ybmmd9'  AmmmmmMMmm .MM:.  .:MMa.
                              MM                
                              MM                ,

"""
print(banner)

if __name__ == "__main__":
    target = input('Host IP Gir root/kali$ ')
    t_IP = gethostbyname(target)
    print('Port Taranmaya Başladı: ', t_IP)

    for i in range(50, 500):
        s = socket(AF_INET, SOCK_STREAM)

        conn = s.connect_ex((t_IP, i))
        if (conn == 0):
            print('Port %d: Açık' % (i,))
        s.close()
print("Şu kadar sürdü:", time.time() - startTime)
