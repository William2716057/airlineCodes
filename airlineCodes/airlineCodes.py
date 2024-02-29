airports = {'ATL':"Hartsfield–Jackson Atlanta International Airport",
			"PEK":"Beijing Capital International Airport",
			"DXB":"Dubai International Airport",
			"LAX":"Los Angeles International Airport",
			"HND":"Tokyo Haneda Airport",
			"ORD":"O'Hare International Airport (Chicago)",
			"LHR":"London Heathrow Airport",
			"SAR":"Hong Kong International Airport",
			"PVG":"Shanghai Pudong International Airport",
			"CDG":"Paris-Charles de Gaulle Airport",
			"AMS":"Amsterdam Airport Schiphol",
			"DEL":"Indira Gandhi International Airport (Delhi)",
			"CAN":"Guangzhou Baiyun International Airport",
			"FRA":"Frankfurt Airport",
			"DFW":"Dallas/Fort Worth International Airport",
			"ICN":"Seoul Incheon International Airport",
			"IST":"Istanbul Atatürk Airport",			
			"CGK":"Soekarno-Hatta International Airport",
			"SIN":"Singapore Changi Airport",
			"DEN":"Denver International Airport",
			}
			
code = input("Enter a 3-letter airport code:").upper()			

#Apply a legnth check on the airport code to only accept 3 letter codes.
while len(code)!=3:
  print("Invalid airport code.")
  code = input("Enter a 3-letter airport code:").upper()			
  
#Apply a lookup check to ensure the code is recognised (part of the dictionary)
while not code in airports:
  print("Airport code not recognised. Please try again with a different airport code.")
  code = input("Enter a 3-letter airport code:").upper()			

#Output  
print(airports[code])

airlines = {
    'AA': 'AMERICAN AIRLINES',
    'AC': 'AIR CANADA',
    'AF': 'AIR FRANCE',
    'AI': 'AIR INDIA',
    'BA': 'BRITISH AIRWAYS',
    'DL': 'DELTA AIR LINES',
    'CA': 'AIR CHINA',
    'JL': 'JAPAN AIRLINES',
    'MS': 'EGYPTAIR',
    'QF': 'QANTAS AIRWAYS',
    'SQ': 'SINGAPORE AIRLINES',
    'UA': 'UNITED AIRLINES'
}

airlinecode = input("Enter a two letter airline code:").upper()

while len(airlinecode)!=2:
  print("Computer says no")
  airlinecode = input("Enter a two letter airline code:").upper()
  
while not airlinecode in airlines:
  print("computer says no")
  airlinecode = input("Enter existing airline:").upper()

print(airlines[airlinecode])

