# indian method functions

import wolframalpha
import math
import numpy as np
from sin_table import *
from datetime import datetime


### functions:

def get_number_of_days():
    # Returns days elapsed since 18th february 3102 BC in julian calendar
    date = input("Enter date [ddmmyyyy]: ")
    app_id = '2L4QRV-AGPKRWRLTK'
    client = wolframalpha.Client(app_id)
    res = client.query(date + '- 18th february 3102 BC in Julian calendar in days to 7 digits')
    number_of_days = next(res.results).text

    return decimal_day(number_of_days)


def decimal_day(number):
    # Converts scientific number to decimal format
    number = number.split()[0]
    float_number = ''
    exponent = number[-1]
    
    for character in number:
        if character != '×':
            float_number += character
        else:
            break
        
    number = int(float(float_number) * (10**int(exponent)))

    return number


def deg_min_sec(decimal_number):
    # Convertion to degree, minutes and seconds (special)
    number = decimal_number - int(decimal_number)
    degrees = int(number * 360) 
    number = (number * 360) - int(number * 360)
    minutes,seconds = divmod(number*3600, 60)

    return degrees, int(minutes), seconds


def degree_to_decimal(dms):
    # DMS --> DD (decimal degrees)
    decimal_degree = dms[0] + float(dms[1])/60 + float(dms[2])/3600
    
    return decimal_degree


def decimal_to_degree(dd):
    # DD --> DMS
    minutes,seconds = divmod(dd*3600,60)
    degrees, minutes = divmod(minutes,60)
    
    return degrees, minutes, seconds


def degree_subtraction(lambda_mean, lambda_sigma):
    # Returns positive degree, minutes, seconds of Kappa
    difference = np.subtract(lambda_mean, lambda_sigma)
    if difference[0] < 0:
        degrees = difference[0] + 360
    else:
        degrees = difference[0]
    minutes = difference[1]
    seconds = difference[2]

    if seconds < 0:
        minutes -= 1
        seconds += 60

    if minutes < 0:
        degrees -= 1
        minutes += 60
    
    return degrees, minutes, seconds


def decimaldigits(float_number):
    # Returns decimal digits only
    return float_number - int(float_number)


def roundedlist(my_list):
    # Returns each element of list rounded to 2 decimals
    
    return [ round(elem, 2) for elem in my_list ]

def decimal_angle(dms):
    # Returns float < 1 for input degrees, minutes, seconds
    return degree_to_decimal(dms) / 360





# COMPUTATION FAST AND SLOW


def fast_equation1(
        sin_mode, YUGA, DAYS_PER_YUGA, days_elapsed, mean_revolutions_per_yuga,
        slow_0_180, slow_90_270, fast_0_180, fast_90_270):

    # Returns Lamba for fast equation
    
    # computation:

    lambda_mean = (mean_revolutions_per_yuga * days_elapsed) / DAYS_PER_YUGA
    lambda_mean = deg_min_sec(lambda_mean)
    print("\tLambda_mean\t= " + str(roundedlist(lambda_mean)))


    lambda_sigma = (YUGA * days_elapsed) / DAYS_PER_YUGA
    lambda_sigma = deg_min_sec(lambda_sigma)
    print("\tLambda_sigma\t= " + str(roundedlist(lambda_sigma)))


    kappa_sigma1 = degree_subtraction(lambda_mean, lambda_sigma) 
    print("\tKappa_sigma1\t= " + str(roundedlist(kappa_sigma1)))


    # geometry 
    if sin_mode == "Modern":
        sine = abs(math.sin(math.radians(degree_to_decimal(kappa_sigma1))))
    elif sin_mode == "Ancient":
        sine = interpol(degree_to_decimal(kappa_sigma1))

    radius = fast_0_180 + (fast_90_270 - fast_0_180) * sine
    radius = (radius * 3438) / 360
    print("\tRadius\t\t= " + str(round(radius,2)))

    

    Vm_A = 3438 * sine
    print("\tVm_A\t\t= " + str(round(Vm_A,2)))


    V_B = (radius * abs(Vm_A)) / 3438
    print("\tV_B\t\t= " + str(round(V_B,2)))

    # CORRECT VALUES UNTIL V_B


    # not sure if corr

    Vm_B = math.sqrt(radius**2 - V_B**2)
    print("\tVm_B\t\t= " + str(round(Vm_B, 2)))


    O_B = 3438 - Vm_B
    print("\tO_B\t\t= " + str(round(O_B, 2)))


    O_V = math.sqrt(O_B**2 + V_B**2)
    print("\tO_V\t\t= " + str(round(O_V, 2)))


    if sin_mode == "Modern":
        sigma = math.degrees(math.asin(( V_B / O_V )))
    elif sin_mode == "Ancient":
        sigma = interpol_inverse(( (V_B / O_V) * 3438 ))

    print("\tSigma\t\t= " + str(round(sigma, 2)) + "°")
    
    sigma1 = sigma * decimal_angle(kappa_sigma1)   
    print("\tSigma 1\t\t= " + str(round(sigma1,2)) + "°")

    # final lambda
    lambda1 = degree_to_decimal(lambda_mean) + 0.5 * sigma1
    print("\tLAMBDA 1\t= " + str(round(lambda1,2)) + "°")

    lambda_fast = decimal_to_degree(lambda1)

    return lambda_fast





