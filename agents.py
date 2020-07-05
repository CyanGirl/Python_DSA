import datetime
from datetime import timedelta
from datetime import datetime
import random

#a pure function which calculates the time for which an agent is available
def difference(agent):
    stamp_form='%Y-%m-%d %H:%M:%S.%f'      #format in which a timeStamp is accepted
    diff=datetime.now()-datetime.strptime(agent["available_since"],stamp_form)
    return diff.seconds/60


#filtering for all available and matched roles
def agentSelection(issue,agents,selection_mode):
    agent_available=list(filter(lambda x:x["is_available"]==True and (issue["role"].lower() in x["roles"]),agents ))
    agent_selected=[]    #to make the returns consistent
    
    
    if(selection_mode.lower()=="available all"):
        agent_selected=agent_available
        
    
    elif(selection_mode.lower()=="least busy"):
        timeList=list(map(difference,agent_available))
        least_busy=timeList.index(max(timeList))      #finding the maximum time one is available for
        agent_selected.append(agent_available[least_busy])
        
    
    #assuming random mode is available for all the agents irrespective of the availablity
    elif(selection_mode.lower()=="random"):
        random_index=random.randint(0,len(agents)-1)
        agent_selected.append(agents[random_index])
        
    else:
        return []  #if match not found, will return empty array
    
    return agent_selected
    
#End of function





#issue={"name":"XYZ","role":"sPeaker"}
#agents=[{"is_available":True,"roles":["speaker"],"available_since":"2020-06-23 10:42:51.377423"},{"is_available":True,"roles":["sales"],"available_since":"2020-06-24 07:42:51.377423"},{"is_available":True,"roles":["speaker"],"available_since":"2020-06-24 09:42:51.377423"},{"is_available":False,"roles":["speaker"],"available_since":"2020-06-24 09:42:51.377423"}]

#agentSelection(issue,agents,"random")
#agentSelection(issue,agents,"least busy")
#agentSelection(issue,agents,"availaBle all")
