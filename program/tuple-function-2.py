import math
FileName = input("File name:")
FileData = []
over = 0
try:
    file = open(FileName,"r") 
    FileData = file.read() 
    FileData = FileData.strip()
    FileData = FileData.split("\n")
except Exception as e: 
    print("Wrong file name: ", FileName)
    over = 1
if over != 1:
    #first output in tuple form
    def data_tuple(str):
        data_tuple = tuple(str.split(" "))
        return(data_tuple)
    
    tuple_data = []
    for line in FileData:
        tuple_data.append(data_tuple(line))

    def print_dataTu(data_tuple):
        print("{:15} {:15} {:8}".format (data_tuple[0], data_tuple[1], data_tuple[2]), data_tuple[3])
    for i in range (len(tuple_data)):
        print_dataTu(tuple_data[i])

    #space
    print("\n")
    #second output as city + citizens
    def city_tuple(str):
        city_tuple = tuple(str.split(" "))
        return(city_tuple)

    city_data = []
    for line in FileData:
        city_data.append(city_tuple(line))

    def print_cityTu(city_tuple):
        name = city_tuple[0] + " n. citizens: "
        print("{:30} {:8}".format (name, city_tuple[3]))
    for i in range (len(city_data)):
        print_cityTu(city_data[i])
        
    end = 1
    error = 0
    
    print("\n")
    print("Choose your option: ")
    print("1. Full details of a city.")
    print("2. Full details of the cities with a population in a particular range.")
    print("3. Find a city within 10KM of your coordinates.")
    print("4. Go to the next step.")
    
    option = input()
    while option != "4":
        if option == "1":
            inputCity = input("Enter city name:")
            bad_input = 0 #in case of non valid input
            for i in range(len(city_data)):
                city = str(city_data[i]).split(", ")
                inputCityName = "('"+inputCity+"'"
                if city[0] == inputCityName:
                    bad_input = 1
                    print_cityTu(city_data[i])
            if bad_input == 0:
                print("No results found.")
        elif option == "2":
            min_population = int(input("Enter the minimum population:"))
            max_population = int(input("Enter the maximum population:"))
            while min_population > max_population:
                print("Minimum population is greater than maximum population!")
                min_population = int(input("Enter the minimum population:"))
                max_population = int(input("Enter the maximum population:"))
            bad_input = 0
            for i in range (len(city_data)):
                city = str(city_data[i]).split(", ")
                population = int(city[3].replace("'","").replace(")",""))
                if population in range(min_population, max_population):
                    bad_input = 1
                    print_cityTu(city_data[i])
            if bad_input == 0:
                print("No results found.")
                
            
        elif option == "3":
            bad_input = 0
            lat1 = float(input("Enter the latitude:"))
            long1 = float(input("Enter the longitude:"))
            for i in range (len(city_data)):
                city = str(city_data[i]).split(", ")
                lat2 = float(int(city[1].replace("'","")))
                long2 = float(int(city[2].replace("'","")))
                dist = math.sqrt((lat1 - lat2) * (lat1 - lat2) + (long1 - long2) * (long1 - long2))
                if dist <= 10:
                    print(city[0])
                    bad_input = 1
            if bad_input == 0:
                print("City not found")
        else:
            error = 1
            option = input()
        if error == 0:
            print("You can choose another option.")
            option = input()
        error = 0
    
    option = input("Type 1 to start calculation of the distance between two cities OR type 2 to exit.")
    while end != 0:
        if option == "1":
            lat1 = float(input("Type in the latitude of the first city:"))
            lon1 = float(input("Type in the longitutde of the first city:"))
            lat2 = float(input("Type in the latitude of the second city:"))
            lon2 = float(input("Type in the longitude of the second city:"))
            if lat1 < lat2:
                lat1, lat2 = lat2, lat1
            if lon1 < lon2:
                lon1, lon2 = lon2, lon1
            lat3 = lat1 - lat2
            lon3 = lon1 - lon2
            dist = math.sqrt(lat3 * lat3 + lon3 * lon3)
            print(dist)
            option = input("Type 1 to start calculation of the distance between another two cities or type 2 to exit.")
            if option == "2": 
                end = 0
        else:
            end = 0
