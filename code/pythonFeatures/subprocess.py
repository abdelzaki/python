#####################
# run linux command #
#####################


import subprocess
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
    
linux()