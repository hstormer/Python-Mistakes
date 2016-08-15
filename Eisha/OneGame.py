from sys import exit
from random import randint


def Friends():
    print """ 
		Don't Worry, you are not alone. 
		Your faithful servant Samwise Gamgee,
		And your kinsnmen Meriadoc Brandybuck
	        and Peregrin Took decide to accompany 
		you (ofcourse!)."""
#_________________________________________________________________________
def Bree():
	print """
				You have come to Bree and quickly decide 
	       		to stay at the Prancing Pony for the night.
			You encounter strange looking Ranger who calls himself Strider
      		and knows a creepy bit too much about your errand. Strinder wishes
	  		to assist you but he seems pretty foul (according to Sam).
		     		     Do you accept his offer?"""
	choice =  raw_input("*~ ")
	if "yes" in choice:
		print """
		You recieve a letter from Gandalf advicing that
	Strider can be trusted. You learn that his real name is Aragorn 
		 and that he plans to take you to Rivendell!!!"""
		Rivendell()
	elif "no" in choice:
		print"""		
		Well aware of Stranger Danger, you and your friends decide 
			         to travel alone East"""
		MistyMountains()
	else:
		print "Not sure what to do, you and your friends take your own road"
		BlackRider()
#_________________________________________________________________________
def BlackRider():
	print """
		While you travel your road, you and your friends
	encounter a mysterious rider clad all in black. He doesn't seem 
			    to have noticed you yet."""
	choice =  raw_input("*~ ")
	if "mordor" in choice:
		Mordor()
		BlackRider()
	elif "west" in choice:
		TheShore()
	elif "north" in choice:
		Shire()
	elif "south" in choice:
		TheShore()
	elif "fight" in choice:
		print """
			You fight as a young brave Hobbit
	     Though brave you might be, the evil is too much for you.
		  You are stabbed by a sharp blade and the world 
		      around seems to blur into nothingness."""
		GameOver()
	elif "hide" in choice:
		print"""
		The Rider seems blind and uses other senses than sight,
	   You and your friends hide in the nearby bushes. Until he goes away.
	        o shelter for the night, you travel east to a nearby town."""
		Bree()
	elif "run" in choice:
		print "Run where?"
		BlackRider()
	elif "Shire" in choice:
		Shire()
	else:
		print"""
				Im not sure what you mean.
				   Hurry! Do something."""
		BlackRider()

#_________________________________________________________________________
def Rivendell():
	print """
	 		 You open your eyes to find yourself on soft sheets in Rivendell.
	 		You are soon summoned to the secret counsil of the Ring where more 
	   		than ever you fully realise the evil powers within your reach.
			The council proposes to rid of the Ring in the fire of Mordor where
				it was forged long ago. Will you take on the quest?"""
	choice =  raw_input("*~ ")
	if "no" in choice:
		print"""
		   Hobbits are not meant for dangerous adventures 
	  like this one. You decide to stay with the elves and their luxuries 
	while someone else takes on the quest. However, the enemy's powers soon
            grow until most elves are leaving for the Grey Havens. You are 
			    welcomed to accompany them."""
		TheShore()
	elif "mordor" in choice:
		Mordor()
		Rivendell()
	elif "yes" in choice:
		print"""
					You might be a small Hobbit, but you are brave
	         		and you volunteer to take on this mission....quest.....thing.
					Eight others are chosen to accompany you and
		       		you are all part of The Fellowship of The Ring.
				You and your friends battle storms are Orcs and valiantly
			             		take the journey. """
		MistyMountains()
	else:
		print"""
		Too hesitant to risk the danger, no one volunteers 
		to cast the Ring into the Fire. As for yourself, you 
		are too attatched to your precious by now. Rivendell
		is in a state of chaos and you are growing evil by 
		every minute spent with the Ring. The Middle Earth
		is doomed."""
		GameOver()
