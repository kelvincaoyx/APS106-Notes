import math
def wave_type(wave_parameters):
    '''
    (str) -> str
    Return the type of wave, "surging or collapsing", "plunging"
    or "spilling", according to the wave's Iribarren number.
    '''
    # find the two separators
    first_separator = wave_parameters.find(",")
    second_separator = wave_parameters.rfind(",")
    
    # extract Iribarren parameters and cast to float
    alpha = float(wave_parameters[:first_separator])
    H = float(wave_parameters[first_separator + 1:
                              second_separator])
    L = float(wave_parameters[second_separator + 1:])
    
    # calculate the Iribarren number
    Ir = math.tan(alpha) / math.sqrt(H/L)
    # determine the type of wave
    if Ir <= 0.5:   
        type = "spilling"
    elif Ir <= 3.3:
        type = "plunging"
    else:
        type = "surging or collapsing"
        
    return type

print(wave_type("1.2,2.3,5.7"))
print(wave_type("1,2,3"))
print(wave_type("1.245,5.60,23"))
print(wave_type("1.0,2.3456789,2.19"))