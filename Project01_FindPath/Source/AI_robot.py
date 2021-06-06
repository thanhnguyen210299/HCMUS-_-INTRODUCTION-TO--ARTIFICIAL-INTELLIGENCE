import pygame
import sys
import random
import math

############################################################# FUNCTIONS ########################################################
# Phương trình đường thẳng
def linear_equation(x1,x2,y1,y2):
    a = (y2 - y1 )/(x2 -x1)
    b = (y1 -a*x1)
    return a, b

# Tính khoảng cách pixel giữa 2 điểm
def instance(x, y, u, v):
    count = 0
    if x == u:
        for i in range(min(y,v), max(y,v) +1):
            count = count + 1
    elif y == v:
        for j in range(min(x,u), max(x,u) +1):
            count = count + 1

    else:
        a,b = linear_equation(x,u,y,v)

        count = count + max(max(x,u) - min(x,u), max(y,v) - min(y,v))
    return count

# Vẽ đường thẳng giữa 2 điểm p và q
def draw_line(px, py, qx, qy, R, G, B, l):
    if px == qx:
        for y in range(min(py,qy), max(py,qy) +1):
            draw_point(qx*CONST_SCALE, y*CONST_SCALE, R, G, B, l)
    elif py == qy:
        for x in range(min(px,qx), max(px,qx) +1):
            draw_point(x*CONST_SCALE, py*CONST_SCALE, R, G, B, l)
    else:
        a,b = linear_equation(px, qx, py, qy)
        if (max(px,qx) - min(px,qx) > max(py, qy) - min(py,qy)):
            for x in range(min(px,qx), max(px,qx) +1):
                draw_point(x*CONST_SCALE, round(a*x + b)*CONST_SCALE, R, G, B, l)
        else:
            for y in range(min(py,qy), max(py,qy) +1):
                draw_point(round((y-b)/a)*CONST_SCALE, y*CONST_SCALE, R, G, B, l)
# Vẽ 1 pixel
def draw_point(x, y, R, G, B, l):
    pygame.draw.rect(window, pygame.Color(R,G,B), pygame.Rect(x, y, CONST_SCALE, CONST_SCALE))
    if (l == 1):
        pygame.draw.rect(window, pygame.Color(255, 255, 255), pygame.Rect(x, y, CONST_SCALE, CONST_SCALE), l)

################################################################### CLASSES #################################################
#_________Point_________#
class Point :
    def __init__(self, x, y):
        self.xCoor=x;
        self.yCoor=y;
    def setCoor(self,x,y):
        self.xCoor=x;
        self.yCoor=y;
    def getX(self):
        return self.xCoor;
    def getY(self):
        return self.yCoor;
    def topRight(self): #nhận điểm đi xéo trên bên phải của điểm hiện tại
        xCoor=self.getX()+1;
        yCoor=self.getY() -1;
        if(yCoor<=0):
            yCoor=0;
        return (Point(xCoor,yCoor));
    def topLeft(self): #nhận điểm đi xéo trên bên trái của điểm hiện tại
        xCoor=self.getX()-1;
        yCoor=self.getY() -1;
        if(yCoor<0):
            yCoor=0;
        if(xCoor<0):
            xCoor=0;
        return (Point(xCoor,yCoor));
    def downRight(self): #nhận điểm đi xéo  dưới phải của điểm hiện tại
        xCoor=self.getX()+1;
        yCoor=self.getY() +1;
        return (Point(xCoor,yCoor));
    def downLeft(self): #nhận điểm đi xéo  dưới trái của điểm hiện tại
        xCoor=self.getX()-1;
        yCoor=self.getY() +1;
        if(xCoor<0):
            xCoor=0;
        return (Point(xCoor,yCoor));
    def top(self):   #nhận điểm phía trên của điểm hiện tại
        xCoor=self.getX();
        yCoor=self.getY() -1;
        if(yCoor<=0):
            yCoor=0;
        return (Point(xCoor,yCoor));
    def down(self):  #nhận điểm phía duoi của điểm hiện tại
        xCoor=self.getX();
        yCoor=self.getY() +1;
        return (Point(xCoor,yCoor));
    def right(self):  #nhận điểm phía ben phai của điểm hiện tại
        xCoor=self.getX()+1;
        yCoor=self.getY();
        return (Point(xCoor,yCoor));
    def left(self):  #nhận điểm phía ben trai của điểm hiện tại
        xCoor=self.getX()-1;
        if(xCoor<=0):
            xCoor=0;
        yCoor=self.getY();
        return (Point(xCoor,yCoor));
        
    def __eq__(self,other):
        return self.xCoor == other.xCoor and self.yCoor==other.yCoor;
    def __str__(self):
        return "({0},{1})".format(self.xCoor,self.yCoor)
    def __hash__(self):
        return hash((self.xCoor, self.yCoor));
    def display():
        print('Chua cai dat');  
    def distanceTo(self,point):
        return abs(self.xCoor-point.xCoor)+abs(self.yCoor-point.yCoor); 

