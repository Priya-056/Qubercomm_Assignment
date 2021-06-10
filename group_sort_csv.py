import pandas as pd
df = pd.read_csv('C:/Users/HP/Desktop/Assignment/dataset.csv')
print(df)
print("\n")
df['first_three_digits'] = df.phno.astype(str).str[:3]
print(df)
print("\n")
grouped_obj = df.groupby(["first_three_digits"])
for key, item in grouped_obj:
    print("Key is: " + str(key))
    print(str(item), "\n\n")
    sorted_df = item.sort_values(by=["fname"], ascending=True)
    print("Sorted by fname: " + str(key))
    print(sorted_df)
    print("\n")
