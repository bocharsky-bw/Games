# RPG/Adventure game

print "\n\t\t\t\t******"
print "\tYou are about to play captivating adventure game with two different branches, "
print "\tmultiple death options and a hidden surpize!"
print "\t\t\t\t******"

print "\n\t--------------------------------------"
print "\tTo play the game put numbers as answers."
print "\t--------------------------------------\n"
print "You wake up amids a dark wood with no memories of the last 8 hours."
print 'You dressed in medieval clothing and find a sword and a bow lying on the',\
'ground next to you\n'

name = raw_input("Type in your name here ---> ")

print "\nYou pick up weapons and some vague memories coming back to you..."
raw_input("Continue...")
print "\nYou remember doing Lord of The Rings cosplay with Oleksii yesterday..."
print "But your thoughts are suddenly interrupted by some noise from your left."
raw_input("Continue...")
print "\nYou turn left and see a... goblin?!\n"
raw_input("Continue...")
print "\nYour actions: "
print "1. Kill the creature with the sword!"
print "2. 'Ok guys, I get it, we play LOTR recreation in the wood." 
print "But your costume is so realistic...' "
print "3. Seduce.\n"

act = raw_input("---> ")

# 1st main branch
if act == "1":
	print "The goblin wasn't expecting you to attack, you kill him with one blow!"
	raw_input("Continue...")
	print "\nTwo other goblins saw what you just did." 
	print "They are rushing at you!"
	raw_input("Continue...")
	print "\nYour actions: "
	print "1. Charge to melee combat with the beasts, shouting 'For Winterfell!'."
	print "2. Charge to melee combat with the beasts, shouting 'For Rohan!'"	
	print "3. Shoot down one goblin with the arrow and face another one with the sword!"
	
	actv1 = raw_input("---> ") #action violent
	
	if actv1 == "1" or actv1 == "2":
		print "\nShouting does give you some attack bonus."
		print "Alas, while running towards goblins you trip and fall."
		raw_input("Continue...")
		print "\nThe beasts defeat you easily. You lost. Well, that was fast!"
		# ending	
	else:
		print "\nYou put all the strengths in the shot. Arrow hits one goblin right in the head."
		raw_input("Continue...")
		print "\nNow you are in a close combat with the other beast."
		raw_input("Continue...")
		print "\nYou: "
		print "1. Remember all the experience you obtained while trying to push in marshrutka "
		print "every day."
		print "2. Have a quick flashback to the times when you were a kid and played sticks,"
		print "pretending they were swords."
		print "3. Remember how you played 'Skyrim' and persuade yourself you are level 48 in"
		print "sword fights."
		
		actv2 = raw_input("---> ")
		
		if actv2 == "2" or actv2 == "3":
			print "That was not enough. Goblin slashes you to pieces."
			print "You lost! Come on, put it together!"
			# ending			
		else: 
			print "\nIn close combat you push the opponent as hard as you would push in marshrutka."
			raw_input("Continue...")
			print "\nHe falls under your mighty powers. You cut him through!"
			raw_input("Continue...")
			print "\nYou find a bag that was dropped by one of the goblins."
			print "Inside you find what looks like enchantment stones! And... a map!"
			raw_input("Continue...")
			print "\nYou study the map and realize where the goblins camp is."
			print "There should be answers there."
			raw_input("Continue...")
			print "\nYou walk trhough the forest to the camp."
			raw_input("Continue...")
			print "\nAfter an hour of walking you see two goblins on the passage ahead of you."
			raw_input("Continue...")
			print "\nIt looks like it's there is no other way to the camp."
			raw_input("Continue...")
			print "\nYour actions: "
			print "1. Use duct tape to combine enchantment stones you found earlier with your sword."
			print "Then attack with powerful weapon!"
			print "2. Make a bird sound to distract them and try to slip through."
			print "3. Attack them while they are unprepared."
			
			actv3 = raw_input("---> ")
			
			if actv3 == "1":
				print "\nThat was one of the stupidest decisions you've made so far, %s." % name
				raw_input("Continue...")
				print "\nThe weapon becomes more heavy and you can't fight properly."
				print "Not that you could fight properly before."
				raw_input("Continue...")
				print "\nGoblins cut through you. Nice job!"
				# ending
			elif actv3 == "2":
				print "\nYou are not a great bird sounds maker."
				raw_input("Continue...")
				print "\nYes, %s, you are right. Goblins slash you. Nice job!" % name
				# ending
			else:
				print "\nCreatures don't expect you coming."
				print "You easily kill one goblin, then cut though the throat of another."
				print "Blood is everywhere."
				raw_input("Continue...")
				print "\nYou hear someone coming from behind."
				print "There is another goblin!"
				raw_input("Continue...")
				print "\nThe creature yells 'What have you done, %s?!'" % name 
				raw_input("Continue...")
				print "\nBut you are in a blood fury. You are scared and can't control yourself."
				raw_input("Continue...")
				print "\nYou put your sword through the goblin."
				print "He falls dead."
				raw_input("Continue...")
				print "\nYou are shocked that he knows your name!"
				print "You take some time to adjust to what just happened."
				raw_input("Continue...")
				print "\n'He knew my name!' - you think. There definitely should be answers in the camp."
				print "\nAfter you recovered you contunie your jorney to the camp."
				raw_input("Continue...")
				print "\nYou travel for some time through the woods."
				print "Suddenly a squirrel jumps on the road in front of you."
				raw_input("Continue...")
				print "\nThere is something weird about it..."
				raw_input("Continue...")
				print "\nIt has red eyes! And a little dagged in its paws. -_- "
				raw_input("Continue...")
				print "\nThe squirrel talks to you:"
				print "'No time to explain! Help us save our friend! We need a blood sacrifice!'"
				print "Help us!"
				raw_input("Continue...")
				print "\nYour actions: "
				print "1. Its only a small squirrel. Even though it can talk! What can it do to me?"
				print "Kick it and continue your jorney."
				print "2. The squirrels are important part of ecosystem. Plus they are cute."
				print "Help the poor thing."
				
				actv4 = raw_input("---> ")
				
				if actv4 == "1":
					print "\nYou hear squirrel say: 'Ok, motherfucker! You brought it on yourself!'"
					print "'One way or another I will have my blood sacrifice!'"
					raw_input("Continue...")
					print "\nSquirrel jumps at you and stubs you in the leg."
					raw_input("Continue...")
					print "\nYou feel that there are tens of squirrels jumps at your back."
					print "They all stab you with the small daggers."
					raw_input("Continue...")
					print "\nYou are dead."
					print "Moral: always help those who are in need."
					print "Oh, by the way, they saved their squirrel pal."
					# ending
				else:
					print "\nEven if it all feels weird you agree to help."
					print "You have fought goblins today! What could be worse?"
					raw_input("Continue...")
					print "\nRight?"
					raw_input("Continue...")
					print "\nYou follow red-eyed squirrel."
					print "\nSoon you see some kind of an altar."
					raw_input("Continue...")
					print "\nYou do what you are asked: you cut your hand and spill some blood on the altar."
					raw_input("Continue...")
					print "\nThe squirrel that brought you here says:"
					print "\n'Thank you for the help. Our friend will recover now.'"
					raw_input("Continue...")
					print "\n'I guess you are looking for creatures like you. I saw one in the goblins camp.'"
					print "'I can show a shortcut.'"
					raw_input("Continue...")
					print "\nYou follow the trail that was shown by that crazy squirrel."
					print "After some time the forest becomes less thick. You see mountains."
					raw_input("Continue...")
					print "\nSuddenly a deafening screech catches your attention."
					raw_input("Continue...")
					print "\nYou lift your head and see... A huge Dragon!"
					raw_input("Continue...")
					print "\nYou are shocked and can not move for some time."
					print "Then you see goblins rushing to fight the Dragon. And..."
					raw_input("Continue...")
					print "\nAnd together with them you see Oleksii!"
					raw_input("Continue...")
					print "\nA sudden realization comes to you:"
					print "'Were I fighting the allies all this time?!'"
					raw_input("Continue...")
					print "\nWhile you stand there shocked the Dragon shoots multiple huge fireballs."
					print "\nYou see an enormous explosion. The shockwave reaches you."
					print "You lose consciousness."
					raw_input("Continue...")
					print "\nYou wake up in a bed, covered in sweat. You wonder if it all was a dream." 
					print "A very realistic dream."
					raw_input("Continue...")
					print "\nThe next day you stop by to visit Oleksii, but he is not at home."
					print "His cell doesn't reply. That's weird."
					raw_input("Continue...")
					print "\nSo was it really just a dream? or... "
					# ending

