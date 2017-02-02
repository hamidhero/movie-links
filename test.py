# -*- coding: utf-8 -*-

from bs4 import BeautifulSoup

import urllib

import sys

import mysql.connector as mysql


conn = mysql.connect(host= "localhost",
                  user='root',
                  passwd='',
                  db="movies_db")

x = conn.cursor()

id = 0

for i in range(291,2000):
	print i

	url = "http://www.cinetmag.com/Movies/ShowFilms.asp?ID="+str(i)

	r  = urllib.urlopen(url).read()

	soup = BeautifulSoup(r, "html.parser")
	# a = soup.findAll("p", { "align" : "justify", "style" : "margin: 5px 10px" })
	try:
		c = soup.find("td", {"bgcolor" : "#FFE1A4"})
		d = c.find("font", {"face" : "Tahoma"})

		a = soup.findAll("p", {"class" : "510", "style" : "margin: 5px 10px"})
		aa = a[2].find("span", {"style" : "font-size: 9pt"})

		b = soup.find("p", { "align" : "justify", "style" : "margin: 5px 10px" })



		# with open("test2.txt", "w") as x:
		name = d.encode("utf-8").split(">")

		title = name[1].split("<")[0].lstrip()
		# x.write(name[1].split("<")[0].lstrip())
		# x.write("\n")

		year = name[3].split("<")[0].lstrip()
		# x.write(name[3].split("<")[0].lstrip())
		# x.write("\n")

		director = aa.encode("utf-8").split(">")[1][:-5]

		actors = b.encode("utf-8").split(">")[1].split("<")[0] 
		# x.write(b.encode("utf-8").split(">")[1].split("<")[0])
		# x.write("\n")

		print("Start "+str(id+1)+"...")

		print title
		x.execute("""INSERT INTO iranian_movies VALUES (%s,%s,%s,%s,%s)""",(id+1, title, year, director, actors))
		id += 1
		conn.commit()


		print("done!")
		

	except:
		print(":(")
		continue


		# x.write(i.encode("utf-8"))
		# x.write("\n")
		# x.write(i.next)
		# x.write(str(i.encode()))
