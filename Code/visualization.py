import matplotlib.pyplot as plt
import seaborn as sns
import automaton
import time

# Prints the given lettice
def visualize(lettice):
    f, ax = plt.subplots(figsize=(9, 6))
    sns.heatmap(lettice, ax = ax)
    return f

if __name__ == "__main__":

    f = visualize([[1, 0], [0, 1]])
    plt.show()
    time.sleep(1)
    plt.close()
    f = visualize([[0, 0], [0, 1]])
    plt.show()