#_________Person_________#
class Person(Point):
    def __init__(self,x,y):
        super().__init__(x,y);

#_________Polygon_________#
class Polygon:
    #vers là list chứa các đỉnh của đa giác, mỗi đỉnh có kiểu Point
    def __init__(self,vers,check):
        self.vers=vers;
        if (check):
            self.R = random.randrange(0, 225)
            self.G = random.randrange(0, 225)
            self.B = random.randrange(0, 225)
            self.draw_polygon(0)
    def draw_polygon(self, l):
        if (l == 1):
            for i in range(0, len(self.vers) - 1):
                draw_line(self.vers[i].getX(), self.vers[i].getY(), self.vers[i + 1].getX(), self.vers[i + 1].getY(), 225, 225, 225, l)
            draw_line(self.vers[0].getX(), self.vers[0].getY(), self.vers[i + 1].getX(), self.vers[i + 1].getY(), 225, 225, 225,l)
        else:
            for i in range(0, len(self.vers) - 1):
                draw_line(self.vers[i].getX(), self.vers[i].getY(), self.vers[i + 1].getX(), self.vers[i + 1].getY(), self.R, self.G, self.B, l)
            draw_line(self.vers[0].getX(), self.vers[0].getY(), self.vers[i + 1].getX(), self.vers[i + 1].getY(), self.R, self.G, self.B,l)
    def isInside(self,point):

        x=point.getX();
        y=point.getY();
        
        for i in self.vers:
            for j in self.vers:
                xa=i.getX();
                ya=i.getY();
                xb=j.getX();
                yb=j.getY();
                xmin=xa;
                xmax=xb;
                ymin=ya;
                ymax=yb;
                if(xmin>xmax):
                    temp=xmin;
                    xmin=xmax;
                    xmax=temp;
                if(ymin>ymax):
                    temp=ymin;
                    ymin=ymax;
                    ymax=temp;
                if(x>=xmin and x<=xmax and y>=ymin and y<=ymax ):
                    if(i!=j and (x>=xa or x>=xb) and(y>=ya or y>=yb)  ):
                        if(  ( (ya-yb)*(x-xa) +(xb-xa)*(y-ya) )==0  ):
                            return True;
            
        poly=[];
        for p in self.vers:
            poly.append((p.getX(),p.getY()));
        n = len(poly)
        inside =False
    
        p1x,p1y = poly[0]
        for i in range(n+1):
            p2x,p2y = poly[i % n]
            if y > min(p1y,p2y):
                if y <= max(p1y,p2y):
                    if x <= max(p1x,p2x):
                        if p1y != p2y:
                            xinters = (y-p1y)*(p2x-p1x)/(p2y-p1y)+p1x
                        if p1x == p2x or x <= xinters:
                            inside = not inside
            p1x,p1y = p2x,p2y
        
        return inside
    def randomMove(self):
        k=random.randint(-1,1 );
        for x in self.vers:
            x.setCoor(x.getX()+k,x.getY())
