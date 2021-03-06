from indian_method_functions import *



sin_table = [[3.75, 225], [7.5, 449], [11.25, 671], [15, 890], 
			[18.75, 1105], [22.5, 1315 ], [26.25, 1520], [30, 1719], 
			[33.75, 1910], [37.5, 2093], [41.25, 2267], [45, 2431],
			[48.75, 2585], [52.5, 2728], [56.25, 2859], [60, 2978],
			[63.75, 3084], [67.5, 3177], [71.25, 3256], [75, 3321],
			[78.75, 3372], [82.5, 3409], [86.25, 3431], [90, 3438],

			[93.75, 3431], [97.5, 3409], [101.25, 3372], [105, 3321],
			[108.75, 3256], [112.5, 3177], [116.25, 3084], [120, 2978],
			[123.75, 2859], [127.5, 2728], [131.25, 2585], [135, 2431],
			[138.75, 2267], [142.5, 2093], [146.25, 1910], [150, 1719],
			[153.75, 1520], [157.5, 1315], [161.25, 1105], [165, 890],
			[168.75, 671], [172.5, 449], [176.25, 225], [180, 0],

			[183.75, 225], [187.5, 449], [191.25, 671], [195, 890], 
			[198.75, 1105], [202.5, 1315 ], [206.25, 1520], [210, 1719], 
			[213.75, 1910], [217.5, 2093], [221.25, 2267], [225, 2431],
			[228.75, 2585], [232.5, 2728], [236.25, 2859], [240, 2978],
			[243.75, 3084], [247.5, 3177], [251.25, 3256], [255, 3321],
			[258.75, 3372], [262.5, 3409], [266.25, 3431], [270, 3438],

			[273.75, 3431], [277.5, 3409], [281.25, 3372], [285, 3321],
			[288.75, 3256], [292.5, 3177], [296.25, 3084], [300, 2978],
			[303.75, 2859], [307.5, 2728], [311.25, 2585], [315, 2431],
			[318.75, 2267], [322.5, 2093], [326.25, 1910], [330, 1719],
			[333.75, 1520], [337.5, 1315], [341.25, 1105], [345, 890],
			[348.75, 671], [352.5, 449], [356.25, 225], [3600, 0],]



def interpol(x):
	# returns interpolated value f(x) = y, sin(x) in this case
	sin_table = [[3.75, 225], [7.5, 449], [11.25, 671], [15, 890], 
			[18.75, 1105], [22.5, 1315 ], [26.25, 1520], [30, 1719], 
			[33.75, 1910], [37.5, 2093], [41.25, 2267], [45, 2431],
			[48.75, 2585], [52.5, 2728], [56.25, 2859], [60, 2978],
			[63.75, 3084], [67.5, 3177], [71.25, 3256], [75, 3321],
			[78.75, 3372], [82.5, 3409], [86.25, 3431], [90, 3438],

			[93.75, 3431], [97.5, 3409], [101.25, 3372], [105, 3321],
			[108.75, 3256], [112.5, 3177], [116.25, 3084], [120, 2978],
			[123.75, 2859], [127.5, 2728], [131.25, 2585], [135, 2431],
			[138.75, 2267], [142.5, 2093], [146.25, 1910], [150, 1719],
			[153.75, 1520], [157.5, 1315], [161.25, 1105], [165, 890],
			[168.75, 671], [172.5, 449], [176.25, 225], [180, 0],

			[183.75, 225], [187.5, 449], [191.25, 671], [195, 890], 
			[198.75, 1105], [202.5, 1315 ], [206.25, 1520], [210, 1719], 
			[213.75, 1910], [217.5, 2093], [221.25, 2267], [225, 2431],
			[228.75, 2585], [232.5, 2728], [236.25, 2859], [240, 2978],
			[243.75, 3084], [247.5, 3177], [251.25, 3256], [255, 3321],
			[258.75, 3372], [262.5, 3409], [266.25, 3431], [270, 3438],

			[273.75, 3431], [277.5, 3409], [281.25, 3372], [285, 3321],
			[288.75, 3256], [292.5, 3177], [296.25, 3084], [300, 2978],
			[303.75, 2859], [307.5, 2728], [311.25, 2585], [315, 2431],
			[318.75, 2267], [322.5, 2093], [326.25, 1910], [330, 1719],
			[333.75, 1520], [337.5, 1315], [341.25, 1105], [345, 890],
			[348.75, 671], [352.5, 449], [356.25, 225], [3600, 0],]


	# finding x1, x2, y1, y2
	prev_value_x = 0
	prev_value_y = 0
	for value in sin_table:
		if value[0] >= x:
			x2 = value[0]
			y2 = value[1]
			x1 = prev_value_x
			y1 = prev_value_y
			break
			
		prev_value_x = value[0]
		prev_value_y = value[1]

	y = y1 + ((x - x1) * (y2 - y1)) / (x2 - x1)
	return y / 3438


def interpol_inverse(y):
	# returns interpolated value x = f^-1(y), in this case arcsin(y) = x

	sin_table = [[3.75, 225], [7.5, 449], [11.25, 671], [15, 890], 
			[18.75, 1105], [22.5, 1315 ], [26.25, 1520], [30, 1719], 
			[33.75, 1910], [37.5, 2093], [41.25, 2267], [45, 2431],
			[48.75, 2585], [52.5, 2728], [56.25, 2859], [60, 2978],
			[63.75, 3084], [67.5, 3177], [71.25, 3256], [75, 3321],
			[78.75, 3372], [82.5, 3409], [86.25, 3431], [90, 3438],

			[93.75, 3431], [97.5, 3409], [101.25, 3372], [105, 3321],
			[108.75, 3256], [112.5, 3177], [116.25, 3084], [120, 2978],
			[123.75, 2859], [127.5, 2728], [131.25, 2585], [135, 2431],
			[138.75, 2267], [142.5, 2093], [146.25, 1910], [150, 1719],
			[153.75, 1520], [157.5, 1315], [161.25, 1105], [165, 890],
			[168.75, 671], [172.5, 449], [176.25, 225], [180, 0],

			[183.75, 225], [187.5, 449], [191.25, 671], [195, 890], 
			[198.75, 1105], [202.5, 1315 ], [206.25, 1520], [210, 1719], 
			[213.75, 1910], [217.5, 2093], [221.25, 2267], [225, 2431],
			[228.75, 2585], [232.5, 2728], [236.25, 2859], [240, 2978],
			[243.75, 3084], [247.5, 3177], [251.25, 3256], [255, 3321],
			[258.75, 3372], [262.5, 3409], [266.25, 3431], [270, 3438],

			[273.75, 3431], [277.5, 3409], [281.25, 3372], [285, 3321],
			[288.75, 3256], [292.5, 3177], [296.25, 3084], [300, 2978],
			[303.75, 2859], [307.5, 2728], [311.25, 2585], [315, 2431],
			[318.75, 2267], [322.5, 2093], [326.25, 1910], [330, 1719],
			[333.75, 1520], [337.5, 1315], [341.25, 1105], [345, 890],
			[348.75, 671], [352.5, 449], [356.25, 225], [3600, 0],]


	# finding x1, x2, y1, y2
	prev_value_x = 0
	prev_value_y = 0

	for value in sin_table:
		if value[1] >= y:
			y2 = value[1]
			x2 = value[0]
			y1 = prev_value_x
			x1 = prev_value_y
			break
				
		prev_value_x = value[1]
		prev_value_y = value[0]

	x = x1 + ((y - y1) * (x2 - x1)) / (y2 - y1)
	return x 





