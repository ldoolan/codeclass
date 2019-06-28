# Play RPS-25
import string
import random

player_choice = 'water'

#lists laying out what each thing can be beaten by
gestures = ['gun', 'rock', 'sun', 'fire', 'scissors', 'axe', 'snake', 'monkey', 'woman', 'man', 'tree', 'cockroach', 'wolf', 'sponge', 'paper', 'moon', 'air', 'bowl', 'water', 'alien', 'dragon', 'devil', 'lightning', 'nuke', 'dynamite']
    

def computer_choice(player_choice):
    """
    Do maths and have the computer choose a gesture
    """

    #get indexes of a bunch of positions
    prestart_position = gestures.index(player_choice)
    start_position = prestart_position + 1
    list_end = gestures.index('dynamite')
    remainder_in_list = list_end - start_position
    needed_after_end = 12 - remainder_in_list

    if needed_after_end > 0:

        computer_choice = random.choice(gestures[])

print("Start Position: ", start_position)
print("List End: ", list_end)
print("Of the 12 we need, ", remainder_in_list, " are left in the list.")
print("So we need ", needed_after_end, " elements from the beginning of the list")

#get a list slice of 12 elements in the list, starting with the element after player_choice



