# -*- coding: utf-8 -*-
import requests
import random
import  re
from bs4 import  BeautifulSoup

def qiushibaike():
     content = requests.get('https://www.qiushibaike.com/').content
     soup = BeautifulSoup(content, 'html.parser')
     for div in soup.find_all('div',{'class':'content'}):
         print  div.text.strip()


def demo_string():
    stra = 'hello world'
    print stra.capitalize()
    print stra.replace('world','nowcoder')
    strb ='  \n\rhello nowcoder \r\n '
    print 1,strb.lstrip()
    print 2,strb.rstrip()
    strc = 'hello w'
    print 3, strc.startswith('hel')
    print 7,'-'.join(['a','b','c'])
    print 8,strc.split(' ')
    print 9,strc.find('ello')


def demo_operation():
    print 1,1+2,5-2
    print 4,2 << 2

def demo_buildinfunction():
    print 1,max(2,1), min(5,3)
    print 2, len('xxx'), len([1,2,3])
    print  5,dir(list)
    x=2
    print 6,eval('x+3')
    print 7,chr(65),ord('a')

def demo_controlflow():
    score = 65
    if score >99:
        print 1,'A'
    elif score >60:
        print 2,'B'
    else:
        print 3,'C'

    while score < 100:
        print score
        score += 10
    score = 65
    for i in range(0,10,2):
        if i ==0:
            pass #do_special
        if i < 5:
            continue
        print  3, i
        if i ==6:
            break

def demo_list():
    lista=[1,2,3]
    print 1, lista
    listb = ['a',1,'c',1.1]
    print 2, listb
    lista.extend(listb)
    print 3,lista
    print 4, len(lista)
    print 5,'a' in listb
    lista = lista + listb
    print 6, lista
    listb.insert(0,'www')
    print 7,listb
    listb.pop(1)
    print 8,listb
    listb.reverse()
    print 9,listb
    print 10,listb[0], listb[1]
    listb.sort()
    print 11,listb
    listb.sort(reverse=True)
    print 12,listb
    print 13,listb * 2
    listaa = [1,2,3]
    listaa.append(4)
    print 15,listaa

def sub(a,b):
    return a-b

def add(a,b):
    return a+b

def demo_dict():
    dicta = {4:16,1:1,2:4,3:9}
    print 1,dicta
    print 2,dicta.keys(),dicta.values()
    print 3,dicta.has_key(1),dicta.has_key('a')
   # for map<int,int>:: iterator it = x.begin(); it!=x.end()
    for key, value in dicta.items():
        print 'key-value:',key, value
    dictb = {'+':add,'-':sub }
    print 4,dictb['+'](1,2)
    print 5,dictb.get('-')(15,3)
    dictb['*'] = 'x'
    print dictb
    dicta.pop(4)
    print 6, dicta
    del dicta[1]
    print 7,dicta

def demo_set():
    seta = set((1,2,3))
    setb = set((2,3,4))
    print 1, seta
    print 2,seta
    print 3, seta.intersection(setb),seta & setb
    print 4,seta | setb, seta.union(setb)
    print 5,seta - setb
    print 6,seta
    print len(seta)
    print seta.isdisjoint(set((1,2)))

## 面向对象   继承  封装(可以多继承)    多态(核心)
class User:
    type = 'USER'

    def __init__(self,name,uid):
        self.name = name
        self.uid = uid

    def __repr__(self):
        return 'im '+ self.name+' '+ str(self.uid)
#继承User
class Guest(User):
    def __repr__(self):
        return 'im guest:'+self.name+' '+str(self.uid)

##   继承User
class Admin(User):
    type = 'ADMIN'

    def __init__(self,name,uid,group):
        User.__init__(self,name,uid)
        self.group = group

    def __repr__(self):
        return 'im' + self.name + ' ' + str(self.uid) + ' ' + self.group

def create_user(type):
     if type == 'USER':
         return User('u1',1)
     elif type == 'ADMIN':
         return Admin('a1',101,'g1')
     else:
         return Guest('gul',201)
         #raise ValueError('error')
# 异常
def demo_exception():
    try:
        print 2 / 1
      #  print 2 / 0
        raise Exception('Raise Error','NowCoder')
    except Exception as e:
        print 'error:',e
    finally:
        print 'clean up'
# 随机数
def demo_random():
    random.seed(1) # 有点像序列化  与反序列化
    # x=prex * 100007 % xxxx
    # prex = x 幂等性
    print 1, int(random.random() * 100)
    print 2,random.randint(0,200)
    print 3,random.choice(range(0,100,10))
    print 4,random.sample(range(0,100),4)
    a = [1,2,3,4,5]
    random.shuffle(a)
    print 5,a

# 正则表达式 的原理是  编译原理的状态机转移
def demo_re():
    str = 'abc123def12gh15'
    p1 = re.compile('[\w]+')
    p2 = re.compile('\d')
    print 1,p1.findall(str)
    print 2,p2.findall(str)

    str = 'a@163.com;b@gmail.com;c@qq.com;e@163.com;z@qq.cpm'
    p3 = re.compile('[\w]+@[163|qq]+\.com')
    print  3,p3.findall(str)

    str = '<html><h>title</h><body>xxx</body></html>'
    p4 = re.compile('<h>[^<]+</h>')
    print 4,p4.findall(str)
    p4 = re.compile('<h>([^<]+)</h><body>([^<]+)</body>')
    print 5,p4.findall(str)

    str = 'xx2016-06-11yy'
    p5 = re.compile('\d{4}-\d{2}-\d{2} ')
    print 5,p5.findall(str)

if __name__ == '__main__':
    '''
    user1 = User('u1',1)
    print user1
    admin1 = Admin('a1',101,'g1')
    print admin1
    print  create_user('USERx')
   '''
   # demo_random() 随机数
   #  demo_exception() 异常
  #  print 'hello nowcoder'
    #qiushibaike()        爬虫
   # demo_string();        字符串
    #demo_operation();      运算符
    #demo_buildinfunction();   内置函数
    ##demo_controlflow()  控制流
    #demo_list();   list集合
   # demo_dict();   字典
   # demo_set();  set集合
    demo_re()