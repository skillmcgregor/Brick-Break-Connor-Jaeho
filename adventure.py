# my game

mystate = 1 #initial
a = ("east")
b = ("west")
c = ("north")
d = ("south")
print "Use inputs of north, south, east, and west."
while True: 
	
	if mystate == 1:
		x = raw_input("You find yourself in a large field at night. It stretches on as far as the eye can see.")
		if x == a: 
				mystate = 2
		elif x == b:
				mystate = 3
		elif x == c:
				mystate = 4
		elif x == d:
				mystate = 5
	
	if mystate == 2:
		x = raw_input("You see the outline of a large forest spanning out in front of you to the east.")
		if x == a:
				mystate = 6
		elif x == b:
				mystate = 1
		elif x == c:
				mystate = 10
		elif x == d:
				mystate = 12

	if mystate == 3:
		x = raw_input("A wide, dark, rushing river flows by in front of you from north to south.")
		if x == a:
				mystate = 1
		elif x == b:
				mystate = 7
		elif x == c:
				mystate = 11
		elif x == d:
				mystate = 13

	if mystate == 4:
		x = raw_input("An enormous volcano towers over you to the north, covering the sky with lava and ash in all directions.")
		if x == a:
				mystate = 10
		elif x == b:
				mystate = 11
		elif x == c:
				mystate = 8
		elif x == d:
				mystate = 1

	if mystate == 5:
		x = raw_input("You spy the entrance to a large, sandy desert to the south of you.")
		if x == a:
				mystate = 12
		elif x == b:
				mystate = 13
		elif x == c:
				mystate = 1
		elif x == d:
				mystate = 9

	if mystate == 6:
		x = raw_input("The forest expands in front of you in all directions. It seems to cover you in its dark leaves. A strange noise comes from the north.")
		if x == a:
				print "The woods are too thick to get through. You could probably get through with a tool."
		elif x == b:
				mystate = 2
		elif x == c:
				mystate = 14
		elif x == d:
				mystate = 17
	
	if mystate == 7:
		x = raw_input("You use a bridge to cross the river; however, you are blocked by large, unpassable mountains. West is not an option.")
		if x == a:
				mystate = 3
		elif x == b:
				print "Weren't you paying attention, you stupid idiot?"
		elif x == c:
				mystate = 15
		elif x == d:
				mystate = 16

	if mystate == 8:
		print "You proceed to climb the volcano; however, it's a freaking volcano. You are burned alive before you get a chance to choke to death on gases and ash."
		print "YOU DIED"
		break

	if mystate == 9:
		x = raw_input("You are surrounded by vast sands on all sides. A dried river bed flows from east to west.")
		if x == a:
				mystate = 21
		elif x == b:
				mystate = 20
		elif x == c:
				mystate = 5
		elif x == d:
				print "Huge gusts of wind blow up sand with great force. You cannot progress further south."

	if mystate == 10:
		x = raw_input("Large forestry blocks you to the north and east. You can hear a mixture of rumbling from the nearby volcano and an odd sound in the forest.")
		if x == a:
				print "You are blocked by heavy forest. The odd sound gets slightly louder."
		elif x == b:
				mystate = 4
		elif x == c:
				print "You are blocked by forest, but you spot a volcano rising in the distance."
		elif x == d:
				mystate = 2

	if mystate == 11:
		x = raw_input("A large river blocks your path to the north and west. There appears to be a bridge to the south.")
		if x == a:
				mystate = 4
		elif x == b:
				print "The river blocks your path. You can't Oregon Trail this sh*t."
		elif x == c:
				print "The river blocks your path, but you spot a volcano rising in the distance."
		elif x == d:
				mystate = 3

	if mystate == 12:
		x = raw_input("The field comes to an end, surrounded by forestry to the south and east. A large, singular tree dominates the others.")
		if x == a:
				print "The forest is too thick to pass by."
		elif x == b:
				mystate = 5
		elif x == c:
				mystate = 2
		elif x == d:
				print "The forest is too thick to pass by. There are traces of sand on the ground, blowing over the trees from the south."

	if mystate == 13:
		x = raw_input("A river flows into its bed, rising into high mountains to the south.")
		if x == a:
				mystate = 5
		elif x == b:
				print "The river is too fast to cross safely."
		elif x == c:
				mystate = 3
		elif x == d:
				print "The mountain range, covered in loose sand, barely blocks your path."

	if mystate == 14:
		x = raw_input("The strange noise becomes even louder than before. It sounds like some odd, shrill wailing.")
		if x == a:
				print "The shrubbery is much too thick to pass by."
		elif x == b:
				print "The forest is too thick to pass by."
		elif x == c:
				mystate = 22
		elif x == d:
				mystate = 6

	if mystate == 15:
		x = raw_input("The mountains appear to be getting larger, with some snowcapped peaks as well.")
		if x == a:
				print "The river blocks your path."
		elif x == b:
				print "The mountains are much too steep to cross."
		elif x == c:
				mystate = 23
		elif x == d:
				mystate = 7

	if mystate == 16:
		x = raw_input("You stumble across a mysterious clearing, fertilized well by the nearby river.")
		if x == a:
				print "The river is too fast to cross safely."
		elif x == b:
				print "The terrain is much too treacherous, a mixture of steep foothills and dense woods."
		elif x == c:
				mystate = 7
		elif x == d:
				mystate = 24

	if mystate == 17:
		x = raw_input("The forest gets even deeper as you venture further. One tree to the west is especially large.")
		if x == a:
				print "The forest is too dense, with no clear path to venture forth."
		elif x == b:
				print "The massive tree blocks your path. It's cool though."
		elif x == c:
				mystate = 6
		elif x == d:
				print "You see a dried lakebed on the other side of a small tree in your way. However, you haven't learned HMO1 Cut yet."

	if mystate == 18:
		print "You come across a bunch of howling werewolves in a clearing. You begin to realize that they were the sound but are immediately rekt."
		print "YOU DIED"
		break

	if mystate == 19:
		print "You are surrounded by snowy mountains. You slowly freeze to death and become a new scientific discovery 2000 years later."
		print "YOU DIED"
		break

	if mystate == 20:
		x = raw_input("The desert seems to stretch on forever to the west.")
		if x == a:
				mystate = 9
		elif x == b:
				mystate = 24
		elif x == c:
				print "Large mountains block your path."
		elif x == d:
				print "Big wind blowing sand in your face makes you feel like you don't want to go that way."

	if mystate == 21:
		x = raw_input("The dry riverbed leads to a big, deep, empty lake to the east. You can see something shiny at the bottom of the pit.")
		if x == a:
				mystate = 25
		elif x == b:
				mystate = 9
		elif x == c:
				print "Faraway forestry looks too hard to pass through."
		elif x == d:
				print "The lakebed is next to a huge, endless plot of sand. You attempt to traverse the desert but are led back to where you were before."
			
	if mystate == 22:
		x = raw_input("The noise is very ominous and very loud. The only further path leads west.")
		if x == a:
				print "The forest is thicker than your girlfriend. Good luck."
		elif x == b:
				mystate = 18
		elif x == c:
				print "The forest is thicker than your girlfriend. Good luck."
		elif x == d:
				mystate = 14

	if mystate == 23:
		x = raw_input("The snow gets thicker as you climb the mountains. The only clear way further is east.")
		if x == a:
				mystate = 19
		elif x == b:
				print "You don't want to fall down that big slope. Don't go west."
		elif x == c:
				print "The mountains are way too steep to climb."
		elif x == d:
				mystate = 7

	if mystate == 24:
		print "The desert never ends as you traverse onwards. You eventually pass out from heat stroke."
		print "YOU DIED"
		break

	if mystate == 25:
		print "The shiny object appears to be a mirror. As you stare into it, the light begins to fade, and you wake up in your normal bed. It was all a dream."
		print "Original, I know."
		print "YOU WIN"
		break