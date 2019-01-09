# The template for the story

STORY = "This morning %s woke up feeling %s. 'It is going to be a %s day!' Outside, a bunch of %ss were protesting to keep %s in stores. They began to %s to the rhythm of the %s, which made all the %ss very %s. Concerned, %s texted %s, who flew %s to %s and dropped %s in a puddle of frozen %s. %s woke up in the year %s, in a world where %ss ruled the world."

print "Mad Libs Has Started!"

#user inputs
name = raw_input("Enter a name:")
adj_1 = raw_input("Enter your first adjective:")
adj_2 = raw_input("Enter your second adjective:")
adj_3 = raw_input("Enter your third adjective:")
verb = raw_input("Enter a verb:")
noun_1 = raw_input("Enter your first noun:")
noun_2 = raw_input("Enter your second noun:")
animal = raw_input("Enter a animal:")
food = raw_input("Enter a food:")
fruit = raw_input("Enter a fruit:")
superhero = raw_input("Enter a superhero:")
country = raw_input("Enter a country:")
dessert = raw_input("Enter a dessert:")
year = raw_input("Enter a year:")

#print MadLib
print STORY % (name, adj_1, adj_2, animal, food, verb, noun_1, fruit, adj_3, name, superhero, name, country, name, dessert, name, year, noun_2)