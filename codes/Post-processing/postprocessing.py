import os
import pandas as pd 

directory = r'C:\Users\rscombd\Desktop\Predicted data'
for filename in os.listdir(directory):
    if filename.endswith(".csv") or filename.endswith(".csv"):
        file=filename
        patient='Patient '+filename[3:5]
        seizureno=filename[:8]
        
        df= pd.read_csv(file)
        df=df['Predicted_values']
        df=df.iloc[:540]
        window_size=30 #5mins
        segments = 5 #window_size broken into segments of five rows
        no_of_segments = int(window_size/segments)
        x=0
        zero_count=0
        one_count=0
        step_one=3
        step_two=2
        main_list=[]
        for i in range(18):
            window=[]
            seizure_count=0
            
            for z in range(no_of_segments):
                for i in range(segments):
                    if(df.iloc[x]==0):
                        zero_count=zero_count+1
                    else:
                        one_count=one_count+1
                    x=x+1
                if (zero_count>=step_one):
                    window.append(0)
                else:
                    window.append(1)
                zero_count=0
                one_count=0
            for m in range(len(window)):
                if (window[m]==1):
                    seizure_count=seizure_count+1
                
            if(seizure_count>=step_two):
                main_list.append(1)
            else:
                main_list.append(0)
        print(patient)
        print(seizureno)
        print(main_list)
    
            
    
    
        
        
    

        
    else:
        continue

