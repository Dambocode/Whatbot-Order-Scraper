
def whatbotOrderScraper(orderFile):
    count = 0
    with open(orderFile, 'r') as readobj:
        for i in readobj:
            checkoutArray = i.split(':')
            exists = '"Successfully checked out with profile' in checkoutArray
            if exists == True:
                count += 1
    return count

totalCheckouts = 0
while True:
    userInput = input('Import Log or type Done to view output:\n')
    if userInput.startswith('c:\\'):
        checkouts = whatbotOrderScraper(userInput)
        totalCheckouts = totalCheckouts + checkouts
    elif userInput == 'done' or 'Done':
        print(f'Total Checkouts: {totalCheckouts}')
        break