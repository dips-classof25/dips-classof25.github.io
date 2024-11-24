import random

first_names = [
    "Olivia", "Liam", "Emma", "Noah", "Ava", "James", "Sophia", "Lucas", "Isabella", "Mason",
    "Mia", "Benjamin", "Charlotte", "Ethan", "Amelia", "Henry", "Harper", "Jack", "Ella", "Samuel", "Scarlett"
]

last_names = [
    "Smith", "Johnson", "Brown", "Williams", "Jones", "Miller", "Davis", "Garcia", "Rodriguez", "Martinez",
    "Hernandez", "Lopez", "Gonzalez", "Wilson", "Anderson", "Thomas", "Taylor", "Moore", "Jackson", "Martin"
]

words = [
    "abandon", "ability", "absence", "academy", "account", "accuse", "action", "admire", "affect", "agency",
    "album", "amazing", "analysis", "ancient", "appeal", "attempt", "balance", "benefit", "beyond", "breeze",
    "capture", "celebrate", "chance", "classic", "climate", "combine", "comfort", "create", "debate", "defend",
    "deliver", "demand", "discovery", "enrich", "example", "extend", "family", "famous", "fantasy", "flood",
    "frozen", "gather", "growth", "genuine", "grateful", "hidden", "honest", "improve", "impact", "inspire",
    "journey", "justice", "kitchen", "legacy", "laughter", "leader", "library", "lonely", "lucky", "major",
    "mystery", "nature", "notable", "outcome", "parent", "perfect", "pleasure", "plenty", "promise", "quality",
    "question", "rescue", "result", "safety", "secure", "serenity", "simplify", "society", "success", "superb",
    "trouble", "unique", "vintage", "vocal", "winner", "wonder", "yesterday", "youth", "zealous", "zero",
    "advance", "afford", "adore", "alright", "balance", "benefit", "bless", "bother", "breathe", "bravery",
    "capture", "celebrate", "champion", "charming", "choice", "combine", "comment", "connect", "control", "creator",
    "deliver", "difficult", "display", "duty", "earnest", "encourage", "excited", "explore", "express", "fable",
    "failure", "fiction", "forgive", "freedom", "genuine", "glance", "goal", "greet", "grip", "growth",
    "habit", "hero", "hunger", "honor", "impact", "inquire", "innovate", "inspire", "instance", "intent",
    "journey", "justice", "kettle", "kneel", "knowledge", "laughter", "leader", "library", "lone", "matter",
    "meaning", "mellow", "mimic", "mysterious", "navigate", "novel", "obtain", "occupy", "option", "outlook",
    "practical", "preserve", "profit", "regret", "rescue", "resume", "secure", "serene", "sincere", "social",
    "suggest", "thrive", "trust", "unique", "vision", "valid", "virtue", "vivid", "weight", "witness",
    "yoga", "youth", "zealous", "zephyr", "accomplish", "animate", "ashore", "automate", "brilliant", "butterfly",
    "connect", "create", "decide", "distant", "dreamer", "direct", "efficient", "enlighten", "exact", "fallout",
    "fantasy", "feature", "genuine", "goal", "harmony", "heroic", "ideal", "impress", "journey", "lively"
]


print("section,name,message")

for s in list("ABCDEFG"):
	for _ in range(random.randint(20, 30)):
		print(f"{s},{random.choice(first_names)} {random.choice(last_names)},\"{" ".join([random.choice(words) for _ in range(random.randint(10, 40))])}\"")



