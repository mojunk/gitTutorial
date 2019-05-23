from indian_method_functions import *



# input function
def collect_variables():
	# takes all input variables and stores them in global variables
	
	global celestial_body
	global days_elapsed
	global sin_mode
	global YUGA
	global DAYS_PER_YUGA
	global mean_revolutions_per_yuga
	global revolutions_fast_apogee_per_yuga
	global longitude_slow_apogee
	global slow_0_180
	global slow_90_270
	global fast_0_180
	global fast_90_270

	# special case moon



	# values:
	mean_revolutions_per_yuga = [4320000, 57753336, 2296832, 4320000, 364220, 4320000, 146568]
	revolutions_fast_apogee_per_yuga = [0, 0, 4320000, 17937060, 4320000, 7022376, 4320000]
	longitude_slow_apogee = [[77, 17, 0], ['N/A', 'N/A', 'N/A'], [130, 2, 0], [220, 27, 0],
                         [171, 18, 0], [79, 50, 0], [236, 37, 0]]
	slow_0_180 = [14, 32, 75, 30, 33, 12, 49]
	slow_90_270 = [13.333, 31.333, 72, 28, 32, 11, 48]
	fast_0_180 = [0, 0, 235, 133, 70, 262, 39]
	fast_90_270 = [0, 0, 232, 132, 72, 260, 40]

	
	# start taking input

	#celestial_body = "Jupiter"
	celestial_body = input("Enter Planet: ").title()

	sin_mode = input("Sine mode ['ancient' or 'modern']: ").title()

	



	planet_dict = {
	    'Sun' : 0,
	    'Moon' : 1,
	    'Mars' : 2,
	    'Mercury' : 3,
	    'Jupiter' : 4,
	    'Venus' : 5,
	    'Saturn' : 6,
	    }

	#planet = 4 
	planet = planet_dict[celestial_body]

	
	days_elapsed = get_number_of_days()
	YUGA = 4320000
	DAYS_PER_YUGA = 1577917828

	mean_revolutions_per_yuga = mean_revolutions_per_yuga[planet]
	revolutions_fast_apogee_per_yuga = revolutions_fast_apogee_per_yuga[planet]
	longitude_slow_apogee = longitude_slow_apogee[planet]

	slow_0_180 = slow_0_180[planet]
	slow_90_270 = slow_90_270[planet]
	fast_0_180 = fast_0_180[planet]
	fast_90_270 = fast_90_270[planet]




# print input
def print_inputs():
    # Prints all given arguments
    print("Celestial Body:\t\t\t\t " + str(celestial_body))
    print("Sine Mode: \t " + sin_mode)
    print("Yuga:\t\t\t\t\t " + str(YUGA))
    print("Days per Yuga:\t\t\t\t " + str(DAYS_PER_YUGA))
    print("Days elapsed:\t\t\t\t " + str(days_elapsed) + "\n")
    print("Mean revolutions per Yuga:\t\t " + str(mean_revolutions_per_yuga))
    print("Revolutions of fast apogee per Yuga:\t " + str(revolutions_fast_apogee_per_yuga))
    print("Longitude of slow apogee:\t\t " + str(longitude_slow_apogee))
    print("Slow 0° and 180°:\t\t\t " + str(slow_0_180))
    print("Slow 90° and 270°:\t\t\t " + str(slow_90_270))
    print("Fast 0° and 180°:\t\t\t " + str(fast_0_180))
    print("Fast 90° and 270°:\t\t\t " + str(fast_90_270))



# full iteration
def full_iteration():
	


	# lamba_1 FAST

	print("First Iteration:\n ")

	lambda1 = fast_equation1(
	        sin_mode, YUGA, DAYS_PER_YUGA, days_elapsed, mean_revolutions_per_yuga,
	        slow_0_180, slow_90_270, fast_0_180, fast_90_270)

	print("\nLambda 1 = " + str(roundedlist(lambda1)))



	# lamba_2 SLOW

	print("\nSecond Iteration:\n ")

	lambda2 = slow_equation1(sin_mode, lambda1, YUGA, DAYS_PER_YUGA, days_elapsed, mean_revolutions_per_yuga, 
				  longitude_slow_apogee, slow_0_180, slow_90_270, fast_0_180, fast_90_270)

	print("\nLambda 2 = " + str(roundedlist(lambda2)))



	# lamba_3 SLOW

	print("\nThird Iteration:\n ")

	lambda3 = slow_equation2(sin_mode, lambda2, YUGA, DAYS_PER_YUGA, days_elapsed, mean_revolutions_per_yuga, 
				  longitude_slow_apogee, slow_0_180, slow_90_270, fast_0_180, fast_90_270)

	print("\nLambda 3 = " + str(roundedlist(lambda3)))



	# lamba_4 FAST

	print("\nFourth Iteration:\n ")

	lambda_true = fast_equation2(
	        sin_mode,lambda3, YUGA, DAYS_PER_YUGA, days_elapsed, mean_revolutions_per_yuga,
	        slow_0_180, slow_90_270, fast_0_180, fast_90_270)


	print("\nLambda True = " + str(roundedlist(lambda_true)))



	return lambda_true






# input

collect_variables()
print_inputs()
print("\n")

# computation 


if celestial_body == "Sun" or celestial_body == "Moon":

	lambda2 = slow_equation_sun(sin_mode, YUGA, DAYS_PER_YUGA, days_elapsed, mean_revolutions_per_yuga, 
				  longitude_slow_apogee, slow_0_180, slow_90_270, fast_0_180, fast_90_270)

	print("\nLambda TRUE = " + str(roundedlist(lambda2)))




else:
	full_iteration()



















