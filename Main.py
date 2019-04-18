import Chord, random

def generate(n): #generates n chords in scale
    chords = []
    octave = 5
    for _i in range(n):
        randomChordNum = random.randint(1,7) #generates chord number
        randomChordType = random.randint(0,1) #TODO: incorporate chord qualities
        chords.append(Chord.Chord(randomChordNum,randomChordType,octave))
    return chords

def getKey(n): #returns a string from the keys file based on n. (ex. n = 0 returns C, n = 11 returns B)
    keys = open("keys", "r")
    for _i in range(n):
        key = keys.readline()
        #print(key)
    key = keys.readline()
    print(key)
    keys.close()
    return key

def main():
    key = getKey(random.randint(0,11))
    
    try:
        n = int(input("How many chords? (default 4): "))
    except ValueError:
        n = 4
    print("chord numbers for your song: " + str(generate(n)))
    print("key: " + str(key))

main()