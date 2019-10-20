# read mail file and average the X-DSPAM-Confidence

filename = input("Enter the file name: ")

fh = open(filename)

spam = 0
counter = 0

for line in fh:
    if line.startswith('X-DSPAM-Confidence:'):
        counter = counter + 1
        num = float(line[20:])
        spam = spam + num

avg_spam = spam / counter
print("Average spam confidence: ", avg_spam)