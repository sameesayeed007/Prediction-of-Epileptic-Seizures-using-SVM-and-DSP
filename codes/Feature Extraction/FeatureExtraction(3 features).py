import numpy as np
import scipy as sp
import scipy.fftpack
import pandas as pd
from scipy.fftpack import fft, fftfreq, fftshift
import statistics
import scipy.fftpack

thesis_final_files = ['chb01_21Final.csv','chb01_26Final.csv']
iterator = 0

while(iterator < len(thesis_final_files)) :
    
    file_name = thesis_final_files[iterator]
    
    data = pd.read_csv(file_name)
    a=[]
    d=0
    for i in range(23):
        Channel = data.iloc[:,i]
        num_of_iterations = int((len(Channel)-1)/2560)
    
        # making a list of lists with 10 seconds data
        #a=[]
        p=0
        q= 2560
        b=[]
        for i in range(num_of_iterations):
            c=[]
            for j in range(2560):
    
                c.append(Channel[p])
                p+=1
            b.append(c)
        a.append(b)
        print(d)
        d=d+1
    
    print('**1**')
    
    def angle(a):
        #no of points
        n=2560
    
        #Time period is 10s
        Lx=10
    
        x=np.linspace(0,Lx,n)
        
            #Creating all the necessary frequencies
        freqs=fftfreq(n)
    
        #mask array to be used for power spectra
        #ignoring half the values, as they are complex conjugates of the other
        mask=freqs>0
            #FFT values
        fft_values=fft(a)
    
        #true theoretical fft values
        fft_theo = 2.0*np.abs(fft_values/n)
        
            #FFT shift
        fftshift_values = fftshift(fft_values)
    
        #Calculating the angle
        out_angle = np.angle(fftshift_values, deg = True)  
        #print ("output angle in degrees : ", out_angle)
        out_angle2=statistics.mean(abs(out_angle))
        #print("Mean angle: ")
        return out_angle2
    
    
    
    
    #Calculates the energy
    def energy(a):
        
        #no of points
        n=2560
    
        #Time period is 10s
        Lx=10
    
        x=np.linspace(0,Lx,n)
        
            #Creating all the necessary frequencies
        freqs=fftfreq(n)
    
        #mask array to be used for power spectra
        #ignoring half the values, as they are complex conjugates of the other
        mask=freqs>0
            #FFT values
        fft_values=fft(a)
    
        #true theoretical fft values
        fft_theo = 2.0*np.abs(fft_values/n)
        
            #FFT shift
        fftshift_values = fftshift(fft_values)
        
        ps = 2.0*(np.abs(fft_values/n)**2)
    
    #Calculating the mean of power spectrum-energy
    
        ps_mean = statistics.mean(ps)
        return ps_mean
    
    
    
    #Calculates tthe amplitude
    def amplitude(a):
        
        #no of points
        n=2560
    
        #Time period is 10s
        Lx=10
    
        x=np.linspace(0,Lx,n)
        
            #Creating all the necessary frequencies
        freqs=fftfreq(n)
    
        #mask array to be used for power spectra
        #ignoring half the values, as they are complex conjugates of the other
        mask=freqs>0
            #FFT values
        fft_values=fft(a)
    
        #true theoretical fft values
        fft_theo = 2.0*np.abs(fft_values/n)
        
            #FFT shift
        fftshift_values = fftshift(fft_values)
        amplitudes = 2 / n * np.abs(fft_values)
        amplitudes_mean = statistics.mean(amplitudes)
        return amplitudes_mean
    
    
    #Channel=[]
    
    Channel=[] #23
    #tenseconds=[]
    
    for m in range(23):
        tenseconds=[]
        for n in range(540):
            features=[]
            angle_value=angle(a[m][n])
            features.append(angle_value)
            energy_value=energy(a[m][n])
            features.append(energy_value)
            amplitude_value=amplitude(a[m][n])
            features.append(amplitude_value)
            tenseconds.append(features)
        Channel.append(tenseconds)
        
    print('**2**')
    
    w=1
    x=[]
    df1 = pd.DataFrame()
    ind=[]
    for j in range(540):
        ind.append(w)
        w=w+1
        
    df1['index']=ind
    C="c"
    F='f'
    
    for i in range(23):
        for f in range(3):
            g=[]
            name="C"+str(i+1)+"F"+str(f+1)
            for j in range(540):
                
                r=Channel[i][j][f]
                g.append(r)
            
            df1[name]=g
            
    cvalue=[]
    for i in range(360):
        cvalue.append(0)
        
    for j in range(180):
        cvalue.append(1)
        
    df1['class']=cvalue
    
    saved_feature_file_name = file_name[0:8] + 'S.csv'
    df1.to_csv(saved_feature_file_name,index=False)
    
    print('**3**')
    
    iterator += 1
    print('***********************************************')




































