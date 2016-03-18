import subprocess

print "-------------------------Gestore Repository-------------------------"
print "pulling from bare into nonb"
subprocess.call('git pull', shell=True)
print "nonb updated."
