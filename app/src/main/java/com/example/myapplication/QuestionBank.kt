package com.example.myapplication

data class Question(
    val text: String,
    val options: List<String>,
    val correctIndex: Int,
    val category: String
)

object QuestionBank {

    val categories = listOf(
        "🌍 Caribbean History",
        "🧪 Science & Tech",
        "🏅 Sports",
        "🗺️ World Geography",
        "🎭 Arts & Culture",
        "🇻🇨 SVG & Vincy Life"
    )

    private fun q(text: String, opts: String, correct: Int, cat: String) =
        Question(text, opts.split("|"), correct, cat)

    // ── 1. CARIBBEAN HISTORY (17 questions) ──────────────────

    private val caribbeanHistory = listOf(        q("Which country was the FIRST Caribbean nation to gain independence?",
            "Haiti|Cuba|Jamaica|Trinidad and Tobago", 0, "🌍 Caribbean History"),
        q("In what year did Haiti declare independence from France?",
            "1791|1804|1838|1962", 1, "🌍 Caribbean History"),
        q("Which Caribbean island was the first to be colonized by the British?",
            "Barbados|Jamaica|St. Kitts|Antigua", 2, "🌍 Caribbean History"),
        q("The 1831 Baptist War slave rebellion took place in which island?",
            "Barbados|Jamaica|Trinidad|St. Vincent", 1, "🌍 Caribbean History"),
        q("Which European power first colonized Trinidad?",
            "Britain|France|Spain|Netherlands", 2, "🌍 Caribbean History"),
        q("In what year did slavery officially end in the British Caribbean?",
            "1834|1838|1807|1865", 1, "🌍 Caribbean History"),
        q("CARICOM was formally established in which year?",
            "1958|1973|1965|1981", 1, "🌍 Caribbean History"),
        q("The West Indies Federation was dissolved in which year?",
            "1958|1962|1965|1970", 1, "🌍 Caribbean History"),
        q("Which country hosts the CARICOM Secretariat?",
            "Barbados|Trinidad|Guyana|Jamaica", 2, "🌍 Caribbean History"),
        q("The Caribbean Community was established by which treaty?",
            "Treaty of Chaguaramas|Treaty of Kingston|Treaty of Bridgetown|Treaty of Basseterre",
            0, "🌍 Caribbean History"),
        q("Marcus Garvey, the Pan-African leader, was born in which country?",
            "Trinidad|Barbados|Jamaica|Haiti", 2, "🌍 Caribbean History"),
        q("The 1970 Black Power Revolution occurred in which Caribbean nation?",
            "Jamaica|Trinidad and Tobago|Barbados|Guyana", 1, "🌍 Caribbean History"),
        q("Which Caribbean island is known as 'The Land of Wood and Water'?",
            "Barbados|Jamaica|Dominica|St. Lucia", 1, "🌍 Caribbean History"),
        q("The Morant Bay Rebellion of 1865 took place in which country?",
            "Barbados|Jamaica|Trinidad|Guyana", 1, "🌍 Caribbean History"),
        q("Toussaint Louverture led the revolution in which country?",
            "Cuba|Haiti|Dominican Republic|Martinique", 1, "🌍 Caribbean History"),
    )

    // ── 2. SCIENCE & TECH (17 questions) ─────────────────────

    private val scienceTech = listOf(        q("What does DNA stand for?",
            "Deoxyribonucleic Acid|Dinitrogen Acid|Dynamic Nuclear Array|Dense Nucleic Arrangement",
            0, "🧪 Science & Tech"),
        q("Which planet is known as the Red Planet?",
            "Venus|Jupiter|Mars|Saturn", 2, "🧪 Science & Tech"),
        q("What is the chemical symbol for gold?",
            "Go|Gd|Au|Ag", 2, "🧪 Science & Tech"),
        q("How many bones are in the adult human body?",
            "196|206|216|226", 1, "🧪 Science & Tech"),
        q("What is known as the powerhouse of the cell?",
            "Nucleus|Ribosome|Mitochondria|Chloroplast", 2, "🧪 Science & Tech"),
        q("The speed of light is approximately how many km per second?",
            "150,000|300,000|450,000|600,000", 1, "🧪 Science & Tech"),
        q("What is the most abundant gas in Earth's atmosphere?",
            "Oxygen|Carbon Dioxide|Hydrogen|Nitrogen", 3, "🧪 Science & Tech"),
        q("Which scientist formulated the theory of general relativity?",
            "Newton|Bohr|Einstein|Hawking", 2, "🧪 Science & Tech"),
        q("What does HTTP stand for?",
            "HyperText Transfer Protocol|High Tech Transfer Process|HyperText Transmission Path|Host Transfer Protocol",
            0, "🧪 Science & Tech"),
        q("The unit of electrical resistance is called what?",
            "Volt|Ampere|Ohm|Watt", 2, "🧪 Science & Tech"),
        q("What is the hardest natural substance on Earth?",
            "Gold|Diamond|Platinum|Quartz", 1, "🧪 Science & Tech"),
        q("Which planet has the most moons in our solar system?",
            "Jupiter|Saturn|Uranus|Neptune", 1, "🧪 Science & Tech"),
        q("What does AI stand for in technology?",
            "Automated Interface|Artificial Intelligence|Advanced Integration|Analytic Index",
            1, "🧪 Science & Tech"),
        q("The study of earthquakes is called what?",
            "Meteorology|Seismology|Volcanology|Geology", 1, "🧪 Science & Tech"),
        q("How many chromosomes does a typical human cell have?",
            "23|36|46|48", 2, "🧪 Science & Tech"),
    )

    // ── 3. SPORTS (17 questions) ──────────────────────────────

