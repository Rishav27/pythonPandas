import pandas as pd


def main():
    print("Hello from pandaspython!")


if __name__ == "__main__":
    df = pd.read_csv("data/data.csv", index_col="Name")

    # df = pd.read_json("data/data.json")
    n = input("Enter a pokimon name:")
    try:
        print(df.loc[n])
    except KeyError:
        print("Pokimon not found")

