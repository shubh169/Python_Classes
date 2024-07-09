# travel_log={
#         "Uttar_pradesh":{"Noida":10,"Lucknow":2,"Kanpur":10},
#         "Utarakand":{"Haridwar":5,"Dehradoon":2,"Rishikesh":2}
#         }
# print(travel_log["Uttar_pradesh"]["Noida"])


#Nesting Dictionaries in Lists

travel_log = [
{
  "country": "France", 
  "cities_visited": ["Paris", "Lille", "Dijon"], 
  "total_visits": 12,
},
{
  "country": "Germany",
  "cities_visited": ["Berlin", "Hamburg", "Stuttgart"],
  "total_visits": 5,
},
]

print(travel_log[1]["cities_visited"][1])