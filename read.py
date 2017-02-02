# -*- coding: utf-8 -*-

import igraph as gr

g = gr.Graph()

file = open("dic.txt", "r")
dic = str(file.read())
code = compile(dic, '<string>', 'exec')
exec(code)

#print (dic['\xd9\x85\xd8\xac\xdb\x8c\xd8\xaf \xd8\xa8\xd8\xb1\xd8\xb2\xda\xaf\xd8\xb1'])
#print (dic["مسعود کیمیایی"][9])

actors = []
f = open("r.txt", "a")
for i in dic.keys():
    g.add_vertex(i)
    
    for j in dic[i]:
        if j not in actors:
            g.add_vertex(j)
            actors.append(j)
        
        
        
        eid = g.get_eid(i, j, error=False)
        if(eid != -1):
            g.es[eid]["weight"] += 1
#            f.write(str(i.encode("utf-8"))+"  "+str(j.encode("utf-8")))
#            f.write("\n")
#            print(i, "  ", j)
        else:
            g.add_edge(i, j, weight=1)
#            f.write("No Such Edge \n")
#            print("No Such Edge")
            continue

roles = []
for item in g.vs:
    if item["name"] in actors and item["name"] not in dic.keys():
        roles.append("a")
        #g.vs["role"][counter] = "a"
    elif item["name"] in dic.keys() and item["name"] not in actors:
        #g.vs["role"][counter] = "d"
        roles.append("d")
    else:
    	roles.append("b")

g.vs["role"] = roles
        
color_dict = {"a": "red", "d": "blue", "b": "green"}
g.vs["color"] = [color_dict[role] for role in g.vs["role"]]

#        if eid >= 0:
#            print(eid)
#            g.es[eid]["weight"] += 1
#        else:
#            g.add_edge(i, j, weight=1)
#        
#            
#     
# pl=gr.plot(g);
# pl.add(g);
# pl._windows_hacks=True;
# pl.show()
 
       
gr.write(g,"E:/Related to Univesity/Arshad/term 1/Network Science(Teimourpour)/exercise4(project)/graph2.gml")