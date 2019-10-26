# read mail file and average the X-DSPAM-Confidence

filename = input("Enter the file name: ")

fh = open(filename)
spam_values = []

for line in fh:
    if line.startswith('X-DSPAM-Confidence:'):
        parts = line.split(':')
        num = float(parts[1])
        spam_values.append(num)

print(sum(spam_values) / len(spam_values))