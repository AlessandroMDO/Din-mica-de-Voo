"""
Trabalho T1 Dinâmica de Vôo

Nome: Alessandro Melo de Oliveira
Número USP: 10788662
"""

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.ticker import MultipleLocator
import math

#constantes
rho0=1.225;# [kg/m^3]
p0=101325;# [Pa]
t0=288.15;# [K]
beta=-0.0065;# [K/m]
a0=334.1; # [m/s]
g=9.81; #[m/s^2]
R=287.053; # [J/kg.K]
gama = 1.4 # adimensional
referencia =11000 # [m] separação entre as duas camadas

#Parte I do trabalho: uma função que forneça [P,a,rho,T] dada uma altitude em metros
def atmo_isa(altis):
    global T,P,a,rho #torna as variaveis acessíveis fora da função
    T=[];P=[];a=[];rho=[] #lista onde será colocado os valores calculados
    for altitude in altis:    
    
        if altitude <= referencia: #trecho linear
            t=t0+beta*altitude 
            p = (t/t0)**(-g/(beta*R)); p=p*p0 
            a_=math.sqrt(gama*R*t) 
            rho_ = (t/t0)**((-g/(beta*R))-1); rho_=rho_*rho0
                          
        else: #trecho constante
            t=216.65
            a_=math.sqrt(gama*R*t)
            p= math.exp((-g*(altitude-referencia))/(R*t));p=p*22620.47
            rho_=math.exp((-g*(altitude-referencia))/(R*t));rho_=rho_*0.3639
            
        T.append(round(t,3));P.append(round(p,3));a.append(round(a_,3));rho.append(round(rho_,3))
        
    print(f'T: {T}')
    print(f'a: {a}')
    print(f'P: {P}')
    print(f'rho: {rho}')

#Parte II do trabalho: plotar um gráfico de altitude densidade
def graph_da():
    
    fig,ax=plt.subplots(figsize=(7,10)) #cria o ambiente gráfico e seta a escala
    
    #relação ISA entre temperatura e altitude (gráfico linear)
    altitude=np.linspace(-5000,36000,5000)
    t=15+(beta/3.28)*altitude
    plt.plot(t,altitude,color='k',linestyle='-.')
    plt.annotate(s='Atmosfera Padrão (ISA)',xy=(-45,31000),xytext=(-15,33000),
                 arrowprops=dict(arrowstyle="->"))
    
    #isolinhas de altitude densidade      
    h_ft=np.arange(-5000,36000,1000) #vetor altitude em pés
    h_m=[i/3.28 for i in h_ft] #conversão da altitude para metros

    atmo_isa(h_m) # a função da Parte I é usada para calcular os valores de densidade
       
    for rhoo in rho: #aqui de fato começa o cálculo das isolinhas, onde será varrido a lista contendo as densidades
        pp=[]
        hh=[]
        tt=np.arange(223.15,328.15,5) #vetor temperatura em kelvin
        for t in tt:
            p = rhoo*R*t #relação dos gases ideais
            pp.append(p)            
        for p in pp:
            h=(((p/p0)**0.19)-1)*(t0/beta) #relação entre pressão e altitude
            hh.append(h) #lista contendo as altitudes de pressão          
        temp = [i-273.15 for i in tt] #conversão para celcius
        alti = [i*3.28 for i in hh] #conversão para pés       
        plt.plot(temp,alti,c='navy',lw=2 if rhoo in rho[::5] else 0.5)
        
    #Customização do gráfico                   
    plt.annotate(s='Altitude Densidade',xy=(10,29500),xytext=(20,30000),
                 arrowprops=dict(arrowstyle="->"))      
    ax.text(x=17,y=0,s='0 ft',rotation=-18)
    ax.text(x=51,y=25500,s='35000 ft',rotation=-18)
    ax.text(x=51,y=16700,s='25000 ft',rotation=-18)
    ax.text(x=51,y=8000,s='15000 ft ',rotation=-18)
    ax.text(x=51,y=-300,s='5000 ft',rotation=-18)    
    ax.text(x=-35,y=-700,s='-5000 ft',rotation=-25) 
    plt.xlabel('Temperatura [ºC]')
    plt.ylabel('Altitude de Pressão [ft]')  
    plt.title('Gráfico Altitude de Densidade')
    ax.xaxis.set_major_locator(MultipleLocator(10))
    ax.xaxis.set_minor_locator(MultipleLocator(5))
    ax.yaxis.set_major_locator(MultipleLocator(5000))
    ax.yaxis.set_minor_locator(MultipleLocator(1000))
    plt.grid(True, which='major', color='black', linestyle='--', lw=0.5)
    plt.grid(True, which='minor', color='black', linestyle='--', lw=0.2)
    plt.xlim(-50,65,10)
    plt.ylim(-1500,36000,5000)
    #plt.savefig('graph_da.pdf')
    plt.show()
        
print("Digite 'atmo_isa([altitude em metros])' para obter [P,a,rho,T] ou digite 'graph_da()' para obter um gráfico de altitude densidade.")
  

    
        
    
    
      
    
    



