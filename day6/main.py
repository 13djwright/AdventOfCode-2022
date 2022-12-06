buffer = ""
with open('./input.txt', 'r') as f:
    buffer = f.read()
f.close()

last_four = []

# the number of characters that have been processed so far
num_processed = 0

num_distinct = 14
# iterate over the characters in the buffer
for c in buffer:
  # add the current character to the last_four list
  last_four.append(c)

  # if we have more than four characters in the list, remove the first one
  if len(last_four) > num_distinct:
    last_four = last_four[1:]

  # if the last four characters are all different, return the number of
  # characters that have been processed so far
  if len(set(last_four)) == num_distinct:
    print(set(last_four))
    print(num_processed+1)
    break

  # increment the number of characters that have been processed
  num_processed += 1