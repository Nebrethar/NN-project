import matplotlib.pyplot as plt
import random

perfect = [100, 100]
bounds = [[0, 200],[0, 200]]

def compare(guess):
    if guess[0] != perfect[0]:
        if guess[0] < perfect[0]:
            bounds[0][0] = guess[0]
        if guess[0] > perfect[0]:
            bounds[0][1] = guess[0]
    if guess[1] != perfect[1]:
        if guess[1] < perfect[1]:
            bounds[1][0] = guess[1]
        if guess[1] > perfect[1]:
            bounds[1][1] = guess[1]

def dart():
    guess = [random.randint(bounds[0][0], bounds[0][1]), random.randint(bounds[1][0], bounds[1][1])]
    #print("initial x: " + str(guess[0]))
    #print("initial y: " + str(guess[1]))
    print(guess)
    if guess == perfect:
        print("Found it!")
        img = plt.imread("target.jpg")
        fig, ax = plt.subplots()
        ax.imshow(img)
        plt.plot(perfect[0], marker="o", markersize=20, markeredgecolor="red", markerfacecolor="green")
        plt.title('My first graph!')
        plt.show()
        exit(0)
    else:
        print("working on it...")
        print("I failed!")
        print("I guessed " + str(guess))
        print("My bounds were: " + str(bounds))
        compare(guess)
        print("Updated to: " + str(bounds))
        dart()

dart()
