import matplotlib.pyplot as plt
import time

testword = "spelling"
print ("Typing test: write '"+testword+"' 5 times and I will analyze your typing prowess.")

results = []
mistakes = 0

while len(results) < 5:
    starttime = time.time()
    typedword = input(str(len(results)+1) + " (" + testword + "): ")
    stoptime = time.time()

    if (typedword != testword):
        mistakes += 1

    results.append(stoptime - starttime)


print ("You made", mistakes, "errors")

attempt = [1,2,3,4,5]
plt.plot(attempt, results)
plt.ylabel("Time (s)")
plt.xlabel("Round")
plt.xticks(ticks = attempts, labels= attempt)
plt.show()
