import random

class Vertex:
    def __init__(self, v, connections):
        self.v=v
        self.connections=connections
        
    def insert_connection(self, connection):
        self.connections.append(connection)
        
    def remove_connection(self, connection):
        self.connections.remove(connection)
        
    def exist_connection(self, t):
        for c in self.connections:
            if c[0]==t:
                return True
            return False
        
def defined_degree_graph(n, degree):
    g = []
    v_list = []
    edges = []
    for i in range(n):
        v_list.append(i)
        g.append(Vertex(i, []))
    random.shuffle(v_list)
    for i in range(n):
        right = i   
        left = i
        for k in range(int(degree / 2)):
            left += 1
            if left >n-1:
                left = 0
            if left > i:
                wt=random.randint(0,100)   
                g[v_list[i]].insert_connection([v_list[left], wt])
                g[v_list[left]].insert_connection([v_list[i], wt])
            if v_list[i]> v_list[left]:
                edges.append([v_list[left],v_list[i],wt])
            else:
                edges.append([v_list[i],v_list[left],wt])
            right -= 1
            if right <0:
                right= n-1
            if right > i:
                wt=random.randint(0,100) 
                g[v_list[i]].insert_connection([v_list[right],wt])
                g[v_list[right]].insert_connection([v_list[i],wt])
            if v_list[i]> v_list[right]:
                edges.append([v_list[right],v_list[i],wt])
            else:
                edges.append([v_list[i],v_list[right],wt])
                
    file = open ('./edges.txt', 'a')
    for e in edges :
        file.write(str(e[0]) + '' + str(e[1]) + '' + str(e[2])+ '\n')
    file.close ()
    return g
  
defined_degree_graph(5000, 6);
defined_degree_graph(5000, 1000);

