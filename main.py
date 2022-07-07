
import pandas

data = pandas.read_csv("50_states.csv")
all_states = data.state.to_list()

learning_list = [state for state in all_states if state not in guessed_states]

new_data = pandas.DataFrame(learning_list)

new_data.to_csv("State_to_learn.csv")




