#_Vladimir Ovsyannikov_
#Russian Recipe Book

#Welcome Statement
print("Hello, World!", end=" ")
#End= combines the two seperate lines into one

#Introduction to user
print("Welcome to my Russian Recipe Book")
userName = input("What is your name?: ")
print("")  #Seperates lines
print(
	"I am glad you decided to learn Russian cuisine, ", userName, ".", sep="")
#Sep= combines the quotations

#Program purpose outlined
print("Today, we will learn how to make Borsht.")
print("")

#User eligibility, in terms of age
age = input("How old are you?: ")
userSkillRating = input("Rate your cooking skills from 1-10: ")
if not (int(age) > 18 and int(userSkillRating) > 3):
	print("You are not eligible to cook.\n" "Please, exit this recipe book.")
	exit()
else:
	print("Good, you are eligible to cook.")
print("")
#Relational operators

#User prior knowledge
userSkill = input("Have you ever cooked Borsht?: ")
if userSkill == "Yes" or userSkill == "yes" or userSkill == "yeah" or userSkill == "ye" or userSkill == "yea" or userSkill != "no":
	print("")
	print("Great! You can close this recipe book and eat some Borsht.")
	exit()
elif userSkill == "Maybe" or userSkill == "I don't know":
	print("")
	print("In any case, this will be a great way to refresh your mind.")
else:
	print("")
	print("It's your lucky day! Today you will learn how to cook Borscht.")
print("")
#Relational operators
#Conditional statements (if,elif,else)

#Borscht introduction:
#Anonymous.17/08/2021, et al. “9 Traditional Russian Dishes to Help You Discover This Great Country.” Real Word, 8 June 2021, www.trafalgar.com/real-word/traditional-russian-dishes/. 
print("WHAT IS BORSCHT?")
print(
	"Borscht is a beetroot soup that originated in Ukraine. It is now a speciality in soviet countries, like Russia."
)
print("")

#User Availability
print("This recipe takes approximately 3 hours.")
userTime = input("Do you have enough time?: ")
if userTime == "No" or userTime == "no":
	print("")
	print("I'm sorry, maybe next time?")
	exit()
else:
	print("")
	print("Perfect, Let's start!")
print("")

#Recipe variables
#Ciation for recipe:
#Bauer, Elise. “Borscht.” Simply Recipes, Simply Recipes, 9 July 2021, www.simplyrecipes.com/recipes/borscht/. 
beefStewMeat = 1  #pound
beefBroth = 2  #cups
beets = 4  #count
carrots = 4  #count
russetPotato = 1  #count
cabbage = 2  #cups
dill = 0.75  #cups
redWineVinegar = 3  #tablespoons
sourCream = 1  #cup

#Serving size
servingSize = int(input("How many people are you cooking for? (2-8): "))

#Result for input 1
if (servingSize == 1):
	print("Borscht is meant to be shared. The serving size may not be 1")
	exit()

