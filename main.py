# These are the provided data samples.
mission_names = ['Apollo 11', 'Challenger', 'Curiosity Rover', 'Viking 1', 'Mars Pathfinder', 'Hubble Telescope', 'Apollo 13']
mission_years = [1969, 1986, 2012, 1975, 1996, 1990, 1970]
mission_success = [True, False, True, True, True, True, False]

# These three variable lines are used to count and store data from the list above.
# The first variable counts how many missions there are with "TotalMissionsNum."
# The second variable counts how many successful missions there have been with "SuccessfulMissionsNum."
# The last variable stores the names of the missions that launched before the year 2000 with "MissionsPreY2K."
TotalMissionsNum = 0
SuccessfulMissionsNum = 0
MissionsPreY2K = []

# The first line initiates the for loop that iterates each mission's indexed data until it counts the final number of missions available in the data.
# "TotalMissionsNum" counts how many missions there are in the data.
# The first if statement counts how many successful missions are in "mission_success" and then adds the amount to "SuccessfulMissionsNum."
# The second if statement checks if "mission_years" is less than 2000 and then adds the corresponding name from "mission_names" to "MissionsPreY2K."
for i in range(len(mission_names)):
    TotalMissionsNum += 1
    if mission_success[i]:
        SuccessfulMissionsNum += 1
    if mission_years[i] < 2000:
        MissionsPreY2K.append(mission_names[i])

# The calculated rate of successful missions is stored in "MissionSuccessRate."
# It is calculated by dividing the number of successful missions by the total number of missions and then multiplying that by 100. (5/7) * 100 = 71.42857.
# The "MissionSuccessRate" result is saved into "SuccessRateVariable" so it can be printed later with proper formatting.
MissionSuccessRate = (SuccessfulMissionsNum / TotalMissionsNum) * 100
SuccessRateVariable = MissionSuccessRate

# These print lines print out the updated data into the required assignment template.
# The first print line converts and prints the total number of missions, "TotalMissionsNum," from integers to strings.
# Again, the second print line does the same as the first print line but with the "SuccessfulMissionsNum" data.
# Next, the third print line takes the calculated success rate number that was stored in "SuccessRateVariable" and formats it to two decimal places. 71.43
# The fourth print line prints the string "Missions launched before the year 2000: "
# Finally, the last two lines belong to the second for loop, "MissionNameOutput," which loops and prints the data from "MissionsPreY2K," so it matches the required format design.
print("Total number of missions: " + str(TotalMissionsNum))
print("Number of successful missions: " + str(SuccessfulMissionsNum))
print(f"Success rate: {SuccessRateVariable:.2f}%")
print("Missions launched before the year 2000:")
for MissionNameOutput in MissionsPreY2K:
    print("- " + MissionNameOutput)