def fast_equation2(
        sin_mode, lambda3, YUGA, DAYS_PER_YUGA, days_elapsed, mean_revolutions_per_yuga,
        slow_0_180, slow_90_270, fast_0_180, fast_90_270):

    # Returns Lamba for fast equation
    
    # computation:

    print("\tLambda 3\t= " + str(roundedlist(lambda3)))


    lambda_sigma = (YUGA * days_elapsed) / DAYS_PER_YUGA
    lambda_sigma = deg_min_sec(lambda_sigma)
    print("\tLambda_sigma\t= " + str(roundedlist(lambda_sigma)))


    kappa_sigma2 = degree_subtraction(lambda3, lambda_sigma) 
    print("\tKappa_sigma2\t= " + str(roundedlist(kappa_sigma2)))


    # geometry 
    
    if sin_mode == "Modern":
        sine = abs(math.sin(math.radians(degree_to_decimal(kappa_sigma2))))
    elif sin_mode == "Ancient":
        sine = interpol(degree_to_decimal(kappa_sigma2))

    radius = fast_0_180 + (fast_90_270 - fast_0_180) * sine
    radius = (radius * 3438) / 360
    print("\tRadius\t\t= " + str(round(radius,2)))

    
    Vm_A = 3438 * sine
    print("\tVm_A\t\t= " + str(round(Vm_A,2)))


    V_B = (radius * abs(Vm_A)) / 3438
    print("\tV_B\t\t= " + str(round(V_B,2)))

    # CORRECT VALUES UNTIL V_B


    # not sure if corr

    Vm_B = math.sqrt(radius**2 - V_B**2)
    print("\tVm_B\t\t= " + str(round(Vm_B, 2)))


    O_B = 3438 - Vm_B
    print("\tO_B\t\t= " + str(round(O_B, 2)))


    O_V = math.sqrt(O_B**2 + V_B**2)
    print("\tO_V\t\t= " + str(round(O_V, 2)))

    if sin_mode == "Modern":
        sigma = math.degrees(math.asin(( V_B / O_V )))
    elif sin_mode == "Ancient":
        sigma = interpol_inverse(((V_B / O_V) * 3438 ))

    print("\tSigma\t\t= " + str(round(sigma, 2)) + "°")
    
    sigma2 = sigma * decimal_angle(kappa_sigma2)   
    print("\tSigma 2\t\t= " + str(round(sigma2,2)) + "°")

    # final lambda
    lambda_true = degree_to_decimal(lambda3) + sigma2
    print("\tLAMBDA True\t= " + str(round(lambda_true,2)) + "°")

    lambda_true = decimal_to_degree(lambda_true)

    return lambda_true



    


def slow_equation1(
        sin_mode, lambda1, YUGA, DAYS_PER_YUGA, days_elapsed, mean_revolutions_per_yuga,
        longitude_slow_apogee, slow_0_180, slow_90_270, fast_0_180, fast_90_270):
    

    print("\tLambda 1\t= " + str(roundedlist(lambda1)))

    print("\tlongitude_slow_apogee\t= " + str(roundedlist(longitude_slow_apogee)))


    kappa_mu1 = degree_subtraction(lambda1, longitude_slow_apogee) 
    print("\tKappa_mu1\t= " + str(roundedlist(kappa_mu1)))

    
    if sin_mode == "Modern":
        sine = abs(math.sin(math.radians(degree_to_decimal(kappa_mu1))))
    elif sin_mode == "Ancient":
        sine = interpol(degree_to_decimal(kappa_mu1))
    
    radius = slow_0_180 + (slow_90_270 - slow_0_180) * sine
    radius = (radius * 3438) / 360
    print("\tRadius\t\t= " + str(round(radius,2)))

    Vm_A = 3438 * sine
    print("\tVm_A\t\t= " + str(round(Vm_A,2)))

    Vprime_B = (radius * abs(Vm_A)) / 3438
    print("\tVprime_B\t\t= " + str(round(Vprime_B,2)))

    if sin_mode == "Modern":
            mu = math.degrees(math.asin(( Vprime_B / 3438 )))
    elif sin_mode == "Ancient":
        mu = interpol_inverse(( Vprime_B ))

    print("\tMu\t\t= " + str(round(mu, 2)) + "°")

    mu1 = mu * decimal_angle(kappa_mu1)   
    print("\tMu 1\t\t= " + str(round(mu1,2)) + "°")


    # final lambda
    lambda2 = degree_to_decimal(lambda1) + 0.5 * mu1
    print("\tLAMBDA 2\t= " + str(round(lambda2,2)) + "°")

    lambda_slow = decimal_to_degree(lambda2)

    return lambda_slow



