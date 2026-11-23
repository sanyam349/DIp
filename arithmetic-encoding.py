
message = input("Enter the message: ")

# Calculate character frequencies
freq = {}

for ch in message:
    freq[ch] = freq.get(ch, 0) + 1

low = 0.0
high = 1.0

total = len(message)

if total == 0:
    print("Message cannot be empty.")
else:
    for ch in message:

        range_value = high - low
        cumulative = 0.0

        for key, count in freq.items():

            probability = count / total

            if key == ch:
                high = low + range_value * (cumulative + probability)
                low = low + range_value * cumulative
                break

            cumulative += probability

    code = (low + high) / 2

    print("Final Range: [{}, {})".format(low, high))
    print("Encoded Value:", code)
