from map_functions import save_map, graph_from_place
from matrix_functions import from_graph_to_matrix
from algorithm_functions import chinese_postman

# Calculate and display the prices

# Super Drone
# Speed : 70 km / h
# Price : 100€ / day + 0.01€ / km

# Snow plough Type II
# Snow plough speed : 20 km / h
# Snow plough price : 800€ / day + 1.3€ / km (first 8 hours) + 1.5€ / km (after 8 hours)

def price(distance) :
    
    d = distance / 1000
    
    droneTime = round(d / 70, 2)
    dronePriceKm = round(0.01 * d, 2)
    tmp = round(droneTime / 24)
    dronePriceTime = round(tmp + 1 if tmp < 1 else tmp) * 100
    
    snowploughTime = round(d / 20, 2)
    firstHours = 8 if snowploughTime > 8 else snowploughTime
    restOfHours = 0 if firstHours < 8 else snowploughTime - 8
    priceFirstHours = round(1.3 * 20 * firstHours, 2)
    priceRestOfHours = round(1.5 * 20 * restOfHours, 2)
    snowploughPriceFirstHoursKm = round(priceFirstHours, 2)
    snowploughPriceRestOfHoursKm = round(priceRestOfHours, 2)
    tmp = round(snowploughTime / 24)
    snowploughPriceTime = round(tmp + 1 if tmp < 1 else tmp) * 800
    
    result = dronePriceKm + dronePriceTime + snowploughPriceFirstHoursKm + snowploughPriceRestOfHoursKm + snowploughPriceTime
    
    print("Durée d'utilisation du drone :", droneTime, "h")
    print("Prix par km du drone:", dronePriceKm, "€")
    print("Prix des journées de location du drone :", dronePriceTime, "€")
    print("Prix total du drone :", dronePriceKm + dronePriceTime, "€")
    
    print("--------------------------------------------------------------------------")
    
    print("Durée d'utilisation de la déneigeuse :", snowploughTime, "h")
    print("Prix par km des 8 premières heures de la déneigeuse :", snowploughPriceFirstHoursKm, "€")
    print("Prix par km du reste des heures de la déneigeuse :", snowploughPriceRestOfHoursKm, "€")
    print("Prix des journées de location de la déneigeuse :", snowploughPriceTime, "€")
    print("Prix total de la déneigeuse :", snowploughPriceFirstHoursKm + snowploughPriceRestOfHoursKm + snowploughPriceTime, "€")
    
    print("--------------------------------------------------------------------------")
    
    print("Prix total :", round(snowploughPriceFirstHoursKm + snowploughPriceRestOfHoursKm + snowploughPriceTime + dronePriceKm + dronePriceTime, 2))
    
    return result

# Main execution
G = graph_from_place("Le Plateau-Mont-Royal, Montreal, CANADA")
save_map(G, 'map.html')

res, duo = from_graph_to_matrix(G)
distance = round(chinese_postman(res))

print("Distance minimale à parcourir :", distance)
print("--------------------------------------------------------------------------")

price(distance)