def readFromFile(filename):
    data = []
    f = open("spending.csv","r")

    lines = f.readlines()

    f.close()

    for i in range(len(lines)):
        lines[i] = lines[i].strip()

    for i in range(len(lines)):
        items = lines[i].split(",")
        date = items[0]
        product = items[1]
        price = items[2]        
        data.append((date, product, float(price[1:])))
    return(data)

def total(data):
    total = 0

    for x in range(len(data)):
        total += data[x][2]
    return(round(total, 2))

def daily(data):
    newData = []
    sortedList = []
    dateSum = {}
    firstPointer = 0
    secondPointer = 0

    for x in range(len(data)):
        date = data[x][0]
        price = data[x][2]
        date = (date[:10])
        if(date in dateSum):
            dateSum[date] = round(dateSum[date] + price,2)
        else:
             dateSum[date] = price
    newData = list(dateSum.items())

    for x in range(len(newData)):

        for y in range(0, (len(newData) -  x - 1)):

            date = newData[y][0].split("-")
            date2 = newData[y+1][0].split("-")

            firstPointer = date[0]+date[1]+date[2]
            secondPointer = date2[0]+date2[1]+date2[2]

            if(date > date2):
                newData[y], newData[y+1] = newData[y+1], newData[y]
    return newData

def productsOnDay(data, day):
    newData = []
    products = {}

    for x in range(len(data)):
        date = data[x][0]
        name = data[x][1]
        date = (date[:10])
        newData.append((date,name))

    for x in range(len(newData)):
        date = newData[x][0]
        if(day == date and newData[x][1] not in products):
            products[x] = newData[x][1]
    return(list(products.values()))

if __name__ == "__main__":   # Only do the following if this file is called direfctly
    print(total(readFromFile("spending.csv")))
    print(daily(readFromFile("spending.csv")))
    print(productsOnDay(readFromFile("spending.csv"),"2021-11-01"))




