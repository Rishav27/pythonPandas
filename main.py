import pandas as pd


def main():
    print("Hello from pandaspython!")


if __name__ == "__main__":
    df = pd.read_csv("data/data.csv", index_col="Name")

    # tall_poki = df[df['Height']>2]
    # Heavy_poki = df[df['Weight']>=100]
    # legen_poki = df[df['Legendary']>=1]

    # waterType = df[(df["Type1"] == "Water") |
    #                (df["Type2"] == "Water")]

    ff_poki = df[(df["Type1"] == "Fire") & (df["Type2"] == "Flying")]
    print(ff_poki)