class Map:
    def __init__(self,topLeft,bottomRight,listPol,start,goal, nPickUp, lisPickUp): #gán giá trị ban đầu cho map
        self.topLeft=topLeft;
        self.bottomRight=bottomRight;
       
        self.start=Point(start.getX(),start.getY());   #Vị trí bắt đầu
        self.person=Person(start.getX(),start.getY()); #vị trí hiện tại của người
        self.goal=Point(goal.getX(),goal.getY());      #vị trí đích
        draw_point(self.start.getX()*CONST_SCALE, self.start.getY()*CONST_SCALE, 0,255,0, 1)
        draw_point(self.goal.getX()*CONST_SCALE, self.goal.getY()*CONST_SCALE, 0,0,255, 1)
        self.listPol=listPol;
        self.sum_pixel = 1;
        self.solution=[];                              #Các bước đi từ viện trí hiện tại đến vị trí đích  
        self.nPickUp=nPickUp; #So diem ngau nhien se co 
        self.listPickUp = lisPickUp;  #danh sach chua cac diem ngau nhiem
        self.pickUpPoint = []
        for i in range(self.nPickUp):
            x = lisPickUp[i].getX()
            y = lisPickUp[i].getY()
            temp = Point(x,y)
            self.pickUpPoint.append(temp)
        self.PolyMove_Path = []   
    def isValidPoint(self,point):  # điểm có nằm trong đa giác nào không
        if(point.getY()<=self.topLeft.getX()):
            return False
        if(point.getX()<=self.topLeft.getY()):
            return False
        if(point.getY()>=self.bottomRight.getX()):
            return False
        if(point.getX()>=self.bottomRight.getY()):
            return False
            
        for i in self.listPol:
            if(i.isInside(point)):
                return False;
        return True;        
        
    def BFS(self):
        visited=[];
        queue=[];
        father=dict();
        self.solution.clear();
        person=Person(self.person.getX(),self.person.getY());
        queue.append(person)
        visited.append(person);
        
        while queue:
            temp=queue.pop(0);
            person.setCoor(temp.getX(),temp.getY());
            if person==self.goal:
                break;
            
            temp5=person.topRight();
            if(not temp5 in visited and self.isValidPoint(temp5)):
                queue.append(temp5);
                visited.append(temp5);
                father[temp5]=temp;
                
            temp6=person.downRight();
            if(not temp6 in visited and self.isValidPoint(temp6)):
                queue.append(temp6);
                visited.append(temp6);
                father[temp6]=temp;
                
            temp1=person.top();
            if(not temp1 in visited and self.isValidPoint(temp1)):
                queue.append(temp1);
                visited.append(temp1);
                father[temp1]=temp;
                
            temp2=person.right();
            if(not temp2  in visited and self.isValidPoint(temp2)):
                queue.append(temp2);
                visited.append(temp2);
                father[temp2]=temp;
                
            temp3=person.down();
            if(not temp3 in visited and self.isValidPoint(temp3)):
                queue.append(temp3);
                visited.append(temp3);
                father[temp3]=temp;
                
            temp4=person.left();
            if(not temp4 in visited and self.isValidPoint(temp4)):
                queue.append(temp4);
                visited.append(temp4);
                father[temp4]=temp;
                
        if(person==self.goal):        
            self.solution.append(father[self.goal]);
            while self.solution[-1]!=self.goal:
                self.solution.append(father[self.solution[-1]]);
                
            self.solution.pop();    
            self.solution.reverse();
            self.solution.append(self.goal);
            self.solution.insert(0,self.start);
    def printSolution(self, R, G, B): #trả về 1 nếu có lời giải, trả về 0 nếu không có lời giải,in ra màn hình solution
        n = len(self.solution)
        if (n == 0): return False
        print(self.person,end="->")
        for i in range(n):
            if (i == n - 1):
                print(self.solution[i], end = "")
            else:
                print(self.solution[i],end="->")
            t1 = self.solution[i].getX()
            t2 = self.solution[i].getY()
            draw_point(t1*CONST_SCALE, t2*CONST_SCALE, R, G, B, 1)
            if (i > 0):
                t3 = self.solution[i - 1].getX()
                t4 = self.solution[i - 1].getY()
            else:
                t3 = self.person.getX()
                t4 = self.person.getY()
            if (t1 == t3 + 1 and t2 == t4 + 1) or (t1 == t3 - 1 and t2 == t4 - 1) or (t1 == t3 + 1 and t2 == t4 - 1) or (t1 == t3 - 1 and t2 == t4 + 1):
                self.sum_pixel = self.sum_pixel + 1.5
            else:
                self.sum_pixel = self.sum_pixel + 1;
        return True;
    def Greedy(self):
        visited=[];
        queue=[];
        father=dict();
        self.solution.clear();
        
        person=Person(self.person.getX(),self.person.getY());
        queue.append(person)
        visited.append(person);
        
        while queue:
            temp=queue.pop(0);
            person.setCoor(temp.getX(),temp.getY());
            if person==self.goal:
                break;
            
            temp5=person.topRight();
            if(not temp5 in visited and self.isValidPoint(temp5)):
                queue.append(temp5);
                visited.append(temp5);
                father[temp5]=temp;
                
            temp6=person.downRight();
            if(not temp6 in visited and self.isValidPoint(temp6)):
                queue.append(temp6);
                visited.append(temp6);
                father[temp6]=temp;   
            
            temp1=person.top();
            if(not temp1 in visited and self.isValidPoint(temp1) ):
                j=len(queue)-1;
                for i in range(0,len(queue)):
                    if temp1.distanceTo(self.goal)<queue[i].distanceTo(self.goal) :
                        j=i;
                        break;
                queue.insert(j,temp1);
                visited.append(temp1);
                father[temp1]=temp;
                
            temp2=person.right();
            if(not temp2 in visited and self.isValidPoint(temp2) ):
                j=len(queue)-1;
                for i in range(0,len(queue)):
                    if temp2.distanceTo(self.goal)<queue[i].distanceTo(self.goal) :
                        j=i;
                        break;
                queue.insert(j,temp2);
                visited.append(temp2);
                father[temp2]=temp;
                
            temp3=person.down();
            if(not temp3 in visited and self.isValidPoint(temp3) ):
                j=len(queue)-1;
                for i in range(0,len(queue)):
                    if temp3.distanceTo(self.goal)<queue[i].distanceTo(self.goal) :
                        j=i;
                        break;
                queue.insert(j,temp3);
                visited.append(temp3);
                father[temp3]=temp;
                
            temp4=person.left();
            if(not temp4 in visited and self.isValidPoint(temp4) ):
                j=len(queue)-1;
                for i in range(0,len(queue)):
                    if temp4.distanceTo(self.goal)<queue[i].distanceTo(self.goal) :
                        j=i;
                        break;
                queue.insert(j,temp4);
                visited.append(temp4);
                father[temp4]=temp;
        
        if(person==self.goal):        
            self.solution.append(father[self.goal]);
            while self.solution[-1]!=self.goal:
                self.solution.append(father[self.solution[-1]]);
                
            self.solution.pop();    
            self.solution.reverse();
            
            self.solution.append(self.goal);
    def aStar(self):
        visited=[];
        queue=[];
        father=dict();
        self.solution.clear();
        person=Person(self.person.getX(),self.person.getY());
        queue.append(person)
        visited.append(person);
        
        while queue:
            
            min=queue[0];
            idx=0;
            
            for i in range(0,len(queue)):
                
                if( min.distanceTo(self.goal)+min.distanceTo(self.start) >queue[i].distanceTo(self.start)+ queue[i].distanceTo(self.goal)):
                    min=temp;
                    idx=i;
                    
            temp=queue[idx];
            queue[idx]=queue[0];
            queue[0]=temp;
                    
            temp=queue.pop(0);
            person.setCoor(temp.getX(),temp.getY());
            if person==self.goal:
                break;
                
            temp5=person.topRight();
            if(not temp5 in visited and self.isValidPoint(temp5)):
                queue.append(temp5);
                visited.append(temp5);
                father[temp5]=temp;
            
            temp6=person.downRight();
            if(not temp6 in visited and self.isValidPoint(temp6)):
                queue.append(temp6);
                visited.append(temp6);
                father[temp6]=temp;
            
            temp1=person.top();
            if(not temp1 in visited and self.isValidPoint(temp1)):
                queue.append(temp1);
                visited.append(temp1);
                father[temp1]=temp;
                
            temp2=person.right();
            if(not temp2  in visited and self.isValidPoint(temp2)):
                queue.append(temp2);
                visited.append(temp2);
                father[temp2]=temp;
                
            temp3=person.down();
            if(not temp3 in visited and self.isValidPoint(temp3)):
                queue.append(temp3);
                visited.append(temp3);
                father[temp3]=temp;
                
            temp4=person.left();
            if(not temp4 in visited and self.isValidPoint(temp4)):
                queue.append(temp4);
                visited.append(temp4);
                father[temp4]=temp;
                
        if(person==self.goal):        
            self.solution.append(father[self.goal]);
            while self.solution[-1]!=self.goal:
                self.solution.append(father[self.solution[-1]]);
                
            self.solution.pop();    
            self.solution.reverse();
            self.solution.append(self.goal);
            self.solution.insert(0,self.start); 
    def getPerson(self):
        return self.person;
    def checkPoint(self, poly, x_min, x_max, y_min, y_max, k,tx, ty):
        if (x_max>=self.start.getX() and x_min<=self.start.getX() and y_min <= self.start.getY() and y_max >= self.start.getY()):
            return False
        if (x_max == self.person.getX()) or (x_min == self.person.getX())or (y_min == self.person.getY()) or (y_max == self.person.getY()):
            return False
        if (x_max>=self.goal.getX() and x_min<=self.goal.getX() and y_min <= self.goal.getY() and y_max >= self.goal.getY()):
            return False
        if(y_min<=self.topLeft.getX()):
            return False
        if(x_min<=self.topLeft.getY()):
            return False
        if(y_max>=self.bottomRight.getX()):
            return False
        if(x_max>=self.bottomRight.getY()):
            return False
        t1 = [];
        t1.append(Point(x_min,y_min))
        t1.append(Point(x_min,y_max))
        t1.append(Point(x_max,y_min))
        t1.append(Point(x_max,y_max))
        temp = Polygon(t1, False)
        for i in range(len(poly.vers)):
            x = poly.vers[i].getX() + tx
            y = poly.vers[i].getY() + ty
            for j in range(len(self.listPol)):
                if (not j == k):
                    if self.listPol[j].isInside(Point(x,y)):
                        return False;
                    for l in range(len(self.listPol[j].vers)):
                        if (temp.isInside(self.listPol[j].vers[l])):
                            return False
                        if (self.listPol[j].vers[l].getX() == x_min) or (self.listPol[j].vers[l].getX() == x_max) or (self.listPol[j].vers[l].getY() == y_min) or (self.listPol[j].vers[l].getY() == y_max):
                            return False
        return True;        
    def movePolygons(self):
        Direct = [-1,0,1]
        tx = Direct[random.randrange(0,3)]
        ty = Direct[random.randrange(0,3)]
        for i in range(len(self.listPol)):
            n = len(self.listPol[i].vers)
            x_min = self.listPol[i].vers[0].getX()
            x_max = self.listPol[i].vers[0].getX();
            y_min = self.listPol[i].vers[0].getY()
            y_max = self.listPol[i].vers[0].getY();
            for j in range(1, len(self.listPol[i].vers)):
                a = self.listPol[i].vers[j].getX();
                b = self.listPol[i].vers[j].getY();
                if (a < x_min): x_min = a;
                if (a > x_max): x_max = a;
                if (b < y_min): y_min = b;
                if (b > y_max): y_max = b;
            x_min = x_min + tx
            y_min = y_min + ty
            x_max = x_max + tx
            y_max = y_max + ty
            if self.checkPoint(self.listPol[i], x_min, x_max, y_min, y_max, i, tx, ty):
                for j in range(n):
                    x = self.listPol[i].vers[j].getX() + tx
                    y = self.listPol[i].vers[j].getY() + ty
                    self.listPol[i].draw_polygon(1)
                    self.listPol[i].vers[j].setCoor(x, y)
    def step(self, option):
        if(self.person==self.goal): #đã tới đích
            self.draw_Path_PolyMove()
            return 0;
        else:
            self.movePolygons(); 
            if(option==1):# tìm lời giải bằng greed
                self.Greedy();      
            elif(option==2): # tìm lời giải bằng BFS
                self.BFS();
            else:
                self.aStar(); # tìm lời giải bằng A*
                
            if(len(self.solution)==0):  # kiểm tra có lời giải hay không
                for i in range(len(self.listPol)):
                    n = len(self.listPol[i].vers)
                    for j in range(n):
                        self.listPol[i].draw_polygon(0)
                return -1;
            else:
                draw_point(self.person.getX()*CONST_SCALE, self.person.getY()*CONST_SCALE, 225, 225, 225, 1)
                self.person.setCoor(self.solution[0].getX(),self.solution[0].getY()); # cho người đi 1 bước
                self.PolyMove_Path.append(self.solution[0])
                print(self.solution[0], end="->")
                draw_point(self.person.getX()*CONST_SCALE, self.person.getY()*CONST_SCALE, 0, 0, 0, 1)
                for i in range(len(self.listPol)):
                    n = len(self.listPol[i].vers)
                    for j in range(n):
                        self.listPol[i].draw_polygon(0)
                return 1;
    def draw_Path_PolyMove(self):
        for i in range(len(self.listPol)):
            self.listPol[i].draw_polygon(1)
        self.sum_pixel = 1
        for i in range(len(self.PolyMove_Path)):
            t1 = self.PolyMove_Path[i].getX()
            t2 = self.PolyMove_Path[i].getY()
            draw_point(t1*CONST_SCALE, t2*CONST_SCALE, 0, 0, 0, 1)
            if (i > 0):
                t3 = self.PolyMove_Path[i - 1].getX()
                t4 = self.PolyMove_Path[i - 1].getY()
            else:
                t3 = self.person.getX()
                t4 = self.person.getY()
            if (t1 == t3 + 1 and t2 == t4 + 1) or (t1 == t3 - 1 and t2 == t4 - 1) or (t1 == t3 + 1 and t2 == t4 - 1) or (t1 == t3 - 1 and t2 == t4 + 1):
                self.sum_pixel = self.sum_pixel + 1.5
            else:
                self.sum_pixel = self.sum_pixel + 1;
        draw_point(self.start.getX()*CONST_SCALE, self.start.getY()*CONST_SCALE, 0,255,0, 1)
        draw_point(self.goal.getX()*CONST_SCALE, self.goal.getY()*CONST_SCALE, 0,0,255, 1)
    def stepAndPickUp(self, option):
        goal=self.goal;
        start=self.start;
        for i in range(self.nPickUp):
            x = lisPickUp[i].getX()
            y = lisPickUp[i].getY()
            draw_point(x*CONST_SCALE, y*CONST_SCALE, 255,0,0,1)
        while(len(self.listPickUp) > 0):
            temp=self.listPickUp[0];
            idx=0;
            for i in range(0,len(self.listPickUp)):
                t1 = instance(temp.getX(), temp.getY(), self.person.getX(), self.person.getY())
                t2 = instance(self.listPickUp[i].getX(), self.listPickUp[i].getY(), self.person.getX(), self.person.getY())
                if (t1 > t2):
                    temp=self.listPickUp[i];
                    idx=i;
                elif (t1 == t2):
                    if (instance(self.listPickUp[i].getX(), self.listPickUp[i].getY(), goal.getX(), goal.getY()) > instance(temp.getX(), temp.getY(), goal.getX(), goal.getY())):
                        temp=self.listPickUp[i];
                        idx=i;
            temp=self.listPickUp[0];
            self.listPickUp[0]=self.listPickUp[idx];
            self.listPickUp[idx]=temp;
            
            print('Điểm cần đón: ',end=" ");
            print(self.listPickUp[0])
            R = random.randrange(0, 225)
            G = random.randrange(0, 225)
            B = random.randrange(0, 225)
            self.goal=self.listPickUp.pop(0)

            if(option==1):# tìm lời giải bằng greed
                self.Greedy();      
            elif(option==2): # tìm lời giải bằng BFS
                self.BFS();
            else:
                self.aStar(); # tìm lời giải bằng A*
            
            if (not self.printSolution(R,G,B)):
                draw_point(self.start.getX()*CONST_SCALE, self.start.getY()*CONST_SCALE, 0,255,0, 1)
                for i in range(self.nPickUp):
                    draw_point(self.pickUpPoint[i].getX()*CONST_SCALE, self.pickUpPoint[i].getY()*CONST_SCALE, 255,0,0,1)
                print("\nKhông tìm thấy đường đi tới điểm đón!")
                print("\nKhông tìm thấy đường đi tới đích!!!")
                return
            print('\n');
            self.person=self.goal;

        self.goal=goal;
        if(option==1):# tìm lời giải bằng greed
            self.Greedy();      
        elif(option==2): # tìm lời giải bằng BFS
            self.BFS();
        else:
            self.aStar(); # tìm lời giải bằng A*
        R = random.randrange(0, 225)
        G = random.randrange(0, 225)
        B = random.randrange(0, 225)  
        print("Diem dich:", goal);
        t = self.printSolution(R,G,B)
        draw_point(self.start.getX()*CONST_SCALE, self.start.getY()*CONST_SCALE, 0,255,0, 1)
        draw_point(self.goal.getX()*CONST_SCALE, self.goal.getY()*CONST_SCALE, 0,0,255, 1)
        for i in range(self.nPickUp):
            draw_point(self.pickUpPoint[i].getX()*CONST_SCALE, self.pickUpPoint[i].getY()*CONST_SCALE, 255,0,0,1)
        if (t):
            print("\nĐộ dài đường đi: ", self.sum_pixel)
        else:
            print("\nKhông tìm thấy đường đi tới đích!!!")

