import matplotlib.pyplot as plt
from clean_data import simplify_bom_data, simplify_us_data
from get_data import get_bom_weather, get_us_weather


#### Retrieving & Manipulating the data ####
# Getting data
print("getting data...")
raw_bom_data = get_bom_weather()
print("gotten BOM data!")
raw_us_data = get_us_weather()
print("gotten US data!")

# Cleaning data (making it into monthly and removing the outliers)
print("simplifying DOM data...")
better_data_bris = simplify_bom_data(raw_bom_data.brisbane)
print("simplified BOM data!")
print("simplifying US data...")
better_data_kmlb = simplify_us_data(raw_us_data.kmlb)
print("simplified US data!")


#### Set up Matplotlib ####
plt.figure(figsize = (7, 9))
plt.suptitle("Is there a corelation of weather across places?", y=0.965, fontweight="bold", fontsize=16)

#### Temperature plot ####
plt.subplot(2, 1, 1)

# set basic data
plt.title("Temperatures across places")
plt.ylabel("Average Temperature (C)")

# add first data (Brisbane - BOM)
plot1, = plt.plot([f"{str(data.month)}/{str(data.year).removeprefix('20')}" for data in better_data_bris], [data.temp for data in better_data_bris], label="Brisbane, AU", color="C0")
plt.tick_params(colors="C0", axis="x")

# add second data (Klax - US)
twin = plt.twiny(plt)
plot2, = twin.plot([f"{str(data.month)}/{str(data.year).removeprefix('20')}" for data in better_data_kmlb], [data.temp for data in better_data_kmlb], label="Melbourne, USA", color="C1", )
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
plt.subplots_adjust(hspace=0.5)

# set basic data
plt.title("Rainfall across places")
plt.ylabel("Accumulated rainfall (mm)")

# add first data (Brisbane - BOM)
plot1, = plt.plot([f"{str(data.month)}/{str(data.year).removeprefix('20')}" for data in better_data_bris], [data.rain for data in better_data_bris], label="Brisbane, AU", color="C0")
plt.tick_params(colors="C0", axis="x")

# add second data (Klax - US)
twin = plt.twiny(plt)
plot2, = twin.plot([f"{str(data.month)}/{str(data.year).removeprefix('20')}" for data in better_data_kmlb], [data.rain for data in better_data_kmlb], label="Melbourne, USA", color="C1", )
twin.tick_params(colors="C1", axis="x")

# Add the second's ticks underneath first data
twin.xaxis.set_ticks_position("bottom")
twin.xaxis.set_label_position("bottom")
twin.spines["bottom"].set_position(("outward", 25))

# add legend & other basic data
plt.xlabel("Date")
plt.legend(handles=[plot1, plot2], loc="upper left")


### Showing/saving the plot ###
print("showing plot...")
plt.savefig("current_graph.png")
plt.show()
print("shown and saved plot!")
