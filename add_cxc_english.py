import re

filepath = "./app/src/main/java/com/example/myapplication/QuestionBank.kt"

with open(filepath, "r") as f:
    content = f.read()

new_questions = """
        // ── CXC English A ──────────────────────────────────────────
        Question("CXC English A", "Which of the following is an example of a compound sentence?",
            listOf("She ran fast.", "She ran fast but she missed the bus.", "Running fast, she missed the bus.", "Because she ran fast."), 1),
        Question("CXC English A", "Which punctuation mark is used to introduce a list?",
            listOf("Comma", "Semicolon", "Colon", "Dash"), 2),
        Question("CXC English A", "A summary should be written in:",
            listOf("Note form with bullet points", "The writer's own words in continuous prose", "Direct quotations from the passage", "Exactly the same words as the original"), 1),
        Question("CXC English A", "Which of the following is NOT a feature of persuasive writing?",
            listOf("Use of rhetorical questions", "Emotional appeal", "Objective reporting of facts only", "Strong concluding argument"), 2),
        Question("CXC English A", "The main purpose of a topic sentence in a paragraph is to:",
            listOf("Summarize the entire essay", "Introduce the main idea of the paragraph", "Provide evidence for an argument", "Conclude the writer's thoughts"), 1),
        Question("CXC English A", "Which word is an example of a conjunction?",
            listOf("Quickly", "Beautiful", "Although", "Running"), 2),
        Question("CXC English A", "In Caribbean Standard English, which sentence is grammatically correct?",
            listOf("He don't know the answer.", "He doesn't know the answer.", "He ain't know the answer.", "He not knowing the answer."), 1),
        Question("CXC English A", "Which of the following best describes an expository text?",
            listOf("A text that tells a fictional story", "A text that persuades the reader to act", "A text that explains or informs about a topic", "A text that describes personal feelings"), 2),
        Question("CXC English A", "Which sentence contains a subordinate clause?",
            listOf("The dog barked loudly.", "Maria cooks and James cleans.", "When the rain fell, the children ran inside.", "Stop that noise!"), 2),
        Question("CXC English A", "Which of the following is a correct formal letter salutation?",
            listOf("Hey John,", "Dear Mr. Williams,", "What's up, Sir?", "Yo, Principal!"), 1),

        // ── CXC English B ──────────────────────────────────────────
        Question("CXC English B", "What is a simile?",
            listOf("A comparison using 'is' or 'are'", "A comparison using 'like' or 'as'", "A word that imitates a sound", "A repeated consonant sound"), 1),
        Question("CXC English B", "The term 'protagonist' refers to:",
            listOf("The main conflict in the story", "The narrator of the story", "The main character in the story", "The villain of the story"), 2),
        Question("CXC English B", "Which literary device is used in 'the wind whispered through the trees'?",
            listOf("Simile", "Hyperbole", "Personification", "Alliteration"), 2),
        Question("CXC English B", "The repetition of consonant sounds at the beginning of nearby words is called:",
            listOf("Assonance", "Alliteration", "Onomatopoeia", "Rhyme"), 1),
        Question("CXC English B", "A story told from the first-person point of view uses which pronoun?",
            listOf("He/She", "They", "I", "You"), 2),
        Question("CXC English B", "What is the 'theme' of a literary work?",
            listOf("The sequence of events in the story", "The central message or underlying idea", "The time and place where the story is set", "The author's writing style"), 1),
        Question("CXC English B", "Which term describes the time and place in which a story is set?",
            listOf("Plot", "Theme", "Setting", "Tone"), 2),
        Question("CXC English B", "A Type B question in CXC English B requires you to:",
            listOf("Analyse a single text in detail", "Compare two texts or poems", "Write a creative short story", "Summarize a passage"), 1),
        Question("CXC English B", "Which of the following is a well-known West Indian novel on the CXC English B prescribed list?",
            listOf("Pride and Prejudice", "In the Castle of My Skin", "Great Expectations", "Animal Farm"), 1),
        Question("CXC English B", "The mood of a poem refers to:",
            listOf("The poet's biography", "The rhyme scheme of the poem", "The emotional atmosphere created for the reader", "The length of the poem"), 2),
"""

# Insert before the closing of the questions list
# Find the last Question entry and insert after it
insert_marker = "    )\n}"
if insert_marker in content:
    content = content.replace(insert_marker, new_questions + "    )\n}", 1)
    with open(filepath, "w") as f:
        f.write(content)
    print("SUCCESS: CXC English A and B questions added.")
else:
    print("ERROR: Could not find insertion point. Check QuestionBank.kt closing pattern.")
