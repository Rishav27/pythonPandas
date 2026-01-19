import pandas as pd


def main():
    print("Hello from pandaspython!")


if __name__ == "__main__":
    df = pd.read_csv("data/data.csv")

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

    # group = df.groupby("Type1")

    # print(group["Height"].mean())
    # print(group["Height"].count())

    # drop irravalent data
    # df = df.drop(columns=["Legendary", "No"])

    # handle missing data
    # df = df.dropna(subset = ["Type2"])
    # df = df.fillna({"Type2" : "None"})

    # fix inconstint data
    # df["Type1"] = df["Type1"].replace({"Grass" : "GRASS",
    #                                    "Fire" : "FIRE",
    #                                    "Water" : "WATER"})
    # df["Type2"] = df["Type2"].replace({"Grass" : "GRASS",
    #                                    "Fire" : "FIRE",
    #                                    "Water" : "WATER"})

    # standardize text
    # df["Name"] = df["Name"].str.lower()

    # fix data type
    # df["Legendary"] = df["Legendary"].astype(bool)

    # REmove the dublicate data
    # df = df.drop_duplicates()

    print(df.to_string())
