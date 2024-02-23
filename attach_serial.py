import serial
import os

serial_checked = False


serial_ask_1 = str(input("Do you want to enable uart [Y/N] ? :"))
serial_ask_2 = ""
serial_name = ""
serial_bad = ""




def write_port():
    try:
      print("Selected : " , serial_name , " " , serial_bad)
      s = serial.Serial(port=serial_name , baudrate=serial_bad)
 #s = serial.Serial(port=serial_name, baudrate=serial_bad, bytesize=EIGHTBITS, parity=PARITY_NONE, stopbits=STOPBITS_ONE, timeout=None, xonxoff=False, rtscts=False, write_timeout=None, dsrdtr=False )
      print("Port correct !")
      serial_checked = True
    except Exception as e:
      print("Port failed ! : " ,e)
      serial_checked = False
    if(serial_checked == True):
        try:
           s.open()
           print("Port initial success !")
           while True:
       #s.write("0x0")
            print("Serial written !")
        except Exception as e:
            print("Port initial failed !" + str(e))
            if(str(e).find("is already") != 1):
              print("Starting writing data ..")
            while True:
              s.write(0x84)
              print("Reading : " + str(s.read()))
#	s.write("data")
#	print("serial writting in progress")


uart_select = 0

if(serial_ask_1.lower() == "y" or serial_ask_1.lower() == "yes"):
  
  print("RASPBERRY PI 4 UARTS")
  print("") 
  print("UART     GPIO PIN")
  print("UART0     14/15 (not recommend !)")
  print("UART1     14/15 (not recommend !)")
  print("UART2      0/1")
  print("UART3      4/5")
  print("UART4      8/9")
  print("UART5     12/13")
  print("")
  print("nothing script written by rezier")
  print("")


  print("")
  uart_select = int(eval(input("Which UARTS you choose [0-5] ? : ")))
  print("")
  try:

    bootloader = open("/boot/firmware/config.txt")
    if(str(bootloader.read()).__contains__("uart" + str(uart_select)) > 0):
      
      print("UART already opened !")
      print("")
    else:
      if(uart_select <= 5 and uart_select >= 0):   
       
       bootwritten = open("/boot/firmware/config.txt" ,  "a")
       bootwritten.write("\n" + "dtoverlay=uart" + str(uart_select))
       print("UART " + str(uart_select) + " : " + " ACTIVE !")
       print("")  
       str_ = str(input("Please restart to take effect [Y/N] "))
       print("")
       if(str_.lower() == "y" or str_.lower() == "yes"):
          bootwritten.close()
          print("Restarting !")
          os.system("sudo reboot")
       else:
          print("Trust me restart to enable your uarts !")
        
       print("")
  except Exception as e:
    if(str(e).__contains__("not")):
      print("No permission to openning uart : " + (e))
      print("")
  
else :
  print("")
  input_str = str(input("Starting serial communication tester ? [Y/N] : "))
  print("")
  if(input_str.lower() == "y" or input_str.lower() == "yes"):   
    var = os.system("ls -l /dev/ttyA*")
    print("")
    serial_name = str(input("enter your port url  : "))
    print("")
    serial_bad = int(eval(input("enter your baudrate : ")))
    print("")
    write_port()
  else:
    print("Goodbye sir !")



