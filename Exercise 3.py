

#Exersise 3
BARLEYCORNS_IN_METER = 117.647
ONE_METER__IN_FURLONGS = 201.170
HOURS_IN_DAY = 24.0
METERS_IN_MILE = 1609.344
YARDS_IN_MILE = 1760
DAYS_IN_FORTNIGHT = 14
MACH_IN_HOUR = 767.7
FURLONG_IN_HOUR = 2688
SPEED_OF_LIGHT = 1.491 * 10**-9

miles = float(raw_input ("Please, enter a value for speed in miles per hour: "))
print "Original speed in mph: %.1f" % miles

num_barleycorn = (miles * METERS_IN_MILE * BARLEYCORNS_IN_METER) * HOURS_IN_DAY
num_furlongs = miles * FURLONG_IN_HOUR
num_mach = miles / MACH_IN_HOUR
num_speed_of_light = miles * SPEED_OF_LIGHT

print "Converted to barleycorn/day is: %s" % num_barleycorn
print "Converted to furlongs/fortnight is: %s" % num_furlongs
print "Converted to Mach number is : %s" % num_mach
print "Converted to the percentage of the speed of light is %s" % num_speed_of_light"""




