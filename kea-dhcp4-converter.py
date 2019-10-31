#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
#  kea-dhcp4-converter.py
#  
#  Copyright 2019 Erik Ostrom <eostrom@protonmail.com>
#  
#  This program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation; either version 2 of the License, or
#  (at your option) any later version.
#  
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#  
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software
#  Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
#  MA 02110-1301, USA.
#  
#  
import json, socket, sys
def main(argv):
	f = open("kea-dhcp4.conf", "r")
	kea = json.loads(f.read())
	f.close()
	o = open("output.txt", "a")

	for i in kea["Dhcp4"]["shared-networks"]:
		for j in (i["subnet4"]):
			# print(j["reservations"])
			# subnet = j["subnet"][:-3]
			# subnetmask = get_subnetmask(j["subnet"][-3:])

			# o.write('subnet ' + subnet + ' netmask ' + subnetmask + ' {\n')
			# o.write('\t authoritative;\n')
			# o.write('}\n')

			for k in (j["reservations"]):
				try:
					hostname = socket.gethostbyaddr(k["ip-address"])[0]
				except socket.herror:
					print("Couldn't get a hostname for " + k["ip-address"])
				else:
					o.write('host ' + hostname + ' {\n')
					o.write('\tfixed-address ' + k["ip-address"] + ';\n')
					o.write('\thardware ethernet ' + k["hw-address"] + ';\n')
					o.write('}\n')
			input("Press Enter to continue")


	for i in kea["Dhcp4"]["subnet4"]:
		for j in i["reservations"]:
			try:
				hostname = socket.gethostbyaddr(j["ip-address"])[0]
			except socket.herror:
				print("Couldn't get a hostname for " + j["ip-address"])
			else:
				o.write('host ' + hostname + ' {\n')
				o.write('\tfixed-address ' + j["ip-address"] + ';\n')
				o.write('\thardware ethernet ' + j["hw-address"] + ';\n')
				o.write('}\n')
			# 	print('}\n')
		input("Press Enter to continue")

def get_subnetmask(cidr):
	if(cidr=="/32"):
		return "255.255.255.255"
	elif (cidr=="/31"):
		return "255.255.255.254"
	elif (cidr=="/30"):
		return "255.255.255.252"
	elif (cidr=="/29"):
		return "255.255.255.248"
	elif (cidr=="/28"):
		return "255.255.255.240"
	elif (cidr=="/27"):
		return "255.255.255.224"
	elif (cidr=="/26"):
		return "255.255.255.192"
	elif (cidr=="/25"):
		return "255.255.255.128"
	elif (cidr=="/24"):
		return "255.255.255.0"
	elif (cidr=="/23"):
		return "255.255.254.0"
	elif (cidr=="/22"):
		return "255.255.252.0"
	elif (cidr=="/21"):
		return "255.255.248.0"
	else:
		raise Exception('cidr netmask was not found. The cidr netmask was {}', format(cidr))
		return result

if __name__ == '__main__':
    sys.exit(main(sys.argv))