    private val sports = listOf(        q("Which country won the FIFA World Cup in 2022?",
            "France|Brazil|Argentina|Germany", 2, "🏅 Sports"),
        q("How many players from each team are on the court in basketball?",
            "4|5|6|7", 1, "🏅 Sports"),
        q("Usain Bolt, the world's fastest man, is from which Caribbean country?",
            "Trinidad|Barbados|Jamaica|Bahamas", 2, "🏅 Sports"),
        q("Which country has won the most Cricket World Cups?",
            "Australia|West Indies|India|England", 0, "🏅 Sports"),
        q("In tennis, what is the term for a score of 40-40?",
            "Tie|Deuce|Set Point|Match Point", 1, "🏅 Sports"),
        q("The Summer Olympic Games are held every how many years?",
            "2|3|4|5", 2, "🏅 Sports"),
        q("Chris Gayle is associated with which Caribbean cricket team?",
            "Trinidad|Barbados|Jamaica|Guyana", 2, "🏅 Sports"),
        q("Which sport uses a shuttlecock?",
            "Squash|Badminton|Volleyball|Polo", 1, "🏅 Sports"),
        q("How many holes are played in a standard round of golf?",
            "9|12|18|21", 2, "🏅 Sports"),
        q("The Shot Put is a discipline in which sport?",
            "Swimming|Athletics|Gymnastics|Weightlifting", 1, "🏅 Sports"),
        q("Serena Williams is celebrated for which sport?",
            "Golf|Tennis|Basketball|Volleyball", 1, "🏅 Sports"),
        q("Which Caribbean nation is famous for its Winter Olympics bobsled team?",
            "Trinidad|Jamaica|Barbados|Cuba", 1, "🏅 Sports"),
        q("In which country was the sport of cricket invented?",
            "Australia|West Indies|England|India", 2, "🏅 Sports"),
        q("What colour jersey does the leader wear in the Tour de France?",
            "Red|Green|Yellow|Blue", 2, "🏅 Sports"),
        q("How many individual events make up a Decathlon?",
            "8|10|12|15", 1, "🏅 Sports"),
    )

    // ── 4. WORLD GEOGRAPHY (16 questions) ─────────────────────

    private val worldGeo = listOf(        q("What is the largest continent by land area?",
            "Africa|Antarctica|Asia|South America", 2, "🗺️ World Geography"),
        q("Which river is the longest in the world?",
            "Amazon|Congo|Mississippi|Nile", 3, "🗺️ World Geography"),
        q("What is the capital city of Australia?",
            "Sydney|Melbourne|Canberra|Brisbane", 2, "🗺️ World Geography"),
        q("Which country currently has the largest population in the world?",
            "India|China|USA|Indonesia", 0, "🗺️ World Geography"),
        q("Mount Everest is located in which mountain range?",
            "Andes|Alps|Rockies|Himalayas", 3, "🗺️ World Geography"),
        q("What is the smallest country in the world by area?",
            "Monaco|San Marino|Vatican City|Liechtenstein", 2, "🗺️ World Geography"),
        q("Which is the largest ocean on Earth?",
            "Atlantic|Indian|Pacific|Arctic", 2, "🗺️ World Geography"),
        q("The Amazon rainforest is primarily located in which country?",
            "Colombia|Peru|Venezuela|Brazil", 3, "🗺️ World Geography"),
        q("What is the capital city of Japan?",
            "Osaka|Kyoto|Tokyo|Hiroshima", 2, "🗺️ World Geography"),
        q("The Sahara Desert spans across which continent?",
            "Asia|South America|Australia|Africa", 3, "🗺️ World Geography"),
        q("Which country has the most freshwater lakes in the world?",
            "Russia|USA|Brazil|Canada", 3, "🗺️ World Geography"),
        q("The Panama Canal connects which two major oceans?",
            "Indian and Pacific|Atlantic and Pacific|Atlantic and Indian|Pacific and Arctic",
            1, "🗺️ World Geography"),
        q("What is the capital city of Brazil?",
            "Rio de Janeiro|Sao Paulo|Brasilia|Salvador", 2, "🗺️ World Geography"),
        q("Which country is home to the Great Barrier Reef?",
            "New Zealand|Philippines|Australia|Indonesia", 2, "🗺️ World Geography"),
        q("How many member states does the African Union have?",
            "45|54|63|72", 1, "🗺️ World Geography"),
    )

    // ── 5. ARTS & CULTURE (16 questions) ──────────────────────

    private val artsCulture = listOf(        q("Who painted the world-famous Mona Lisa?",
            "Michelangelo|Raphael|Leonardo da Vinci|Caravaggio", 2, "🎭 Arts & Culture"),
        q("Which music genre was pioneered in Trinidad and Tobago?",
            "Reggae|Calypso|Soca|Zouk", 1, "🎭 Arts & Culture"),
        q("The legendary Bob Marley was from which country?",
            "Trinidad|Barbados|Jamaica|Cuba", 2, "🎭 Arts & Culture"),
        q("Who wrote the dystopian novel '1984'?",
            "Aldous Huxley|George Orwell|Ernest Hemingway|Franz Kafka", 1, "🎭 Arts & Culture"),
        q("Which Caribbean writer won the Nobel Prize in Literature in 1992?",
            "C.L.R. James|V.S. Naipaul|Derek Walcott|George Lamming", 2, "🎭 Arts & Culture"),
        q("Reggae music originated and rose to prominence in which decade?",
            "1950s|1960s|1970s|1980s", 1, "🎭 Arts & Culture"),
        q("Which Shakespeare play features 'To be or not to be, that is the question'?",
            "Macbeth|Romeo and Juliet|King Lear|Hamlet", 3, "🎭 Arts & Culture"),
        q("The famous Louvre Museum is located in which city?",
            "Rome|Madrid|Paris|London", 2, "🎭 Arts & Culture"),
        q("Soca music is most closely associated with which Caribbean country?",
            "Jamaica|Barbados|Trinidad and Tobago|St. Lucia", 2, "🎭 Arts & Culture"),
        q("Which Caribbean author wrote the classic novel 'A House for Mr Biswas'?",
            "Derek Walcott|Samuel Selvon|V.S. Naipaul|George Lamming", 2, "🎭 Arts & Culture"),
        q("What instrument is the heart of Caribbean Steelpan music?",
            "Drums|Steel drum pan|Guitar|Saxophone", 1, "🎭 Arts & Culture"),
        q("The Booker Prize is the world's most prestigious award for what?",
            "Film|Music|Literature|Architecture", 2, "🎭 Arts & Culture"),
        q("Who directed the groundbreaking film 'Black Panther'?",
            "Jordan Peele|Ryan Coogler|Spike Lee|Ava DuVernay", 1, "🎭 Arts & Culture"),
        q("Crop Over is a major cultural festival celebrated in which Caribbean island?",
            "Trinidad|Jamaica|Barbados|Grenada", 2, "🎭 Arts & Culture"),
        q("Which famous artist is known for cutting off part of his own ear?",
            "Claude Monet|Pablo Picasso|Vincent van Gogh|Salvador Dali", 2, "🎭 Arts & Culture"),
    )

    // ── 6. SVG & VINCY LIFE (17 questions) ───────────────────

