"""
pipywx.sensors.temperature
==================
Functions for interacting with gpio and USB (and others?) weather sensors.

.. autosummary::
    :toctree: generated/
    get_temp

"""

import Adafruit_DHT


def get_temp_dht(gpio_slot, sensor_type=22, throw_error=True):
    """
       Get temperure from a DHT sensor

       Parameters
       ----------
       gpio_slot : integer
           slot the DHT is connected to
       sensor_type : integer
           22 or 11
       throw_error : Boolean
           Set to False to return a None, leave unset for exception

       Returns
       -------
       (temperature, humidity) : floats
           temperature and humidity from sensor
       """

    humidity, temperature = Adafruit_DHT.read_retry(sensor_type, gpio_slot)

    # some times I have found an old value is stored on the sensor so hit
    # it again

    shumidity, stemperature = Adafruit_DHT.read_retry(sensor_type, gpio_slot)

    if throw_error:
        if shumidity is not None and stemperature is not None:
            humidity = shumidity
            temperature = stemperature
        else:
            raise ValueError('Sensor Fail')
    else:
        humidity = shumidity
        temperature = stemperature

    return humidity, temperature



