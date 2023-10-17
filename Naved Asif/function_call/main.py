import pandas as pd

# Read the Excel sheet into a DataFrame
excel_file = "pitchpal.xlsx"  # Replace with the actual path to your Excel file
df = pd.read_excel(excel_file)

# Convert the DataFrame to a list of dictionaries
data_dict_list = df.to_dict(orient="records")

# Print the list of dictionaries
print(data_dict_list)