    private val svgVincy = listOf(        q("What is the capital city of St. Vincent and the Grenadines?",
            "Georgetown|Layou|Kingstown|Calliaqua", 2, "🇻🇨 SVG & Vincy Life"),
        q("La Soufrière in SVG is a what?",
            "Mountain range|Active volcano|National park|Earthquake fault", 1, "🇻🇨 SVG & Vincy Life"),
        q("St. Vincent and the Grenadines gained independence from Britain in which year?",
            "1969|1974|1979|1983", 2, "🇻🇨 SVG & Vincy Life"),
        q("What is the national bird of St. Vincent?",
            "St. Vincent Amazon parrot|Frigate Bird|Hummingbird|Pelican", 0, "🇻🇨 SVG & Vincy Life"),
        q("Which island is the largest of the Grenadine islands?",
            "Bequia|Union Island|Mustique|Canouan", 0, "🇻🇨 SVG & Vincy Life"),
        q("SVG is a member of which major Caribbean regional organisation?",
            "NAFTA|MERCOSUR|CARICOM|ASEAN", 2, "🇻🇨 SVG & Vincy Life"),
        q("Which staple food features prominently in SVG's national dish, Roasted Breadfruit and Jackfish?",
            "Breadfruit|Ackee|Plantain|Cassava", 0, "🇻🇨 SVG & Vincy Life"),
        q("Hurricane Beryl caused major damage to SVG in which year?",
            "2022|2023|2024|2025", 2, "🇻🇨 SVG & Vincy Life"),
        q("What has historically been the main agricultural export of SVG?",
            "Sugar|Bananas|Cocoa|Coffee", 1, "🇻🇨 SVG & Vincy Life"),
        q("The RSS Regional Security System headquarters is in which country?",
            "Trinidad|Barbados|SVG|Jamaica", 1, "🇻🇨 SVG & Vincy Life"),
        q("Vincy Mas is SVG's version of which annual cultural celebration?",
            "Christmas|Carnival|Easter|Independence Day", 1, "🇻🇨 SVG & Vincy Life"),
        q("Which political party won SVG's November 2025 general election ending 25 years of ULP rule?",
            "ULP|NDP|SVG Labour|PDP", 1, "🇻🇨 SVG & Vincy Life"),
        q("The Argyle International Airport in SVG opened in which year?",
            "2015|2016|2017|2018", 2, "🇻🇨 SVG & Vincy Life"),
        q("What is the official name of SVG's national police force?",
            "RSVGPF|SVGPF|CSVGP|VPF", 0, "🇻🇨 SVG & Vincy Life"),
        q("The Black Caribs (Garifuna people) were exiled from SVG to Central America in which year?",
            "1783|1797|1814|1838", 1, "🇻🇨 SVG & Vincy Life"),
    )

    fun getQuestions(category: String): List<Question> = when {
        category.contains("Caribbean History") -> caribbeanHistory
        category.contains("Integrated Science") -> cxcIntScienceQuestions
        category.contains("Social Studies")   -> cxcSocialStudiesQuestions
        category.contains("POB")              -> cxcPOBQuestions
        category.contains("CXC IT")           -> cxcITQuestions
        category.contains("Office Admin")     -> cxcOfficeAdminQuestions
        category.contains("Physical Education") -> cxcPEQuestions
        category.contains("Science")           -> scienceTech
        category.contains("Sports")            -> sports
        category.contains("CXC Geography")       -> cxcGeographyQuestions
        category.contains("Geography")         -> worldGeo
        category.contains("Arts")              -> artsCulture
        category.contains("Vincy")             -> svgVincy
        category.contains("English A")      -> cxcEnglishAQuestions
        category.contains("English B")      -> cxcEnglishBQuestions
        category.contains("Maths")          -> cxcMathsQuestions
        else                                   -> caribbeanHistory
    }



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


    val cxcEnglishAQuestions = listOf(
        Question(
            text = "Which sentence is punctuated correctly?",
            options = listOf("Its a lovely day, isn't it.", "It's a lovely day, isn't it?", "Its a lovely day isn't it?", "It's a lovely day isn't it."),
            correctIndex = 1,
            category = "CXC English A"
        ),
        Question(
            text = "The word 'benevolent' most nearly means:",
            options = listOf("Strict", "Clever", "Kind and generous", "Angry"),
            correctIndex = 2,
            category = "CXC English A"
        ),
        Question(
            text = "Which of the following is a compound sentence?",
            options = listOf("She ran quickly.", "She ran quickly because she was late.", "She ran quickly, and she arrived on time.", "Running quickly, she arrived."),
            correctIndex = 2,
            category = "CXC English A"
        ),
        Question(
            text = "Which punctuation mark introduces a list?",
            options = listOf("Semicolon", "Colon", "Comma", "Dash"),
            correctIndex = 1,
            category = "CXC English A"
        ),
        Question(
            text = "'The students were advised to study.' This sentence is in:",
            options = listOf("Active voice", "Passive voice", "Direct speech", "Reported question"),
            correctIndex = 1,
            category = "CXC English A"
        ),
        Question(
            text = "Which word correctly completes: 'Neither the teacher nor the students ___ ready'?",
            options = listOf("was", "were", "is", "has been"),
            correctIndex = 1,
            category = "CXC English A"
        ),
        Question(
            text = "A formal letter to a principal should begin:",
            options = listOf("Hey there,", "Dear Sir/Madam,", "Yo Principal,", "Hi,"),
            correctIndex = 1,
            category = "CXC English A"
        ),
        Question(
            text = "Which is an example of a metaphor?",
            options = listOf("She runs like the wind.", "The wind howled angrily.", "Life is a journey.", "He almost fell."),
            correctIndex = 2,
            category = "CXC English A"
        ),
        Question(
            text = "The purpose of a topic sentence is to:",
            options = listOf("Conclude the paragraph", "Introduce the main idea of the paragraph", "Give supporting details", "Transition to the next paragraph"),
            correctIndex = 1,
            category = "CXC English A"
        ),
        Question(
            text = "'Affect' and 'effect' are examples of:",
            options = listOf("Synonyms", "Antonyms", "Homophones", "Commonly confused words"),
            correctIndex = 3,
            category = "CXC English A"
        ),
        Question(
            text = "Which sentence contains a dangling modifier?",
            options = listOf("Running fast, John caught the bus.", "Running fast, the bus was caught by John.", "John, running fast, caught the bus.", "John ran fast to catch the bus."),
            correctIndex = 1,
            category = "CXC English A"
        ),
        Question(
            text = "A summary should be:",
            options = listOf("Longer than the original text", "Written in the author's exact words", "In your own words and shorter than the original", "Full of the writer's opinions"),
            correctIndex = 2,
            category = "CXC English A"
        ),
        Question(
            text = "Which word is spelled correctly?",
            options = listOf("Recieve", "Receive", "Receve", "Reciev"),
            correctIndex = 1,
            category = "CXC English A"
        ),
        Question(
            text = "'The principal called the students.' The object of this sentence is:",
            options = listOf("Called", "The principal", "The students", "Principal"),
            correctIndex = 2,
            category = "CXC English A"
        ),
        Question(
            text = "Which type of writing aims to convince the reader?",
            options = listOf("Narrative", "Descriptive", "Persuasive", "Expository"),
            correctIndex = 2,
            category = "CXC English A"
        )
    )


