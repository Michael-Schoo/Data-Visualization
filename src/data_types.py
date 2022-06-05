

class BomObservation:
    """
    Class that represents a single observation from the BOM (bom.gov.au)
    """
    station_name: str = "BATCHELOR AERO"
    date: str = "1/02/2009"
    # 0000-2400 (mm)
    evapo_transpiration: float = 4.2
    # 0900-0900 (mm)
    rain: float = 20.4
    # 0900-0900 (mm)
    pan_evaporation: float = 0.0
    # (°C)
    maximum_temperature: float = 30.1
    # (°C)
    minimum_temperature: float = 22.7
    # (%)
    maximum_relative_humidity: float = 95
    # (%)
    minimum_relative_humidity: float = 74
    # (m/sec)
    average_10m_wind_speed: float = 3.47
    # (MJ/sq m)
    solar_radiation: float = 19.09


class USWeatherObservation:
    """
    Class that represents a single observation from the US Weather (weather.gov - synopticdata.org )
    """
    station_id: str = "KLAX"
    date_time: str = "2021-01-01T12:00:00Z"
    # Celsius
    air_temp_set_1: float = 9.0
    # Millimeters
    precip_accum_one_hour_set_1: float = 0.0
    # Millimeters
    precip_accum_24_hour_set_1: float = 0.0


class NewBetterObservation:
    """
    Class that represents a single observation from the any data source
    """
    month: int = 1
    year: int = 2020
    # The acuminated rain through out the month (mm)
    rain: float = 20.4
    # The average temp or the average between min/max  (°C)
    temp: float = 30.1


class BomData:
    """
    Class that represents the data lists from the BOM
    """
    brisbane: list[BomObservation] = []


class USWeather:
    """
    Class that represents the data lists from the US Weather
    """
    kmlb: list[USWeatherObservation] = []
