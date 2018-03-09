# BK PRECISION 
#Sample script to establish communication with a USBTMC instrument"

import visa   #Imports visa, package that helps you control instrumentation
    
try:
    #Open Connection
    manager = visa.ResourceManager()  #Creating a resource manager object
    manager.list_resources() #listing all available resources (COM Ports, etc)
    
    wavegen = manager.open_resource('USB0::0xF4ED::0xEE3A::448::INSTR') #Opens the Communication Port 
                                                                       #this can be copied from the previous command "List Resources"
    #Setting the baudrate                                           
    wavegen.baudrate = 9600    
        
    wavegen.timeout = 5000 #Set Timeout - 5 seconds
  
    wavegen.ask("*IDN?")  #Sends the command *IDN to the unit
  #  print wavegen.read() # Reads the response from the unit to previous command
   
 
    wavegen.write('C1: BSWV FRQ, 2000HZ')    #Changes current signal frequency of channel one to 2000 Hz.
    wavegen.write('C1: BSWV WVTP, SQUARE') #Changes channel 1 wave type to Square
    
    wavegen.write('C1:BSWV?')       #reads 'Wave type, Frequency, Period, Amplitude, Offset, High Level, Low Level, Phase'
    print wavegen.read()   #It reads previous query
    
    wavegen.write('C1: OUTP ON') # Turns the output on
    wavegen.write('C1: OUTP?') #Queries state of output
    print wavegen.read() #It reads previous query   
    
    wavegen.close() #Close Communication Port
    print 'close instrument connection'

finally:
    #perfomanager clean up operations
    print 'complete'