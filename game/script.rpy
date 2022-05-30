﻿# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define e = Character("Eileen")
define homer = Character("Homer", color="#F8347C")
define crewmen = Character("Odysseus' crewmen", color="#FFA630")
define crewman_1 = Character("Crewman 1", color="#B5FD39")
define crewman_2 = Character("Crewman 2", color="#B5FD39")
define crewman_3 = Character("Crewman 3", color="#B5FD39")
define odysseus = Character("Odysseus", color="#4DA1A9")
define polyphemus = Character("Polyphemus", color="#FF0000")

# This is a variable that is True if you've compared a VN to a book, and False
# otherwise.
default bag_of_winds = False
default bag_of_endless_bread = False
default moly = False
default drug = False
default teiresias = False
default sacrificed_all_men = False
default intoxicated = False
default guilty_conscience = False



# The game starts here.

label start:

    scene bg ithaca

    show homer at left with dissolve

    homer "A long time ago, in the land of Greece, there lived a man named Odysseus."

    scene bg trojan war
    
    show homer at left with dissolve
    
    homer "When the Trojan War broke out, Odysseus left his home in Ithaca to go fight in Troy."
    
    homer "After the Trojan War ended, Odysseus hops up in his ship, together with his crewmen, in order to go back to Ithaca."
    
    homer "... but his journey back from the war took a little bit longer than expected..."

    hide homer with dissolve

    menu:

        "Wanna know how it went? :D"

        "HECK YEAH!":

            jump lotus_flowers

        "I'd rather not, I prefer maths...":

            jump goodbye

label lotus_flowers:

    scene bg djerba

    show homer at left with dissolve

    homer "\"10 days after leaving Ismarus, Odysseus and his men stop at Djerba, land of the \'Lotus Eaters\'\""

    hide homer at left with dissolve

    show odysseus at right with dissolve
    
    odysseus "Gentlemen, we'll stay here in Djerba for a very brief period, just to get some rest."

    hide odysseus at right with dissolve

    show crewmen at right with dissolve

    crewmen "Chief, we are hungry! Is there something to eat?"

    hide crewmen at right with dissolve

    show odysseus at right with dissolve

    odysseus "I don't know, let's find something to eat in the island!"

    hide odysseus

    show lotus flower at topleft

    show crewmen at right with dissolve

    menu:
        
        crewmen "Hey! Look! We found these! Shall we eat them?"

        "Yes, we are starving!":

            jump ate_lotus_flowers

        "Uhm, better safe then sorry, let's find something more familiar...":

            jump die_starving

label ate_lotus_flowers:
    
    scene bg ate lotus

    show crewmen stunned at right with dissolve

    play sound "cough_1.mp3"

    crewman_1 "GASP! what was there in those flowers?"

    play sound "cough_2.mp3" volume 0.3

    crewman_2 "My head is spinnin' like crazy!"

    play sound "cough_1.mp3"
    
    crewman_3 "I don't feel really well..."

    hide crewmen stunned

    show odysseus at right with dissolve

    odysseus "What is going on?!?"

    hide odysseus

    show crewmen stunned at right with dissolve

    play sound "cough_2.mp3" volume 0.3

    crewmen "We ate the lotus flowers and now we are all sick..."

    hide crewmen
    
    show odysseus at right with dissolve

    odysseus "What?!? Really?!? Well, let's go back to our ship then, fast!"

    jump polyphemus


label polyphemus:

    scene bg cave of polyphemus

    show homer at left with dissolve

    homer "After recovering from the lotus flowers' intoxication, Odysseus and his men reach the land of the Cyclopes."
    
    homer "Here lives Polyphemus"

    homer "The travelers assume Polyphemus would understand them and be gentle and welcoming with them"

    homer "But..."

    hide homer

    show polyphemus at left with dissolve

    polyphemus "WHO ARE YOU? WHAT DO YOU WANT?!?"
    
    polyphemus "YOU ENTERED MY CAVE WITHOUT MY PERMISSION, NOW I WILL EAT YOU ALIVE!"

    hide polyphemus

    show homer at left with dissolve

    homer "Polyphemus actually proceeds to eat four crewmen alive"
    
    homer "Odysseus is saddened and angry about this loss, so he decides to hide, in order to organize his thoughts..."

    hide homer

    show odysseus at right with dissolve

    menu:

        odysseus "Uhm... what do I do?"

        "Make Polyphemus drunk and blind him, sticking a burning stake into his eye while he's asleep":

            jump blinded_polyphemus

        "Makes Polyphemus drunk and kill him, cutting his head with a giant sharp rock":

            $ intoxicated = True

            jump blinded_polyphemus
        
        "Takes the loss. I'll never be able to counter a giant. I can not win.":

            $ guilty_conscience = True

            jump aeolus
    

