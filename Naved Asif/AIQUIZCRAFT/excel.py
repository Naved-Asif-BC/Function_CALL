import pandas as pd

# Load the Excel file into a pandas DataFrame
file_path = 'questions.xlsx'  # Replace 'path_to_your_excel_file.xlsx' with the actual file path
df = pd.read_excel(file_path)

# Define a function to extract options from the 'options' column
def extract_options(options_str):
    options_str = options_str.strip("[]")  # Remove square brackets
    options = [option.strip("' ") for option in options_str.split(",")]  # Split options and remove leading/trailing characters
    return options

# Apply the 'extract_options' function to the 'options' column to create separate columns for options
df['Option 1'], df['Option 2'], df['Option 3'], df['Option 4'] = zip(*df['options'].apply(extract_options))

# Drop the original 'options' column as it's no longer needed
df.drop(columns='options', inplace=True)

# Save the modified DataFrame back to a new Excel file
output_file_path = 'new_file.xlsx'  # Replace 'path_to_output_excel_file.xlsx' with the desired output file path
df.to_excel(output_file_path, index=False)
