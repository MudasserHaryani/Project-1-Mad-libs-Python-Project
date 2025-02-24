print("🌟 Welcome to the Enchanted Adventure!")
print("✨ Fill in the blanks to create your own Aladdin-inspired tale!\n")

# Input prompts for an Aladdin-like story
hero = input("Enter the name of your brave hero: ")
magic_item = input("Enter a magical object (e.g., lamp): ")
genie_name = input("Enter the name of your genie: ")
adjective = input("Enter an adjective: ")
kingdom = input("Enter the name of a mystical kingdom: ")
challenge = input("Enter a daring challenge (e.g., battling a dragon): ")
treasure = input("Enter a treasure (e.g., golden crown): ")
wish = input("Enter your greatest wish: ")

story = f"""
Once upon a time in the mystical kingdom of {kingdom} 🕌, there lived a brave soul named {hero} who dreamed of adventure.
One fateful day, while wandering through an ancient bazaar, {hero} discovered a mysterious {magic_item} glimmering under the desert sun 🌞.
Curious and hopeful, {hero} rubbed the {magic_item} and, to their amazement, out popped a dazzling genie named {genie_name} 🧞,
whose {adjective} smile lit up the twilight sky. "Your destiny awaits!" boomed {genie_name}, as the air filled with swirling magic and stardust 🌌.
Together, they embarked on a perilous journey, facing trials such as {challenge} 🐉, which tested their courage and wit.
Deep within a hidden cavern, {hero} unearthed an ancient secret—a {treasure} that shimmered with untold power 💎.
With a heart full of hope, {hero} declared, "{wish}!" and in that very moment, the fate of {kingdom} was forever transformed, and a new legend was born ✨.
"""

print("\n" + "="*50)
print(story)
print("="*50 + "\n")
