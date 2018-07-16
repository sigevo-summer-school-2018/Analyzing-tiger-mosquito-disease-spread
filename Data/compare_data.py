import pandas as pd

def read_data():    
    data = pd.read_csv("/home/nixizi/Repository/Analyzing-tiger-mosquito-disease-spread/Data/flu.csv")
    return [d / 100 for d in list(data["Positive"])]

if __name__ == "__main__":
    print(read_data())