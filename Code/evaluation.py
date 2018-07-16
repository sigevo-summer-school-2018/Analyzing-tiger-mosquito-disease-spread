import pandas as pd

def read_data():    
    data = pd.read_csv("../Data/flu.csv")
    return [d / 100 for d in list(data["Positive"])]

# Gets a lettice and returns the fitness of the solution.
def run(percentage_of_dead_list):
    """
    Input 40 lettice in list

    Parameters
    ----------
    percentage_of_dead_list: Percentage of dead in each checkpoint

    Returns
    -------
    How close the result compare with the realworld data
    Measure in real number
    """
    diff = 0
    real_data = read_data()
    for i in range(len(real_data)):
        diff += abs(read_data[i] - percentage_of_dead_list[i])
    return diff