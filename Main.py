import Chord, random

def generate(n): #generates n chords in scale
    chords = []
    octave = 5
    for i in range(n):
        randomChordNum = random.randint(1,7) #generates chord number
        randomChordType = random.randint(0,1) #TODO: incorporate chord qualities
        chords.append(Chord.Chord(randomChordNum,randomChordType,octave))
    return chords

def main():
    try:
        n = int(input("How many chords? (default 4): "))
    except ValueError:
        n = 4
    print("chord numbers for your song: " + str(generate(n)))
    print("key: c major")

main()