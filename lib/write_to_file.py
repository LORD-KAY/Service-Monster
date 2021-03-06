import os
import re
from variables import Platform

init_d = Platform()
distros  = init_d.dist()
directory = 'console/os.txt'

# Getting the distro from the distros
distro = distros[0]
regex_exp = re.compile(r'\"')
filter_distro = regex_exp.sub('',distro)

filename = '../console/os.txt'
try:
	if not os.path.exists(filename):
		with open(filename,'w+') as file:
			file.write(filter_distro)
			file.close()
	else:
		with open(filename,'w') as file:
			file.write(filter_distro)
			file.close()
except Exception as e:
	raise e
	print("Could not open file for writing ..")
