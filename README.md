# macflood
MAC flooding script that sends broadcast Ethernet frames with randomized MAC addresses (with a fixed vendor prefix) to simulate CAM table flooding in a lab environment.

macflood is a simple MAC flooding tool built using Python and scapy.
It continuously sends Ethernet frames with random source MAC addresses
(preserving a specific vendor prefix/OUI) to the broadcast MAC address. This
can be used in a lab to simulate switch CAM table flooding.

⚠️ Offensive technique – use only in isolated labs and with explicit
permission.

Features

Uses a fixed vendor prefix for the MAC address, such as:

vendor = "b8:e8:56:"


Generates random MAC addresses by combining the vendor prefix with random bytes

Sends broadcast Ethernet/ARP frames with padding

Prints each generated MAC address before sending the packet

Requirements

Python 3

scapy

Root/administrator privileges

Install:

pip install scapy


Usage
sudo python3 macflood.py

Example output:

Invio con MAC: b8:e8:56:aa:bb:cc
Invio con MAC: b8:e8:56:dd:ee:ff
...


Disclaimer

This tool is intended for educational and lab simulation purposes only.
Do not run it on production or unmanaged networks.
