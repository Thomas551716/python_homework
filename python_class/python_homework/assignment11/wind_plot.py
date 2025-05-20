import plotly.express as px
import plotly.data as pldata

# Load dataset
df = pldata.wind(return_type='pandas')

# Print head and tail
print("First 10 rows:")
print(df.head(10))
print("Last 10 rows:")
print(df.tail(10))

# Clean 'strength' column
df['strength'] = df['strength'].str.replace(r'\D', '', regex=True).astype(float)

# Create interactive plot
fig = px.scatter(df, x='frequency', y='strength', color='direction', title='Wind Strength vs Frequency')
fig.write_html("wind.html")
fig.show()