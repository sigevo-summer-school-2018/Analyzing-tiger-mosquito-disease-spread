import matplotlib.pyplot as plt
import seaborn as sns

# Prints the given lettice
def visualize(lettice):
    f, ax = plt.subplots(figsize=(9, 6))
    sns.heatmap(lettice, annot=True, fmt="d", linewidths=.5, ax=ax)
    return f

if __name__ == "__main__":
    f = visualize([[1, 0], [0, 1]])
    plt.show()
    f = visualize([[0, 0], [0, 1]])
    plt.show()