#####################
# run linux command #
#####################


import subprocess
from time import sleep
from typing import Text

def linux():
    import os
    os.system('pwd')
    # using shell
    p1 = subprocess.run("ls -la dne" ,shell=True, capture_output=True,text=True, check=True)
    # using shell
    #p1 = subprocess.run(["ls ","-la" ])
    # to get the return code
    
 
    print(p1.returncode)
    print(p1.stdout)
    print(p1.stderr)
#
# poll return None if the process is active otherwise return the code of the process
#
def pollSub():
    procss = subprocess.Popen(["sleep", "2"])
    
    while  procss.poll() is None:
        print("still active")
    print(procss.poll())
        
pollSub()

