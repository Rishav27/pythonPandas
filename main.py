import pandas as pd


def main():
    print("Hello from pandaspython!")


if __name__ == "__main__":
    # df = pd.read_csv("data.csv")

    df = pd.read_json("data.json")
    print(df.to_string())
