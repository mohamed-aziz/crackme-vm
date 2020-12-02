import subprocess
import sys

with open("vm1.cpp", "r") as myfile:
    content = myfile.read()

out = subprocess.check_output(["/usr/bin/python2", "assembler.py"])
content =content.replace("PROGRAMHERE", out)


sys.stdout.write(content)
