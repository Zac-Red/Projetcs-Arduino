import pyfirmata, time

port='COM5'

board=pyfirmata.Arduino(port)

for x in range(3):
    board.digital[8].write(0)
    time.sleep(0.5)
    board.digital[8].write(1)
    time.sleep(0.3)
    board.digital[8].write(0)
    
    
    board.digital[9].write(0)
    time.sleep(0.5)
    board.digital[9].write(1)
    time.sleep(0.3)
    board.digital[9].write(0)
    
    
    board.digital[10].write(0)
    time.sleep(0.5)
    board.digital[10].write(1)
    time.sleep(0.3)
    board.digital[10].write(0)
    
      
    
    board.digital[9].write(0)
    time.sleep(0.5)
    board.digital[9].write(1)
    time.sleep(0.3)
    board.digital[9].write(0)
    
      
    board.digital[10].write(0)
    time.sleep(0.5)
    board.digital[10].write(1)
    time.sleep(0.3)
    board.digital[10].write(0)
    
    
    board.digital[9].write(0)
    time.sleep(0.5)
    board.digital[9].write(1)
    time.sleep(0.3)
    board.digital[9].write(0)
    
     
    board.digital[8].write(0)
    time.sleep(0.5)
    board.digital[8].write(1)
    time.sleep(0.3)
    board.digital[8].write(0)
board.exit()
