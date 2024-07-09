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
def add_new_country(new_country_name,new_city_list,new_total_visits):
    new_country={}
    new_country["country"]=new_country_name
    new_country["cities_visited"]=new_city_list
    new_country["total_visits"]=new_total_visits
    travel_log.append(new_country)

country=input("Enter the country you want to visit: ").lower()
cities_visited=[]
for i in range(2):
    city=input("Enter the cities:")
    cities_visited.append(city)
total_visits=int(input("Type the number:"))
add_new_country(country,cities_visited,total_visits )

print(f"I have been to {travel_log[2]['country']} {travel_log[2]['total_visits']} times.")
print(f"My favourate city was {travel_log[2]['cities_visited'][1]}")