#_________________________________________________________________________
def TheShore():
	print """
			On the horizon, you see water as far
		as your eyes can reach. Across the sea you have heard
		lies the Grey Haven. You can leave Middle Earh and start
		over your new life, but you are also concerned and guilty
		thinking about all the years you have spent here and all
				the people you have known."""
	GreyHaven()
#_________________________________________________________________________
def Eagle():
	print"""
		High up in the sky you see a strange bird
	who claims to know Gandalf. The bird offers to take you to
	a random place in Middle Earth. You may reach your goal very 
	         fast or might be delayed, none can tell.
	     You and your friends clminb on the bird's back. 
		   Press any key when you are ready..."""
	choice =  raw_input("*~ ")
	print """
		You feel a ghust of air as the massive wings unfold.
	You you open your eyes again, you and your friends have landed and
		     you bid farewell to the strange bird.
		You look around to discover where you have come and..."""
	num = randint(1,11)
	if num == 1:
		TheShore()
	if num == 2:
		Shire()
	if num == 3:
		Dragon()
	if num == 4:
		Bree()
	if num == 5:
		Rivendell()
	if num == 6:
		Moria()
	if num == 7:
		Lothorien()
	if num == 8:
		Isengard()
	if num == 9:
		Gondor()
	if num == 10:
		Rohan()
	if num == 11:
		MistyMountains()
#_________________________________________________________________________
def Mirkwood():
	print """
		 You find yourself surrounded by a dark forest.
		           Yes, you are in Mirkwood.
	You see dark trees everywhere. High up you see birds in the sky
	       and a little further off you catch a glimpse of the
			           Wood Elves."""
	choice =  raw_input("*~ ")
	if "tree" in choice:
		print "The trees don't look to friendly to be bothered with"
		Mirkwood()
	elif "bird" in choice:
		Eagle()
	elif "elf" in choice:
		print """
			Cautiosly, you approach the elves because
		the fair folks do not approve of trespassers, especially
	Now in the Dark Days (but Sam REALLY wants a closer look!). However, 
                        you soon find that these Wood Elves have 
     known Bilbo from his adventures and will be glad to assist you. King Thranduil
	arms you with fair weapons and you are off with Legolas to Rivendell. """
		Rivendell()
	elif "elves" in choice:
		print """
			Cautiosly, you approach the elves because
		the fair folks do not approve of trespassers, especially
	Now in the Dark Days (but Sam REALLY wants a closer look!). However, 
                        you soon find that these Wood Elves have 
     known Bilbo from his adventures and will be glad to assist you. King Thranduil
	arms you with fair weapons and you are off with Legolas to Rivendell. """
		Rivendell()
	else:
		print "We can't do that here"
		Mirkwood()

#_________________________________________________________________________
def Caradhras():
	print """
		You are climbing the Caradhras Mountain and you find yourself
	  in the middle of a savage snowstorm. You are freezing and you do not think
	your friends will be able to survive the night. Do you wish to continue?"""
	choice =  raw_input("*~ ")
	if "no" in choice:
		Moria()
	elif "yes" in choice:
		print """
		Hobbits are made of tough stuff. Luckily you all
		   survive the climb and reach the top."""
		Eagle()
	else:
		print "Sorry, I didn't quite get that."
		print "You need to make a decision quick!"
		Caradhras()
#_________________________________________________________________________
def Mordor():
	print "One does not simply walk into Mordor"
