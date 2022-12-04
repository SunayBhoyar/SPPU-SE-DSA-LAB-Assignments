# <-------------------------------------------------------->
# Created by -  Sunay Bhoyar 
# Roll No. - 21110
# Course - SE (sem 3) DSL CE (SPPU 2019)
# <-------------------------------------------------------->

#all function are declared below 
class operations:
    
    # this is the basic object creator function
    def __init__(self,data):
        self.lis = data
        for i in range(len(self.lis)):               #this is done to ensure that the percentage value are correctly entered
            if(data[i]>100 or data[i]<0):
                print("Enter a valid percentage")
                break

    #<------------------------------------------>    
    
    # this is Insertion sort function        
    def Insertion_Sort (self):
        MyList = self.lis
        for i in range(len(MyList)-1):   
            if (MyList[i]>MyList[i+1]):
                MyList = self.swap(MyList,i,i+1)
                for j in range(i):
                    if(MyList[i-j-1]>MyList[i-j]):
                        MyList = self.swap(MyList,i-j,i-j-1)
                    else:
                        break    
                    j+=1                   
        return MyList
    
    #<------------------------------------------>    
    
    # this is Shell sort function 
    def Shell_Sort(self):
        MyList = self.lis
        N = len(self.lis)
        interval = N // 2
        while (interval > 0 ):
            for i in range(interval,N):
                temp = MyList[i]
                j = i
                while j >= interval and MyList[j - interval] > temp:
                    MyList[j] = MyList[j - interval]
                    j -= interval
                MyList[j] = temp
            interval = interval // 2          
        return MyList
    
    #<------------------------------------------>  
        
    # this is swap items from list function
    def swap(self,giv_list ,pos1,pos2):
        giv_list[pos1],giv_list[pos2] = giv_list[pos2],giv_list[pos1]
        return giv_list
        
    #<------------------------------------------>  
    
         
while (1>0):
    print("========================================================")
    menu = int(input("Enter the menu option you want to select\n1)Enter the data\n0)Exit\n"))
    if(menu== 0):
        print("Thanks for using the software")
        print("========================================================")
        break
    elif (menu == 1):        
        data1 = operations(list(map(int,input("Enter the students percentage space separated\n").split())))      
        while(1>0):
            print("========================================================")
            menu1=int(input("\nEnter the menu choice you want to check \n1)Insertion Sort:\n2)Shell Sort\n3)top 5 by insertion\n4)top 5 by shell sort\n0)Return to main menu / Re-enter the data\n"))
            if(menu1 == 0):
                break
            elif(menu1==1):    
                print(data1.Insertion_Sort())
            elif(menu1 ==2):    
                print(data1.Shell_Sort()) 
            elif(menu1==3):    
                temp = data1.Insertion_Sort()
                temp = temp[::-1]
                print(temp[0:5])
            elif(menu1 ==4):    
                temp = data1.Shell_Sort()
                temp = temp[::-1]
                print(temp[0:5])       
            else :
                print("Enter valid input")
    else :
        print("Enter valid input")            