import pandas as pd


def main():
    print("Hello from pandaspython!")


if __name__ == "__main__":
    df = pd.read_csv("data/data.csv", index_col="Name")

    # Whole DataFrame
    # print(df.sum(numeric_only=True))
    # print(df.mean( numeric_only=True))
    # print(df.min( numeric_only=True))
    # print(df.max( numeric_only=True))
    # print(df.count())

    # single column
    # print(df["Height"].sum())
    # print(df["Height"].mean())
    # print(df["Height"].min())
    # print(df["Height"].max())
    # print(df["Height"].count())

    group = df.groupby("Type1")

    # print(group["Height"].mean())
    # print(group["Height"].count())