#_________________________________________________________________________
def Orcs():
	print """
		 	You find yourself soon surrounded by 
		        hideous Orcs. They only mean to kill."""
	choice =  raw_input("*~ ")
	if "fight" in choice:
		fate = randint(1,3)
		if fate == 1:
			print "You fight as you flee for your life"
			print "At a distance you see a hopeful light"
			Lothorien()
		if fate == 2:
			print "You fight as you flee for your life"
			print "But the Orcs are just too many..."
			GameOver()
		if fate == 3:
			print "You fight as you flee for your life"
			print "At a distance you see a hopeful light"
			Lothorien()
	
	elif "run" in choice:
		print "You fight as you flee for your life"
		print "At a distance you see a hopeful light"
		Lothorien()
	if "kill" in choice:
		fate = randint(1,3)
		if fate == 1:
			print "You fight as you flee for your life"
			print "At a distance you see a hopeful light"
			Lothorien()
		if fate == 2:
			print "You fight as you flee for your life"
			print "But the Orcs are just too many..."
			GameOver()
		if fate == 3:
			print "You fight as you flee for your life"
			print "At a distance you see a hopeful light"
			Lothorien()
	else:
		print "Hurry, they are overpowering you!"
		Orcs()

#_________________________________________________________________________
def MoriaIn():
	print """ 
		You and your company are travelling the Mines of Moria.
		It is dark and damp in here. You see webs and dead bodies
		of dwarfs around you. In the distance you hear a booming
		noice of a drum. There is a dark passage on your left and 
		a stair case that leads up. There is also a narrow path that
		leads down into a dark tunnel. You hear another boom.""" 
	choice =  raw_input("*~ ")
	if "mordor" in choice:
		Mordor()
		Moria()
	elif "up" in choice:
		print" As the last one in your compnany climbs up,"
		print"the staircase closes behind you."
		print" You cannot go back the way you came"
		MistyMountains()
	elif "stair" in choice:
		print" As the last one in your compnany climbs up,"
		print"the staircase closes behind you."
		print" You cannot go back the way you came"
		MistyMountains()
	elif "left" in choice:
		print"""
			You take the dark passage on your left,
		anticipating danger at every turn. However, you are still
		    safe and you see a pure light coming from outside."""
		Lothorien()
	elif "passage" in choice:
		print"""
			You take the dark passage on your left,
		anticipating danger at every turn. However, you are still
		    safe and you see a pure light coming from outside."""
		Lothorien()
	elif "down" in choice:
		print"""
			As you decide to take the downward path,
		you soon find yourself in a small chamber. The Booming
			of the drums is stronger than ever before."""
		Orcs()
	elif "narrow" in choice:
		print"""
			As you decide to take the downward path,
		you soon find yourself in a small chamber. The Booming
			of the drums is stronger than ever before."""
		Orcs()
	else:
		print"""
			FOOL OF A TOOK!!!
		What are you doing?! The Orcs have heard you.
			They are coming."""
		Orcs()	
#_________________________________________________________________________
def Moria():

	print"""
	        		You have come to the Gates of Moria"""


        print"		                          ___________    "                              
        print"		                        _/           \_ "
        print"		                      _/ speak, friend \_" 
        print"		                    _/     and enter     \_"
        print"		                  _/     _____________     \_"     
        print"		                _/     _/     *       \_     \_"
        print"		              _/     _/     * /\ *      \_     \_"
        print"		             /______/    * _/\/\/\_ *     \______\ "           
        print"		            /-------   *   \______/   *    -------\ "        
        print"		            \|     |                       |     |/  "           
        print"		             |     |                       |     |"
        print"		             |     |                       |     |"
        print"		             |  \/ |         __/\__     _  | \/  |\_"
        print"		             |   \_|\_ \_    \/\/\/    / \ |_ \_ |/"
        print"		            /|_/ _ \/ _/ \   /\/\/\     _/ | \/ _/\_"
        print"		            \| \/_ |\/ _       \/      \/_ |\/_/ |   "   
        print"		             \__\_\|/ /_             \__\ \|/_   |"
        print"		             |  / \|_/  \              / \_|/ \  |"
        print"		             |-----||                     ||-----| "              
        print"		             |_____||        ~p*r         ||_____|  "           
        print"		           __|_____||_____________________||_____|__"
	choice =  raw_input("*~ ")
	if "mellon" in choice:
		print " 	You guessed the Password!!!"
		MoriaIn()  
	if "melon" in choice:
		print " 	You guessed the Password!!!"
		MoriaIn() 
	if "up" in choice:
		Caradhras()
	if "mordor" in choice:
		Mordor()
		Moria()
	if "back" in choice:
		MistyMountains()
	if "return" in choice:
		MistyMountains()
	if "fire" in choice:
		Fire()
	else:
		Moria() 
	
