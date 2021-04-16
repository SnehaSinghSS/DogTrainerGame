import random

class Cat:
  def __init__(self):
    self.health = random.randint(100,110)
    self.strength = random.randint(5,10)
    self.defense = random.randint(5, 10)
    self.speed = random.randint(5,10)

  def get_stats(self):
    print("\nCAT")
    print("Health: " + str(self.health))
    print("Attack: " + str(self.strength))
    print("Defense: " + str(self.defense))
    print("Speed: " + str(self.speed))

  def take_damage(self, damage):
    self.health -= damage

  def attempt_dodge(self,opponent):
    if(self.speed > opponent.speed):
      return True
    else:
      return False

  def attack(self, opponent):
    damageDealt = abs(self.strength - opponent.defense)
    if not opponent.attempt_dodge(self):
      opponent.take_damage(damageDealt)
    else:
      opponent.take_damage(damageDealt/2)

  def is_alive(self):
    if self.health > 0:
      return True
    else:
      return False

  def build_strength(self):
    self.strength += 2
    print("\nThe CAT's strength went up!")

  def build_speed(self):
    self.speed += 2
    print("\nThe CAT's speed went up!")

  def build_defense(self):
    self.defense += 1
    print("\nThe CAT's defense went up!")

  def action(self, opponent):
    r = random.randint(0, 4)
    if r == 0:
      self.build_strength()
    elif r == 1:
      self.build_defense()
    elif r == 2:
      self.build_speed()
    else:
      self.attack(opponent)
      print("\nThe CAT attacked!")



class Dog:
  def __init__(self, name, breed):
    self.name = name
    self.breed = breed
    self.health = 100
    self.strength = 10
    self.defense = 5
    self.speed = 10

  def get_stats(self):
    print("\n" + self.name.upper() + " THE " + self.breed.upper())
    print("Health: " + str(self.health))
    print("Strength: " + str(self.strength))
    print("Defense: " + str(self.defense))
    print("Speed: " + str(self.speed))

  def take_damage(self, damage):
    self.health -= damage

  def attempt_dodge(self,opponent):
    if(self.speed > opponent.speed):
      return True
    else:
      return False

  def attack(self, opponent):
    damageDealt = abs(self.strength - opponent.defense)
    if not opponent.attempt_dodge(self):
      opponent.take_damage(damageDealt)
    else:
      opponent.take_damage(damageDealt/2)

  def is_alive(self):
    if self.health > 0:
      return True
    else:
      return False

  def build_strength(self):
    self.strength += 2
    print("\n" + self.name.upper() + "'s strength went up!")

  def build_speed(self):
    self.speed += 2
    print("\n" + self.name.upper() + "'s speed went up!")

  def build_defense(self):
    self.defense += 1
    print("\n" + self.name.upper() + "'s defense went up!")

  def action(self, opponent):
    r = random.randint(0, 4)
    if r == 0:
      self.build_strength()
    elif r == 1:
      self.build_defense()
    elif r == 2:
      self.build_speed()
    else:
      self.attack(opponent)
      print("\n" + self.name.upper() + " attacked!")



class Arena:
    def __init__(self, Dog, Cat):
        self.dog = Dog
        self.cat = Cat
    def battle(self):
        strength = self.dog.strength
        defense = self.dog.defense
        speed = self.dog.speed
        round = 1
        while self.dog.is_alive() and self.cat.is_alive():
            print("\nROUND " + str(round))

            self.dog.action(self.cat)
            self.cat.action(self.dog)
            self.cat.get_stats()
            self.dog.get_stats()
            if not self.cat.is_alive():
              print("\n" + self.dog.name.upper() + " is the winner!")
              self.dog.strength = strength + 2
              self.dog.defense = defense + 2
              self.dog.speed = speed + 2
              sentence = self.dog.name + "'s "
              if self.dog.strength >= 15 or self.dog.defense >= 15 or self.dog.speed >= 15:
                self.dog.strength = 15
                self.dog.defense = 15
                self.dog.speed = 15
                if self.dog.strength >= 15:
                  sentence += "strength is at FULL capacity, "
                else:
                  sentence += "strength has increased by 2, "
                if self.dog.defense >= 15:
                  sentence += "defense is at FULL capacity, "
                else:
                  sentence += "defense has increased by 2, "
                if self.dog.speed >= 15:
                  sentence += "and speed is at FULL capacity!"
                else:
                  sentence += "and speed has increased by 2!"
              else:
                sentence += "strength, defense, and speed have all gone up by 2!"
              print("\n" + sentence)
              break
              
            elif not self.dog.is_alive():
              print("\nOH NO! The CAT is the winner! " + self.dog.name + " has died!")
              if not self.dog.name == "dEaD":
                self.dog.name = "dEaD"
              else:
                self.dog.name = "ded"

              break
            input("Press enter for next round")
            round += 1
        



