###############################################
# APS106  2022 - Lab 5 - Measurement Parser   #
###############################################

############################
# Part 1 - Email to Name   #
############################

def email_to_name(email):
    """
    (str) -> str
    
    Given a string with the format "first_name.last_name@domain.com",
    return a string "LAST_NAME,FIRST_NAME" where all the characters are upper
    case
    
    
    >>> email_to_name("anna.conda@mail.utoronto.ca")
    'CONDA,ANNA'
    """
    ## TODO: YOUR CODE HERE
    name_section = email.split("@")[0]
    first_name = name_section.split(".")[0]
    last_name = name_section.split(".")[1]
    return (last_name + "," + first_name).upper()
    

###############################
# Part 2 - Count Measurements #
###############################

def count_measurements(s):
    """
    (str) -> int
 
    Given s, a string representation of comma separated site-measurement
    pairs, return the total number of measurements
 
    >>> count_measurements("B, 5.6, Control, 5.5, Db, 3.2")
    3
    
    >>> count_measurements("Control, 7.5")
    1
    """
    
    #TODO: YOUR CODE HERE
    return len(s.replace(" ","").split(","))//2


######################################
# Part 3 - Calculate Site Average    #
######################################

def calc_site_average(measurements, site):
    """
    (str, str) -> float
 
    Given s, a string representation of comma separated site-measurement
    pairs, and the name of a site, 
    return the average of the site measurements to one decimal place
    
    
    >>> calc_site_average("A, 4.2, B, 6.7, Control, 7.1, B, 6.5, Control, 7.8, Control, 6.8, A, 3.9", "Control")
    7.2
    """
    
    ## TODO: YOUR CODE HERE
    site_list = measurements.replace(" ","").split(",")
    num_total = 0
    num_counter = 0
    for i in range(len(site_list)):
        if site_list[i] == site:
            num_counter += 1
            num_total += float(site_list[i+1])
            
    return round(num_total/num_counter,1)
    


###############################
# Part 4 - Generate Summary   #
###############################

def generate_summary(measurement_info, site):
    """
    (str, str) -> str
    
    Extract technician name, number of measurements, and average of control
    site pH level measurements from string of technician measurements. Input
    string is formatted as
    
        firstname.lastname@domain.com, date, sitename, measurement, sitename, measurement, ...
    
    returns a string with the extracted information formatted as
    
        LASTNAME,FIRSTNAME,number of measurements,average pH of specified site
 
    >>> generate_summary("dina.dominguez@company.com, 01/11/20, A, 4.2, B, 6.7, Control, 7.1, B, 6.5, Control, 7.8, Control, 6.8, A, 3.9", "Control")
    'DOMINGUEZ,DINA,7,7.2'
    """
    
    ## TODO: YOUR CODE HERE
    entire_list = measurement_info.replace(" ","").split(",")
    
    return_list = []
    
    return_list.extend(email_to_name(entire_list[0]).split(","))
    return_list.append(str(count_measurements(",".join(entire_list[2:]))))
    return_list.append(str(calc_site_average(",".join(entire_list[2:]),site)))
    return ",".join(return_list)


if __name__ == '__main__':
    import doctest
    doctest.testmod()