"""
Created on 11/26/23

@author: colefitzgerald
"""

import matplotlib.pyplot as plt
import pandas as pd  # Assuming you have your data in a pandas DataFrame

file_path = r'/Users/colefitzgerald/Library/Mobile Documents/com~apple~CloudDocs/Documents/reddit_data.csv'  # TODO: PUT NAME OF FILE HERE
df = pd.read_csv(file_path)


# Scatter plot
plt.figure(figsize=(10, 6))
plt.bar(df['ID'], df['Sentiment'], color='lightgreen')

# Adds labels and title
plt.xlabel('Coin Name')
plt.ylabel('Measured Sentiment 0.0-10.0')
plt.title('Sentiment Analysis of Surveyed Data (Reddit)')

# Annotate each point with the corresponding coin name
for i, txt in enumerate(df['Coin']):
    plt.annotate(txt, (df['ID'][i], df['Sentiment'][i]), textcoords="offset points", xytext=(0,5), ha='center')

# Show the plot
plt.show()

if __name__ == '__main__':
    pass