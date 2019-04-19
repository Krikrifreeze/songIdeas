import Chord, random

def generate(n): #generates n chords in scale
    chords = []
    octave = 5
    for _i in range(n):
        randomChordNum = random.randint(1,7) #generates chord number
        chords.append(Chord.Chord(randomChordNum))
    return chords

def readFile(filename, n): #returns a string based on the line number of a file
    file = open(filename, "r")
    for _i in range(n):
        line = file.readline()
        #print(key)
    line = file.readline()
    print(line)
    file.close()
    return line

def main():
    key = readFile("keys", random.randint(0,11))
    
    try:
        n = int(input("How many chords? (default 4): "))
    except ValueError:
        n = 4
    print("chord numbers for your song: " + str(generate(n)))
    print("key: " + str(key))

main()