# 2nd main branch
else:
	if act == "2":
		print "\nTwo other goblins come from behind and strike you with something blunt!"
		print "You are on the ground. Goblins tie your hands and kick you a bit."

	elif act == "3":
		print "\nWell, yes, %s, you are very sexy! But not for goblins." % name
		print "Two other goblins come from behind and tie yor hands."
	raw_input("Continue...")
	print "\nThen creatures drag you through the woods for some time." 
	print "The forest becomes less thick. You see mountains."
	raw_input("Continue...")
	print "\nFinally they bring you to what looks like their camp."
	print "\n'Que pasa? Who is this?' - shouting one of the chiefs"
	raw_input("Continue...")
	print "\nYour reaction:"
	print "1. Hey cabron! Let me go! I won't play your stupid games anymore!"
	print "2. Seduce"

	actn1 = raw_input("---> ") #action normal

	if actn1 == "1":
		print "\n'Ahh! This is you, %s! Long time no see. Shut up and follow me.'" % name
	elif actn1 == "2":
		print "\nChief goblin looks at you from bottom to top. Then says:"
		print "'You are one handsome human, %s. But we have more urgent matters to talk about'" % name
	
	raw_input("Continue...")
	print "\nYou are quite surprised that THIS THING knows your name. And speaks English."
	raw_input("Continue...")
	print "\nYou say: "
	print "1. 'This is not the human you are looking for.'"
	print "2. 'Valar Morghulis.'"

	actn2 = raw_input("---> ")

	if actn2 == "1":
		print "\n'%s, this is not some Star Wars fans gathering. This is real.'" % name
	elif actn2 == "2":
		print "\n'Valar Dohaeris. Yeah, I like this show as well, %s. But THIS is real'" % name

	raw_input("Continue...")
	print "\nThe chief goblin unties you and you folow him though the camp."
	print "\n'I see, you don't remember what has happened... And It is no wonder, you were hit badly.'"
	raw_input("Continue...")
	print "\n'No time to explain. Long story short, you and Oleksii opened a portal to the other worlds.'"
	raw_input("Continue...")
	print "\n'You two were doing some kind of a cosplay and thought it would be fun to copy "
	print " one of the rituals from the book Oleksii found somewhere...'"
	print "'So, after that...'"

	print "\nHis speech is interrupted by the deafening screech."
	raw_input("Continue...")
	print "\nYou both lift your heads and see... A huge dragon!"
	raw_input("Continue...")
	print "\nYour reaction: "
	print "1. 'I forgot to switch off my stove. See ya!'"
	print "2. 'Mother of Dragons...'"
	print "3. Seduce."

	actn3 = raw_input("---> ")

	if actn3 == "1":
		print "\n'Another direction, weirdo! Follow me!' *runs* "
	elif actn3 == "2":
		print "\n'Neeerd! Follow me!' *runs* "
	elif actn3 == "3":
		print "\nSeriously? -_- "

	raw_input("Continue...")
	print "\nYou run after goblin chief to some cave nearby."
	raw_input("Continue...")
	print "\nWhen you are inside you see... Oleksii!"
	raw_input("Continue...")
	print "\nYour reaction:"
	print "1. Give him a long silent hug."
	print "2. 'Oleksii! What the hell is going on?!! This joke is not fun anymore!'"
	print "3. Seduce."

	actn4 = raw_input("---> ")

	if actn4 == "1":
		print "\nHe hugs you back. You stand in silence."
		print "The chief goblin coughs and says: 'ehmm... the Dragon?'"
	elif actn4 == "2":
		print "\n'Come on, %s! Goblins, dragons, this is fuuun!'" % name
		
	# secret branching
	elif (actn4 == "3" and act == "3" and actn1 == "2" and actn3 == "3"):
		print "\nYou are one sexy hottie, %s." % name 
		print "Come and claim your prize!"
		raw_input("Continue...")
		print "Follow the link http://www.dailyfundose.com/wp-content/uploads/2010/08/88.jpg"
		
	elif actn4 == "3":
		print "\nOleksii looks deep into your eyes for some time. Then says: "
		print "This is not the right time."

	raw_input("Continue...")
	print "\n'Oh, by the way, %s, we would have to fight this Dragon.'" % name
	print "'Choose your weapon:'"
	raw_input("Continue...")
	print "\nYou choose:"
	print "1. Magic staff" 
	print "2. Valyrian sword"
	print "3. Seducing outfit. It's killingly sexy!"

	actn5 = raw_input("---> ")

	if actn5 == "1":
		print "\n'Cheater! So I would have to run in a close battle with the beast now! Great!'"
		raw_input("Continue...")
		print "\nAfter quickly discussing the strategy you come out the cave to encounter the Dragon"
		raw_input("Continue...")
		print "\nWhile others rushed towards the Dragon, you start casting a spell."
		print "You chant:"
		print "1. 'Ahalai mahalai'"
		print "2. 'Expectus patronus!'"
		print "3. 'Fus Ro Da!'"

		spell = raw_input("---> ")

		if spell == "1":
			print "\nYou failed to cast a spell. The Dragon eats all of you."
			print "\nGreat job!"
			# ending
			
		elif spell == "2" or spell == "3":
			print "\nYou cast a very powerful magic on the Dragon and it helps your allies defeat it."
			raw_input("Continue...")
			print "\nThough, the Dragon gathers his last strength and shootes a huge fireball."
			raw_input("Continue...")
			print "\nYou see an enormous explosion. The shockwave reaches you."
			print "You lose consciousness."
			raw_input("Continue...")
			print "\nYou wake up in a bed, covered in sweat. You wonder if it all was a dream." 
			print "A very realistic dream."
			raw_input("Continue...")
			print "\nThe next day you stop by to visit Oleksii, but he is not at home."
			print "His cell doesn't reply. That's weird."
			raw_input("Continue...")
			print "\nSo was it really just a dream? or... "
			# ending
			
	elif actn5 == "2":
		print "\n'We are not in Westeros, but it'll do.'"
		print "\nAfter quickly discussing the strategy you come out the cave to encounter the Dragon"
		raw_input("Continue...")
		print "\nYou run with the goblins towards the Dragon."
		raw_input("Continue...")
		print "\nYou see as Oleksii casts a a very powerful magic on the Dragon."
		print "The Dragon is now grounded."
		raw_input("Continue...")
		print "\nThe goblins and you charge!"
		raw_input("Continue...")
		print "\nYour actions: "
		print "1. Run towards his head and put the sword through his eye!"
		print "2. Tell goblins to distract the Dragon and open his belly with the sword!"
		print "3. 'My watch is over.' Run away screaming like a 6-years old girl. "
		
		sword = raw_input("---> ")
		
		if sword == "1" or sword == "3":
			print "\nThe flames from the Dragon's maw consume you."
			print "You are burnt to ashes. The whole party is dead. Nice job!"
			# ending
		
		else:
			print "\nWhile goblins distracted the Dragon you rush towards him from the right."
			raw_input("Continue...")
			print "\nNow you have the perfect chance! You strike the Dragon from the bottom!"
			raw_input("Continue...")
			print "\nThe Gragon falls."
			raw_input("Continue...")
			print "\nBut you notice that the Dragon gathers his last strength and shootes a huge fireball."
			raw_input("Continue...")
			print "\nYou see an enormous explosion. The shockwave reaches you."
			print "You lose consciousness."
			raw_input("Continue...")
			print "\nYou wake up in a bed, covered in sweat. You wonder if it all was a dream." 
			print "A very realistic dream."
			raw_input("Continue...")
			print "\nThe next day you stop by to visit Oleksii, but he is not at home."
			print "His cell doesn't reply. That's weird."
			raw_input("Continue...")
			print "\nSo was it really just a dream? or... "
			# ending 
		
	elif actn5 == "3":
		print "\nThis looks killing on you! But grab the magic staff. Just in case."
		raw_input("Continue...")
		print "\nAfter quickly discussing the strategy you come out the cave to encounter the Dragon"
		raw_input("Continue...")
		print "\nWhile others rushed towards the Dragon, you start casting a spell."
		print "You chant:"
		print "1. 'Ahalai mahalai'"
		print "2. 'Expectus patronus!'"
		print "3. 'Fus Ro Da!'"
		
		spell = raw_input("---> ")

		if spell == "1":
			print "\nYou failed to cast a spell. The Dragon eats all of you."
			print "\nGreat job!"
			# ending
			
		elif spell == "2" or spell == "3":
			print "\nYou cast a very powerful magic on the Dragon and it helps your allies defeat it."
			raw_input("Continue...")
			print "\nThough, the Dragon gathers his last strength and shootes a huge fireball."
			raw_input("Continue...")
			print "\nYou see an enormous explosion. The shockwave reaches you."
			print "You lose consciousness."
			raw_input("Continue...")
			print "\nYou wake up in a bed, covered in sweat. You wonder if it all was a dream." 
			print "A very realistic dream."
			raw_input("Continue...")
			print "\nThe next day you stop by to visit Oleksii, but he is not at home."
			print "His cell doesn't reply. That's weird."
			raw_input("Continue...")
			print "\nSo was it really just a dream? or... "
			# ending
		
	# There should be nothing after this line 
	