    val cxcEnglishBQuestions = listOf(
        Question(
            text = "'The trees whispered secrets to the wind.' This is an example of:",
            options = listOf("Simile", "Metaphor", "Personification", "Hyperbole"),
            correctIndex = 2,
            category = "CXC English B"
        ),
        Question(
            text = "The atmosphere or feeling created by a piece of writing is called its:",
            options = listOf("Theme", "Tone", "Mood", "Plot"),
            correctIndex = 2,
            category = "CXC English B"
        ),
        Question(
            text = "In a story, the central conflict is usually introduced during the:",
            options = listOf("Resolution", "Climax", "Falling action", "Rising action"),
            correctIndex = 3,
            category = "CXC English B"
        ),
        Question(
            text = "Which Caribbean author wrote 'A House for Mr. Biswas'?",
            options = listOf("Derek Walcott", "V.S. Naipaul", "Samuel Selvon", "Earl Lovelace"),
            correctIndex = 1,
            category = "CXC English B"
        ),
        Question(
            text = "A sonnet traditionally has how many lines?",
            options = listOf("12", "14", "16", "18"),
            correctIndex = 1,
            category = "CXC English B"
        ),
        Question(
            text = "'She's as brave as a lion.' This sentence uses:",
            options = listOf("Metaphor", "Personification", "Simile", "Alliteration"),
            correctIndex = 2,
            category = "CXC English B"
        ),
        Question(
            text = "The narrator who uses 'I' and is a character in the story has which point of view?",
            options = listOf("Second person", "Third person omniscient", "Third person limited", "First person"),
            correctIndex = 3,
            category = "CXC English B"
        ),
        Question(
            text = "The main message or central idea of a literary work is its:",
            options = listOf("Plot", "Setting", "Theme", "Characterisation"),
            correctIndex = 2,
            category = "CXC English B"
        ),
        Question(
            text = "Derek Walcott was awarded the Nobel Prize in:",
            options = listOf("Literature", "Peace", "Economics", "Medicine"),
            correctIndex = 0,
            category = "CXC English B"
        ),
        Question(
            text = "'Season of mists and mellow fruitfulness' uses which device?",
            options = listOf("Onomatopoeia", "Alliteration", "Hyperbole", "Irony"),
            correctIndex = 1,
            category = "CXC English B"
        ),
        Question(
            text = "A story's climax is:",
            options = listOf("The introduction of characters", "The background setting", "The turning point of greatest tension", "The final resolution"),
            correctIndex = 2,
            category = "CXC English B"
        ),
        Question(
            text = "When a character's words mean the opposite of what is literally said, this is:",
            options = listOf("Verbal irony", "Hyperbole", "Allusion", "Paradox"),
            correctIndex = 0,
            category = "CXC English B"
        ),
        Question(
            text = "The repetition of initial consonant sounds is called:",
            options = listOf("Assonance", "Rhyme", "Alliteration", "Onomatopoeia"),
            correctIndex = 2,
            category = "CXC English B"
        ),
        Question(
            text = "In drama, a soliloquy is when:",
            options = listOf("Two characters speak privately", "A character speaks their thoughts aloud alone", "The audience speaks to the cast", "The narrator describes the scene"),
            correctIndex = 1,
            category = "CXC English B"
        ),
        Question(
            text = "Samuel Selvon's 'The Lonely Londoners' is set in:",
            options = listOf("Trinidad", "Barbados", "London", "New York"),
            correctIndex = 2,
            category = "CXC English B"
        )
    )


    val cxcMathsQuestions = listOf(
        Question(
            text = "What is the value of 2³ × 3²?",
            options = listOf("36", "72", "48", "54"),
            correctIndex = 1,
            category = "CXC Maths"
        ),
        Question(
            text = "Solve for x: 3x + 7 = 22",
            options = listOf("3", "4", "5", "6"),
            correctIndex = 2,
            category = "CXC Maths"
        ),
        Question(
            text = "What is 15% of 200?",
            options = listOf("25", "30", "35", "40"),
            correctIndex = 1,
            category = "CXC Maths"
        ),
        Question(
            text = "The area of a circle with radius 7 cm is approximately:",
            options = listOf("44 cm²", "154 cm²", "49 cm²", "22 cm²"),
            correctIndex = 1,
            category = "CXC Maths"
        ),
        Question(
            text = "Simplify: 4x² + 3x - 2x² + x",
            options = listOf("2x² + 4x", "6x² + 4x", "2x² - 4x", "6x² - 4x"),
            correctIndex = 0,
            category = "CXC Maths"
        ),
        Question(
            text = "What is the HCF of 24 and 36?",
            options = listOf("6", "8", "12", "18"),
            correctIndex = 2,
            category = "CXC Maths"
        ),
        Question(
            text = "Express 0.35 as a fraction in its simplest form:",
            options = listOf("35/100", "7/20", "7/25", "3/5"),
            correctIndex = 1,
            category = "CXC Maths"
        ),
        Question(
            text = "A rectangle has length 12 cm and width 5 cm. What is its perimeter?",
            options = listOf("34 cm", "60 cm", "30 cm", "17 cm"),
            correctIndex = 0,
            category = "CXC Maths"
        ),
        Question(
            text = "What is the gradient of a line passing through (0,2) and (4,10)?",
            options = listOf("2", "3", "4", "8"),
            correctIndex = 0,
            category = "CXC Maths"
        ),
        Question(
            text = "Factorise: x² - 9",
            options = listOf("(x-3)(x-3)", "(x+9)(x-1)", "(x+3)(x-3)", "(x-9)(x+1)"),
            correctIndex = 2,
            category = "CXC Maths"
        ),
        Question(
            text = "If a = 3 and b = -2, what is the value of 2a - 3b?",
            options = listOf("0", "12", "6", "9"),
            correctIndex = 1,
            category = "CXC Maths"
        ),
        Question(
            text = "What is the LCM of 4, 6 and 8?",
            options = listOf("12", "16", "24", "48"),
            correctIndex = 2,
            category = "CXC Maths"
        ),
        Question(
            text = "A triangle has angles 90° and 35°. What is the third angle?",
            options = listOf("45°", "55°", "65°", "75°"),
            correctIndex = 1,
            category = "CXC Maths"
        ),
        Question(
            text = "What is the probability of rolling an even number on a standard die?",
            options = listOf("1/6", "1/3", "1/2", "2/3"),
            correctIndex = 2,
            category = "CXC Maths"
        ),
        Question(
            text = "Convert 3/4 to a percentage:",
            options = listOf("34%", "57%", "70%", "75%"),
            correctIndex = 3,
            category = "CXC Maths"
        )
    )


