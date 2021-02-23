#!usr/bin/python
#*_*coding:utf-8*_*
import Queue
class BFS:
    def __init__(self):
        self.ClosedList = []
        self.OpenList = Queue.LifoQueue()
    #判断是否是目标节点
    def IsGoal(self,tNode):
        if(tNode[0]+tNode[1]+tNode[2] == 0):
            return True
        else:
            return False

    #判断是否是合法状态
    def IsLegal(self,tNode):
        if(tNode[0]>=0 and tNode[0]<=3 and tNode[1]>=0 and tNode[1]<=3):
            if(tNode[0]==tNode[1] or tNode[0]==3 or tNode[0]==0):
                return True
            else:
                return False
        else:
            return False

    '''#重载运算符，判断两个结构体是否相等
    def EqualOperator(self,tNode1,tNode2):
        if(tNode1[0]==tNode2[0] and tNode1[1]==tNode2[1] and tNode1[2]==tNode2[2]):
            return True
        else:
            return False
    '''

    #判断是否在closed表中
    def InClosedList(self,tNode):
        if tNode in self.ClosedList:
            return True
        else:
            return False

    #扩展节点
    def ExpandNode(self,tNode,b):
        node = [[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0]]
        if(b==1):
            for i in range(5):
                node[i][2]=0
            node[0][0]=tNode[0]-1
            node[0][1]=tNode[1]
            node[1][0]=tNode[0]
            node[1][1]=tNode[1]-1
            node[2][0]=tNode[0]-1
            node[2][1]=tNode[1]-1
            node[3][0]=tNode[0]-2
            node[3][1]=tNode[1]
            node[4][0]=tNode[0]
            node[4][1]=tNode[1]-2
        else:
            for i in range(5):
                node[i][2]=1
            node[0][0] = tNode[0] + 1
            node[0][1] = tNode[1]
            node[1][0] = tNode[0]
            node[1][1] = tNode[1] + 1
            node[2][0] = tNode[0] + 1
            node[2][1] = tNode[1] + 1
            node[3][0] = tNode[0] + 2
            node[3][1] = tNode[1]
            node[4][0] = tNode[0]
            node[4][1] = tNode[1] + 2
        for i in range(5):
            if(self.IsLegal(node[i]) and not self.InClosedList(node[i])):
                self.OpenList.put(node[i])    #队列先进先出，广度优先搜索
    def ExpandNode(self,tNode,b):
        node = [[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0]]
        if(b==1):
            for i in range(5):
                node[i][2]=0
            node[0][0]=tNode[0]-1
            node[0][1]=tNode[1]
            node[1][0]=tNode[0]
            node[1][1]=tNode[1]-1
            node[2][0]=tNode[0]-1
            node[2][1]=tNode[1]-1
            node[3][0]=tNode[0]-2
            node[3][1]=tNode[1]
            node[4][0]=tNode[0]
            node[4][1]=tNode[1]-2
        else:
            for i in range(5):
                node[i][2]=1
            node[0][0] = tNode[0] + 1
            node[0][1] = tNode[1]
            node[1][0] = tNode[0]
            node[1][1] = tNode[1] + 1
            node[2][0] = tNode[0] + 1
            node[2][1] = tNode[1] + 1
            node[3][0] = tNode[0] + 2
            node[3][1] = tNode[1]
            node[4][0] = tNode[0]
            node[4][1] = tNode[1] + 2
        for i in range(5):
            if(self.IsLegal(node[i]) and not self.InClosedList(node[i])):
                self.OpenList.put(node[i])    #队列先进先出，广度优先搜索
    def ExpandNode1(self,tNode,b):
        node = [[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0]]
        if(b==1):
            for i in range(5):
                node[i][2]=0
            node[0][0]=tNode[0]
            node[0][1]=tNode[1]-1
            node[1][0]=tNode[0]-1
            node[1][1]=tNode[1]
            node[2][0]=tNode[0]-1
            node[2][1]=tNode[1]-1
            node[3][0]=tNode[0]
            node[3][1]=tNode[1]-2
            node[4][0]=tNode[0]-2
            node[4][1]=tNode[1]
        else:
            for i in range(5):
                node[i][2]=1
            node[0][0] = tNode[0]
            node[0][1] = tNode[1] + 1
            node[1][0] = tNode[0] + 1
            node[1][1] = tNode[1]
            node[2][0] = tNode[0] + 1
            node[2][1] = tNode[1] + 1
            node[3][0] = tNode[0]
            node[3][1] = tNode[1] + 2
            node[4][0] = tNode[0]
            node[4][1] = tNode[1] + 2
        for i in range(5):
            if(self.IsLegal(node[i]) and not self.InClosedList(node[i])):
                self.OpenList.put(node[i])    #队列先进先出，广度优先搜索
    def ExpandNode2(self,tNode,b):
        node = [[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0]]
        if(b==1):
            for i in range(5):
                node[i][2]=0
            node[0][0]=tNode[0]-1
            node[0][1]=tNode[1]
            node[1][0]=tNode[0]
            node[1][1]=tNode[1]-1
            node[2][0]=tNode[0]-2
            node[2][1]=tNode[1]
            node[3][0]=tNode[0]
            node[3][1]=tNode[1]-2
            node[4][0]=tNode[0]-1
            node[4][1]=tNode[1]-1
        else:
            for i in range(5):
                node[i][2]=1
            node[0][0] = tNode[0] + 1
            node[0][1] = tNode[1]
            node[1][0] = tNode[0]
            node[1][1] = tNode[1] + 1
            node[2][0] = tNode[0] + 2
            node[2][1] = tNode[1]
            node[3][0] = tNode[0]
            node[3][1] = tNode[1] + 2
            node[4][0] = tNode[0] + 1
            node[4][1] = tNode[1] + 1
        for i in range(5):
            if(self.IsLegal(node[i]) and not self.InClosedList(node[i])):
                self.OpenList.put(node[i])    #队列先进先出，广度优先搜索
    def ExpandNode3(self,tNode,b):
        node = [[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0]]
        if(b==1):
            for i in range(5):
                node[i][2]=0
            node[0][0]=tNode[0]
            node[0][1]=tNode[1] - 1
            node[1][0]=tNode[0] - 1
            node[1][1]=tNode[1]
            node[2][0]=tNode[0]
            node[2][1]=tNode[1] - 2
            node[3][0]=tNode[0] - 2
            node[3][1]=tNode[1]
            node[4][0]=tNode[0]-1
            node[4][1]=tNode[1]-1
        else:
            for i in range(5):
                node[i][2]=1
            node[0][0] = tNode[0]
            node[0][1] = tNode[1] + 1
            node[1][0] = tNode[0] + 1
            node[1][1] = tNode[1]
            node[2][0] = tNode[0]
            node[2][1] = tNode[1] + 2
            node[3][0] = tNode[0] + 2
            node[3][1] = tNode[1]
            node[4][0] = tNode[0] + 1
            node[4][1] = tNode[1] + 1
        for i in range(5):
            if(self.IsLegal(node[i]) and not self.InClosedList(node[i])):
                self.OpenList.put(node[i])    #队列先进先出，广度优先搜索
