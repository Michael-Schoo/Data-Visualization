import matplotlib.pyplot as plt
from clean_data import simplify_bom_data, simplify_us_data
from get_data import GetData


#### Retrieving & Manipulating the data ####
# Getting data
print("getting data...")
raw_bom_data = GetData().get_bom_weather()
print("gotten BOM data!")
raw_us_data = GetData().get_us_2021_weather()
print("gotten US data!")

# Cleaning data
print("simplifing DOM data...")
better_data_bris = simplify_bom_data(raw_bom_data.brisbane)
print("simplified BOM data!")
print("simplifing US data...")
better_data_klax = simplify_us_data(raw_us_data.klax)
print("simplified US data!")


#### Temperature plot ####
plt.subplot(2, 1, 1)

# set basic data
plt.title("Temperatures across places")
plt.ylabel("Average Temperature (C)")

# add first data (Brisbane - BOM)
plot1, = plt.plot([f"{str(data.year).removeprefix('20')}/{str(data.month)}" for data in better_data_bris], [data.temp for data in better_data_bris], label="Brisbane", color="C0")
plt.tick_params(colors="C0", axis="x")

# add second data (Klax - US)
twin = plt.twiny(plt)
plot2, = twin.plot([f"{str(data.year).removeprefix('20')}/{str(data.month)}" for data in better_data_klax], [data.temp for data in better_data_klax], label="KLAX", color="C1", )
twin.tick_params(colors="C1", axis="x")

# Add the second's ticks underneath first data
twin.xaxis.set_ticks_position("bottom")
twin.xaxis.set_label_position("bottom")
twin.spines["bottom"].set_position(("outward", 25))

# add legend & other basic data
plt.xlabel("Date")
plt.legend(handles=[plot1, plot2], loc="upper left")


#### Precipitation plot ###
plt.subplot(2, 1, 2)
plt.subplots_adjust(hspace=1)

# set basic data
plt.title("Rainfall across places")
plt.ylabel("Accumulated rainfall (mm)")

# add first data (Brisbane - BOM)
plot1, = plt.plot([f"{str(data.year).removeprefix('20')}/{str(data.month)}" for data in better_data_bris], [data.rain for data in better_data_bris], label="Brisbane", color="C0")
plt.tick_params(colors="C0", axis="x")

# add second data (Klax - US)
twin = plt.twiny(plt)
plot2, = twin.plot([f"{str(data.year).removeprefix('20')}/{str(data.month)}" for data in better_data_klax], [data.rain for data in better_data_klax], label="KLAX", color="C1", )
twin.tick_params(colors="C1", axis="x")

# Add the second's ticks underneath first data
twin.xaxis.set_ticks_position("bottom")
twin.xaxis.set_label_position("bottom")
twin.spines["bottom"].set_position(("outward", 25))

# add legend & other basic data
plt.xlabel("Date")
plt.legend(handles=[plot1, plot2], loc="upper left")


### Showing the plot ###
print("showing plot...")
plt.show()
print("shown plot!")