    val cxcIntScienceQuestions = listOf(
        Question(
            text = "What is the chemical symbol for water?",
            options = listOf("WO", "H2O", "HO2", "W2O"),
            correctIndex = 1,
            category = "CXC Integrated Science"
        ),
        Question(
            text = "Which organ pumps blood around the human body?",
            options = listOf("Lungs", "Kidney", "Heart", "Liver"),
            correctIndex = 2,
            category = "CXC Integrated Science"
        ),
        Question(
            text = "What type of energy does the sun produce that plants use in photosynthesis?",
            options = listOf("Chemical energy", "Light energy", "Thermal energy", "Kinetic energy"),
            correctIndex = 1,
            category = "CXC Integrated Science"
        ),
        Question(
            text = "Which of the following is a conductor of electricity?",
            options = listOf("Rubber", "Plastic", "Copper", "Wood"),
            correctIndex = 2,
            category = "CXC Integrated Science"
        ),
        Question(
            text = "What gas do plants absorb from the atmosphere during photosynthesis?",
            options = listOf("Oxygen", "Nitrogen", "Carbon dioxide", "Hydrogen"),
            correctIndex = 2,
            category = "CXC Integrated Science"
        ),
        Question(
            text = "The unit of electric current is the:",
            options = listOf("Volt", "Watt", "Ohm", "Ampere"),
            correctIndex = 3,
            category = "CXC Integrated Science"
        ),
        Question(
            text = "Which of the following is NOT a renewable energy source?",
            options = listOf("Solar", "Wind", "Natural gas", "Hydroelectric"),
            correctIndex = 2,
            category = "CXC Integrated Science"
        ),
        Question(
            text = "What is the process by which water turns into vapour called?",
            options = listOf("Condensation", "Evaporation", "Precipitation", "Transpiration"),
            correctIndex = 1,
            category = "CXC Integrated Science"
        ),
        Question(
            text = "The pH of a neutral solution is:",
            options = listOf("0", "5", "7", "14"),
            correctIndex = 2,
            category = "CXC Integrated Science"
        ),
        Question(
            text = "Which part of the cell controls its activities?",
            options = listOf("Cell membrane", "Cytoplasm", "Nucleus", "Vacuole"),
            correctIndex = 2,
            category = "CXC Integrated Science"
        ),
        Question(
            text = "What is the force that pulls objects towards the centre of the Earth?",
            options = listOf("Friction", "Magnetism", "Gravity", "Tension"),
            correctIndex = 2,
            category = "CXC Integrated Science"
        ),
        Question(
            text = "Which blood vessels carry blood away from the heart?",
            options = listOf("Veins", "Capillaries", "Arteries", "Lymph nodes"),
            correctIndex = 2,
            category = "CXC Integrated Science"
        ),
        Question(
            text = "What is the chemical formula for table salt?",
            options = listOf("KCl", "NaCl", "CaCl", "MgCl"),
            correctIndex = 1,
            category = "CXC Integrated Science"
        ),
        Question(
            text = "Sound travels fastest through:",
            options = listOf("Vacuum", "Air", "Water", "Steel"),
            correctIndex = 3,
            category = "CXC Integrated Science"
        ),
        Question(
            text = "Which nutrient provides the body with the most energy per gram?",
            options = listOf("Carbohydrates", "Protein", "Vitamins", "Fats"),
            correctIndex = 3,
            category = "CXC Integrated Science"
        )
    )


    val cxcSocialStudiesQuestions = listOf(
        Question(
            text = "CARICOM was established in which year?",
            options = listOf("1958", "1973", "1981", "1962"),
            correctIndex = 1,
            category = "CXC Social Studies"
        ),
        Question(
            text = "Which of the following is a function of the family?",
            options = listOf("Collecting taxes", "Socialisation of children", "Enforcing laws", "Managing the economy"),
            correctIndex = 1,
            category = "CXC Social Studies"
        ),
        Question(
            text = "The head of government in a Westminster system is the:",
            options = listOf("President", "Governor General", "Prime Minister", "Chief Justice"),
            correctIndex = 2,
            category = "CXC Social Studies"
        ),
        Question(
            text = "Which of the following best defines 'culture'?",
            options = listOf("The government of a country", "The way of life of a group of people", "The economic system of a nation", "The laws of a society"),
            correctIndex = 1,
            category = "CXC Social Studies"
        ),
        Question(
            text = "What is the main purpose of a constitution?",
            options = listOf("To collect taxes", "To declare war", "To outline the fundamental laws and rights of a nation", "To manage trade"),
            correctIndex = 2,
            category = "CXC Social Studies"
        ),
        Question(
            text = "Which institution is responsible for making laws in most Caribbean countries?",
            options = listOf("The Cabinet", "The Parliament", "The Judiciary", "The Police"),
            correctIndex = 1,
            category = "CXC Social Studies"
        ),
        Question(
            text = "A person who enters a country to live permanently is called an:",
            options = listOf("Tourist", "Emigrant", "Immigrant", "Refugee"),
            correctIndex = 2,
            category = "CXC Social Studies"
        ),
        Question(
            text = "Which of the following is a non-governmental organisation (NGO)?",
            options = listOf("The Cabinet", "The Red Cross", "The Parliament", "The Police Force"),
            correctIndex = 1,
            category = "CXC Social Studies"
        ),
        Question(
            text = "The process by which a person learns the norms of their society is called:",
            options = listOf("Industrialisation", "Socialisation", "Urbanisation", "Globalisation"),
            correctIndex = 1,
            category = "CXC Social Studies"
        ),
        Question(
            text = "Which of the following is a cause of unemployment?",
            options = listOf("High literacy rates", "Lack of skills matching job market needs", "Strong GDP growth", "Low inflation"),
            correctIndex = 1,
            category = "CXC Social Studies"
        ),
        Question(
            text = "The Universal Declaration of Human Rights was adopted in which year?",
            options = listOf("1945", "1948", "1952", "1960"),
            correctIndex = 1,
            category = "CXC Social Studies"
        ),
        Question(
            text = "Which of the following is an example of social mobility?",
            options = listOf("Moving from one city to another", "A farmer's child becoming a doctor", "Changing religion", "Joining a new club"),
            correctIndex = 1,
            category = "CXC Social Studies"
        ),
        Question(
            text = "The main export of most Caribbean economies has traditionally been:",
            options = listOf("Oil", "Sugar", "Bauxite", "Tourism"),
            correctIndex = 1,
            category = "CXC Social Studies"
        ),
        Question(
            text = "Which of the following rights is a civil right?",
            options = listOf("Right to work", "Right to education", "Right to vote", "Right to healthcare"),
            correctIndex = 2,
            category = "CXC Social Studies"
        ),
        Question(
            text = "Saint Vincent and the Grenadines gained independence in which year?",
            options = listOf("1962", "1966", "1974", "1979"),
            correctIndex = 3,
            category = "CXC Social Studies"
        )
    )


