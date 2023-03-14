import pandas as pd
import math
#Function that Calculate Root Mean Square
def rmsValue(arr, n):
    square = 0
    mean = 0.0
    root = 0.0
     
    #Calculate square
    for i in range(0,n):
        square += (arr[i]**2)
     
    #Calculate Mean
    mean = (square / (float)(n))
    #Calculate Root
    root = math.sqrt(mean)
     
    return root
 
#Driver code
strt = 0
end = 9
cntr = 0
n = 9
rms_values = []
if __name__=='__main__':
    df = pd.read_excel('data.xlsx') # can also index sheet by name or fetch all sheets
    arr = df['X'].tolist()
    for x in arr:
        arr = df['X'].tolist()
        if cntr%9 == 0 or cntr==0:
            arr = arr[strt:end]
            strt +=9
            end +=9
            print(arr)
            rms = rmsValue(arr, n)
            rms_values.append(rms)
            print (rms_values)
        cntr +=1
        

    # n = 9
    # print(rmsValue(arr, n))