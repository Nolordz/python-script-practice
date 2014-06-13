#Exersise 4
years = float(raw_input("Please enter the number of years to see estimated population:"))

US_POPULATION = 307357870
BIRTH = 7
DEATH = 13
IMMIGRANT = 35
SEC_IN_A_YEAR = 31536000


BIRTH_IN_A_YEAR = SEC_IN_A_YEAR / BIRTH
DEATH_PER_YEAR = SEC_IN_A_YEAR / DEATH
IMMIGRANT_PER_YEAR = SEC_IN_A_YEAR / IMMIGRANT
GROWING_POPULATION = BIRTH_IN_A_YEAR + IMMIGRANT
NEW_POPULATION = GROWING_POPULATION * years


print "New population in" ,int(years),"years will change by",(BIRTH_IN_A_YEAR),"to be",(NEW_POPULATION)