    val cxcGeographyQuestions = listOf(
        Question(
            text = "Which of the following is the largest island in the Caribbean?",
            options = listOf("Jamaica", "Trinidad", "Cuba", "Hispaniola"),
            correctIndex = 2,
            category = "CXC Geography"
        ),
        Question(
            text = "What type of climate does most of the Caribbean experience?",
            options = listOf("Temperate", "Arid", "Tropical", "Polar"),
            correctIndex = 2,
            category = "CXC Geography"
        ),
        Question(
            text = "Which of the following is a fold mountain?",
            options = listOf("The Himalayas", "The Hawaiian Islands", "The Appalachians", "The Rockies"),
            correctIndex = 0,
            category = "CXC Geography"
        ),
        Question(
            text = "The imaginary line at 0° latitude is called the:",
            options = listOf("Prime Meridian", "Tropic of Cancer", "Equator", "Arctic Circle"),
            correctIndex = 2,
            category = "CXC Geography"
        ),
        Question(
            text = "Which Caribbean island is the most densely populated?",
            options = listOf("Cuba", "Barbados", "Jamaica", "Trinidad"),
            correctIndex = 1,
            category = "CXC Geography"
        ),
        Question(
            text = "What is the name of the process where rock is broken down in place without being moved?",
            options = listOf("Erosion", "Transportation", "Weathering", "Deposition"),
            correctIndex = 2,
            category = "CXC Geography"
        ),
        Question(
            text = "The Atlantic hurricane season officially runs from:",
            options = listOf("January to June", "April to October", "June to November", "July to December"),
            correctIndex = 2,
            category = "CXC Geography"
        ),
        Question(
            text = "Which of the following is an example of a renewable resource?",
            options = listOf("Coal", "Natural gas", "Timber", "Petroleum"),
            correctIndex = 2,
            category = "CXC Geography"
        ),
        Question(
            text = "The movement of people from rural to urban areas is called:",
            options = listOf("Emigration", "Immigration", "Rural-urban migration", "Urbanisation"),
            correctIndex = 2,
            category = "CXC Geography"
        ),
        Question(
            text = "Which of the following best describes a delta?",
            options = listOf("A deep valley carved by a river", "A flat landform at the mouth of a river", "A mountain formed by volcanic activity", "A coastal cliff formed by wave erosion"),
            correctIndex = 1,
            category = "CXC Geography"
        ),
        Question(
            text = "The Northern Range is a mountain range located in:",
            options = listOf("Jamaica", "Barbados", "Trinidad", "Saint Vincent"),
            correctIndex = 2,
            category = "CXC Geography"
        ),
        Question(
            text = "Which of the following is a greenhouse gas?",
            options = listOf("Oxygen", "Nitrogen", "Carbon dioxide", "Hydrogen"),
            correctIndex = 2,
            category = "CXC Geography"
        ),
        Question(
            text = "Contour lines on a map that are close together indicate:",
            options = listOf("Flat land", "Gentle slopes", "Steep slopes", "River valleys"),
            correctIndex = 2,
            category = "CXC Geography"
        ),
        Question(
            text = "La Soufrière is an active volcano located in:",
            options = listOf("Dominica", "Martinique", "Saint Lucia", "Saint Vincent"),
            correctIndex = 3,
            category = "CXC Geography"
        ),
        Question(
            text = "Which type of rainfall is caused by air rising over mountains?",
            options = listOf("Convectional rainfall", "Frontal rainfall", "Relief rainfall", "Cyclonic rainfall"),
            correctIndex = 2,
            category = "CXC Geography"
        )
    )


