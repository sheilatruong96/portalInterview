from datetime import datetime

##create data structure that contains/represents all the information
events = ["Interview at the Portal: Feb 23 2017 3:00PM - 4:30PM",
 "Lunch with Cindy: Feb 25 2017 12:00PM - 1:00PM",
 "Dinner with John: Feb 24 2017 5:00PM - 5:30PM",
 "Conference: Feb 24 2017 11:00AM - 4:30PM"]

eventDict = dict()
for eachEvent in events:
    eventandDatetime = eachEvent.split(": ",1)
    eventDict[eventandDatetime[0]] = eventandDatetime[1]

##Add 4 more vents to dataset making sure 2 added events overlap

eventDict["Morning job"] = 'Nov 1 2017 12:00PM - 3:00PM'
eventDict["Dinner with family"] = 'Nov 1 2017 10:00AM - 1:00PM'
eventDict["Study for midterm"] = 'Feb 25 2017 1:00PM - 3:00PM'
eventDict["Project Presentation"] = 'Nov 2 2017 12:00PM - 3:00PM'

##Develop algorithm to find overlapping events


##remake specific dictionary
for event in eventDict:
    splitPart = eventDict[event].split("-")
    firstPart = splitPart[0].strip()
    secPart = splitPart[1].strip()
    eventDate = datetime.strptime(firstPart,'%b %d %Y %I:%M%p').date()
    eventStartTime = datetime.strptime(firstPart,'%b %d %Y %I:%M%p').time()
    eventEndTime = datetime.strptime(secPart,'%I:%M%p').time()

    eventDict[event] = dict()
    eventDict[event][eventDate] = (eventStartTime, eventEndTime)

dateConflict = dict()
##check for date conflict
for item in eventDict:
    for d in eventDict[item]:
        if d not in dateConflict:
            dateConflict[d] = [item]
        else:
            dateConflict[d].append(item)

##check for time conflict
start = 0
end = 0
for eachDate in dateConflict:
    if len(dateConflict[eachDate]) > 1:
        for eachEvent in dateConflict[eachDate]:
            start = eventDict[eachEvent][eachDate][0]
            end = eventDict[eachEvent][eachDate][1]
            
        
    
