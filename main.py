import csv

# Certain characters e.g. I, O, S are banned from ULNs and UPNs; as such, the list of check characters is smaller.
CHECKVALUES = "ABCDEFGHJKLMNPQRTUVWXYZ"
CHECKVALUES_lower = CHECKVALUES.lower()


def checkULN(studentULN, studentCode):
    """
    
    :param studentULN:
    :param studentCode:
    :return:
    """
    if len(studentULN) != 10:
        # All valid ULNs must be ten characters in length.
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


def checkUPN(studentUPN, studentCode, acceptTemporary=False):
    tempFlag = False
    if len(studentUPN) != 13:
        # All valid UPNs must be thirteen characters in length.
        print(f'Invalid length UPN for {studentCode}: {studentUPN}')
    else:
        sum = 0
        for i in range(1, 12):
            if studentUPN[i] in CHECKVALUES or studentUPN[i] in CHECKVALUES_lower:
                tempFlag = True
                sum += (CHECKVALUES.index(studentUPN[i].upper())) * (i + 1)
            else:
                sum += int(studentUPN[i]) * (i + 1)

        if (studentUPN[12] in CHECKVALUES or studentUPN[12] in CHECKVALUES.lower):
            # If the 13th character is a check character, the UPN being checked is temporary.
            tempFlag = True
            if acceptTemporary:
                sum += (CHECKVALUES.index(studentUPN[i].upper())) * (i + 1)
            else:
                print(f'Temporary UPN for {studentCode}: {studentUPN}')

        remainder = sum % 23
        checkKey = CHECKVALUES[remainder]

        if studentUPN[0].upper() != checkKey:
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
