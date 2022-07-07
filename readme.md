# Weather

Simple program, that take your location (city, full address) and using `geopy` takes latitude and longitude.
Using latitude and longitude program takes weather using openweather API.

## Weather example

Input:

```text
Enter your location (City, address, etc...): London
```

Output:

```text
London, Temperature 17°С, Clouds
Sunrise: 08:52
Sunset: 01:03
```

## Forecast example
5 day / 3 hour forecast.

Output:

```text
Date: 2022-07-07 19:37:43,
London, Temperature 24°С, Clouds
Sunrise: 08:52
Sunset: 01:18

Thursday, 20:00:00
24°С, Clouds

Thursday, 23:00:00
24°С, Clouds

Friday, 02:00:00
21°С, Clear

Friday, 05:00:00
17°С, Clear

Friday, 08:00:00
16°С, Clear

... 37 times
```

## Requirments

geographiclib==1.52
geopy==2.2.0