    val cxcPOBQuestions = listOf(
        Question(
            text = "Which type of business is owned and operated by one person?",
            options = listOf("Partnership", "Sole trader", "Public limited company", "Cooperative"),
            correctIndex = 1,
            category = "CXC POB"
        ),
        Question(
            text = "What does GDP stand for?",
            options = listOf("Gross Domestic Product", "General Development Plan", "Gross Development Price", "General Domestic Production"),
            correctIndex = 0,
            category = "CXC POB"
        ),
        Question(
            text = "Which of the following is a feature of a limited liability company?",
            options = listOf("Owners are personally responsible for all debts", "The business has unlimited life", "Shareholders can lose only what they invested", "Only one person can own shares"),
            correctIndex = 2,
            category = "CXC POB"
        ),
        Question(
            text = "The four Ps of marketing are Product, Price, Place and:",
            options = listOf("Profit", "Promotion", "Production", "Purchase"),
            correctIndex = 1,
            category = "CXC POB"
        ),
        Question(
            text = "Which document outlines a company's objectives and its relationship with the outside world?",
            options = listOf("Articles of Association", "Memorandum of Association", "Prospectus", "Balance Sheet"),
            correctIndex = 1,
            category = "CXC POB"
        ),
        Question(
            text = "When demand for a product increases but supply stays the same, the price will:",
            options = listOf("Fall", "Stay the same", "Rise", "Become zero"),
            correctIndex = 2,
            category = "CXC POB"
        ),
        Question(
            text = "Which of the following is an example of a variable cost?",
            options = listOf("Rent", "Insurance", "Raw materials", "Manager salary"),
            correctIndex = 2,
            category = "CXC POB"
        ),
        Question(
            text = "A cheque that cannot be cashed over the counter but must be paid into a bank account is called a:",
            options = listOf("Bearer cheque", "Crossed cheque", "Post-dated cheque", "Stale cheque"),
            correctIndex = 1,
            category = "CXC POB"
        ),
        Question(
            text = "Which of the following best describes entrepreneurship?",
            options = listOf("Working for a large corporation", "The process of starting and running a new business", "Investing in the stock market", "Managing government funds"),
            correctIndex = 1,
            category = "CXC POB"
        ),
        Question(
            text = "A balance sheet shows a business's:",
            options = listOf("Sales revenue over a period", "Assets, liabilities and capital at a point in time", "Cash flowing in and out", "Production targets for the year"),
            correctIndex = 1,
            category = "CXC POB"
        ),
        Question(
            text = "Which type of production involves extracting raw materials from the earth?",
            options = listOf("Secondary", "Tertiary", "Primary", "Quaternary"),
            correctIndex = 2,
            category = "CXC POB"
        ),
        Question(
            text = "The central bank of Trinidad and Tobago is responsible for:",
            options = listOf("Selling goods overseas", "Controlling monetary policy", "Building infrastructure", "Collecting income tax"),
            correctIndex = 1,
            category = "CXC POB"
        ),
        Question(
            text = "Which of the following is NOT a function of money?",
            options = listOf("Medium of exchange", "Store of value", "Unit of account", "Source of production"),
            correctIndex = 3,
            category = "CXC POB"
        ),
        Question(
            text = "An invoice is sent by the seller to the buyer to:",
            options = listOf("Confirm delivery of goods", "Request payment for goods supplied", "Acknowledge receipt of payment", "List available products"),
            correctIndex = 1,
            category = "CXC POB"
        ),
        Question(
            text = "Which of the following is a disadvantage of a partnership?",
            options = listOf("More capital than sole trader", "Shared decision making", "Unlimited liability for partners", "Shared workload"),
            correctIndex = 2,
            category = "CXC POB"
        )
    )


    val cxcITQuestions = listOf(
        Question(
            text = "What does CPU stand for?",
            options = listOf("Central Processing Unit", "Computer Personal Unit", "Central Program Utility", "Core Processing Unit"),
            correctIndex = 0,
            category = "CXC IT"
        ),
        Question(
            text = "Which of the following is an example of an input device?",
            options = listOf("Monitor", "Printer", "Keyboard", "Speaker"),
            correctIndex = 2,
            category = "CXC IT"
        ),
        Question(
            text = "What does RAM stand for?",
            options = listOf("Read Access Memory", "Random Access Memory", "Rapid Application Memory", "Read Application Module"),
            correctIndex = 1,
            category = "CXC IT"
        ),
        Question(
            text = "Which of the following is an operating system?",
            options = listOf("Microsoft Word", "Google Chrome", "Windows 11", "Adobe Photoshop"),
            correctIndex = 2,
            category = "CXC IT"
        ),
        Question(
            text = "What does HTTP stand for?",
            options = listOf("HyperText Transfer Protocol", "High Transfer Text Program", "HyperText Transmission Process", "High Text Transfer Protocol"),
            correctIndex = 0,
            category = "CXC IT"
        ),
        Question(
            text = "Which storage device has no moving parts and is fastest?",
            options = listOf("Hard Disk Drive", "CD-ROM", "Floppy Disk", "Solid State Drive"),
            correctIndex = 3,
            category = "CXC IT"
        ),
        Question(
            text = "A collection of related records in a database is called a:",
            options = listOf("Field", "Table", "Query", "Form"),
            correctIndex = 1,
            category = "CXC IT"
        ),
        Question(
            text = "Which of the following is malicious software designed to damage a computer?",
            options = listOf("Firewall", "Antivirus", "Virus", "Browser"),
            correctIndex = 2,
            category = "CXC IT"
        ),
        Question(
            text = "What is the binary equivalent of the decimal number 10?",
            options = listOf("0101", "1010", "1100", "0110"),
            correctIndex = 1,
            category = "CXC IT"
        ),
        Question(
            text = "Which network covers the largest geographic area?",
            options = listOf("LAN", "MAN", "PAN", "WAN"),
            correctIndex = 3,
            category = "CXC IT"
        ),
        Question(
            text = "Which of the following is an example of application software?",
            options = listOf("Windows 10", "Device drivers", "Microsoft Excel", "BIOS"),
            correctIndex = 2,
            category = "CXC IT"
        ),
        Question(
            text = "What does URL stand for?",
            options = listOf("Uniform Resource Locator", "Universal Remote Link", "Unified Record Location", "Uniform Routing Link"),
            correctIndex = 0,
            category = "CXC IT"
        ),
        Question(
            text = "Which of the following is an output device?",
            options = listOf("Scanner", "Microphone", "Projector", "Webcam"),
            correctIndex = 2,
            category = "CXC IT"
        ),
        Question(
            text = "What is the main function of a firewall?",
            options = listOf("Speed up internet connection", "Store backup files", "Block unauthorised network access", "Manage email accounts"),
            correctIndex = 2,
            category = "CXC IT"
        ),
        Question(
            text = "Which of the following file extensions is associated with a spreadsheet?",
            options = listOf(".docx", ".pptx", ".xlsx", ".pdf"),
            correctIndex = 2,
            category = "CXC IT"
        )
    )