#_________________________________________________________________________
def Tunnel():
	print "Will you take the undergroud passage before you?"
	choice =  raw_input("*~ ")
	if "yes" in choice:
		Rivendell()
	elif "no" in choice():
		MistyMountains()
	else:
		print"""
		To weary and exhausted from your journey to make a choice,
	you stumble around at the enterace of the the underground pass until you
		        are caputured and slaughtered by Orcs."""
		GameOver()

#_________________________________________________________________________
def Lothorien():
	print"Test"
	Shire()

#_________________________________________________________________________
def Gondor():
	print"Test"
	Shire()

#_________________________________________________________________________
def Rohan():
	print"Test"
	Shire()

#_________________________________________________________________________
def Isengard():
	print"Test"
	Shire()
#_________________________________________________________________________
def Fire():
	print """
			   FOOL OF A TOOK!!!
	You light a fire which draws attention to the enemy's spies.
Soon you see wolves, Orcs, and Black Riders approaching from all directions. 
	And the inhabitants of Middle Earth lived without fire or
		            light everafter."""
	GameOver()
#_________________________________________________________________________
def Stone(): 
	print """
		   You continue to travel northalong
		the Misty Mountains until you encounter
	a huge rock. With the help of your friends you move the 
	     rock to find an underground passage before you."""
	Tunnel()
#_________________________________________________________________________
def UpDown():
	print """
			So you decide to continue yourjourney
		Southward until you encounter two paths; one going up
			the mountains and the other leading
		     down a tunnel. Which path do you choose?"""
	choice =  raw_input("*~ ")
	if "up" in choice:
		Caradhras()
	elif "mountain" in choice:
		Caradhras()
	elif "down" in choice:
		Moria()
	elif "tunnel" in choice:
		Moria()	
	elif "mordor" in choice:
		Mordor()
		UpDown()
	elif "fire" in choice:
		Fire()
	else: 
		print "That's not an option."
		print "You NEED to find Shelter if you wish to survive the night."
		UpDown()
#_________________________________________________________________________
def MistyMountains():
	print """
		You see mountains all around you. 
	      You have come to the Misty Mountains!
		You see a few thin trees, rocks, 
		and mist everywhere. You must do 
               something before the Black Riders
		 come hunting for you at night. """

	choice =  raw_input("*~ ")

	if "north" in choice:
		Stone()
	elif "mordor" in choice:
		Mordor()
		MistyMountains()
	elif "south" in choice:
		UpDown()	
	elif "east" in choice:
		Mirkwood()
	elif "west" in choice:
		Bree()
	elif "up" in choice:
		Caradhras()
	elif "mountain" in choice:
		Caradhras()
	elif "stone" in choice:
		print """
		Not quite sure what you're doing, you randomly
		move a big stone off the ground. To your suprise,
		you find an underground tunnel before you"""
		Tunnel()
	elif "rock" in choice:
		print """
		Not quite sure what you're doing, you randomly
		move a big rock off the ground. To your suprise,
		you find an underground tunnel before you"""	
		Tunnel()
	elif "cave" in choice:
		print "You search for a cave to find shelter for the night"
		Moria()
	elif "tree" in choice:
		print "The trees are too thin to climb or seek shelter"
		MistyMountains()
	elif "fire" in choice:
		Fire()
	else:
		print "I'm not sure what you mean by that"
		MistyMountains()		