################################################################### MAIN ####################################################
CONST_SCALE = 20

# Mở file 
f = open("D:\Input.txt")
l = f.readline()
w, h = [int(x) for x in l.strip().split(',')]

# Tạo khung nhìn 
window = pygame.display.set_mode(((w+1)*CONST_SCALE, (h+1)*CONST_SCALE))
pygame.display.set_caption("AI")
for i in range(w+1):
    for j in range(h + 1):
        draw_point(i * CONST_SCALE, j * CONST_SCALE, 225, 225, 225, 1)

# Vẽ viền tọa độ
for pos in range(h+1):
    draw_point(0, pos * CONST_SCALE, 160, 160, 160, 1)
    draw_point(w*CONST_SCALE, pos * CONST_SCALE, 160, 160, 160, 1)

for pos in range(w+1):
    draw_point(pos * CONST_SCALE, 0, 160, 160, 160, 1)
    draw_point(pos * CONST_SCALE, h*CONST_SCALE, 160, 160, 160, 1)      

#Đọc điểm xuất phát và điểm kết thúc
l = f.readline()
xStart, yStart, xGoal, yGoal = [int(x) for x in l.strip().split(',')]

#Số lượng đa giác trên bản đồ
num_polygon = int(f.readline().strip())
#Vẽ đa giác
lisPol = []
for index in range(num_polygon):
    pol = []
    l = f.readline()
    point_list = [int(x) for x in l.strip().split(',')]
    i = 0
    while i < len(point_list):
        t = Point(point_list[i], point_list[i + 1])
        i = i + 2
        pol.append(t)
    lisPol.append(Polygon(pol, True));

