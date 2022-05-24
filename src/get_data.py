import csv
from data_types import BomData, BomObservation, BomObservation, USWeather, USWeatherObservation


class GetData:
    """
    The class that gets the data from the csv file
    """

    def __init__(self):
        pass

    def get_us_2021_weather(self) -> USWeather:
        """
        The actual function that gets the data from the csv file
        """

        us_2021_weather = USWeather()
        # gets all the observations from the csv file
        us_2021_weather_data_klax = open("./data/us-2021/KLAX.2021-12-31.csv", "r")
        cities = [us_2021_weather_data_klax]

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
                print(row[3], row[4])
                observation.precip_accum_24_hour_set_1 = row[4] or (float(row[3] or 0) / 535) or 0

                observed_data.append(observation)

            if city_data.name == us_2021_weather_data_klax.name:
                us_2021_weather.klax = observed_data

        return us_2021_weather

    def get_bom_weather(self) -> BomData:
        """
        The actual function that gets the data from the csv file
        """

        bom_weather = BomData()
        # gets all the observations from the csv file
        cities = ["brisbane"]

        for city in cities:
            observed_data = []
            for year in range(2019, 2021):
                for month in range(1, 13):

                    if year == 2019 and month < 6:
                        continue
                    elif year == 2020 and month > 5:
                        break


                    data = open(f"./data/bom/{city}/{city}-{year}{'%02d' % month}.csv", "r")

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

                        observed_data.append(observation)

            if city == "brisbane":
                bom_weather.brisbane = observed_data

        return bom_weather
