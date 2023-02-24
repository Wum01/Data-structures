# Index Number: 6922221
# Name: Adam Wumpini Abdul Hakim
# ASSIGNMENT 3

# a sript to determine the prices of cars of different brands available
# carPrices are in U.S Dollars,$
#types of cars available
carTypes=['limousine', 'convertible', 'microCars', 'cityCars', 'hatchbacks', 'SUV',
          'sedans', 'CUV','subcompactCars','familyCars', 'estateCars', 'grandTower',
          'muscleCars', 'superCars','roadsters', 'minivan', 'pickup', 'coupe', 
          'sportsCar', 'raceCars', 'stationWagon', 'van','jeep', 'luxuryCars',
          'compactCars', 'BMW', 'commercialVehicles', 'mercedesBenz', 'kia',
          'chevrolet']
''''car brand with it equivalent price'''
carPrices={'tesla':88000,'ferrari':13000,'ford':10000,'porsche':12000,'honda':4600,
           'lamborhhini':97000,'toyota':5500,'bentley':11000,'maserati':10090,
           'subaru':5070,'hyundai':9700,'cadillac':6400,'nissan':7600,'acura':5070,
           'jaguar':7080,'scania':6500,'dodge':11000,'daimler':7800,'lexus':9800,
           'saleen':8900,'mazda':5600,'tata':4300,'saturn':71000,'KTM':8800,
           'lotus':25000,'hummer':111000,'pagani':3800,'rover':21000,'hino':5400,
           'packard':6600,'scion':4400,'mayback':7200,'audi':7600}
name=input('Please state your name? ')
print()
print('Hello! ' + name )
a=input('Please which type of car are you interested in? ')
b=input('Please type the brand name ')
print()
if b in carPrices:
    print(f'The price of {a} with brand name {b} is ${carPrices[b]:,}')
else:
    print('Sorry the specified brand is currently not available ')

         