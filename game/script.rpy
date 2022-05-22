# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define e = Character("Eileen")
define homer = Character("Homer")
define crewmen = Character("Odysseus' crewmen")
define odysseus = Character("Odysseus")

# This is a variable that is True if you've compared a VN to a book, and False
# otherwise.
default bag_of_winds = False
default bag_of_endless_bread = False
default moly = False
default drug = False
default teiresias = False



# The game starts here.

label start:

    scene bg ithaca

    homer "A long time ago, in the land of Greece, there lived a man named Odysseus."

    scene bg trojan war
    
    homer "When the Trojan War broke out, Odysseus left his home in Ithaca to go fight in Troy..."
    
    homer "... but his journey back from the war took a little bit longer than expected..."    

    menu:

        "Wanna know how it went? :D"

        "HECK YEAH!":

            jump lotus_flowers

        "I'd rather not, I prefer maths...":

            jump goodbye

label lotus_flowers:

    scene bg lotus flowers

    homer "10 days after leaving Ismarus, the ship stopped at the land of the \"Lotus Eaters\""

    homer "The purpose of the brief visit was to to eat and rest."

    show crewmen
    
    menu:

        crewmen "We're exhausted, let's..."

        "eat some of these delicious flowers!":

            jump ate_lotus_flowers

        "catch a good night sleep":

            jump goodbye_error

label ate_lotus_flowers:
    
    scene bg ate lotus

    homer "Lotus flowers stuns Odysseus' crewmen"

    homer "Odysseus has to hurry them back to the ship, so as they can continue their journey back home"

    jump polyphemus


label polyphemus:

    scene bg polyphemus island

    "Odysseus and his men reach the land of the Cyclopes, specifically the cave of a certain Cyclops called Polyphemus"

    scene bg cave of polyphemus

    "The travelers assume Polyphemus would be gentle and welcoming"

    "But that's not the case, and Polyphemus hates four crewmen"

    menu:

        "As a result, Odysseus"

        "Makes Polyphemus drunk and blindes him by plunging a burning stake into his eye while he lay asleep":

            jump blinded_polyphemus

        "Asks the intervention of Greek Gods":

            jump goodbye_greek_gods_intervention
    

label blinded_polyphemus:

    scene bg blinded polyphemus

    "Odysseus and his men take advantage of the situation and manage to escape"

    menu:

        "Where do they head to next?"

        "Aeolia, land of Aeolus":

            jump aeolus

        "Aeaea, home of the goddess, Circe":

            jump circe


label aeolus:

    scene bg land of aeolus

    "In Aeolia Odysseus and the crewmen meet Aeolus, the God of the Winds."

    menu:

        "He's very friendly and gives them a bag with what?"

        "Storm winds, to help them push back to Ithaca":
            $ bag_of_winds = True

            jump crewmen_open_bag

        "\"Endless bread\", a specially-crafted type of bread which satisfies the need of eating forever":

            $ bag_of_endless_bread = True

            jump crewmen_open_bag


    "He gives them a bag of storm winds, to help push them back to Ithaca."
   

label crewmen_open_bag:

    scene bg ithaca

    "Sailing proceeds greatly, Ithaca is now in plain sight, ready to welcome the men."
    
    "Odysseus decides then to take a nap, in order to be well rested for his return home."

    scene bg bag of winds
    
    "His crew had the idea to open up the bag gifted by Aeolus"

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

        "When they reached the Underworld, Odysseus encounters"

        "The ghosts of numerous people, including: his mother, Teiresias and Agamemnon":

            $ teiresias = True

            jump 

        "The Hypnotic cat":

            jump hypnotic_cat
    

label hypnotic_cat:

    #TODO add background

    "Odysseus and his crew are hypnotized by the cat"

    "The hypnosis is so strong that leaves the men confused for entire days"

    "Some men die of natural cause, some commit suicide to free themselves from the pain"

    "The few survivors, including Odysseus, are still quite stunned. They get back in the waters but, due to the confusion, end up back in Polyphemus' land "

    # TODO eval whether to offer the possibility of picking where we want to go back to
    # TODO eval whether variables should be reset or not!

    jump polyphemus














return


label goodbye_endless_bread:
    #TODO


label goodbye_odysseus_turned_pig:
    #TODO
