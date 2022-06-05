from datetime import datetime
from dateutil.parser import parse as date_parse
from numpy import average
from data_types import BomObservation, NewBetterObservation, USWeatherObservation


def simplify_us_data(data: list[USWeatherObservation]) -> list[NewBetterObservation]:
    """
    Function that gets averages for each month **FOR US DATA**
    """

    # get averages
    sorted_data: dict[tuple[int, int], list[float]] = {}

    # Make the new list that will contain the averages
    new_data: list[NewBetterObservation] = []

    for entry in data:
        # remove outliers (temp and rain)
        if (float(space_is_null(entry.air_temp_set_1) or 0) > 60 or float(space_is_null(entry.air_temp_set_1) or 0) < -5):
            continue

        if (float(space_is_null(entry.precip_accum_24_hour_set_1) or 0) > 100 or float(space_is_null(entry.precip_accum_24_hour_set_1) or 0) < 0):
            continue
        
        # Get the date out of a string (from )
        date = date_parse(entry.date_time)
        
        # Find the month and year in the dict and append (otherwise make it)
        if sorted_data.keys().__contains__((date.year, date.month)):
            sorted_data[(date.year, date.month)].append(entry)
        else:
            sorted_data[(date.year, date.month)] = [entry]
    
    # Go through the months of data data and get the averages for them
    for month in sorted_data:
        data = [data for data in sorted_data[month]]

        # If there is no data for the month, skip it
        if not data or len(data) < 0:
            continue

        entry = NewBetterObservation()
        entry.year = month[0]
        entry.month = month[1]
        entry.temp = average([float(d.air_temp_set_1 or 0) for d in data])
        entry.rain = sum([float(d.precip_accum_24_hour_set_1 or 0) for d in data])

        new_data.append(entry)

    return new_data


def simplify_bom_data(data: list[BomObservation]) -> list[NewBetterObservation]:
    """
    Function that gets averages for each month
    """

    # get averages
    sorted_data: dict[tuple[int, int], list[float]] = {}

    # Make the new list that will contain the averages
    new_data: list[BomObservation] = []

    for entry in data:

        # remove outliers (temp and rain)
        if (float(space_is_null(entry.maximum_temperature) or 0) > 60 or float(space_is_null(entry.minimum_temperature) or 0) < -10):
            continue

        if (float(space_is_null(entry.rain) or 0) > 50 or float(space_is_null(entry.rain) or 0) < 0):
            continue

        date = datetime.strptime(entry.date, "%d/%m/%Y")

        # Find the month and year in the dict and append (otherwise make it)
        if sorted_data.keys().__contains__((date.year, date.month)):
            sorted_data[(date.year, date.month)].append(entry)
        else:
            sorted_data[(date.year, date.month)] = [entry]

    # Go through the months of data data and get the averages for them
    for month in sorted_data:
        data = [data for data in sorted_data[month]]

        # If there is no data for the month, skip it
        if not data:
            continue

        entry = NewBetterObservation()
        entry.year = month[0]
        entry.month = month[1]
        entry.temp = average([average([float(space_is_null(d.minimum_temperature) or 0), float(space_is_null(d.minimum_temperature) or 0)]) for d in data])
        entry.rain = sum([float(space_is_null(d.rain) or 0) for d in data])
        new_data.append(entry)

    return new_data


def space_is_null(data: str) -> str:
    """
    A function that was made to make space values be actually null
    """
    if data == " ":
        return None
    else:
        return data