label blinded_polyphemus:

    scene bg blinded polyphemus

    hide odysseus

    show homer at left with dissolve

    homer "Odysseus and his men take advantage of the situation and manage to escape"

    homer "Still shocked about what happened with Polyphemus, they are undecided about where to go next..."

    hide homer

    show crewmen at right with dissolve

    menu:

        "Where to next, chief?"

        "Aeolia, land of Aeolus":

            jump aeolus

        "Aeaea, home of the goddess, Circe":

            jump circe


label aeolus:

    scene bg land of aeolus

    show homer at left with dissolve

    homer "In Aeolia, Odysseus and the crewmen meet Aeolus, the God of the Winds."

    menu:

        "Aeolus is very friendly with them, and gives them a bag with what?"

        "Storm winds, to help them push back to Ithaca":
            $ bag_of_winds = True

            jump crewmen_open_bag

        "\"Endless bread\", a specially-crafted type of bread which satisfies the need of eating forever":

            $ bag_of_endless_bread = True

            jump crewmen_open_bag
   

label crewmen_open_bag:

    scene bg ithaca

    hide homer

    show crewmen at right with dissolve

    crewmen "Chief, sailing is proceeding greatly."
    
    crewmen "Ithaca is now in plain sight, just right in front of us!"

    crewmen "We should arrive there tomorrow morning, at worse!"

    hide crewmen

    show odysseus at right with dissolve
    
    odysseus "That's fantastic news!"
    
    odysseus "Since everything seems smooth, I'll take a quick nap, so as I will be well rested for my return home."

    hide odysseus
    
    scene bg bag of winds

    show homer at left with dissolve
    
    homer "Excited by the prospect of getting back home, the crewmen decide to open the bag gifted to them by Aeolus"

    hide homer 

    if bag_of_endless_bread == True:
        
        jump goodbye_endless_bread
    
    if bag_of_winds == True: 
        
        jump circe

label circe:
    
    scene bg circe

    show homer at left with dissolve

    # TODO add windstorm sound
    
    homer "Little did the men know!"

    homer "The bag of winds released a windstorm, which actually pushes them far away from Ithaca"

    homer "As a result, they get pushed towards Aeaea, lands of Circe goddess"
    
    homer "In Aeaea, Odysseus meets with Hermes, who is very gentle with the travelers."

    menu:

        "What does Hermes gift to Odysseus?"

        "\"moly\": an antidote preventing him from turning into a pig":

            $ moly = True

        "The flame of Gods: a never-ending fire torch":

            $ moly = False

    hide homer

    show odysseus at right with dissolve

    odysseus "Crew, go explore the island!"
    
    odysseus "Look for food and a place where to rest, so as we can continue our journey back home well rested"

    hide odysseus

    show homer at left with dissolve
    
    scene bg circe turns men into pigs
    
    homer "Circe is not welcoming of the men in the lands"

    homer "She uses to turn men into pigs, and so it does with Odysseus and his men"

    hide homer

    if moly == True:

        show odysseus at right with dissolve

        odysseus "What is happening?!?"

        odysseus "There must be an explanation, I'll look for Circe..."

        hide odysseus

        scene bg circe together odysseus

        show homer at left with dissolve

        homer "Odysseus indeed finds Circe"

        homer "They actually end up together, spending an entire year in a relationship in the island"

        homer "Eventually, Circe understands that Odysseus has to go home, so she advises him to what route to take"

        homer "Specifically, she tells him to visit the Underworld..."

        hide homer

        jump underworld

    else:

        show odysseus at right with dissolve

        odysseus "What is happening?!?"

        scene bg odysseus defeated

        odysseus "I don't feel very well, my entire body hurts!"

        hide odysseus
    
        show homer at left with dissolve

        homer "The transformation to pig affects Odysseus as well"

        homer "The effects of the transformation seem to be much stronger on Odysseus..."

        hide homer

        jump goodbye_odysseus_dies_turned_pig

label underworld:

    scene bg underworld

    show homer at left with dissolve

    homer "Following the Circe's advice, the men arrive in the Underworld"

    menu:

        "Who does Odysseus meet here?"

        "The ghosts of numerous people, including: his mother, Teiresias and Agamemnon":

            $ teiresias = True

            jump sirens_choice

        "The Hypnotic cat":

            jump hypnotic_cat
    