#Số lượng điểm đón
nPickUp = int(f.readline().strip())
#Đọc các điểm đón
lisPickUp = []
if (not nPickUp == 0):
    l = f.readline()
    point_list = [int(x) for x in l.strip().split(',')]
    i = 0
    while i < len(point_list):
        t = Point(point_list[i], point_list[i + 1])
        i = i + 2
        lisPickUp.append(t)

l = f.readline()
move, option = [int(x) for x in l.strip().split(',')]

f.close()

#Tìm đường đi
map=Map(Point(0, 0),Point(h, w),lisPol,Point(xStart, yStart),Point(xGoal,yGoal), nPickUp, lisPickUp); 
if (move == 0):
    map.stepAndPickUp(option)
if (move == 1):
    print(Point(xStart, yStart),end="->")

# Dừng màn hình pygame
done = False
t = h*w;
isEnd = False
while not done:
     
    for event in pygame.event.get():
        if event.type == pygame.QUIT: #Nếu người dùng đóng màn hình Pygame thì kết thúc vòng lặp
            done = True #Cờ để tiếp tục hay thoát khỏi vòng lặp
    if (not isEnd):
        if (move == 1):
            t = map.step(option)
        if (t == 0):
            print("End")
            print("\nĐộ dài đường đi:", map.sum_pixel)
            isEnd = True
        if (t == -1):
            print("Không tìm thấy đường đi")
            isEnd = True
    pygame.display.flip() # Hiện màn hình
    pygame.time.wait(100)

# Be IDLE friendly
pygame.quit()







