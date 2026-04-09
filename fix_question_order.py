filepath = "./app/src/main/java/com/example/myapplication/QuestionBank.kt"

with open(filepath, "r") as f:
    content = f.read()

# Remove the broken blocks entirely and rewrite correctly
import re

# Strip out the bad cxcEnglishA and cxcEnglishB val blocks
content = re.sub(r'\n    val cxcEnglishA = listOf\(.*?\)\n', '', content, flags=re.DOTALL)
content = re.sub(r'\n    val cxcEnglishB = listOf\(.*?\)\n', '', content, flags=re.DOTALL)

# Also fix getAllQuestions if it was already updated
old_return = "caribbeanHistory + scienceTech + sports + worldGeo + artsCulture + svgVincy + cxcEnglishA + cxcEnglishB"
content = content.replace(old_return, "caribbeanHistory + scienceTech + sports + worldGeo + artsCulture + svgVincy")

new_vals = """
    val cxcEnglishA = listOf(
        Question("Which of the following is an example of a compound sentence?", listOf("She ran fast.", "She ran fast but she missed the bus.", "Running fast, she missed the bus.", "Because she ran fast."), 1, "CXC English A"),
        Question("Which punctuation mark is used to introduce a list?", listOf("Comma", "Semicolon", "Colon", "Dash"), 2, "CXC English A"),
        Question("A summary should be written in:", listOf("Note form with bullet points", "The writer's own words in continuous prose", "Direct quotations from the passage", "Exactly the same words as the original"), 1, "CXC English A"),
        Question("Which of the following is NOT a feature of persuasive writing?", listOf("Use of rhetorical questions", "Emotional appeal", "Objective reporting of facts only", "Strong concluding argument"), 2, "CXC English A"),
        Question("The main purpose of a topic sentence is to:", listOf("Summarize the entire essay", "Introduce the main idea of the paragraph", "Provide evidence for an argument", "Conclude the writer's thoughts"), 1, "CXC English A"),
        Question("Which word is an example of a conjunction?", listOf("Quickly", "Beautiful", "Although", "Running"), 2, "CXC English A"),
        Question("In Caribbean Standard English, which sentence is grammatically correct?", listOf("He don't know the answer.", "He doesn't know the answer.", "He ain't know the answer.", "He not knowing the answer."), 1, "CXC English A"),
        Question("Which of the following best describes an expository text?", listOf("A text that tells a fictional story", "A text that persuades the reader to act", "A text that explains or informs about a topic", "A text that describes personal feelings"), 2, "CXC English A"),
        Question("Which sentence contains a subordinate clause?", listOf("The dog barked loudly.", "Maria cooks and James cleans.", "When the rain fell, the children ran inside.", "Stop that noise!"), 2, "CXC English A"),
        Question("Which of the following is a correct formal letter salutation?", listOf("Hey John,", "Dear Mr. Williams,", "What's up, Sir?", "Yo, Principal!"), 1, "CXC English A")
    )

    val cxcEnglishB = listOf(
        Question("What is a simile?", listOf("A comparison using 'is' or 'are'", "A comparison using 'like' or 'as'", "A word that imitates a sound", "A repeated consonant sound"), 1, "CXC English B"),
        Question("The term 'protagonist' refers to:", listOf("The main conflict in the story", "The narrator of the story", "The main character in the story", "The villain of the story"), 2, "CXC English B"),
        Question("Which literary device is used in 'the wind whispered through the trees'?", listOf("Simile", "Hyperbole", "Personification", "Alliteration"), 2, "CXC English B"),
        Question("The repetition of consonant sounds at the beginning of nearby words is called:", listOf("Assonance", "Alliteration", "Onomatopoeia", "Rhyme"), 1, "CXC English B"),
        Question("A story told from the first-person point of view uses which pronoun?", listOf("He/She", "They", "I", "You"), 2, "CXC English B"),
        Question("What is the 'theme' of a literary work?", listOf("The sequence of events in the story", "The central message or underlying idea", "The time and place where the story is set", "The author's writing style"), 1, "CXC English B"),
        Question("Which term describes the time and place in which a story is set?", listOf("Plot", "Theme", "Setting", "Tone"), 2, "CXC English B"),
        Question("A Type B question in CXC English B requires you to:", listOf("Analyse a single text in detail", "Compare two texts or poems", "Write a creative short story", "Summarize a passage"), 1, "CXC English B"),
        Question("Which is a well-known West Indian novel on the CXC English B prescribed list?", listOf("Pride and Prejudice", "In the Castle of My Skin", "Great Expectations", "Animal Farm"), 1, "CXC English B"),
        Question("The mood of a poem refers to:", listOf("The poet's biography", "The rhyme scheme of the poem", "The emotional atmosphere created for the reader", "The length of the poem"), 2, "CXC English B")
    )

"""

if "fun getAllQuestions()" in content:
    content = content.replace("    fun getAllQuestions()", new_vals + "    fun getAllQuestions()", 1)
    print("Step 1 OK: val blocks inserted")
else:
    print("FAIL: getAllQuestions not found")
    exit()

old_return = "caribbeanHistory + scienceTech + sports + worldGeo + artsCulture + svgVincy"
new_return = "caribbeanHistory + scienceTech + sports + worldGeo + artsCulture + svgVincy + cxcEnglishA + cxcEnglishB"
if old_return in content:
    content = content.replace(old_return, new_return, 1)
    print("Step 2 OK: getAllQuestions return updated")
else:
    print("FAIL: return line not found")
    exit()

with open(filepath, "w") as f:
    f.write(content)

print("SUCCESS")
