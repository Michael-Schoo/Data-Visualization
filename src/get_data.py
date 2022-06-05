import codecs
import csv
from data_types import BomData, BomObservation, BomObservation, USWeather, USWeatherObservation


class GetData:
    """
    The class that gets the data from the csv file(s)
    """

    def __init__(self):
        # Doesn't actually do much
        pass

    def get_us_2021_weather(self) -> USWeather:
        """
        The actual function that gets the data from the csv file
        """

        us_2021_weather = USWeather()
        # gets all the observations from the csv file
        us_2021_weather_data_kmlb = codecs.open("./data/us-2021/KMLB.2015-12-31.csv", 'r', encoding='utf-8', errors='ignore')
        cities = [us_2021_weather_data_kmlb]

        # go through each city and get their data
        for city_data in cities:
            observed_data = []
            for index, row in enumerate(csv.reader(city_data)):
                # skip header
                if index < 12:
                    continue
                observation = USWeatherObservation()
                observation.station_id = row[0]
                observation.date_time = row[1]
                observation.air_temp_set_1 = float(row[2] or 0)
                observation.precip_accum_one_hour_set_1 = row[3]
                row.append(0)
                observation.precip_accum_24_hour_set_1 = row[4] or (float(row[3] or 0) / 535) or 0

                # append the observation to the list
                observed_data.append(observation)

            # find which source it is, and then add the observation to the list
            if city_data.name == us_2021_weather_data_kmlb.name:
                us_2021_weather.kmlb = observed_data

        # finally return the data
        return us_2021_weather

    def get_bom_weather(self) -> BomData:
        """
        The actual function that gets the data from the csv file
        """

        bom_weather = BomData()
        # gets all the observations from the csv file
        cities = ["brisbane"]

        # sets the years to be observed
        min_year, max_year = 2010, 2011

        # go through each city and get their data
        for city in cities:
            observed_data = []
            # go through the years to collect the data
            for year in range(min_year, max_year+1):
                for month in range(1, 12+1):

                    # skip the first 6 months
                    if year == min_year and month < 6:
                        continue 
                    # skip the last 6 months
                    elif year == max_year and month > 5:
                        break

                    data = codecs.open(f"./data/bom/{city}/{city}-{year}{'%02d' % month}.csv", 'r', encoding='utf-8', errors='ignore')

                    for index, row in enumerate(csv.reader(data)):
                        # skip header
                        if index < 13 or row[0] == "Totals:":
                            continue
                        observation = BomObservation()
                        observation.station_name = row[0] or ""
                        observation.date = row[1] or ""
                        observation.evapo_transpiration = row[2] or 0
                        observation.rain = row[3] or 0
                        observation.pan_evaporation = row[4] or 0
                        observation.maximum_temperature = row[5] or 0
                        observation.minimum_temperature = row[6] or 0
                        observation.maximum_relative_humidity = row[7] or 0
                        observation.minimum_relative_humidity = row[8] or 0
                        observation.average_10m_wind_speed = row[9] or 0
                        observation.solar_radiation = row[10] or 0

                        # append the observation to the list
                        observed_data.append(observation)

            # find which source it is, and then add the observation to the list
            if city == "brisbane":
                bom_weather.brisbane = observed_data
        
        # finally return the data
        return bom_weather
