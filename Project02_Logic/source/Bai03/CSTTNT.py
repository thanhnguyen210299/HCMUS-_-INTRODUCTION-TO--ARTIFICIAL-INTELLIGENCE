import itertools

class Relation:
    def __init__(self,s):
        name="";
        data="";

        flag=0;
        for i in s:
            if i=='(':
                flag=1;
                continue;
            if i==')':
                break;
            if (flag==0):
                name+=i;
            else:
                data+=i;
                
        self.name=name;
        self.data=list(data.split(','));
        
    def isKB(self):
        if( self.data[0][0].isupper() ):
            return False;
        return True;
    def getName(self):
        return self.name;
    def getValues(self):
        return self.data;
    def getValue(self,i):
        return self.data[i];
    def setValues(self,values):
        self.data=values;
    def setName(self,name):
        self.name=name;
    def isCompatible(self,r):
        if(self.isKB()):
            return False;
        if(self.name==r.getName()):
            return True;
        return False;
    def __str__(self):
        data=','.join(self.data);
        return self.name+"("+data+")";
    def __eq__(self, other):
        if(other==False):
            return False;
        if other.getName()== self.name and other.getValues()==self.getValues():
            return True;
        return False;
    def toString(self):
        data=','.join(self.data);
        return self.name+"("+data+")";
class Infer:
    def __init__(self,s):
        #print(s);
        s=s.split('->');
        left=s[0].split('^');
        right=s[1];
        self.left=[];
        self.right=Relation(right);
        for i in left:
            temp=Relation(i);
            self.left.append(temp);
    def myHash(self,x):
        temp=[];
        n=len(x);
        for i in range(0,n):
            temp.append(i);
        i=n-1;
        while(i>=0):
            j=i;
            while(j>=0):
                if(x[j]==x[i]):
                    temp[i]=j;
                j=j-1;
            i=i-1;
        return temp     
    def generate(self,KB):
        temp=[];
        for i in self.left:
            temp1=[];
            
            for j in KB:
                if(i.isCompatible(j)):
                    temp1.append(j.getValues());
            temp.append(temp1);
        #temp chứa các bộ giá trị có thể thay vào I

        for i in temp:
            if(i==[]):
                return False;
            
        temp1=[];
        for j in self.left:
                temp1=temp1+j.getValues();
        #temp1 chứa bộ biến bên trái của I

        for element in itertools.product(*temp):
            #print(element);
            temp=[];
            for j in element:
                temp=temp+j;
            
            if(self.myHash(temp)==self.myHash(temp1)):
                m=len(temp1);
                n=len(self.right.getValues());
                #print(temp);
                temp3=temp1+self.right.getValues();
                indexData=self.myHash(temp3);
                data=[];
                #print(temp3);
                for i in range(0,n):
                    data.append(temp[indexData[m+i]]);
                    
                temp2=Relation("default(x)");
                temp2.setValues(data);
                temp2.setName(self.right.getName());
                #print(temp2);
                if(temp2 in KB):
                    continue;
                #print('send to KB');
                return temp2;
            
        return False;
    
class MainProgram:
    def __init__(self,KB,I):
        self.KB=KB;
        self.I=I;
        
    def run(self):
        count=0;
        while(1):
            flag=0;
            for j in self.I:
                temp=j.generate(self.KB);
                if(temp!=False):
                    if(not temp in self.KB):
                        self.KB.append(temp);
                        flag=1;
            if(flag==0):
                break;
    def writeAnswer(self,questions):
        f=open('output.txt','w')
        for i in questions:
            temp=i.split('-');
            f.write(temp[0]);
            f.write('\n');
            temp1=Relation(temp[1]);
            for j in self.KB:
                if(temp1.getName()==j.getName() and temp1.getValue(1)==j.getValue(1)):
                    f.write(j.toString());
                    f.write('\n');
        print('Đã xuất kết quả ra file output.txt')
        f.close();
    def printKB(self):
        f=open('test.txt','w')
        for i in self.KB:
            f.write(i.getName());
            f.write(",");
            listToStr = ' '.join(map(str, i.getValues()));
            f.write(listToStr);
            f.write('\n');


#ĐỌC FILE INPUT
fp=input('Nhập tên  file input (hoang_gia_anh.txt hoặc truong_dai_hoc.txt ): ');            
f=open(fp,'r');
#f=open('truong_dai_hoc.txt','r');
print('Đang xử lý(khoảng 10 giây với Hoàng Gia Anh và 5 giây ở Trường Đại Học tự cài đặt)....');

f1=f.read().splitlines();
count=0;
KB=[];
I=[];
questions=[];
for x in f1:
    if(x=='x'):
        count=count+1;
        continue;
    if(count==0):
        temp=Relation(x);
        KB.append(temp);
    elif(count==1):
        temp=Infer(x);
        I.append(temp);
    else:
        questions.append(x);
        
f.close();
program=MainProgram(KB,I);
program.run();
#program.printKB();
program.writeAnswer(questions);
