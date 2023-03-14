"""
Creating own game about Lviv
"""
class Character:
    """
    Creates character class
    """
    def __init__(self , name , description) -> None:
        """
        Initialization of class
        """
        self.name = name
        self.description = description
    
    def set_phrase(self , phrase):
        """
        Sets a phrase which character will say
        """
        self.phrase = phrase


class Enemy(Character):
    """
    Creates an enemy class after a character classs
    """
    def __init__(self, name, description ,health) -> None:
        """
        Initialization of class
        """
        super().__init__(name, description)
        self.health = health
    
    def set_weakness(self , weakness):
        """
        Sets a weakness for the enemy 
        """
        self.weakness = weakness

    def fight(self , obj):
        """
        Creates fight between user and enemy
        """
        if obj == self.weakness:
            return True
        return False
    

class Friend(Character):
    """
    Creates a friend class after character class
    """
    def __init__(self, name, description) -> None:
        """        
        Initialization of class
        """
        super().__init__(name, description)
    
    def set_help(self , help):
        """
        Sets a help which friend will provide
        """
        self.help = help   
        return self.help
    

class Pet(Friend):
    """
    Creates a class of pet after Friend class
    """
    def __init__(self, name, description) -> None:
        """
        Initialization of class
        """
        super().__init__(name, description)


class User:
    """
    Creates user class
    """
    def __init__(self , name) -> None:
        """       
        Initialization of class
        """
        self.lives = 1
        self.name = name
        self.damage = 1

    def add_to_backpack(self , itm):
        """
        Adds an item to abckpack of user
        """
        self.backpack.append(itm)


class Room:
    """
    Creates room class
    """
    def __init__(self , name) -> None:
        """
        Initialization of class
        """
        self.name = name
        self.possibible_ways = []
        self.inhabitants = []
        self.item = None

    def set_description(self , description):
        """
        Sets decription to class
        """
        self.description = description
        return None
    

    def set_character(self , character):
        """
        Sets a character for room
        """
        self.inhabitants.append(character)

    
    def link_room(self,room, way_of_world):
        """
        Links rooms between each other
        """
        self.possibible_ways.append((room , way_of_world))

    def set_item(self ,item):
        """
        Sets item for a room
        """
        self.item = item
    
    def move(self , way):
        """
        Shows if user changed room or not 
        """
        for i in self.possibible_ways:
            if i[1] == way:
                return i[0]

class Item:
    """
    Creates a class for all items
    """
    def __init__(self , name) -> None:
        """
        Initialization of class
        """
        self.name = name

    def set_description(self , desc):
        """
        Creates a description to an item
        """
        self.description = desc
    
class MedKit(Item):
    """
    Creates a medkit class after item class
    """
    def __init__(self, name) -> None:
        """
        Initialization of class
        """
        super().__init__(name)
        self.addhp = 0

    def give_hp(self , amount):
        """
        Sets how much additional health medkit will provide
        """
        self.addhp += amount

class Weapon(Item):
    """
    Creates a weapon class after item class
    """
    def __init__(self, name) -> None:
        """
        Initialization of class
        """
        super().__init__(name)

    def damage(self , dmg):
        """
        Sets how much damage this weapon has
        """
        self.damage = dmg

Kulpar = Room("Kulparkivska")
Kulpar.set_description('Long street which gets throught almost whole city')


Stry = Room('Stryiska')
Stry.set_description('A long old street')

Kozelnytska = Room('Kozelnytska')
Kozelnytska.set_description('A street where UKU is located')

Center = Room('Center')
Center.set_description('An old part of city')

Zamok = Room('Vysokyy Zamok')
Zamok.set_description('The highest point in Lviv')


Kulpar.link_room(Stry , 'north')
Kulpar.link_room(Center ,'south')
Stry.link_room(Kozelnytska , 'west')
Stry.link_room(Center, 'east')
Stry.link_room(Kulpar  ,'south')
Center.link_room(Stry , 'west')
Center.link_room(Kulpar , 'north')
Kozelnytska.link_room(Stry , 'east')
Zamok.link_room(Center , 'north')  
Center.link_room(Zamok , 'south')

uni = Pet('Uni' , 'A magic creature which gives you 2 additional lives')
drag = Pet('Drag' , "Dragon which gives you 2 additional damage")
phoenix = Pet('Phoenix' , 'A creature which gives you 1 additional life and one additional damage')  

Oggy = Friend("Oggy" , "A blue cat who can help you")
Jack = Friend('Jack' , 'A green cat who is ready to help you')

Oggy.set_help("I would highly reccommend visit UCU to find something that can help you with boss")
Jack.set_help('To win this character you should discover Center')

Chuba = Enemy('Chugaister' , "A monseter who kills mavkas. Knives can't do anything to him, the only thing he is afraid of is water." , 3)
Chuba.set_weakness('Water')
Chuba.set_phrase("What you have for me today?")
Perun = Enemy('Perun' , 'An ancient God of Thunder' , 15)
Perun.set_phrase("You are not worthy to live here")
Bandit = Enemy('Bandit' , "He doesn't wish you anything good , but if you have a knife..." , 7)
Bandit.set_weakness('Knife')
Bandit.set_phrase('Give me your money')

kit = MedKit('medkit')
kit.set_description("Gives additional hp")
kit.give_hp(1)

