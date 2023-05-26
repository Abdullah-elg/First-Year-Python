# Function to make the csv files into lists
def LoadCSVData(filename):
    list = []
    result = []
    fileContent = open(filename, 'r', encoding='utf8')
    # Removes the commas and any extra words and puts them in a list
    for line in fileContent:
        line = line.replace('\n','')
        words = line.split(',')
        list.append(words)
    # Sorts the list into the headers and a list of everything that falls under that header
    for n in range(len(list[0])):
        newlist = []
        l = [item[n] for item in list]
        l.pop(0)
        newlist.append(list[0][n])
        newlist.append(l)
        result.append(newlist)
        n += 1
    fileContent.close()
    # Returns the list
    return result

# Gets all the information needed about the selected country and the universities that are located in the country
def getInformation(selectedCountry,rankingFileName,capitalsFileName):
    # Calls the function to make the csv files into lists
    capitals = LoadCSVData(capitalsFileName)
    topUni = LoadCSVData(rankingFileName)
    # If country has more than 3 letters it capitalizes the first letter of every word, otherwise it capitalizes the whole word
    if len(selectedCountry) > 3:
        selectedCountry = selectedCountry.title()
    else:
        selectedCountry = selectedCountry.upper()
    # Opens an text file to write the output in
    f = open('output.txt', 'w')
    # Finds the information using the indexes of the lists
    print('Total number of universities => {}'.format(len(topUni[1][1])))
    print('Available countries => {}'.format((', '.join(capitals[0][1])).upper()))
    print('Available continents => {}'.format((', '.join(set(capitals[5][1]))).upper()))
    f.write('Total number of universities => {}\n'.format(len(topUni[1][1])))
    f.write('Available countries => {}\n'.format((', '.join(capitals[0][1])).upper()))
    f.write('Available continents => {}\n'.format((', '.join(set(capitals[5][1]))).upper()))
    n = []
    # Appends all universities in selected country to a list
    for x in enumerate(topUni[2][1]):
        if x[1] == selectedCountry:
            n.append(x[0])
            # Finds university that is number 1 in national rank and gets the rank and university name
            if int(topUni[3][1][x[0]]) == 1:
                natrank = topUni[3][1][x[0]]
                natuni = topUni[1][1][x[0]]
    try:
        # Finds the international rank using the indexes of the list
        print('At international rank => {} the university name is => {}'.format(topUni[0][1][n[0]], topUni[1][1][n[0]].upper()))
        print('At national rank => {} the university name is => {}'.format(natrank, natuni.upper()))
        f.write('At international rank => {} the university name is => {}\n'.format(topUni[0][1][n[0]], topUni[1][1][n[0]].upper()))
        f.write('At national rank => {} the university name is => {}\n'.format(natrank, natuni.upper()))
    except IndexError:
        print("At international rank => N/A the university name is => N/A")
        print("At national rank => N/A the university name is => N/A")
        f.write("At international rank => N/A the university name is => N/A\n")
        f.write("At national rank => N/A the university name is => N/A\n")
    total = 0
    # Finds the sum of all university scores within selected country
    for x in n:
        total += float(topUni[8][1][x])
    try:
        # Calculates average score and rounds it to 2
        avgscore = round(total/len(n), 2)
        print('The average score => {}%'.format(avgscore))
        f.write('The average score => {}%\n'.format(avgscore))
    except ZeroDivisionError:
        print("The average score => N/A")
        f.write("The average score => N/A\n")
    try:
        # Finds the continent of selected country using indexes
        continent = capitals[5][1][capitals[0][1].index(selectedCountry)]
        n1 =[]
        # Gets the index of every country with the same continent as selected country
        for x in enumerate(capitals[5][1]):
            if x[1] == continent:
                n1.append(x[0])
        grades = []
        # Appends all the scores of the countries with the same continent into a list
        for x in n1:
            if capitals[0][1][x] in topUni[2][1]:
                grades.append(float(topUni[8][1][topUni[2][1].index(capitals[0][1][x])]))
        # Calculates the relative score and rounds it to 2
        relscore = round((avgscore/max(grades))*100, 2)
        print('The relative score to the top university in {} is => ({} / {}) x 100% = {}%'.format(continent.upper(), avgscore, max(grades), relscore))
        f.write('The relative score to the top university in {} is => ({} / {}) x 100% = {}%\n'.format(continent.upper(), avgscore, max(grades), relscore))
    except UnboundLocalError:
        print("The relative score to the top university in {} is => N/A".format(continent.upper()))
        f.write("The relative score to the top university in {} is => N/A\n".format(continent.upper()))
    # Finds the capital of selected country using indexes
    capital = capitals[1][1][capitals[0][1].index(selectedCountry)]
    print('The capital is => {}'.format(capital.upper()))
    print('The universities that contain the capital name =>')
    f.write('The capital is => {}\n'.format(capital.upper()))
    f.write('The universities that contain the capital name =>\n')
    n = 1
    # Finds all the universities with the capital name in them
    for x in topUni[1][1]:
        if capital in x:
            print('   #{} {}'.format(n, x.upper()))
            f.write('   #{} {}\n'.format(n, x.upper()))
            n += 1
    # If there are no universities with the capital name in them it prints none
    if n == 1:
        print("   None")
        f.write("   None")
    # Closes the text file
    f.close()


getInformation('usa', 'TopUni.csv', 'capitals.csv')
