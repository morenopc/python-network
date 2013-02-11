How to play   
===========  
About the network enviroment
----------------------------

There are three networks:
-------------------------

201.10.0.0
Router01
Switch01
Host01~04


200.171.0.0
Router02
Switch02
Host05~08


192.168.0.0
Router03
Switch03
Host09~12


Routers:
--------
Router01 can communicate with Router02;
Router02 can communicate with Router01 and 03;
and Router03 can communicate with Router02.

Switchs:
The Switchs make the communication
between the Router and the Hosts.

Start to play:
--------------
To start to play you need to turn on a host (click on host you want), connect cables and open the terminal (click on the Terminal button).

To know which commands you can use in the terminal type help (@169.254.0.0:~$ help) and press enter to see the command list.

Use the command ping IP to test if there is communication between two hosts.

Command list:
-------------
help get (this) commands list
ping [ip address] get ping
ifconfig get host information
ifconfig [ip address] set IP
netmask [mask address] set mask
ifconfig [ip address] netmask [mask address] set IP and Mask
route get host routes
clear clean bash
bash --version see bash version
date get today date