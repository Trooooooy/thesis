#Full file developed by Troy for thesis! meant to be run from a model folder and reads the training logs
# then prints the overall mean reward per second and the highest mean reward p/s reached

log =  open("log.txt")
total = 0
count = 0
max = (0,0)

for line in log.readlines():
    words = line.split(" ")
    # print(words)
    if words[0] != "Saving":
        continue

    count +=1
    if float(words[6]) > max[0]:
        max = (float(words[6]), count)

    total += float(words[6])


avg = total/count
print(total, "/", count, "=", avg)
print("highest: ", max)

log.close()