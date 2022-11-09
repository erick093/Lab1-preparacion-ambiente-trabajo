import pandas as pd
import sys

# Defining a simple data dictionary
data_dict = {
    "name": ["erick", "juan"],
    "age": [7, 8]
}

# Create a dataframe
df = pd.DataFrame(data_dict)

# Display the dataframe
print(df.head())

# Display a welcome message
print(f"Hello {sys.argv[1]}")