    val cxcOfficeAdminQuestions = listOf(
        Question(
            text = "Which of the following is a function of a receptionist?",
            options = listOf("Managing company accounts", "Greeting and directing visitors", "Repairing office equipment", "Writing company policy"),
            correctIndex = 1,
            category = "CXC Office Admin"
        ),
        Question(
            text = "Which filing system arranges records in order from A to Z?",
            options = listOf("Numerical", "Geographical", "Alphabetical", "Chronological"),
            correctIndex = 2,
            category = "CXC Office Admin"
        ),
        Question(
            text = "A memorandum is used for communication:",
            options = listOf("Between two companies", "Within an organisation", "To customers only", "To government offices"),
            correctIndex = 1,
            category = "CXC Office Admin"
        ),
        Question(
            text = "Which of the following is an example of reprographic equipment?",
            options = listOf("Stapler", "Photocopier", "Filing cabinet", "Telephone"),
            correctIndex = 1,
            category = "CXC Office Admin"
        ),
        Question(
            text = "The petty cash book is used to record:",
            options = listOf("Large business transactions", "Employee salaries", "Small day-to-day expenses", "Bank deposits"),
            correctIndex = 2,
            category = "CXC Office Admin"
        ),
        Question(
            text = "Which of the following is the correct layout for a formal business letter?",
            options = listOf("Date, salutation, heading, body, closing", "Heading, date, inside address, salutation, body, closing", "Salutation, body, date, closing, heading", "Body, date, inside address, closing"),
            correctIndex = 1,
            category = "CXC Office Admin"
        ),
        Question(
            text = "What is the purpose of an agenda in a meeting?",
            options = listOf("To record what was discussed", "To outline the topics to be discussed", "To list attendees only", "To confirm the meeting venue"),
            correctIndex = 1,
            category = "CXC Office Admin"
        ),
        Question(
            text = "Minutes of a meeting are:",
            options = listOf("A plan for the next meeting", "An official record of what was discussed and decided", "A list of people invited", "A financial summary"),
            correctIndex = 1,
            category = "CXC Office Admin"
        ),
        Question(
            text = "Which of the following is a primary storage method for physical documents?",
            options = listOf("Cloud storage", "USB drive", "Filing cabinet", "Email"),
            correctIndex = 2,
            category = "CXC Office Admin"
        ),
        Question(
            text = "Which type of communication uses body language and facial expressions?",
            options = listOf("Written communication", "Oral communication", "Non-verbal communication", "Electronic communication"),
            correctIndex = 2,
            category = "CXC Office Admin"
        ),
        Question(
            text = "An office that has all departments in one large open space is called a:",
            options = listOf("Private office", "Closed office", "Open-plan office", "Virtual office"),
            correctIndex = 2,
            category = "CXC Office Admin"
        ),
        Question(
            text = "Which of the following is an electronic method of communication?",
            options = listOf("Memorandum", "Notice board", "Email", "Letter"),
            correctIndex = 2,
            category = "CXC Office Admin"
        ),
        Question(
            text = "The person who chairs a meeting is called the:",
            options = listOf("Secretary", "Treasurer", "Chairperson", "Recorder"),
            correctIndex = 2,
            category = "CXC Office Admin"
        ),
        Question(
            text = "Which filing system organises records by date?",
            options = listOf("Alphabetical", "Numerical", "Geographical", "Chronological"),
            correctIndex = 3,
            category = "CXC Office Admin"
        ),
        Question(
            text = "What is the main purpose of a telephone message pad?",
            options = listOf("To send faxes", "To record messages when someone is unavailable", "To list office supplies", "To track employee hours"),
            correctIndex = 1,
            category = "CXC Office Admin"
        )
    )


    val cxcPEQuestions = listOf(
        Question(
            text = "Which of the following is a component of physical fitness?",
            options = listOf("Intelligence", "Cardiovascular endurance", "Memory", "Creativity"),
            correctIndex = 1,
            category = "CXC Physical Education"
        ),
        Question(
            text = "The heart rate measured when the body is at complete rest is called:",
            options = listOf("Maximum heart rate", "Working heart rate", "Resting heart rate", "Recovery heart rate"),
            correctIndex = 2,
            category = "CXC Physical Education"
        ),
        Question(
            text = "Which body system is responsible for transporting oxygen to muscles?",
            options = listOf("Digestive system", "Nervous system", "Circulatory system", "Skeletal system"),
            correctIndex = 2,
            category = "CXC Physical Education"
        ),
        Question(
            text = "What is the term for the range of motion available at a joint?",
            options = listOf("Strength", "Flexibility", "Agility", "Power"),
            correctIndex = 1,
            category = "CXC Physical Education"
        ),
        Question(
            text = "Which vitamin is produced by the body when exposed to sunlight?",
            options = listOf("Vitamin A", "Vitamin B", "Vitamin C", "Vitamin D"),
            correctIndex = 3,
            category = "CXC Physical Education"
        ),
        Question(
            text = "A sprain is an injury to a:",
            options = listOf("Muscle", "Bone", "Ligament", "Tendon"),
            correctIndex = 2,
            category = "CXC Physical Education"
        ),
        Question(
            text = "Which of the following best describes aerobic exercise?",
            options = listOf("Short bursts of high intensity activity", "Exercise that requires oxygen over a sustained period", "Lifting heavy weights", "Stretching and flexibility work"),
            correctIndex = 1,
            category = "CXC Physical Education"
        ),
        Question(
            text = "How many players are on a standard basketball team on the court?",
            options = listOf("4", "5", "6", "7"),
            correctIndex = 1,
            category = "CXC Physical Education"
        ),
        Question(
            text = "The FITT principle stands for Frequency, Intensity, Time and:",
            options = listOf("Technique", "Training", "Type", "Timing"),
            correctIndex = 2,
            category = "CXC Physical Education"
        ),
        Question(
            text = "Which of the following is a bone in the human leg?",
            options = listOf("Humerus", "Radius", "Femur", "Ulna"),
            correctIndex = 2,
            category = "CXC Physical Education"
        ),
        Question(
            text = "What does BMI stand for?",
            options = listOf("Body Mass Index", "Basic Muscle Intensity", "Body Movement Index", "Basic Mass Indicator"),
            correctIndex = 0,
            category = "CXC Physical Education"
        ),
        Question(
            text = "Which nutrient is the body's preferred source of energy during exercise?",
            options = listOf("Protein", "Fat", "Carbohydrates", "Vitamins"),
            correctIndex = 2,
            category = "CXC Physical Education"
        ),
        Question(
            text = "In volleyball, how many touches is each team allowed before returning the ball?",
            options = listOf("2", "3", "4", "5"),
            correctIndex = 1,
            category = "CXC Physical Education"
        ),
        Question(
            text = "Which of the following is a principle of training?",
            options = listOf("Confusion", "Overload", "Underperformance", "Isolation"),
            correctIndex = 1,
            category = "CXC Physical Education"
        ),
        Question(
            text = "First aid treatment for a minor burn is to:",
            options = listOf("Apply butter or oil", "Cover with a dry cloth", "Run cool water over it for 10 minutes", "Pop any blisters immediately"),
            correctIndex = 2,
            category = "CXC Physical Education"
        )
    )

    fun getAllQuestions(): List<Question> =
        caribbeanHistory + scienceTech + sports + worldGeo + artsCulture + svgVincy + cxcEnglishA + cxcEnglishB
}
