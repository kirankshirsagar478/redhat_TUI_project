import os
os.system ("tput setaf 2")
print ("\t Welcome to TUI Project ")
os.system ("tput setaf 7")
print("\t ------------------- ")
location = input("Enter The Location (local/remote) :")
if location == "remote" :
	remoteIP = input("Enter remote IP:")
while True:
	print ('''
	press 1: to see date
	press 2: to check calender
	press 3: conf web server
	press 4: to create user
	press 5: create file
	press 6: to setup n/w
	press 7: to exit
	''')
	ch = int(input("Enter Your Choice:"))
	print(ch)
	if location == "local" :
		if int(ch) == 1:
			os.system("date")
		elif int(ch) == 2:
			os.system("cal")
		elif int(ch) == 3:
			os.system("yum install httpd")
		elif int(ch) == 4:
			create_user = input("Enter User Name:")
			os.system("useradd {}".format(create_user))
		elif int(ch) == 5:
			fileName = input("Enter File Name: ")
			os.system("touch {}".format(fileName))
		elif int(ch) == 6:
			os.system("")
		elif int(ch) == 7:
			exit()
		else:
			print("option not supported")
		input("Press Enter to continue ..... ")
		os.system("clear")

	elif location == "remote" :
		if int(ch) == 1:
			os.system("ssh {} date".format(remoteIP))
		elif int(ch) == 2:
			os.system("ssh {} cal".format(remoteIP))
		elif int(ch) == 3:
			os.system("ssh {} yum install httpd".format(remoteIP))
		elif int(ch) == 4:
			create_user = input("Enter User Name:")
			os.system("ssh {0} useradd {1}".format(remoteIP, create_user))
		elif int(ch) == 5:
			fileName = input("Enter File Name:")
			os.system("ssh {0} touch {1}".format(remoteIP, fileName))
		elif int(ch) == 6:
			os.system("")
		elif int(ch) == 7:
			exit()
		else:
			print("option not supported")
		input("Press Enter to continue .... ")
		os.system("clear")
	else:
		print("Enter Valid Location")
