import pandas as pd


def main():
    print("Hello from pandaspython!")


if __name__ == "__main__":
    data = ["Bulbasaur", "Ivysaur", "Venusaur", "Charmander", "Charmeleon", "Chalizard"]

    series = pd.Series(data, index=["1", "2", "3", "4", "5", "6"])

    print(series)
