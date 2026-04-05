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
        "⚽ Sports",
        "🗺️ World Geography",
        "🎭 Arts & Culture",
        "🇻🇨 SVG & Vincy Life"
    )

    private fun q(text: String, opts: String, correct: Int, cat: String) =
        Question(text, opts.split("|"), correct, cat)

    // ── 1. CARIBBEAN HISTORY (17 questions) ──────────────────

    private val caribbeanHistory = listOf(
        q("Which country was the FIRST Caribbean nation to gain independence?",
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
        q("Which Caribbean nation was the last to gain independence from Britain (1983)?",
            "St. Kitts and Nevis|Belize|St. Vincent|Antigua", 0, "🌍 Caribbean History"),
        q("The Grenada Revolution of 1979 was led by which political movement?",
            "GULP|New Jewel Movement|NDC|GNP", 1, "🌍 Caribbean History")
    )

    // ── 2. SCIENCE & TECH (17 questions) ─────────────────────

    private val scienceTech = listOf(
        q("What does DNA stand for?",
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
        q("What is the boiling point of water in Celsius?",
            "90|95|100|105", 2, "🧪 Science & Tech"),
        q("Which organ produces insulin in the human body?",
            "Liver|Kidney|Stomach|Pancreas", 3, "🧪 Science & Tech")
    )

    // ── 3. SPORTS (17 questions) ──────────────────────────────

    private val sports = listOf(
        q("Which country won the FIFA World Cup in 2022?",
            "France|Brazil|Argentina|Germany", 2, "⚽ Sports"),
        q("How many players from each team are on the court in basketball?",
            "4|5|6|7", 1, "⚽ Sports"),
        q("Usain Bolt, the world's fastest man, is from which Caribbean country?",
            "Trinidad|Barbados|Jamaica|Bahamas", 2, "⚽ Sports"),
        q("Which country has won the most Cricket World Cups?",
            "Australia|West Indies|India|England", 0, "⚽ Sports"),
        q("In tennis, what is the term for a score of 40-40?",
            "Tie|Deuce|Set Point|Match Point", 1, "⚽ Sports"),
        q("The Summer Olympic Games are held every how many years?",
            "2|3|4|5", 2, "⚽ Sports"),
        q("Chris Gayle is associated with which Caribbean cricket team?",
            "Trinidad|Barbados|Jamaica|Guyana", 2, "⚽ Sports"),
        q("Which sport uses a shuttlecock?",
            "Squash|Badminton|Volleyball|Polo", 1, "⚽ Sports"),
        q("How many holes are played in a standard round of golf?",
            "9|12|18|21", 2, "⚽ Sports"),
        q("The Shot Put is a discipline in which sport?",
            "Swimming|Athletics|Gymnastics|Weightlifting", 1, "⚽ Sports"),
        q("Serena Williams is celebrated for which sport?",
            "Golf|Tennis|Basketball|Volleyball", 1, "⚽ Sports"),
        q("Which Caribbean nation is famous for its Winter Olympics bobsled team?",
            "Trinidad|Jamaica|Barbados|Cuba", 1, "⚽ Sports"),
        q("In which country was the sport of cricket invented?",
            "Australia|West Indies|England|India", 2, "⚽ Sports"),
        q("What colour jersey does the leader wear in the Tour de France?",
            "Red|Green|Yellow|Blue", 2, "⚽ Sports"),
        q("How many individual events make up a Decathlon?",
            "8|10|12|15", 1, "⚽ Sports"),
        q("The FIFA World Cup is held every how many years?",
            "2|3|4|6", 2, "⚽ Sports"),
        q("Which Caribbean nation won gold in the men's 4x100m relay at the 2008 Beijing Olympics?",
            "Trinidad|Jamaica|Bahamas|Cuba", 1, "⚽ Sports")
    )

    // ── 4. WORLD GEOGRAPHY (16 questions) ─────────────────────

    private val worldGeo = listOf(
        q("What is the largest continent by land area?",
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
        q("The Strait of Hormuz connects the Persian Gulf to which body of water?",
            "Red Sea|Gulf of Oman|Arabian Sea|Bay of Bengal", 1, "🗺️ World Geography")
    )

    // ── 5. ARTS & CULTURE (16 questions) ──────────────────────

    private val artsCulture = listOf(
        q("Who painted the world-famous Mona Lisa?",
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
        q("The Notting Hill Carnival in London primarily celebrates which cultures?",
            "Asian|Caribbean|African|Latin American", 1, "🎭 Arts & Culture")
    )

    // ── 6. SVG & VINCY LIFE (17 questions) ───────────────────

    private val svgVincy = listOf(
        q("What is the capital city of St. Vincent and the Grenadines?",
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
        q("Mustique island in the Grenadines is world-renowned for attracting which visitors?",
            "Fishermen|Royalty and celebrities|Marine scientists|Backpackers", 1, "🇻🇨 SVG & Vincy Life"),
        q("What is the name of the volcanic eruption in SVG that caused mass evacuations in 2021?",
            "Hurricane Elsa|La Soufrière eruption|Mount Bequia blast|Kingstown earthquake",
            1, "🇻🇨 SVG & Vincy Life")
    )

    fun getQuestions(category: String): List<Question> = when (category) {
        "🌍 Caribbean History" -> caribbeanHistory
        "🧪 Science & Tech"   -> scienceTech
        "⚽ Sports"            -> sports
        "🗺️ World Geography"  -> worldGeo
        "🎭 Arts & Culture"   -> artsCulture
        "🇻🇨 SVG & Vincy Life" -> svgVincy
        else -> caribbeanHistory
    }

    fun getAllQuestions(): List<Question> =
        caribbeanHistory + scienceTech + sports + worldGeo + artsCulture + svgVincy
}
