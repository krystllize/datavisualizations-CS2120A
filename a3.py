import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.lines import Line2D
import plotly.express as px

# -------------------- Visual 1: Pizza Hut Scatterplot - Latitude vs. Longitude Plot ----------------------------------

x1, y1 = 'Latitude', 'Longitude'
pizzahuts = pd.read_csv('pizzahut.csv', names=[x1, y1, 'state'])

# regions for reference:
# west = ['WA', 'OR', 'ID', 'MT', 'WY', 'CO', 'NM', 'AZ', 'CA', 'NV', 'UT', 'AK', 'HI']
# midwest = ['ND', 'SD', 'NE', 'KS', 'OK', 'MN', 'IA', 'MO', 'WI', 'IL', 'IN', 'MI', 'OH']
# south = ['TX', 'AR', 'LA', 'MS', 'TN', 'KY', 'WV', 'VA', 'NC', 'SC', 'GA', 'FL', 'AL']
# northeast = ['MD', 'PA', 'NY', 'VT', 'NH', 'DC', 'MA', 'ME', 'RI', 'CT', 'NJ', 'DE']
# canada = ['AB', 'BC', 'MB', 'NB', 'NS', 'ON', 'QC', 'SK', 'YT']

# creating a color dictionary to assign each state to a region of a specific color, where West = red,
# Midwest = green, South = yellow, Northeast = blue, and Canada = Magenta.
colors = {'WA':'r', 'OR':'r', 'ID':'r', 'MT':'r', 'WY':'r', 'CO':'r', 'NM':'r', 'AZ':'r', 'CA':'r', 'NV':'r', 'UT':'r', 'AK':'r', 'HI':'r',
          'ND':'g', 'SD':'g', 'NE':'g', 'KS':'g', 'OK':'g', 'MN':'g', 'IA':'g', 'MO':'g', 'WI':'g', 'IL':'g', 'IN':'g', 'MI':'g', 'OH':'g',
          'TX':'y', 'AR':'y', 'LA':'y', 'MS':'y', 'TN':'y', 'KY':'y', 'WV':'y', 'VA':'y', 'NC':'y', 'SC':'y', 'GA':'y', 'FL':'y', 'AL':'y',
          'MD':'b', 'PA':'b', 'NY':'b', 'VT':'b', 'NH':'b', 'DC':'b', 'MA':'b', 'ME':'b', 'RI':'b', 'CT':'b', 'NJ':'b', 'DE':'b',
          'AB':'m', 'BC':'m', 'MB':'m', 'NB':'m', 'NS':'m', 'ON':'m', 'QC':'m', 'SK':'m', 'YT':'m'}

figure, axis = plt.subplots(figsize=(18,10))

# plotting points for scatterplot and assigning the respective colors to each region from the color dictionary:
for i in range(len(pizzahuts[x1])):
    axis.scatter(pizzahuts[x1][i], pizzahuts[y1][i], s=10, color=colors[pizzahuts['state'][i]])

# plotting legend elements
legend_elements = [Line2D([0],[0], marker='o', color='w', label="US West", markerfacecolor='r', markersize=10),
                   Line2D([0],[0], marker='o', color='w', label="US Midwest", markerfacecolor='g', markersize=10),
                   Line2D([0],[0], marker='o', color='w', label="US South", markerfacecolor='y', markersize=10),
                   Line2D([0],[0], marker='o', color='w', label="US Northeast", markerfacecolor='b', markersize=10),
                   Line2D([0],[0], marker='o', color='w', label="Canada", markerfacecolor='m', markersize=10)]
axis.legend(handles=legend_elements, loc='upper right')

# setting gridlines and axis labels
axis.grid(True)
axis.set_title("Latitude vs Longitude of Pizza Huts in the US and Canada")
axis.set_xlabel(x1)
axis.set_ylabel(y1)
plt.show()

# -------------------- Visual 2: Tesla YTD Daily Stock Price Line Chart (Dec 31 2019 - Nov 19 2020)---------------------

data = pd.read_csv('TSLA.csv')

# creating a line chart
tesla = px.line(data, x = data['Date'], y = data['Share Price in USD'], title = "Tesla YTD Daily Share Price")

# changing visual aspects of chart
tesla.update_layout(plot_bgcolor='rgb(255, 235,235)', font_color='black')
tesla.show()

# -------------------- Visual 3: Bar graph Calorie Count for various fruits --------------------------------------------

# tuples of the fruit names and their respective calories
names_data = ("Rhubarb", "Lemon", "Lime", "Watermelon", "Starfruit", "Strawberries", "Cantaloupe", "Peach", "Greengage", "Mulberries",
              "Blackberries", "Papaya", "Nectarine", "Plum", "Cranberries", "Clementine", "Orange", "Apricot", "Physalis", "Cherries",
              "Blood Oranges", "Fruit salad", "Pineapple", "Raspberries", "Apple", "Mandarin Oranges", "Tangerine", "Currants", "Quince",
              "Blueberries", "Pear", "Mango", "Kiwi", "Minneola", "Lychees", "Guava", "Applesauce", "Grapes", "Acai", "Figs", "Jujube",
              "Rambutan", "Pomegranate", "Banana", "Jackfruit", "Passion Fruit", "Custard Apple", "Olives", "Plantains", "Persimmon",
              "Avocado", "Tamarind", "Dates", "Raisins")
calories_data = (21, 29, 30, 30, 31, 32, 34, 39, 41, 43, 43, 43, 44, 46, 46, 47, 47, 48, 49, 50, 50, 50, 50, 52, 52, 53, 53,
                 56, 57, 57, 57, 60, 61, 63, 66, 68, 68, 69, 70, 74, 79, 82, 83, 89, 95, 97, 101, 115, 122, 127, 160, 239,
                 282, 299)

fruit_names = list(names_data)
fruit_calories = list(calories_data)

plt.figure(figsize=(18,10))
plt.bar(fruit_names, fruit_calories, color='black')

# creating gridlines
plt.grid(which='major', linestyle='-', color='black', axis='y')
plt.minorticks_on()
plt.grid(which='minor', color='#d3d3d3', linestyle='-', axis='y')

# Since the graph kept on getting cut off at the bottom:
plt.gcf().subplots_adjust(bottom=0.20)

# adjusting visual aspects and including axis titles
plt.xticks(rotation = 90)
plt.xlabel("Fruit type (per 100g)")
plt.ylabel("Calories")
plt.title("Calorie Count for various fruits per 100g")
plt.show()