# <-------------------------------------------------------->
# Created by -  Sunay Bhoyar 
# Roll No. - 21110
# Course - SE (sem 3) DSL CE (SPPU 2019)
# <-------------------------------------------------------->

#all function are declared below 
class operations :  
    # this is the basic object creator function
    def __init__(self,data):
        self.lis = data
        
        
    #<------------------------------------------>    
    
    # this is main quick sort function
    def quick_sort (self,arr,start,end):
        while(start < end ):                            # this is base condition
            res = self.piv_shift(arr, start, end)       # pivot shifting takes place here
            arr = res[0]                                # old array is replace by modified one
            pivloc = res[1]                             # it stores the pivot location
            self.quick_sort(arr, pivloc +1 , end)       # quick sort further part of the array
            self.quick_sort(arr, start, pivloc -1 )     # quick start behind part
            break                                       # end condition
        return arr                                      # return the sorted array

    #<------------------------------------------>   
    
        
    # this is pivot shifter function
    def piv_shift (self,arr,start,end):
        pivot = arr[start]                              # we select the first element of the list is pivot
        inc = 0                                         # this data is used to mark the location
        for j in range(start+1,end):                    # we check for all element leaving first
            if(pivot>arr[j]):
                arr.insert(start,arr[j])
                arr.pop(j+1)
                inc+=1
        return [arr,start+inc] 
    
    #<------------------------------------------>   
    
    
# run this code to test check              
# print(quick_sort([5,6,5,4,9,7,5,1,3,6,10,9,7], 0,13 ))            
     
     
     
#<------------------------------------------>        
while (1>0):
    print("========================================================")
    menu = int(input("Enter the menu option you want to select\n1)Enter the data\n0)Exit\n"))
    obj = operations([])
    if(menu== 0):
        print("Thanks for operations using the software")
        print("========================================================")
        break
    elif (menu == 1):        
        data1 = list(map(int,input("Enter the students percentage space separated\n").split()))    
        while(1>0):
            print("========================================================")
            menu1=int(input("\nEnter the menu choice you want to check \n1)Quick Sort\n2)0)Return to main menu / Re-enter the data\n"))
            if(menu1 == 0):
                break
            elif(menu1==1):    
                print(obj.quick_sort(data1,0,len(data1)))
            elif(menu1==2):    
                tempLis = obj.quick_sort(data1,0,len(data1))
                tempLis = tempLis[::-1]
                print(tempLis[0:5])
            else :
                print("Enter valid input")
    else :
        print("Enter valid input")            