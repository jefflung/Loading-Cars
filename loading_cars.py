def write_file():
    buffer = []
    with open("cars_exercise.txt", "r") as file:
        for line in file:
            buffer.append(line.strip())
    print(buffer)
    cars = []
    i = 0
    while i < len(buffer):
        make = buffer[i]
        model = buffer[i + 1]
        year = buffer[i + 2]
        cars.append({
            "Make": make,
            "Model": model,
            "Year": year
        })
        i += 3
    print(cars)

    for car in cars:
        print("==========")
        print("Make:", car["Make"])
        print("Model:", car["Model"])
        print("Year:", car["Year"])

   

    newest = cars[0]["Year"]
    for i in range(0, len(cars)):
        if cars[i]["Year"] > newest:
            newest = cars[i]["Year"]
            print("The newest car is",cars[i])

    oldest = cars[0]["Year"]
    for i in range(0, len(cars)):
        if cars[i]["Year"] < oldest:
            oldest = cars[i]["Year"]
            print("The oldest car is",cars[i])

write_file()
