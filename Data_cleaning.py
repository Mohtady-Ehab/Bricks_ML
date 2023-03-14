import pandas as pd
import math
import random as rnd
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
rms_values_x = []
rms_values_y = []
rms_values_z = []
if __name__=='__main__':
    df = pd.read_excel("data.xlsx") 
    arrX = df['X'].tolist()
    for x in arrX:
        # takes the entire x column
        arr = df['X'].tolist()
        # just a check to take one sample only 
        if cntr%9 == 0 or cntr==0:
            arr = arr[strt:end]
            strt +=9
            end +=9
            # print(arr)
            rms = rmsValue(arr, n)
            rms_values_x.append(rms)
        cntr +=1

    strt = 0
    end = 9
    cntr = 0
    n = 9

    df = pd.read_excel("data.xlsx")  
    arrY = df['Y'].tolist()
    for y in arrY:
        # takes the entire x column
        arr = df['Y'].tolist()
        # just a check to take one sample only 
        if cntr%9 == 0 or cntr==0:
            arr = arr[strt:end]
            strt +=9
            end +=9
            # print(arr)
            rms = rmsValue(arr, n)
            rms_values_y.append(rms)
        cntr +=1
    
    strt = 0
    end = 9
    cntr = 0
    n = 9


    df = pd.read_excel("data.xlsx") 
    arrZ = df['Z'].tolist()
    for z in arrZ:
        # takes the entire x column
        arr = df['Z'].tolist()
        # just a check to take one sample only 
        if cntr%9 == 0 or cntr==0:
            arr = arr[strt:end]
            strt +=9
            end +=9
            # print(arr)
            rms = rmsValue(arr, n)
            rms_values_z.append(rms)
        cntr +=1


    print("\nRMS FOR X: ")
    print (rms_values_x)
    print("\nRMS FOR Y: ")
    print (rms_values_y)
    print("\nRMS FOR Z: ")
    print (rms_values_z)

    #generate wind/human interation dataset
    windx = []
    windy = []
    windz = []
    for x in range(10):
        rnd_windx = rnd.uniform(0,0.1)
        windx.append(rnd_windx)
    

    for y in range(10):
        rnd_windy = rnd.uniform(0,0.1)
        windy.append(rnd_windy)
    

    for z in range(10):
        rnd_windz = rnd.uniform(0,0.1)
        windz.append(rnd_windz)
    

    df_rms_values = {
         "X": rms_values_x + windx, "Y":rms_values_y  + windy, "Z": rms_values_z + windz
    }
    
    df_rms = pd.DataFrame(df_rms_values)

    df_rms.to_excel("rms_data.xlsx")