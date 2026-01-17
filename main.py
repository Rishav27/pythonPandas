import pandas as pd


def main():
    print("Hello from pandaspython!")


if __name__ == "__main__":
    data = {"name": ["Alice", "Bob", "Charlie"], "age": [25, 30, 35]}
    df = pd.DataFrame(data, index=["employee1", "employee2", "employee3"])

    # add_a_new_column
    df["job"] = ["Engineer", "Doctor", "Artist"]
    # add_a_new_row
    new_row = pd.DataFrame(
        [{"name": "David", "age": 28, "job": "Lawyer"}], index=["employee4"]
    )
    df = pd.concat([df, new_row])
    print(df)