class DogTrainer:
    def __init__(self, name):
      self.name = name

      self.dogList = [Dog("Star", "Chihuahua")]
      self.actionsLeft = 3
      self.day = 0

    def fight_with_a_cat(self):
      cat = Cat()
      cat.get_stats()
      for a in self.dogList:
        a.get_stats()
      fighterDog = input("\nType the name of the dog you want to fight with: ")
      chosen = False
      for a in self.dogList:
        if a.name.lower() == fighterDog.lower():
          nameBefore = a.name
          chosen = True
          arena = Arena(a, cat)
          arena.battle()
          if a.name != nameBefore:
              self.dogList.remove(a)
          
      while chosen == False:
        fighterDog = input("\nI'm sorry, I didn't get that. Type the name of the dog you want to fight with: ")
        for a in self.dogList:
          if a.name.lower() == fighterDog.lower():
            nameBefore = a.name
            chosen = True
            arena = Arena(a, cat)
            arena.battle()
            if a.name != nameBefore:
              self.dogList.remove(a)
          
        
      


    def play_with_a_dog(self):
      if len(self.dogList) == 0:
        print("\nNO DOGS TO PLAY WITH")
        self.actionsLeft += 1
      else:
        for a in self.dogList:
          a.get_stats()
        whichDog = input("\nType the name of the dog that you want to play with and click enter!: ")
        chosen = False
        for a in self.dogList:
          if a.name.lower() == whichDog.lower():
            chosen = True
            a.speed += 1
            a.defense += 1
            if a.speed >= 15 and a.defense >= 15:
              a.speed = 15
              a.defense = 15
              print("\n" + a.name + "'s speed and defense are at FULL capacity!")
            elif a.speed >= 15 and a.defense < 15:
              a.speed = 15
              print("\n" + a.name + "'s speed is at FULL capacity and defense went up by 1!")
            elif a.defense >= 15 and a.speed < 15:
              a.defense = 15
              print("\n" + a.name + "'s defense is at FULL capacity and speed went up by 1!")
            else:
              print("\n" + a.name + "'s defense and speed went up by 1!")
            
        while chosen == False:
          whichDog = input("\nI'm sorry, I didn't get that. Type the name of the dog that you want to play with and click enter!: ")
          for a in self.dogList:
            if a.name.lower() == whichDog.lower():
              chosen = True
      

    def find_a_dog(self):
      chance = random.randint(0,10)
      if(chance <= 2 and len(self.dogList) <= 4):
        twice = True
        while(twice):
          dogBreedChance = random.randint(1,7)
          if dogBreedChance == 1:
            dogBreed = "Golden Retriever"
            twice = False
            for a in self.dogList:
              if(a.breed == dogBreed):
                twice = True
          elif dogBreedChance == 2:
            dogBreed = "Goldendoodle"
            twice = False
            for a in self.dogList:
              if(a.breed == dogBreed):
                twice = True
          elif dogBreedChance == 3:
            dogBreed = "Poodle"
            twice = False
            for a in self.dogList:
              if(a.breed == dogBreed):
                twice = True
          elif dogBreedChance == 4:
            dogBreed = "Russel Terrier"
            twice = False
            for a in self.dogList:
              if(a.breed == dogBreed):
                twice = True
          elif dogBreedChance == 5:
            dogBreed = "Labradoodle"
            twice = False
            for a in self.dogList:
              if(a.breed == dogBreed):
                twice = True
          elif dogBreedChance == 6:
            dogBreed = "Multese"
            twice = False
            for a in self.dogList:
              if(a.breed == dogBreed):
                twice = True
          elif dogBreedChance == 7:
            dogBreed = "Bichon Fraise"
            twice = False
            for a in self.dogList:
              if(a.breed == dogBreed):
                twice = True
          elif dogBreedChance == 8:
            dogBreed = "Bichpoo"
            twice = False
            for a in self.dogList:
              if(a.breed == dogBreed):
                twice = True
          elif dogBreedChance == 9:
            dogBreed = "Pomeranian"
            twice = False
            for a in self.dogList:
              if(a.breed == dogBreed):
                twice = True
          else:
            dogBreed = "Cocker Spaniel"
            twice = False
            for a in self.dogList:
              if(a.breed == dogBreed):
                twice = True
        wantIt = input("\nYou found a " + dogBreed.upper() + "! Do you want to take him in? Remember that you can only have 5 dogs at a time!: ")
        if (wantIt.lower() == "yes"):
          name = input("\nWhat are you going to name your new furry friend? ")
          print("\nThat's a great name!")
          self.dogList.append(Dog(name, dogBreed))
        elif(wantIt.lower() == "no"):
           print("\n Okay!")
        else:
          confused = True
          while confused:
            wantIt = input("\nI'm sorry, I don't understand. Do you want to take him in? Remember that you can only have 5 dogs at a time!: ")
            if (wantIt.lower() == "yes"):
              name = input("\nWhat are you going to name your new furry friend? ")
              print("\nThat's a great name!")
              self.dogList.append(Dog(name, dogBreed))
              confused = False
            elif(wantIt.lower() == "no"):
              print("\n Okay!")
              confused = False
            else:
              confused = True
        self.actionsLeft -= 1
      elif (len(self.dogList) <= 4):
        print("\nI'm sorry, no dogs found this time!")
        self.actionsLeft -= 1
      else:
        print("\nYour number of dogs is at FULL capacity!")
  
    def feed_dogs(self):
      if len(self.dogList) == 0:
        print("\nNO DOGS TO FEED")
        self.actionsLeft += 1
      else:
        for a in self.dogList:
          a.health += 20
          if (a.health >= 100):
            a.health = 100
            print("\n" + a.name + "'s health is at FULL capacity!")
          else:
            print("\n" + a.name + "'s health is at " + str(a.health) + ".")

    def new_day(self):

      keepPlaying = True
      while keepPlaying:
        self.day += 1
        self.actionsLeft = 3
        print("\nDay "+ str(self.day) + "! Good Morning, " + self.name + "!")
        
        while self.actionsLeft > 0:
          
          print("\nWhat would you like to do? You have " + str(self.actionsLeft) + " actions left.\n1. Look for a dog\n2. Feed your dogs\n3. Fight a cat\n4. Play with one of your dogs\n5. Look at my dog stats (Does not take up an action)")
          number = input("\nType the number next to what you want to do and click enter!: ")
          if number == "1":
            self.find_a_dog()
          elif number == "2":
            self.feed_dogs()
            self.actionsLeft -= 1
          elif number == "3":
            self.fight_with_a_cat()
            self.actionsLeft -= 1
          elif number == "4":
            self.play_with_a_dog()
            self.actionsLeft -= 1
          elif number == "5":
            if len(self.dogList) == 0:
              print("\nNO DOGS AVAILABLE!")
            else:
              for a in self.dogList:
                a.get_stats()
          else:
            confused = True
            while confused:
              number = input("\nI'm sorry, I didn't understand. Type the number next to what you want to do and click enter!: ")
              if number == "1":
                self.find_a_dog()
                confused = False
              elif number == "2":
                self.feed_dogs()
                self.actionsLeft -= 1
                confused = False
              elif number == "3":
                self.fight_with_a_cat()
                self.actionsLeft -= 1
                confused = False
              elif number == "4":
                self.play_with_a_dog()
                self.actionsLeft -= 1
                confused = False
              elif number == "5":
                if len(self.dogList) == 0:
                  print("\nNO DOGS AVAILABLE!")
                else:
                  for a in self.dogList:
                    a.get_stats()
                confused = False
              else:
                confused = True
      
        play = input("\nDay " + str(self.day) + " over. Do you want to keep playing?: ")
        if play == "yes":
          keepPlaying = True
        elif play == "no":
          keepPlaying = False
          print("sure")
        else:
          confused = True
          while confused:
            play = input("\nI'm sorry, I didn't get that. Do you want to keep playing?: ")
            if play == "yes":
              keepPlaying = True
              confused = False
            elif play == "no":
              keepPlaying = False
              confused = False
            else:
              confused = True
      print("\nGoodbye! Start a new game soon!")


playerName = input("\nHello, Player. What is your name?: ")
trial = DogTrainer(playerName)
trial = DogTrainer(playerName)
trial.new_day()