water = Item('Water')
water.set_description('It might be useful against Chuba')

knife = Item('Knife')
knife.set_description('This item may help you with bandit')

pistol = Weapon('pistol')
pistol.set_description('A dangerous and useful weapon')
pistol.damage(5)

lightning = Weapon('lightning')
lightning.set_description("It is said that this weapon can even kill Perun")
lightning.damage(15)
weapons = {'pistol' : 5, 'lightning' : 15}

Zamok.set_character(Oggy)
Zamok.set_character(Perun)
Kulpar.set_character(Chuba)
Kozelnytska.set_character(Jack)
Kozelnytska.set_character(Bandit)

Zamok.set_item(kit)
Kozelnytska.set_item(lightning)
Stry.set_item(water)
Kulpar.set_item(knife)
Center.set_item(pistol)

if __name__ == "__main__":
    print('Enter your name')
    name = input('> ')
    user= User(name)
    print(f'Hello, {user.name}')
    print('I am Howard and I will be your guide in this journey')
    print('There are the following commands possible in this game:')
    print('help - works if a friend is in this room ')
    print('fight - works if an enemy is in room')
    print('take - works if an item is in room')
    print('talk - you can have a conversation with enemy')
    print('also you can move by choosing sides of world [north , south , east, west]\n')
    print('First of all you have to choose a pet')
    print('Here are possible options:')
    print(f'{uni.name} - {uni.description}')
    print(f'{drag.name} - {drag.description}')
    print(f'{phoenix.name} - {phoenix.description}')
    pet = input('> ')
    pet_option = False
    while pet_option == False:
        if pet in ['Uni' , 'Drag' , 'Phoenix']:
            print('Your pet is ' + pet)
            pet_option = True
        else:
            print("I don't understand " + pet)
            pet = input('> ')
    if pet == "Uni":
        user.lives +=2
    elif pet == "Drag":
        user.damage +=2
    elif pet == 'Phoenix':
        user.damage +=1
        user.lives +=1
    
    current_room = Kulpar
    backpack = []

    dead = False

    while dead == False:

        print("\n")
        print(current_room.name)
        print('--------------------')
        print(current_room.description)
        for i in current_room.possibible_ways:
            print(f'{i[0].name} is {i[1]}')
        for i in current_room.inhabitants:
            print(f'{i.name} is here! - {i.description}')

        inhabitants = current_room.inhabitants
        enemy_check = False
        helper = False

        item = current_room.item
        if item is not None:
            print(f'The [{item.name}] is here - {item.description}')

        command = input("> ")

        if command in ["north", "south", "east", "west"]:
            # Move in the given direction
            current_room = current_room.move(command)
        elif command == "talk":
            # Talk to the inhabitant - check whether there is one!
            for i in inhabitants:
                if isinstance(i , Enemy):
                    print(i.phrase)
            else:
                print('There is no enemy to speak with')
        elif command == 'help':
            for i in inhabitants:
                if isinstance(i , Friend):
                    print(i.help)
                    helper = True
            if helper == False:
                print('Unfortunitely, noone in this room can help you')
        elif command == "fight":
            for i in inhabitants:
                if isinstance(i , Enemy):
                    enemy_check = True
                    inhabitant = i
                    break
            if enemy_check == True:
                # Fight with the inhabitant, if there is one
                print('Don\'t forget, that some enemies can be defeated as wtih brute forse as by finding their weakness')
                print("What will you fight with?")
                print(f'You can choose between {backpack}')
                fight_with = input('> ')
                if inhabitant.name == 'Perun':
                    if fight_with in weapons:
                        user.damage += weapons[fight_with]
                        if user.damage > inhabitant.health:
                            print('Congratulations, you have won the fight against Boss, the game is over!')
                            dead = True
                        else:
                            print('You lost the fight and all of your lives, game is over')
                            dead =True
                # Do I have this item?

                elif fight_with in backpack and fight_with not in weapons:
                        if inhabitant.fight(fight_with) == True:
                            # What happens if you win?
                            print("Hooray, you won the fight!")
                            current_room.inhabitants.remove(inhabitant)
                        else:
                            # What happens if you lose?
                            print("Oh dear, you lost the fight.")
                            user.lives -= 1
                            print(f'You have {user.lives} lives left')
                            if user.lives == 0:
                                print('This is the end of your road, but you can try again')
                                dead = True
                elif fight_with in weapons:
                    user.damage += weapons[fight_with]
                    if user.damage > inhabitant.health:
                        print('Congratulations, you won the fight')
                        current_room.inhabitants.remove(inhabitant)
                    else:
                        print("Oh dear, you lost the fight.")
                        user.lives -= 1
                        print(f'You have {user.lives} lives left')
                        if user.lives == 0:
                            print('This is the end of your road, but you can try again')
                            dead = True
                else:
                    print("You don't have a " + fight_with)
            else:
                print("There is no one here to fight with")
        elif command == "take":
            if item is not None and item.name != 'medkit':
                print("You put the " + item.name + " in your backpack")
                backpack.append(item.name)
                current_room.item = None
            elif item is not None and item.name == 'medkit':
                print('Medkit added you one extra life')
                current_room.item = None
            else:
                print("There's nothing here to take!")
        else:
            print("I don't know how to " + command)