if __name__ == "__main__":
    InitNode = [3,3,1]
    bfs = BFS()
    bfs.OpenList.put(InitNode)
    while(not bfs.OpenList.empty()):
        unode = bfs.OpenList.get()
        if(bfs.IsGoal(unode)):
            bfs.ClosedList.append(unode)
            for i in range(len(bfs.ClosedList)):
                print bfs.ClosedList[i]
            break
        if(not bfs.InClosedList(unode)):
            bfs.ClosedList.append(unode)
            bfs.ExpandNode(unode,unode[2])

    print "路径2:"
    bfs1 = BFS()
    bfs1.OpenList.put(InitNode)
    while (not bfs1.OpenList.empty()):
        unode = bfs1.OpenList.get()
        if (bfs1.IsGoal(unode)):
            bfs1.ClosedList.append(unode)
            for i in range(len(bfs1.ClosedList)):
                print bfs1.ClosedList[i]
            break
        if (not bfs1.InClosedList(unode)):
            bfs1.ClosedList.append(unode)
            bfs1.ExpandNode1(unode, unode[2])
    print "路径3:"
    bfs1 = BFS()
    bfs1.OpenList.put(InitNode)
    while (not bfs1.OpenList.empty()):
        unode = bfs1.OpenList.get()
        if (bfs1.IsGoal(unode)):
            bfs1.ClosedList.append(unode)
            for i in range(len(bfs1.ClosedList)):
                print bfs1.ClosedList[i]
            break
        if (not bfs1.InClosedList(unode)):
            bfs1.ClosedList.append(unode)
            bfs1.ExpandNode2(unode, unode[2])
    print "路径4:"
    bfs1 = BFS()
    bfs1.OpenList.put(InitNode)
    while (not bfs1.OpenList.empty()):
        unode = bfs1.OpenList.get()
        if (bfs1.IsGoal(unode)):
            bfs1.ClosedList.append(unode)
            for i in range(len(bfs1.ClosedList)):
                print bfs1.ClosedList[i]
            break
        if (not bfs1.InClosedList(unode)):
            bfs1.ClosedList.append(unode)
            bfs1.ExpandNode3(unode, unode[2])