import csv
CHECKVALUES = "ABCDEFGHJKLMNPQRTUVWXYZ"
CHECKVALUES_lower = CHECKVALUES.lower()

def checkULN(studentULN, studentCode):
    if len(studentULN) != 10:
        print(f'Invalid length ULN for {studentCode}: {studentULN}')
    else:
        sum = 0
        for i in range(0, 9):
            digit = studentULN[i]
            multiplier = 10 - i
            sum += int(digit) * multiplier
        remainder = sum % 11
        if remainder == 0:
            print(f'Invalid ULN for {studentCode}: {studentULN}')
        else:
            checkdigit = 10 - remainder
            if int(studentULN[9]) == checkdigit:
                pass
            else:
                print(f'Invalid checkdigit on ULN for {studentCode}: {studentULN}')

def checkUPN(studentUPN, studentCode, acceptTemporary = False):
    tempFlag = False
    if len(studentUPN) != 13:
        print(f'Invalid length UPN for {studentCode}: {studentUPN}')
    else:
        sum = 0
        for i in range(1, 13):
            if studentUPN[i] in CHECKVALUES or studentUPN[i] in CHECKVALUES_lower:
                tempFlag = True
                sum += (CHECKVALUES.index(studentUPN[i].upper())) * (i+1)
            else:
                sum += int(studentUPN[i]) * (i + 1)
        remainder = sum % 23
        checkKey = CHECKVALUES[remainder]
        if studentUPN[0].upper() == checkKey:
            if tempFlag:
                print(f'Valid but TEMPORARY UPN for {studentCode}: {studentUPN}')
        else:
            print(f'Invalid UPN (temp: {tempFlag}) for {studentCode}: {studentUPN}')


def main():
    with open('students.csv', 'r') as f:
        """
        CSV file expected with columns of studentCode, ULN and UPN
        """
        reader = csv.reader(f)
        for row in reader:
            studentCode = row[0]
            studentULN = row[1]
            studentUPN = row[2]
            checkULN(studentULN, studentCode)
            checkUPN(studentUPN, studentCode)



if __name__ == '__main__':
    main()