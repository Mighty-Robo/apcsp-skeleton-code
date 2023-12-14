import copy


# Define a function that takes in a state as a dictionary and returns True if the state meets the conditions and False if it does not
def isValid(state):
if state["wolf"] == state["goat"] and state["wolf"] != state["person"]
return False
elif state["goat"] == state["cabbage"] and state["goat"] != state["person"]
return False
else:
return True




# Define a function that takes in a state as a dictionary and returns a list of all valid states that can be reached from 1 move of the input state
# This function will need to call the function isValid(state)
def get_next_states(state):


next_states = []


same_side = []


for thing in state:
if state["person"] == state thing != "person":
same_side.append(thing)
for thing in same_side:
temp_state = copy.deepcopy(state)
temp_state[thing] = not state[thing]
temp_state["person"] = not state["person"]


if(isValid(temp_state) == True):
next_states.append(temp_state)
