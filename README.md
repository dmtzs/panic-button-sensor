<p align="center">
  <img width="300" src="./Imgs/cover.png" alt="cover-image">
  <h1 align="center" style="margin: 0 auto 0 auto;">MQTT messages</h1>
  <h5 align="center" style="margin: 0 auto 0 auto;">Panic button and Alcohol message</h5>
</p>

<p align="center">
  <img src="https://img.shields.io/github/last-commit/dmtzs/panic-button-sensor">
  <img src="https://img.shields.io/github/contributors/dmtzs/panic-button-sensor">
  <img src="https://img.shields.io/github/issues/dmtzs/panic-button-sensor?label=issues">
  <img src="https://img.shields.io/github/stars/dmtzs/panic-button-sensor">
  <img alt="GitHub top language" src="https://img.shields.io/github/languages/top/dmtzs/panic-button-sensor">
</p>

<p align="center">
  <img src="https://img.shields.io/github/languages/code-size/dmtzs/panic-button-sensor">
  <img alt="GitHub repo size" src="https://img.shields.io/github/repo-size/dmtzs/panic-button-sensor">
  <img alt="Lines of code" src="https://img.shields.io/tokei/lines/github/dmtzs/panic-button-sensor?label=total%20lines%20in%20repo">
  <img alt="GitHub language count" src="https://img.shields.io/github/languages/count/dmtzs/panic-button-sensor">
</p>

- [Documentation](#Documentation)
- [Supported versions for releases](#Supported-versions-for-releases)
- [ESP32 program](#ESP32-program)
  - [Specifications](#Specifications)
- [Lambda program](#Lambda-program)
  - [Specifications](#Specifications-1)
- [Sensor´s and materials list used](#sensors-and-materials-list-used)
- [Connection diagram](#connection-diagram)

## Documentation
I´m developing a github page in the wiki part in order to use that space as a documentation, that documentation is still in development but is going to be there. [Click here]() in order to go to that documentation page.
<br>
Also please see below the list of the hardware which are going to be used in this project.

## Supported versions for releases
To see the releases supported versions please [click here](https://github.com/dmtzs/panic-button-sensor/blob/master/SECURITY.md) to see the supported ones and unsupported ones.
## ESP32-program
### Specifications

## Lambda-program
### Specifications

## sensors-and-materials-list-used
* MQ-3 sensor
* NEO 6M GPS module
* ESP32
* Lipo battery
* TP4056 module
* Step up voltage module
* Push buttons
* Buzzer

## connection-diagram
![Connection diagram]()
## Tasks to do
The tasks described below are linked to an issue that also appears in the section of projects of the present github project.
What you see below is a resume of some of the issues opened but are not all of them, only the main functionalities.

The nomenclature is the next one:

:white_check_mark:: Done
:x:: Not done yet

For the sensors:
- :white_check_mark: MQ-3
- :white_check_mark: GPS
- :x: Push button lecture
- :x: Set both together

For the MQTT
- :x: Send coordinates to google iot core MQTT
- :x: Add register to firebase

### Personal notes
* [Para el certificado ssl con c++](http://blog.espol.edu.ec/girni/mqtt-tls-archivo-ino-para-mensajes-de-estado-led/)
* [Enlace google iot core(este es el bueno)](https://www.survivingwithandroid.com/cloud-iot-core-esp32/)
* [Este segundo enlace es para el sensor de gps bueno](https://blog.asksensors.com/iot-cloud-based-gps-tracking-esp32-gps-neo-6m-module/)

* [Instructivo de la api de geolocalizacion](https://developers.google.com/maps/documentation/geolocation/cloud-setup)
* [Github para instructivo de Wifi Location](https://github.com/gmag11/WifiLocation)
* [Decodificaion y codificacion de base 64 para Esp32](https://pcbartists.com/firmware/base64-encoding-and-decoding-on-esp32/)
