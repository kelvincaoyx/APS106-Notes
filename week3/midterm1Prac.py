def what_factors(num):
    '''
    (int) -> NoneType
    '''
    
    if num % 2 == 0:
        print("Even")
    else: 
        print("odd. ")
    if num % 3 ==0:
        print("Divisible by 3.")
    if num % 4 == 0:
        print("Divisible by 4.")
    return


import math
def wave_type(wave_parameters): 
    '''(str) -> str 
    Return the type of wave, "surging or collapsing", "plunging"   
    or "spilling", according to the wave's Irribarren number. 
    ''' 
    convertedlist = list(wave_parameters.split(","))
    
    bedSlope = float(convertedlist[0])
    waveHeight = float(convertedlist[1])
    waveLength = float(convertedlist[2])
    
    _iribarrenNumber = math.tan(bedSlope)/(waveHeight/waveLength)**(0.5)
    
    if _iribarrenNumber <= 0.5:
        return "spilling"
    elif _iribarrenNumber <= 3.3:
        return "plunging"
    else:
        return "Surging or collapsing"
    
def test ():
    num = 35
    return num == 35

