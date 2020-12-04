import csv
list_names = ['1. Bar 61 Restaurant', '2. Companero', '3. 28 Church Row', '4. Miss Tapas', '5. The Little Taperia', '6. Twist', '7. Volare']

file_to_output = open("newfile.csv", "w", newline="")
csv_writer = csv.writer(file_to_output,delimiter=",")

csv_writer.writerows([list_names,])

file_to_output.close()
