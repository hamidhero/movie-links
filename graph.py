import mysql.connector as mysql

# import igraph as gr

# g = gr.Graph()

conn = mysql.connect(host= "localhost",
                  user='root',
                  passwd='',
                  db="movies_db")

x = conn.cursor()

director = ("SELECT * FROM iranian_movies")
x.execute(director)

nodes = {}

for i in x:
	act_node = []
	dir_node = i[3].encode("utf-8").split("* ")[0]
	old_act_node = i[4].encode("utf-8").split("* ")
	for act in old_act_node:
		act = act.strip()
		act_node.append(act)

	if dir_node not in nodes.keys():
		 
		nodes[dir_node] = act_node


		print nodes[dir_node][0]

	else:
		for a in act_node:
			nodes[dir_node].append(a)
	
		print nodes[dir_node][0]

with open ("dic.txt", "w") as r:
	r.write(str(nodes))
# print nodes


# b'\xd9\xbe\xd8\xaf\xd8\xb1\xd8\xa7\xd9\x85 \xd9\x85\xd8\xb9\xdb\x8c\xd8\xb1\xdb\x8c\xd8\xa7\xd9\x86'.decode("utf-8")