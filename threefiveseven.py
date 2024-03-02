PlaceWhereNumbersAreCollecting = set()

while True:
    question = int(input("Enter a number: "))
    PlaceWhereNumbersAreCollecting.add(question)

    if 3 in PlaceWhereNumbersAreCollecting and 5 in PlaceWhereNumbersAreCollecting and 7 in PlaceWhereNumbersAreCollecting:
        print("Three of them are existing 👍")
        break