#_________________________________________________________________________
def Dragon():
	print """
			Not sure where you are headed,
		You encounter a Dragon who has just awakened 
			  and looks quite hungry!"""

	choice =  raw_input("*~ ")

	if "flee" in choice:
		GreyHaven()
	elif "back" in choice:
		Shire()
	elif "return" in choice:
		Shire()
	elif "home" in choice:
		Shire()
	elif "fight" in choice:
		print """ 
			  You fight like a brave warrior
			Out of the legend. But you are just 
		a hobbit and the Dragon is too savage for you. 
         It exhales its fiery breath and like a brave young soldier, you
                               are toasted on spot. """
		GameOver()
	elif "mordor" in choice:
		Mordor()
		Dragon()
	elif "ride" in choice:
		print "Wow! you can ride the dragon!"
		print " and the dragon drops you off too..."
		ride = randint(1,11)
		if ride == 1:
			TheShore()
		if ride == 2:
			Shire()
		if ride == 3:
			Eagle()
		if ride == 4:
			Bree()
		if ride == 5:
			Rivendell()
		if ride == 6:
			Moria()
		if ride == 7:
			Lothorien()
		if ride == 8:
			Isengard()
		if ride == 9:
			Gondor()
		if ride == 10:
			Rohan()
		if ride == 11:
			MistyMountains()
	elif "fly" in choice:
		print "Wow! you can ride the dragon!"
		print " and the dragon drops you off too..."
		ride = randint(1,11)
		if ride == 1:
			TheShore()
		if ride == 2:
			Shire()
		if ride == 3:
			Eagle()
		if ride == 4:
			Bree()
		if ride == 5:
			Rivendell()
		if ride == 6:
			Moria()
		if ride == 7:
			Lothorien()
		if ride == 8:
			Isengard()
		if ride == 9:
			Gondor()
		if ride == 10:
			Rohan()
		if ride == 11:
			MistyMountains()
	else:
		print "Sorry, you can't do that my young reckless Hobbit!"
		Dragon()
       

#___________________________________________________________________
def GameOver():
	exit(0)

#___________________________________________________________________
def GreyHaven():
	print "Are you sure you want to leave Middle Earth?"

	choice =  raw_input("*~ ")
	
	if "yes" in choice:
		print """
			    You decide to take the Grey Ships
			Along with the Elven folk in hopes to find
		mose peaceful lands. Not everyone is meant for these kins of 
	unexpected adventures...especially not a Hobbit. You cross the Grey Haven and
        	hope that Middle Earth would be in good hands for the future. 
            	                 And the Ring?
             	  You toss it in the waters and hope that it is
                	   not the hand of the evil who finds it.
				   Farewell Middle Earth! """
		exit(0)

	elif "no" in choice:
		Shire()
	elif "mordor" in choice:
		Mordor()
		GreyHaven()
	else:
		print "Sorry, I didn't quite get that"
		GreyHaven()

#___________________________________________________________________
def Shire():
	print """ 
				Welcome to The Shire!
		It is one of the most peaceful places in Middle Earth...
		     ...That is, before the Ring came along.
	Gandalf the Grey infoms you about the evil crisis that Middle Earth
	is facing. All because of the One Ring. Middle Earth will soon be
	a place of misery and doom; including the Shire. The Ring must not 
	stay in this peaceful village, but you seem to be the only one who
	can resist its dark powers. You can either choose a direction to start
	off with, or flee from your destiny. """
	
	choice =  raw_input("*~ ")

	if "north" in choice:
		Friends()		
		Dragon()
	elif "south" in choice:
		Friends()
		BlackRider()
	elif "east" in choice:
		Friends()
		Bree()
	elif "west" in choice:
		TheShore()
	elif "mordor" in choice:
		Mordor()
		Shire()				
	elif "flee" in choice:
		GreyHaven()
	else:
		print """Sorry, I did not get that.
		     State a direction or choose to flee."""
		Shire()

#____________________________________________________________________

Shire()