label hypnotic_cat:

    scene bg cat

    homer "Odysseus and his crew observe intrigued the giant cat"

    homer "The animal is calm lookinh, it seems inocuous"

    hide homer

    show crewmen at right with dissolve
    
    crewmen "What is happening? Is this cat even alive?"

    hide crewmen

    show odysseus at right with dissolve

    odysseus "That's strange... something is going on with his eyes..."

    odysseus "Can you guys see it too?"

    hide odysseus

    show homer at left with dissolve

    homer "Odysseus was right."

    homer "The cat's eyes have a strange power: they can hypnotize everyone they point to, even if for just a few seconds"

    homer "It'll be a matter of instant and the men will notice the effects of the hypnosis..."

    hide homer 

    show crewmen stunned at right with dissolve

    crewman_1 "MY EYES! MY EYES! I CAN'T ANYTHING!!! "

    crewman_2 "MY EAR! WHAT IS THIS SOUND? IT'S ATROCIOUS!"

    hide crewmen stunned

    show homer at left with dissolve
    
    homer "The crew is in heavy pain"

    homer "Some men die of natural cause, some commit suicide to free themselves from the unbearable pain"

    homer "The few survivors, including Odysseus, are still quite stunned."

    homer "Odysseus understands that he has to bring his crew as far as possible"

    hide homer

    show odysseus stunned at right with dissolve

    menu:
        
        odysseus "Getlemen, follw me! This way, it will lead us to..."

        "Polyphemus' land":

            jump polyphemus

            
        "The Underworld":
            
            jump underworld


label sirens_choice:
    scene bg sirens

    show homer at left with dissolve

    homer "Next up for the crew, the Sirens!"

    menu:

        homer "What is the peculiarity of the Sirens?"

        "Getting by the Sirens was an impossible task, as their beautiful song drew anyone who heard it in":

            jump sirens_correct

        "Getting by the Sirens requires sacrificing all Odysseus' crew":

            $ sacrificed_all_men = True

            jump sirens_sacrifice

        "Getting by the Sirens requires at least a woman to be present in the ship":

            jump goodbye_sirens_woman


label sirens_correct:
    scene bg sirens

    if teiresias == True:
        
        hide homer

        show odysseus at right with dissolve 

        odysseus "Gentlemen, Teiresias told me in the underworld what is the deal with the Sirens."

        odysseus "For these reason, you'll tie me to this pole and cover my ears with wax."

        odysseus "This way, I'll be able to conduct you pass the Sirens and we'll be able to continue our navigation"

        odysseus "All clear?"

        hide odysseus

        show crewmen at right with dissolve 

        crewmen "YES, SIR!"

        hide crewmen

        jump monsters

    else:
        homer "The men were not sufficiently prepared and did not cover their ears"

        homer "As a result, all of them hear sirens' songs and get distracted by them"

        hide homer

        show crewmen at right with dissolve

        crewmen_1 "Wow, this chant is so beautiful!"

        crewmen_1 "This is the only thing I want to listen to for the rest of my life!"

        hide crewmen

        show odysseus at left with dissolve

        odysseus "\"I want to focus so much, but I just can't seem to!\""

        odysseus "Gentleman! Let's stir away!"
        
        odysseus "I have to admit, I'm so distracted, I'm not sure I gave the right directions to my crew..."

        hide odysseus

        jump start

label monsters:

    scene bg monsters
    
    menu:

        "Odysseus had to sacrifice 6 of his men by going past Scylla as opposed to losing the whole ship if they were to go by Charybdis."

        "What does he do?"

        "Sacrifices 6 men":

            if sacrificed_all_men == False:

                jump helios

            else:

                jump already_sacrificed_all_men

        "Sacrifices the entire ship, himself included":

            jump sacrifies_ship

label helios:

    scene bg helios

    "Destroyed by the loss of his 6 men, the remaining crewmen and Odysseus arrive in Thriancia, home of Helios's cows"

    menu:

        "After receiving clear instructions not to eat the cows, what does the crew do?"

        "Eat the cows":

            jump ogygia

        "do NOT eat the cows":

            jump die_starving

label ogygia:

    scene bg ogygia

    "In Ogygia, Odyssesu gets captured by Calypso"

    menu:

        "7 long years the segregation will last, until when"

        "Nausicaa frees Odysseus":

            jump conclusion

        "Odysseus dies of natural cause, exhausted by the journey":

            jump goodbye_die_natural_cause
    
    
label conclusion:

    "THE END! THX BYEZZZ!"





return


label goodbye_endless_bread:
    #TODO


label goodbye_odysseus_dies_turned_pig:
    #TODO


label goodbye_sirens_woman:
    #TODO

label sacrifies_ship:
    #TODO

    jump goodbye_sacrifies_ship

label goodbye_sacrifies_ship:
    #TODO

label already_sacrificed_all_men:
    #TODO

label die_starving:
    #TODO

    jump goodbye_die_starving

label goodbye_die_starving:
    #TODO

label goodbye_die_natural_cause:
    #TODO



