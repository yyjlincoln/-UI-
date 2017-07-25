import math
import traceback
def main():
    #数据转换开始
    try:
        a=input('A=')
        if a=='':
            a=0.0
        else:
            a=float(a)
        b=input('B=')
        if b=='':
            b=0.0
        else:
            b=float(b)
        c=input('Hypotenuse C=')
        if c=='':
            c=0.0
        else:
            c=float(c)
    except:
        print('出现错误.检查传递参数.')
        main()
        #数据转换结束
        #检查是否成立
    if a==0 and b!=0 and c!=0:
        print('b*b='+str(b*b)+'\nc*c='+str(c*c)+'\nc*c-b*b='+str(c*c-b*b)+'\nsqrta='+str(math.sqrt(c*c-b*b)))
        a=math.sqrt(c*c-b*b)
    elif a!=0 and b==0 and c!=0:
        print('a*a='+str(a*a)+'\nc*c='+str(c*c)+'\nc*c-a*a='+str(c*c-a*a)+'\nsqrtb='+str(math.sqrt(c*c-a*a)))
        b=math.sqrt(c*c-a*a)
    elif a!=0 and b!=0 and c==0:
        print('a*a='+str(a*a)+'\nb*b='+str(b*b)+'\na*a+b*b='+str(a*a+b*b)+'\nsqrtc='+str(math.sqrt(a*a+b*b)))
        c=math.sqrt(a*a+b*b)
    else:
        print('参数错误.')
    if a+b<=c or a+c<=b or b+c<=a or math.fabs(a-b)>=c or math.fabs(a-c)>=b or math.fabs(b-c)>=a:
        print('警告:三角形不成立.\n不符合两边之和大于第三边或两边之差小于第三边.')

    main()
main()


console='''
    a=float(input('A='))
    b=float(input('B='))
    c=float(input('C='))
    '''
    #这几行代码没有任何用，是以前的代码。
