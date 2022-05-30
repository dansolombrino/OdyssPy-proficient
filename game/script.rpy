# The script of the game goes in this file.

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

    "In Aeaea, Odysseus meets with Hermes"

    menu:

        "What does Hermes gift to Odysseus?"

        "\"moly\": an antidote preventing him from turning into a pig":

            $ moly = True

        "The flame of Gods: a never-ending fire torch":

            $ moly = False

    "Odysseus sends his men to explore the island, looking for food and a place where to rest"

    scene bg circe turns men into pigs
    
    "The crewmen get turned into pigs by Circe"

    if moly == True:

        scene bg circe together odysseus

        "Fortunately, Odysseus got \"moly\" by Hermes, so he's immune to the transformation"

        "Furthermore, he decises to look for Circe"

        "The two meet and end up together"

        jump underworld

    else:

        scene bg odysseus defeated
    
        "Odysseus is NOT immune to the transformation, so he's turned into a pig too"

        jump goodbye_odysseus_turned_pig

label underworld:

    scene bg underworld

    "Circe advises the men to go to the Underworld, before going back to Ithaca"

    menu:

        "When they reach the Underworld, Odysseus encounters"

        "The ghosts of numerous people, including: his mother, Teiresias and Agamemnon":

            $ teiresias = True

            jump sirens_choice

        "The Hypnotic cat":

            jump hypnotic_cat
    

label hypnotic_cat:

    scene bg cat

    "Odysseus and his crew are hypnotized by the cat"

    "The hypnosis is so strong that leaves the men confused for entire days"

    "Some men die of natural cause, some commit suicide to free themselves from the pain"

    "The few survivors, including Odysseus, are still quite stunned."
    
    "They manage to get back in the waters but, due to the confusion, end up back in Polyphemus' land..."

    # TODO eval whether to offer the possibility of picking where we want to go back to
    # TODO eval whether variables should be reset or not!

    # TODO eval whether to continue the story a little more on this wrong path

    jump polyphemus


label sirens_choice:
    scene bg sirens

    "Next up for the crew, the Sirens!"

    menu:

        "What is the peculiarity of the Sirens?"

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
        "In order to get through the Sirens, Odysseus had his men tie him to a pole, and put wax in their ears so they would not hear the Sirens."
        
        jump monsters

    else:
        "The men were not sufficiently prepared and did not cover their ears"

        "As a result, all of them hear sirens' songs and get distracted by them"

        "They're so confused that they end up in a familiar place... Circe's land!"

        jump circe

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


label goodbye_odysseus_turned_pig:
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



