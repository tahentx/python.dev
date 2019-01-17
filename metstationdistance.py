import unirest


response = unirest.get("https://010pixel-distance-v1.p.rapidapi.com/?unit=K&lat1=10&long1=-25.3&lat2=34.5&long2=-403.4",
  headers={
    "X-RapidAPI-Key": "54bfa778e0msh52ed7af4b6f98cfp18b709jsnbc0ccec09a9c"
  }
)