#Result for input 2 or 3
elif servingSize == 2 or servingSize == 3:
	print("")
	print("You will need the following ingredients:")
	print("-Extra virgin olive oil or vegetable oil")
	print("-Beef stew meat:", beefStewMeat * .33,
							"pounds" + "(Excess fat trimmed)")
	print("-Small onion: 1", "(Chopped)")
	print("-Beef broth or beef stock:", beefBroth + 0.66, "cups" + "(Divided)")
	print("-Large beets:", beets // 1.5, "(Peeled and chopped)")
	print("-Carrots:", carrots // 1.5, "(Peeled and chopped)")
	print("-Large russet potato:", russetPotato % 1.33,
							"(Peeled and cut into 1/2-inch cubes)")
	print("-Thinly sliced cabbage:", format(cabbage / 3, '.2f'), "cups")
	print("-Fresh dill:", dill / 3, "cups" + "(Chopped)")
	print("-Red wine vinegar:", redWineVinegar / 3, "tablespoon")
	print("-Sour Cream:", format(sourCream / 3, '.2f'), "cups")
	print("Salt and black pepper to taste")
#Multiplication,addition,division w/ integral,remainder,modulus
#String operator (Concatenation)

#Result for input 4 or 5
elif servingSize == 4 or servingSize == 5:
	print("")
	print("You will need the following ingredients:")
	print("-Extra virgin olive oil or vegetable oil")
	print("-Beef stew meat:", beefStewMeat * .66,
							"pounds" + "(Excess fat trimmed)")
	print("-Medium onion: 1", "(Chopped)")
	print("-Beef broth or beef stock:", beefBroth**2, "cups" + "(Divided)")
	print("-Large beets:", beets // 1.2, "(Peeled and chopped)")
	print("-Carrots:", carrots // 1.2, "(Peeled and chopped)")
	print("-Medium russet potato:", russetPotato % 1.66,
							"(Peeled and cut into 1/2-inch cubes)")
	print("-Thinly sliced cabbage:", format(cabbage / 2, '.2f'), "cup")
	print("-Fresh dill:", format(dill / 2, '.2f'), "cups" + "(Chopped)")
	print("-Red wine vinegar:", redWineVinegar - 1, "tablespoons")
	print("-Sour Cream:", sourCream - 0.50, "cups")
	print("Salt and black pepper to taste")
#Exponentition,subtraction

#Result for input 6,7, or 8
elif servingSize == 6 or servingSize == 7 or servingSize == 8:
	print("")
	print("You will need the following ingredients:")
	print("-Extra virgin olive oil or vegetable oil")
	print("-Beef stew meat:", beefStewMeat, "pounds" + "(Excess fat trimmed)")
	print("-Large onion: 1", "(Chopped)")
	print("-Beef broth or beef stock:", beefBroth**3, "cups" + "(Divided)")
	print("-Large beets:", beets, "(Peeled and chopped)")
	print("-Carrots:", carrots, "(Peeled and chopped)")
	print("-Large russet potato:", russetPotato,
							"(Peeled anc cut into 1/2-inch cubes)")
	print("-Thinly sliced cabbage:", cabbage, "cups")
	print("-Fresh dill:", dill, "cups" + "(Chopped)")
	print("-Red wine vinegar:", redWineVinegar, "tablespoons")
	print("-Sour Cream:", sourCream, "cups")
	print("Salt and black pepper to taste")
#Result for "other" input
else:
	print("Sorry, you have exceeded the limit")
	exit()
print("")

#Ingredients overview
print("This is the overview of all the ingredients you need: ")


def function_1(food):
	for x in food:
		print(x)


food = [
	"Beef stew meat", "beefbroth", "beets", "carrots", "russet potatoes",
	"cabbage", "dill", "red wine vinegar", "sour cream"
]
function_1(food)
print("")
#Defines function_1 in terms of food
#Food is expressed within a list of ingredients

#Motivational
print("Cooking is as easy as")
for i in range(1, 4, 1):
	print(i)
#For loop with range

#Method
input("Do you have all your ingredients?: ")
print("")
print("Method!" * 3)
#String operator (multiples printed word)
print("")
print("1. Brown Beef, add onions:")
print(
	"Heat 2 teaspoons oil in large, thick bottomed pot on medium high heat. Add the stew beef. Let the beef brown lightly on one side, then turn over."
)
print(
	"Add the chopped onions to the pot. Let the onions cook and soften, about 5 minuts."
)
print("")
print("2. Add half of the broth, cook until beef is tender:")
print(
	"Pour half of the broth over the beef and onions in the pot. Bring to a boil. Lower the heat to a simmer, cover and cook until the meat is tender (About 1 hour 30 minutes)."
)
print("")
print(
	"3. While beef is cooking, prepare and roast the beets, carrots, and potato:")
print(
	"Toss beets and carrots with a teaspoon (or two) of olive oil and spread them out in a single layer on a foil lined roasting pan. Roast in 400 Fahrenheit for 15 minutes."
)
print(
	"Then toss potatoes with olive oil and add to roasting pan. Roast everything for another 15 minutes."
)
print("")
print("4. Remove the meat from the pot:")
print(
	"Once the beef has cooked through until tender, remove from the pot, and take the pot off the heat. Chop meat into bite-sized pieces."
)
print("")
print("5. Skim off excess fat from the liquid in the pot")
print("")
print("6. Finish cooking the soup:")
print(
	"Return the pot to stove and add the remaining broth, the carrots, beets, and diced potatoes. Add the chopped meat, sliced cabbage, and half of the dill to the pot. Bring to simmer, and cook until cabbage is cooked through (15 minutes.)"
)
print("")
print("Lastly, add vinegar and season to taste.")
print("")
print("HOW TO SERVE?")
print("Ladle into bowls, add sour cream and a dash of fresh dill on top")
print("")
num = 0
while num < 3:
	num += 1
	print("Enjoy!")
#While loop and shortcut operator
