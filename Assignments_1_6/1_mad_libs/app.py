# Once upon a time, there was a [adjective] [noun] who loved to [verb]. 
#     Every day, it would [verb] in the [place], and sometimes even [verb] with other [plural noun]. 
#     One day, the [noun] met a [adjective] [noun] and they decided to [verb] together. 
#     # It was a [adjective] adventure!

# Mad Libs Python Project



# Once upon a time, there was a funny dog who loved to run. 
# Every day, it would run in the park, and sometimes even run with other cars. 
# One day, the dog met a speedy cat and they decided to run together. 
# It was a funny adventure!


def main():
    adj = str(input("Enter an adjective: "))
    name_animal = str(input("Enter a noun (animal): "))
    veb = str(input("Enter a verb: "))
    place = str(input("Enter the place name: "))
    vrb2 = str(input("Enter another verb: "))
    animal_2 = str(input("Enter another noun (animal): "))
    adj2 = str(input("Enter another adjective: "))
    noun3 = str(input("Enter another noun: "))
    verb3 = str(input("Enter another verb: "))

    # Use the correct variables in the story format
    story = f"Once upon a time, there was a {adj} {name_animal} who loved to {veb}. Every day, it would {vrb2} in the {place}, and sometimes even {verb3} with other {animal_2}. One day, the {noun3} met a {adj2} {animal_2} and they decided to {verb3} together. It was a {adj2} adventure!"

    print(story)

main()
