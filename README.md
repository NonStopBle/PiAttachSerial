**I found how to fix UARTs of raspberry by using another UARTs of raspberry pi 4 because rpi4 has 6 UARTs port .**

Example :

 - UART0 , UART1 , UART2 , UART3 , UART4 , UART5

My Devices : 

 - RPI : Raspberry Pi 4 Model B (MASTER)
 - OS : Ubuntu Mate 20.04
 - SLAVE : Teensy 4.1 (Communicate with raspberry pi 4)

References 

 - [Raspberry Pi Pinout][1]
 - [Raspberry Pi UARTs Configuration][2]

You can enable UARTs on RPi4 by editing files /boot/config.txt and add 

    dtoverlay=uartx

x is the number of your UARTs

or

Use my scripts :  sudo python3 attach_serial.py  (not forget sudoo ~!!!)

Requirement :
 - pip install pyserial

1.Before enabling UARTS you can see only /dev/ttyAMA0 

 ![alt text](https://i.imgur.com/Eb6KKW6.png)

2.Select your UARTS (restart required)

 ![alt text](https://i.imgur.com/pDndKV4.png)
 
3.After enabling UARTS you can see another ttyAMA

 ![alt text](https://i.imgur.com/boxuh9u.png)
 
4.Testing Sending & Receiving Serial Communication by ttyAMA

 ![alt text](https://i.imgur.com/mRJm2lg.png)

 







Question (What is path of UARTs): 
 
 - /dev/ttyACM0 - /dev/ttyACM5

  [1]: https://pinout.xyz/pinout/uart
  [2]: https://raspberrypi.stackexchange.com/questions/104464/where-are-%20the-uarts-on-the-raspberry-pi-4
