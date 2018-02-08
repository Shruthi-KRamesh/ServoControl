import fibo
class Speed:
    def __init__(self, start_angle, stop_angle):
        self.startAngle=start_angle
        self.stopAngle=stop_angle

    def incrDecr(self):
        fibobj=fibo.FibonacciSeries()
        angle_diff=self.stopAngle-self.startAngle
        angle1=self.startAngle+(50*angle_diff/100)
        print('angle1 is --', angle1)
        angle2=self.startAngle+(70*angle_diff/100)
        print('angle2 is--', angle2)
        fiboList=fibobj.Fibonacci()#0,1,1,2,3,5,8,13,21,34
        if(angle_diff>=0):
            angle_list=self.AngleListPos(angle1, angle2, fiboList)
        else:
            angle_list=self.AngleListNeg(angle1, angle2, fiboList)
        return (angle_list)

    def AngleListPos(self, angle1, angle2, fiboList):
        angle3=[]
        angle4=[]
        for i in range(2,len(fiboList)):
            if(not angle3):
                angle3.append(self.startAngle)
            elif((self.startAngle+fiboList[i])<=angle1):
                angle3.append(self.startAngle+fiboList[i])
            else:
                angle3.append(abs(angle1))
                break
        for i in range(2,len(fiboList)):
            if(not angle4):
                angle4.append(abs(self.stopAngle))
            elif((self.stopAngle-fiboList[i])>=abs(angle2)):
                angle4.append(abs(self.stopAngle-fiboList[i]))
            else:
                angle4.append(abs(angle2))
                break
        print('angle3 array is--',angle3)
        print('angle4 array is--',angle4)
        angle4=angle4[::-1]
        li=angle3+angle4
        print('li is--', li)
        return (li)

    def AngleListNeg(self, angle1, angle2, fiboList):
        angle3=[]
        angle4=[]
        for i in range(2,len(fiboList)):
            if(not angle3):
                angle3.append(self.startAngle)
            elif((self.startAngle-fiboList[i])>=angle1):
                angle3.append(self.startAngle-fiboList[i])
            else:
                angle3.append(abs(angle1))
                break
        for i in range(2,len(fiboList)):
            if(not angle4):
                angle4.append(self.stopAngle)
            elif((self.stopAngle+fiboList[i])<=abs(angle2)):
                angle4.append(abs(self.stopAngle+fiboList[i]))
            else:
                angle4.append(abs(angle2))
                break
        print('angle3 array is--',angle3)
        print('angle4 array is--',angle4)
        angle4=angle4[::-1]
        li=angle3+angle4
        print('li is--', li)
        return (li)