def slow_equation2(
        sin_mode, lambda2, YUGA, DAYS_PER_YUGA, days_elapsed, mean_revolutions_per_yuga,
        longitude_slow_apogee, slow_0_180, slow_90_270, fast_0_180, fast_90_270):
    

    print("\tLambda 2\t= " + str(roundedlist(lambda2)))

    print("\tlongitude_slow_apogee\t= " + str(roundedlist(longitude_slow_apogee)))


    kappa_mu2 = degree_subtraction(lambda2, longitude_slow_apogee) 
    print("\tKappa_mu2\t= " + str(roundedlist(kappa_mu2)))

    
    if sin_mode == "Modern":
        sine = abs(math.sin(math.radians(degree_to_decimal(kappa_mu2))))
    elif sin_mode == "Ancient":
        sine = interpol(degree_to_decimal(kappa_mu2))

    radius = slow_0_180 + (slow_90_270 - slow_0_180) * sine
    radius = (radius * 3438) / 360
    print("\tRadius\t\t= " + str(round(radius,2)))

    Vm_A = 3438 * sine
    print("\tVm_A\t\t= " + str(round(Vm_A,2)))

    Vprime_B = (radius * abs(Vm_A)) / 3438
    print("\tVprime_B\t\t= " + str(round(Vprime_B,2)))


    if sin_mode == "Modern":
        mu = math.degrees(math.asin(( Vprime_B / 3438 )))
    elif sin_mode == "Ancient":
        mu = interpol_inverse(( Vprime_B  ))

    print("\tMu\t\t= " + str(round(mu, 2)) + "°")

    mu2 = mu * decimal_angle(kappa_mu2)   
    print("\tMu 2\t\t= " + str(round(mu2,2)) + "°")


    # final lambda
    lambda3 = degree_to_decimal(lambda2) + mu2
    print("\tLAMBDA 3\t= " + str(round(lambda3,2)) + "°")

    lambda_slow = decimal_to_degree(lambda3)

    return lambda_slow





def slow_equation_sun(
        sin_mode, YUGA, DAYS_PER_YUGA, days_elapsed, mean_revolutions_per_yuga,
        longitude_slow_apogee, slow_0_180, slow_90_270, fast_0_180, fast_90_270):
    
    
    lambda1 = (mean_revolutions_per_yuga * days_elapsed) / DAYS_PER_YUGA
    lambda1 = deg_min_sec(lambda1)
    print("\tLambda_mean\t= " + str(roundedlist(lambda1)))
    

    print("\tlongitude_slow_apogee\t= " + str(roundedlist(longitude_slow_apogee)))



    kappa_mu1 = degree_subtraction(lambda1, longitude_slow_apogee) 
    print("\tKappa_sigma1\t= " + str(roundedlist(kappa_mu1)))

    
    if sin_mode == "Modern":
        sine = abs(math.sin(math.radians(degree_to_decimal(kappa_mu1))))
    elif sin_mode == "Ancient":
        sine = interpol(degree_to_decimal(kappa_mu1))
    
    radius = slow_0_180 + (slow_90_270 - slow_0_180) * sine
    radius = (radius * 3438) / 360
    print("\tRadius\t\t= " + str(round(radius,2)))

    Vm_A = 3438 * sine
    print("\tVm_A\t\t= " + str(round(Vm_A,2)))

    Vprime_B = (radius * abs(Vm_A)) / 3438
    print("\tVprime_B\t\t= " + str(round(Vprime_B,2)))

    if sin_mode == "Modern":
            mu = math.degrees(math.asin(( Vprime_B / 3438 )))
    elif sin_mode == "Ancient":
        mu = interpol_inverse(( Vprime_B ))

    print("\tSigma\t\t= " + str(round(mu, 2)) + "°")

    mu1 = mu * decimal_angle(kappa_mu1)   
    print("\tSigma 1\t\t= " + str(round(mu1,2)) + "°")


    # final lambda
    lambda2 = degree_to_decimal(lambda1) - 0.5 * mu1
    print("\tLAMBDA TRUE\t= " + str(round(lambda2,2)) + "°")

    lambda_slow = decimal_to_degree(lambda2)

    return lambda_slow






