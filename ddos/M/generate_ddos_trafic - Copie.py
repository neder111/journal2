from mininet.topo import Topo
from mininet.net import Mininet
# from mininet.node import CPULimitedHost
from mininet.link import TCLink
# from mininet.util import dumpNodeConnections
from mininet.log import setLogLevel
# from mininet.cli import CLI
from mininet.node import OVSKernelSwitch, RemoteController
from time import sleep

from datetime import datetime
from random import randrange, choice

class MyTopo( Topo ):

    def build( self ):

        s1 = self.addSwitch( 's1', cls=OVSKernelSwitch, protocols='OpenFlow13' )

        h1 = self.addHost( 'h1', cpu=1.0/20,mac="00:00:00:00:00:01", ip="10.0.0.1/24" )
        h2 = self.addHost( 'h2', cpu=1.0/20, mac="00:00:00:00:00:02", ip="10.0.0.2/24" )
        h3 = self.addHost( 'h3', cpu=1.0/20, mac="00:00:00:00:00:03", ip="10.0.0.3/24" )    

        s2 = self.addSwitch( 's2', cls=OVSKernelSwitch, protocols='OpenFlow13' )

        h4 = self.addHost( 'h4', cpu=1.0/20, mac="00:00:00:00:00:04", ip="10.0.0.4/24" )
        

        s3 = self.addSwitch( 's3', cls=OVSKernelSwitch, protocols='OpenFlow13' )

        

        

        

        # Add links

        self.addLink( h1, s1 )
        self.addLink( h2, s1 )
        self.addLink( h3, s2 )

        self.addLink( h4, s2 )
        

        self.addLink( s2, s3 )
        self.addLink( s1, s3 )
        
def ip_generator():

    ip = ".".join(["10","0","0",str(randrange(1,5))])
    return ip

def startNetwork():

    #print "Starting Network"
    topo = MyTopo()
    #net = Mininet( topo=topo, host=CPULimitedHost, link=TCLink, controller=None )
    #net.addController( 'c0', controller=RemoteController, ip='127.0.0.1', port=6653 )

    c0 = RemoteController('c0', ip='127.0.0.1', port=6653)
    net = Mininet(topo=topo, link=TCLink, controller=c0)

    net.start()

    h1 = net.get('h1')
    h2 = net.get('h2')
    h3 = net.get('h3')
    h4 = net.get('h4')
    
    
    hosts = [h1, h2, h3, h4]
    
    h1.cmd('cd /home/mininet/webserver')
    #h1.cmd('python3 -m http.server 80')
    h2.cmd('cd /home/mininet/webserver')
    #h2.cmd('python3 -m http.server 80')
    h1.cmd('mosquitto -v')
    h2.cmd('mosquitto -v')
    
    
    src = choice(hosts)
    dst = ip_generator()   
    print("--------------------------------------------------------------------------------")
    
    #h4 mqtt attacks to h1 and h2    
    src = choice(hosts)
    dst = ip_generator()   
    print("--------------------------------------------------------------------------------")
    print("Performing Mqtt Attack on h1")  
    print("--------------------------------------------------------------------------------")   
    h4.cmd('python3 MQTT_SlowDoS.py -a 10.0.0.1 -p 1883 -k 60')
    sleep(100)  
    src = choice(hosts)
    dst = ip_generator()   
    print("--------------------------------------------------------------------------------")
    print("Performing LAND Attack in  h1")  
    print("--------------------------------------------------------------------------------")   
    h4.cmd('python3 client_pub.py -a 10.0.0.1 -p 1883 -k 60')  
    sleep(100) 
    src = choice(hosts)
    dst = ip_generator()   
    print("--------------------------------------------------------------------------------")
    print("Performing LAND Attack in h1")  
    print("--------------------------------------------------------------------------------")   
    h4.cmd('python3 client_sub.py -a 10.0.0.1 -p 1883 -k 60')  
    sleep(100) 
    print("--------------------------------------------------------------------------------")

    src = choice(hosts)
    dst = ip_generator()   
    print("--------------------------------------------------------------------------------")
    print("Performing Mqtt Attack on h2")  
    print("--------------------------------------------------------------------------------")   
    h4.cmd('python3 MQTT_SlowDoS.py -a 10.0.0.2 -p 1883 -k 60')
    sleep(100)  
    src = choice(hosts)
    dst = ip_generator()   
    print("--------------------------------------------------------------------------------")
    print("Performing MQTT Attack in  h2")  
    print("--------------------------------------------------------------------------------")   
    h4.cmd('python3 client_pub.py -a 10.0.0.2 -p 1883 -k 60')  
    sleep(100) 
    src = choice(hosts)
    dst = ip_generator()   
    print("--------------------------------------------------------------------------------")
    print("Performing MQTT Attack in h2")  
    print("--------------------------------------------------------------------------------")   
    h4.cmd('python3 client_sub.py -a 10.0.0.2 -p 1883 -k 60')  
    sleep(100) 
    print("--------------------------------------------------------------------------------")


    #h3 mqtt attacks to h1 and h2
    src = choice(hosts)
    dst = ip_generator()   
    print("--------------------------------------------------------------------------------")
    print("Performing Mqtt Attack on h1")  
    print("--------------------------------------------------------------------------------")   
    h3.cmd('python3 MQTT_SlowDoS.py -a 10.0.0.1 -p 1883 -k 60')
    sleep(100)  
    src = choice(hosts)
    dst = ip_generator()   
    print("--------------------------------------------------------------------------------")
    print("Performing LAND Attack in  h1")  
    print("--------------------------------------------------------------------------------")   
    h3.cmd('python3 client_pub.py -a 10.0.0.1 -p 1883 -k 60')  
    sleep(100) 
    src = choice(hosts)
    dst = ip_generator()   
    print("--------------------------------------------------------------------------------")
    print("Performing LAND Attack in h1")  
    print("--------------------------------------------------------------------------------")   
    h3.cmd('python3 client_sub.py -a 10.0.0.1 -p 1883 -k 60')  
    sleep(100) 
    print("--------------------------------------------------------------------------------")

    src = choice(hosts)
    dst = ip_generator()   
    print("--------------------------------------------------------------------------------")
    print("Performing Mqtt Attack on h2")  
    print("--------------------------------------------------------------------------------")   
    h3.cmd('python3 MQTT_SlowDoS.py -a 10.0.0.2 -p 1883 -k 60')
    sleep(100)  
    src = choice(hosts)
    dst = ip_generator()   
    print("--------------------------------------------------------------------------------")
    print("Performing MQTT Attack in  h2")  
    print("--------------------------------------------------------------------------------")   
    h3.cmd('python3 client_pub.py -a 10.0.0.2 -p 1883 -k 60')  
    sleep(100) 
    src = choice(hosts)
    dst = ip_generator()   
    print("--------------------------------------------------------------------------------")
    print("Performing MQTT Attack in h2")  
    print("--------------------------------------------------------------------------------")   
    h3.cmd('python3 client_sub.py -a 10.0.0.2 -p 1883 -k 60')  
    sleep(100) 
    print("--------------------------------------------------------------------------------")



    # CLI(net)
    net.stop()

if __name__ == '__main__':
    
    start = datetime.now()
    
    setLogLevel( 'info' )
    startNetwork()
    
    end = datetime.now()
    
    print(end-start)