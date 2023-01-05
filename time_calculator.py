def add_time(start, duration, day="unknown"):
    
    dayNames = {

      "Monday" : 0,
      "Tuesday" : 1,
      "Wednesday" : 2,
      "Thursday" : 3,
      "Friday" : 4,
      "Saturday" : 5,
      "Sunday" : 6

    }

    dayNamesReverse = {

      0 : "Monday",
      1 : "Tuesday",
      2 : "Wednesday",
      3 : "Thursday",
      4 : "Friday",
      5 : "Saturday",
      6 : "Sunday"

    }

    dayWeek = day
    dayWeek = dayWeek.lower()
    dayWeek = dayWeek.title()

    startSplit = start.split(" ")
    startSplitTime = startSplit[0].split(":")
    startSplitDay = startSplit[1]

    durationSplit = duration.split(":")

    startHour = int(startSplitTime[0])
    durationHour = int(durationSplit[0])
    startMin = int(startSplitTime[1])
    durationMin = int(durationSplit[1])

    totalHour = startHour + durationHour
    totalMin = startMin + durationMin
    originalTotalHour = totalHour
    
    dayCountRound = int(-(-totalHour // 24))

    if totalMin / 60 > 1:
      totalHour += 1
      totalMin = totalMin % 60

    if totalHour < 35:
      dayCountRound = 0
    if totalHour > 24 and totalHour < 35:
      dayCountRound = 1

    amPMCycle = 0

    if startSplitDay == "AM":
      amPMCycle += 2
      amPMCycle = amPMCycle + int(totalHour / 12)

      if amPMCycle % 2 == 0:
        timeDay = "AM"
        totalHour = totalHour % 12
      else:
        timeDay = "PM"
        totalHour = totalHour % 12
    else:
      amPMCycle += 1
      amPMCycle = amPMCycle + int(totalHour / 12)

      if amPMCycle % 2 != 0:
        timeDay = "PM"
        totalHour = totalHour % 12
      else:
        timeDay = "AM"
        totalHour = totalHour % 12

    if totalHour == 0:
      totalHour = 12

    if totalMin < 10:
      totalMin = "0" + str(totalMin)

    if dayWeek != "Unknown":

      dayWeek = dayNames[dayWeek]
      dayWeek = dayWeek + int(-(-dayCountRound))
      finalDay = dayWeek % 7
      finalDay = dayNamesReverse[finalDay]

      if originalTotalHour <= 24 and timeDay == startSplitDay and startSplitDay != "PM":
        new_time = str(totalHour) + ":" + str(totalMin) + " " + timeDay + ", " + finalDay

      elif originalTotalHour <= 24 and timeDay == startSplitDay and startSplitDay == "PM":
        new_time = str(totalHour) + ":" + str(totalMin) + " " + timeDay + ", " + finalDay
    
      elif originalTotalHour <= 24 and timeDay != startSplitDay and startSplitDay != "PM":
        new_time = str(totalHour) + ":" + str(totalMin) + " " + timeDay + ", " + finalDay

      elif originalTotalHour < 35 and timeDay != startSplitDay and startSplitDay == "PM":
        new_time = str(totalHour) + ":" + str(totalMin) + " " + timeDay + ", " + finalDay + " (" + "next day)"

      elif originalTotalHour < 35 and timeDay == startSplitDay and startSplitDay != "PM":
        new_time = str(totalHour) + ":" + str(totalMin) + " " + timeDay + ", " + finalDay + " (" + "next day)"

      else:
        new_time = str(totalHour) + ":" + str(totalMin) + " " + timeDay + ", " + finalDay + " (" + str(dayCountRound) + " days later)"

    else:
      if originalTotalHour <= 24 and timeDay == startSplitDay and startSplitDay != "PM":
        new_time = str(totalHour) + ":" + str(totalMin) + " " + timeDay

      elif originalTotalHour <= 24 and timeDay == startSplitDay and startSplitDay == "PM":
        new_time = str(totalHour) + ":" + str(totalMin) + " " + timeDay
    
      elif originalTotalHour <= 24 and timeDay != startSplitDay and startSplitDay != "PM":
        new_time = str(totalHour) + ":" + str(totalMin) + " " + timeDay

      elif originalTotalHour < 35 and timeDay != startSplitDay and startSplitDay == "PM":
        new_time = str(totalHour) + ":" + str(totalMin) + " " + timeDay + " (" + "next day)"

      elif originalTotalHour < 35 and timeDay == startSplitDay and startSplitDay != "PM":
        new_time = str(totalHour) + ":" + str(totalMin) + " " + timeDay + " (" + "next day)"

      else:
        new_time = str(totalHour) + ":" + str(totalMin) + " " + timeDay + " (" + str(dayCountRound) + " days later)"

    return new_time