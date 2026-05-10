import json, os

OUT = "app/src/main/assets/questions"
os.makedirs(OUT, exist_ok=True)

fixes = {

"cxc_social_studies_l1.json": [
  {"question":"What is the definition of culture?","options":["Only music and art","The way of life of a group of people","Government rules","Religious beliefs only"],"correctIndex":1},
  {"question":"Which of these is a primary socialisation agent?","options":["School","Family","Media","Church"],"correctIndex":1},
  {"question":"What does 'democracy' mean?","options":["Rule by the military","Rule by one person","Government by the people","Rule by religion"],"correctIndex":2},
  {"question":"What is the main function of the family?","options":["To pay taxes","To nurture and socialise children","To make laws","To build roads"],"correctIndex":1},
  {"question":"Which of these best describes a 'society'?","options":["A type of school","A group of people sharing a territory and culture","A government building","A single family unit"],"correctIndex":1},
  {"question":"What is 'gender'?","options":["Biological sex only","Social and cultural roles assigned to males and females","A school subject","A type of work"],"correctIndex":1},
  {"question":"What does 'migration' mean?","options":["Growing crops","Moving from one place to another to live","Celebrating a festival","Trading goods"],"correctIndex":1},
  {"question":"Which of these is a social institution?","options":["A mountain","The family","A river","A car"],"correctIndex":1},
  {"question":"What is 'nation'?","options":["Only a government","A group of people sharing identity, history and often territory","A type of economy","A religious group only"],"correctIndex":1},
  {"question":"What does 'social class' refer to?","options":["School classes","Grouping of people based on wealth, education or occupation","Age groups","Family size"],"correctIndex":1},
  {"question":"Which of these is an example of cultural diffusion?","options":["A family eating together","Adopting another culture's food or music","Going to school","Paying taxes"],"correctIndex":1},
  {"question":"What is 'discrimination'?","options":["Treating everyone equally","Unfair treatment of people based on race, gender or other characteristics","A type of tax","A government policy"],"correctIndex":1},
  {"question":"What does 'socialisation' mean?","options":["Making friends only","Process by which people learn the norms and values of their society","Going to parties","Joining clubs"],"correctIndex":1},
  {"question":"Which of these is a human right?","options":["Right to unlimited wealth","Right to a fair trial","Right to own others","Right to break laws"],"correctIndex":1},
  {"question":"What is the role of government?","options":["To control citizens completely","To make and enforce laws and provide services for the people","To run private businesses","To teach in schools"],"correctIndex":1}
],

"cxc_pob_l1.json": [
  {"question":"What is a 'business'?","options":["Only a large company","An organisation that produces goods or services to satisfy needs and wants","A government department","A school"],"correctIndex":1},
  {"question":"Which of these is a factor of production?","options":["Money in your pocket","Land, Labour, Capital and Enterprise","Only machinery","Only workers"],"correctIndex":1},
  {"question":"What does 'profit' mean?","options":["Total sales revenue","Revenue minus all costs","Money borrowed","Goods produced"],"correctIndex":1},
  {"question":"What is a 'sole trader'?","options":["A business owned by two people","A business owned and run by one person","A government business","A large corporation"],"correctIndex":1},
  {"question":"Which of these is a type of business ownership?","options":["Democracy","Partnership","Parliament","Census"],"correctIndex":1},
  {"question":"What is 'demand' in economics?","options":["What businesses want to produce","The quantity of goods consumers are willing and able to buy at a given price","Government requirements","Imports from abroad"],"correctIndex":1},
  {"question":"What is the purpose of a business plan?","options":["To list employees","To outline goals, strategies and financial projections for a business","To pay taxes","To advertise products"],"correctIndex":1},
  {"question":"Which of these is a fixed cost?","options":["Raw materials","Rent for premises","Sales commission","Packaging costs"],"correctIndex":1},
  {"question":"What does 'supply' mean in business?","options":["What consumers want","The quantity of goods producers are willing to sell at a given price","Government provision","Imported goods"],"correctIndex":1},
  {"question":"What is 'marketing'?","options":["Only advertising","Activities promoting and selling products including research, advertising and distribution","Only selling","Only making products"],"correctIndex":1},
  {"question":"What is a 'limited liability' company?","options":["A company with no debts","A company where owners' financial responsibility is limited to their investment","A very small company","A government company"],"correctIndex":1},
  {"question":"What does 'break-even' mean?","options":["When a business fails","When total revenue equals total costs — neither profit nor loss","When profit is highest","When costs are zero"],"correctIndex":1},
  {"question":"Which of these is an internal stakeholder?","options":["A customer","A supplier","An employee","A competitor"],"correctIndex":2},
  {"question":"What is 'entrepreneurship'?","options":["Working for someone else","Starting and running a new business taking on financial risk","Managing a government office","Studying business"],"correctIndex":1},
  {"question":"What does 'invoice' mean?","options":["An advertisement","A document showing goods supplied and amount owed","A bank statement","A business plan"],"correctIndex":1}
],

"cxc_geography_l1.json": [
  {"question":"What is a 'map'?","options":["A type of graph","A flat representation of the Earth's surface","A photograph","A weather chart"],"correctIndex":1},
  {"question":"What does 'latitude' measure?","options":["Distance east or west","Distance north or south of the equator","Height above sea level","Distance from the coast"],"correctIndex":1},
  {"question":"What is the equator?","options":["The prime meridian","An imaginary line at 0° dividing Earth into Northern and Southern hemispheres","A mountain range","A major river"],"correctIndex":1},
  {"question":"What is 'erosion'?","options":["Building up of land","Wearing away of rock and soil by wind, water or ice","Growing of crops","Formation of mountains"],"correctIndex":1},
  {"question":"What type of climate does the Caribbean have?","options":["Polar","Temperate","Tropical","Desert"],"correctIndex":2},
  {"question":"What is a 'river delta'?","options":["The source of a river","Fan-shaped deposit of sediment at a river's mouth","A waterfall","A type of lake"],"correctIndex":1},
  {"question":"What is 'population density'?","options":["Total population of a country","Number of people per unit area","Rate of population growth","Number of cities"],"correctIndex":1},
  {"question":"What causes seasons?","options":["Distance from the sun","Tilt of Earth's axis as it orbits the sun","Moon's gravity","Cloud cover"],"correctIndex":1},
  {"question":"What is a 'hurricane'?","options":["A light breeze","A large rotating tropical storm with strong winds","A type of rainfall","A cold front"],"correctIndex":1},
  {"question":"What does 'deforestation' cause?","options":["More rainfall","Soil erosion, flooding and loss of biodiversity","Better farming","Cooler temperatures"],"correctIndex":1},
  {"question":"What is 'urbanisation'?","options":["Building farms","Growth of cities as people move from rural to urban areas","Cutting down trees","Ocean pollution"],"correctIndex":1},
  {"question":"What is a 'contour line' on a map?","options":["A road","A line connecting points of equal elevation","A river","A political boundary"],"correctIndex":1},
  {"question":"What is 'coral reef'?","options":["An underwater mountain","Marine ecosystem built by coral polyps; found in warm shallow waters","A type of seaweed","An ocean current"],"correctIndex":1},
  {"question":"What is the 'water cycle'?","options":["Water flowing in a pipe","Continuous movement of water through evaporation, condensation and precipitation","Ocean tides","River flooding"],"correctIndex":1},
  {"question":"Which of these is a renewable resource?","options":["Coal","Oil","Natural gas","Solar energy"],"correctIndex":3}
],

"caribbean_history_l1.json": [
  {"question":"Who were the first known inhabitants of the Caribbean?","options":["Europeans","African slaves","Arawak and Carib indigenous peoples","Chinese immigrants"],"correctIndex":2},
  {"question":"In what year did Christopher Columbus arrive in the Caribbean?","options":["1392","1492","1592","1692"],"correctIndex":1},
  {"question":"What was the main purpose of the plantation system?","options":["Growing food for locals","Producing cash crops for export using enslaved labour","Building cities","Trading with indigenous peoples"],"correctIndex":1},
  {"question":"From where were enslaved Africans brought to the Caribbean?","options":["Europe","Asia","West Africa","North America"],"correctIndex":2},
  {"question":"What was 'emancipation'?","options":["A type of crop","The freeing of enslaved people","A colonial tax","A type of ship"],"correctIndex":1},
  {"question":"In which year was slavery abolished in British Caribbean colonies?","options":["1808","1833","1838","1865"],"correctIndex":2},
  {"question":"What was the 'Middle Passage'?","options":["A mountain route","The sea journey of enslaved Africans across the Atlantic","A trade route for spices","A type of plantation"],"correctIndex":1},
  {"question":"Which country colonised Jamaica?","options":["France","Spain then Britain","Portugal","Netherlands"],"correctIndex":1},
  {"question":"What were 'indentured workers'?","options":["Free workers","Workers brought on fixed contracts mainly from India after emancipation","Enslaved people","European farmers"],"correctIndex":1},
  {"question":"What was the Haitian Revolution?","options":["A peaceful election","The first successful slave revolt leading to Haiti's independence in 1804","A European invasion","A trade agreement"],"correctIndex":1},
  {"question":"What crops were mainly grown on Caribbean plantations?","options":["Wheat and corn","Sugar, coffee, tobacco and cotton","Rice and potatoes","Fruits and vegetables"],"correctIndex":1},
  {"question":"What was 'colonialism'?","options":["A farming method","Control of one country by a more powerful nation","A type of trade","A religious movement"],"correctIndex":1},
  {"question":"Which European countries colonised the Caribbean?","options":["Russia and China","Britain, France, Spain, Netherlands and others","Only Britain","Only Spain"],"correctIndex":1},
  {"question":"What was the significance of 1962 for Jamaica and Trinidad?","options":["They joined CARICOM","They gained independence from Britain","They were colonised","They abolished slavery"],"correctIndex":1},
  {"question":"What was the West Indies Federation?","options":["A cricket team","A political union of British Caribbean territories that lasted 1958–1962","A trade agreement","A cultural organisation"],"correctIndex":1}
],

"cxc_english_b_l1.json": [
  {"question":"What is 'prose'?","options":["Writing in verse","Ordinary written or spoken language without a regular metrical pattern","Only fiction","Only poetry"],"correctIndex":1},
  {"question":"What is the 'narrator' of a story?","options":["The main character","The person or voice telling the story","The villain","The author always"],"correctIndex":1},
  {"question":"What is 'theme' in literature?","options":["The setting of a story","The central idea or message explored in a literary work","The main character","The title"],"correctIndex":1},
  {"question":"What is 'characterisation'?","options":["Listing characters","Methods an author uses to create and develop characters","The setting","The plot"],"correctIndex":1},
  {"question":"What is 'conflict' in a story?","options":["A peaceful moment","The struggle between opposing forces driving the plot","The ending","The introduction"],"correctIndex":1},
  {"question":"What does 'point of view' mean in literature?","options":["An opinion","The perspective from which a story is told","The setting","The theme"],"correctIndex":1},
  {"question":"What is 'first person' narration?","options":["The third person telling the story","Story told using 'I' by a character within the story","Story with no narrator","Only used in poetry"],"correctIndex":1},
  {"question":"What is 'foreshadowing'?","options":["Describing the weather","Hints or clues about events that will happen later in the story","Describing a character","The ending of a story"],"correctIndex":1},
  {"question":"What is 'irony'?","options":["A type of rhyme","When the intended meaning differs from the literal meaning or expectation","A type of character","A story structure"],"correctIndex":1},
  {"question":"What is the 'climax' of a story?","options":["The beginning","The point of highest tension or turning point in the plot","The setting","The first paragraph"],"correctIndex":1},
  {"question":"What is a 'symbol' in literature?","options":["A punctuation mark","An object, person or place representing something beyond its literal meaning","A character's name","A type of setting"],"correctIndex":1},
  {"question":"What does 'tone' mean in literature?","options":["The sound of reading","The author's attitude toward the subject conveyed through word choice","The volume","The pace"],"correctIndex":1},
  {"question":"What is 'dialogue' in a literary work?","options":["Description of setting","Conversation between characters","Internal thoughts","The narrator's voice"],"correctIndex":1},
  {"question":"What is a 'short story'?","options":["A poem","A brief fictional prose narrative with few characters and a single main event","A chapter of a novel","A play"],"correctIndex":1},
  {"question":"What is 'imagery' in literature?","options":["Photographs in a book","Descriptive language that appeals to the senses","A type of character","The plot structure"],"correctIndex":1}
],

"sports_l1.json": [
  {"question":"How many players are in a football (soccer) team?","options":["9","10","11","12"],"correctIndex":2},
  {"question":"Which Caribbean nation is famous for producing world-class sprinters?","options":["Barbados","Jamaica","Trinidad","Guyana"],"correctIndex":1},
  {"question":"What sport is played at Kensington Oval in Barbados?","options":["Football","Tennis","Cricket","Athletics"],"correctIndex":2},
  {"question":"How many points is a try worth in rugby union?","options":["3","4","5","6"],"correctIndex":2},
  {"question":"Which of these is the governing body of world football?","options":["ICC","FIFA","IAAF","NBA"],"correctIndex":1},
  {"question":"What is the length of an Olympic swimming pool?","options":["25 metres","50 metres","75 metres","100 metres"],"correctIndex":1},
  {"question":"How many players are on a basketball team on court at one time?","options":["4","5","6","7"],"correctIndex":1},
  {"question":"Who won the most Olympic gold medals in sprinting representing Jamaica?","options":["Asafa Powell","Yohan Blake","Usain Bolt","Donald Quarrie"],"correctIndex":2},
  {"question":"What is the distance of a standard marathon race?","options":["21.1 km","26.2 miles (42.2 km)","30 km","50 km"],"correctIndex":1},
  {"question":"In cricket, how many balls are in a standard over?","options":["4","5","6","8"],"correctIndex":2},
  {"question":"Which of these is a Caribbean sporting competition?","options":["Copa America","Caribbean Games","CARIFTA Games","Pan-African Games"],"correctIndex":2},
  {"question":"What sport does Brian Lara represent the Caribbean in?","options":["Football","Athletics","Tennis","Cricket"],"correctIndex":3},
  {"question":"How high is a regulation basketball hoop from the floor?","options":["8 feet","10 feet","12 feet","9 feet"],"correctIndex":1},
  {"question":"What is a 'hat-trick' in football?","options":["A special kick","Scoring three goals in one match","Saving three penalties","Three yellow cards"],"correctIndex":1},
  {"question":"Which country hosts the annual Tour de France cycling race?","options":["Italy","Spain","France","Belgium"],"correctIndex":2}
],

"science_tech_l1.json": [
  {"question":"What is the basic unit of life?","options":["Atom","Cell","Organ","Tissue"],"correctIndex":1},
  {"question":"What gas do plants absorb during photosynthesis?","options":["Oxygen","Nitrogen","Carbon dioxide","Hydrogen"],"correctIndex":2},
  {"question":"What is the speed of light approximately?","options":["300 km/s","3,000 km/s","300,000 km/s","30,000 km/s"],"correctIndex":2},
  {"question":"What does DNA stand for?","options":["Deoxyribonucleic Acid","Deoxyribonicotinic Acid","Dinitrogen Acid","Deoxyribose Nucleotide Array"],"correctIndex":0},
  {"question":"What is the internet?","options":["A single computer","A global network connecting millions of computers","A type of software","A television network"],"correctIndex":1},
  {"question":"What planet is known as the Red Planet?","options":["Venus","Jupiter","Mars","Saturn"],"correctIndex":2},
  {"question":"What is photosynthesis?","options":["Animals eating plants","Process where plants make food using sunlight, water and CO2","Plants absorbing water","Animals breathing"],"correctIndex":1},
  {"question":"What does a 'CPU' do in a computer?","options":["Store data permanently","Display images","Process instructions and calculations","Connect to internet"],"correctIndex":2},
  {"question":"What is electricity?","options":["A type of light","Flow of electric charge through a conductor","A form of heat","A type of magnetism"],"correctIndex":1},
  {"question":"What is the function of the heart?","options":["Filter blood","Pump blood around the body","Produce blood cells","Control breathing"],"correctIndex":1},
  {"question":"What is 'renewable energy'?","options":["Energy from oil","Energy from sources that naturally replenish like sun and wind","Energy from coal","Nuclear energy"],"correctIndex":1},
  {"question":"What is the role of the ozone layer?","options":["Produce oxygen","Protect Earth from harmful UV radiation","Cause rainfall","Regulate temperature"],"correctIndex":1},
  {"question":"What does RAM stand for in computing?","options":["Random Access Memory","Read And Modify","Rapid Application Mode","Remote Access Module"],"correctIndex":0},
  {"question":"What is gravity?","options":["A type of electricity","Force that attracts objects with mass toward each other","A form of light","A type of wave"],"correctIndex":1},
  {"question":"What is an 'ecosystem'?","options":["A computer system","Community of living organisms interacting with their environment","A weather system","A type of government"],"correctIndex":1}
],

"cxc_english_a_l1.json": [
  {"question":"What is the purpose of a topic sentence?","options":["To end a paragraph","To introduce the main idea of a paragraph","To provide evidence","To ask a question"],"correctIndex":1},
  {"question":"Which punctuation mark introduces a list?","options":["Comma","Full stop","Colon","Semicolon"],"correctIndex":2},
  {"question":"What is a 'metaphor'?","options":["A direct comparison using like or as","A direct comparison stating one thing IS another","A type of rhyme","A question form"],"correctIndex":1},
  {"question":"What is a 'compound sentence'?","options":["A sentence with one clause","Two or more independent clauses joined by a conjunction","A very long sentence","A question"],"correctIndex":1},
  {"question":"What does the word 'affect' mean?","options":["Result or outcome","To have an influence on something","A false emotion","A type of writing"],"correctIndex":1},
  {"question":"What is the object in 'The teacher marked the papers'?","options":["The teacher","Marked","The papers","Teacher"],"correctIndex":2},
  {"question":"Which of these is correctly spelled?","options":["Recieve","Receive","Receve","Receeve"],"correctIndex":1},
  {"question":"What is a 'formal letter' used for?","options":["Writing to friends","Official communication such as to employers or authorities","Personal messages","Shopping lists"],"correctIndex":1},
  {"question":"What is 'synonyms'?","options":["Words with opposite meanings","Words with similar meanings","Words that rhyme","Made-up words"],"correctIndex":1},
  {"question":"What is the purpose of a summary?","options":["To copy a text exactly","To present the main ideas of a text in your own words concisely","To add your opinion","To ask questions"],"correctIndex":1},
  {"question":"What does an 'adverb' modify?","options":["A noun","A verb, adjective or another adverb","Only nouns","Only adjectives"],"correctIndex":1},
  {"question":"What is 'active voice'?","options":["Loud reading","Sentence where the subject performs the action","Sentence where subject receives action","A type of punctuation"],"correctIndex":1},
  {"question":"Which of these is an example of 'alliteration'?","options":["She runs fast","Peter Piper picked peppers","The sun set slowly","It was a dark night"],"correctIndex":1},
  {"question":"What is a 'thesis statement'?","options":["The title of an essay","A sentence stating the main argument of an essay","The conclusion","A supporting detail"],"correctIndex":1},
  {"question":"What is 'register' in language use?","options":["A list of names","The level of formality appropriate to a situation","A type of punctuation","A grammar rule"],"correctIndex":1}
],

"svg_vincy_l1.json": [
  {"question":"What is the capital city of St. Vincent and the Grenadines?","options":["Georgetown","Bridgetown","Kingstown","Roseau"],"correctIndex":2},
  {"question":"What is the national dish of St. Vincent?","options":["Rice and peas","Roasted breadfruit and fried jackfish","Cou-cou and flying fish","Pelau"],"correctIndex":1},
  {"question":"What is the volcano in St. Vincent called?","options":["Mount Pelée","La Soufrière","Mount St. Catherine","Kick 'em Jenny"],"correctIndex":1},
  {"question":"What is the currency of St. Vincent and the Grenadines?","options":["Barbadian Dollar","Jamaican Dollar","Eastern Caribbean Dollar","US Dollar"],"correctIndex":2},
  {"question":"SVG gained independence from which country?","options":["France","USA","Britain","Netherlands"],"correctIndex":2},
  {"question":"In which year did SVG gain independence?","options":["1962","1966","1979","1983"],"correctIndex":2},
  {"question":"What is the national flower of SVG?","options":["Hibiscus","Heliconia (Lobster Claw)","Plumeria","Bougainvillea"],"correctIndex":1},
  {"question":"Which major island group makes up SVG along with the main island?","options":["The Leewards","The Grenadines","The Windwards","The Antilles"],"correctIndex":1},
  {"question":"What sea lies to the west of SVG?","options":["Atlantic Ocean","Pacific Ocean","Caribbean Sea","Gulf of Mexico"],"correctIndex":2},
  {"question":"Who is known as the 'Father of the Nation' of SVG?","options":["Ralph Gonsalves","James Mitchell","Ebenezer Joshua","Milton Cato"],"correctIndex":3},
  {"question":"What is the main hospital in SVG called?","options":["Queen Elizabeth Hospital","Eric Williams Medical Complex","Milton Cato Memorial Hospital","Georgetown Hospital"],"correctIndex":2},
  {"question":"What type of agriculture is SVG known for?","options":["Large-scale wheat farming","Banana and arrowroot cultivation","Coffee and cocoa only","Sugar cane only"],"correctIndex":1},
  {"question":"What is 'Nine Mornings' in SVG?","options":["A religious holiday","A unique pre-Christmas cultural tradition with early morning festivities","A carnival event","An independence celebration"],"correctIndex":1},
  {"question":"Which island nation is closest to SVG?","options":["Barbados","Trinidad","Grenada","St. Lucia"],"correctIndex":2},
  {"question":"What color is NOT on the SVG national flag?","options":["Green","Yellow","Blue","Red"],"correctIndex":3}
],

"world_geography_l1.json": [
  {"question":"What is the largest continent?","options":["Africa","North America","Europe","Asia"],"correctIndex":3},
  {"question":"What is the longest river in the world?","options":["Amazon","Congo","Nile","Mississippi"],"correctIndex":2},
  {"question":"Which country has the largest population?","options":["USA","India","China","Russia"],"correctIndex":2},
  {"question":"What is the capital of France?","options":["London","Berlin","Paris","Rome"],"correctIndex":2},
  {"question":"What is the largest ocean?","options":["Atlantic","Indian","Arctic","Pacific"],"correctIndex":3},
  {"question":"Which mountain is the highest in the world?","options":["K2","Mount Kilimanjaro","Mount Everest","Mont Blanc"],"correctIndex":2},
  {"question":"What is the smallest country in the world?","options":["Monaco","Liechtenstein","Vatican City","San Marino"],"correctIndex":2},
  {"question":"Which continent is the Sahara Desert located in?","options":["Asia","Australia","Africa","South America"],"correctIndex":2},
  {"question":"What is the capital of Brazil?","options":["Rio de Janeiro","São Paulo","Brasília","Salvador"],"correctIndex":2},
  {"question":"How many continents are there?","options":["5","6","7","8"],"correctIndex":2},
  {"question":"Which country is the largest by area?","options":["Canada","USA","China","Russia"],"correctIndex":3},
  {"question":"What is the capital of Australia?","options":["Sydney","Melbourne","Brisbane","Canberra"],"correctIndex":3},
  {"question":"Which of these countries is in Europe?","options":["Egypt","Morocco","Germany","Nigeria"],"correctIndex":2},
  {"question":"What ocean lies between Europe and America?","options":["Pacific","Indian","Arctic","Atlantic"],"correctIndex":3},
  {"question":"What is the capital of Japan?","options":["Beijing","Seoul","Tokyo","Bangkok"],"correctIndex":2}
],

"cxc_it_l1.json": [
  {"question":"What does 'hardware' refer to in computing?","options":["Computer programs","Physical components of a computer","Internet connections","Data files"],"correctIndex":1},
  {"question":"What does 'software' mean?","options":["Physical computer parts","Programs and applications that run on a computer","The computer screen","The keyboard"],"correctIndex":1},
  {"question":"What is the function of an operating system?","options":["Play music","Manage computer hardware and software resources","Only run games","Store documents"],"correctIndex":1},
  {"question":"What does 'CPU' stand for?","options":["Computer Processing Unit","Central Processing Unit","Core Program Utility","Computer Program Unit"],"correctIndex":1},
  {"question":"What is 'data'?","options":["Only numbers","Raw facts and figures that can be processed by a computer","Finished reports","Computer programs"],"correctIndex":1},
  {"question":"What does 'input' mean in computing?","options":["Data produced by the computer","Data entered into the computer for processing","Storing data","Displaying results"],"correctIndex":1},
  {"question":"What is a 'database'?","options":["A type of network","Organised collection of structured data for easy access and management","A programming language","A type of hardware"],"correctIndex":1},
  {"question":"What is 'email'?","options":["A type of hardware","Electronic mail — messages sent and received over the internet","A programming language","A social media platform"],"correctIndex":1},
  {"question":"What does 'http' stand for?","options":["Home Transfer Text Protocol","HyperText Transfer Protocol","High Traffic Transfer Protocol","HyperText Technical Process"],"correctIndex":1},
  {"question":"What is a 'virus' in computing?","options":["A helpful program","Malicious software that can damage files and spread to other computers","A type of hardware","An internet connection"],"correctIndex":1},
  {"question":"What is 'RAM'?","options":["Read Access Memory","Random Access Memory — temporary working memory","Remote Access Module","Rapid Application Memory"],"correctIndex":1},
  {"question":"What does 'output' mean in computing?","options":["Data entered by user","Results produced by the computer after processing","Storing information","Programs running"],"correctIndex":1},
  {"question":"What is a 'spreadsheet'?","options":["A type of printer","Software organising data in rows and columns for calculation","A word processor","A database program"],"correctIndex":1},
  {"question":"What is 'backup'?","options":["Going backwards","Creating a copy of data to protect against loss","Deleting files","Formatting a drive"],"correctIndex":1},
  {"question":"What is the internet?","options":["A single large computer","A global network of interconnected computers","A type of software","A company"],"correctIndex":1}
],

"cxc_office_admin_l1.json": [
  {"question":"What is the main purpose of office administration?","options":["Only filing documents","Ensuring the smooth running of an organisation through managing information, people and resources","Only answering phones","Only typing letters"],"correctIndex":1},
  {"question":"What is a 'memorandum' (memo)?","options":["A letter to a client","An internal written communication within an organisation","A legal document","An invoice"],"correctIndex":1},
  {"question":"What is 'filing'?","options":["Sharpening pencils","Systematically organising and storing documents for easy retrieval","Only photocopying","Only typing"],"correctIndex":1},
  {"question":"What does 'petty cash' refer to?","options":["All office money","A small fund kept for minor office expenses","Employee salaries","Money for major purchases"],"correctIndex":1},
  {"question":"What is a 'meeting agenda'?","options":["Minutes of a meeting","A list of topics to be discussed at a meeting","A report","An office schedule"],"correctIndex":1},
  {"question":"What are 'minutes' in office administration?","options":["Units of time only","An official written record of what was discussed and decided at a meeting","A type of memo","A filing system"],"correctIndex":1},
  {"question":"What is the purpose of a 'notice board'?","options":["Decoration only","Displaying information and announcements for all staff","Private messaging","Filing documents"],"correctIndex":1},
  {"question":"What is 'reception' in an office context?","options":["A party","The area where visitors are greeted and directed","A meeting room","A storage area"],"correctIndex":1},
  {"question":"What does 'confidentiality' mean in the office?","options":["Sharing all information","Keeping sensitive information private and secure","Being friendly","Working fast"],"correctIndex":1},
  {"question":"What is a 'circular letter'?","options":["A letter written in a circle","A letter sent to many people at once conveying the same information","A secret letter","A formal complaint"],"correctIndex":1},
  {"question":"What is the function of a 'photocopier'?","options":["Send emails","Make copies of documents","Shred documents","Connect to internet"],"correctIndex":1},
  {"question":"What is 'word processing'?","options":["Understanding words","Using software to create, edit and format text documents","Filing papers","Making phone calls"],"correctIndex":1},
  {"question":"What is a 'report' in business communication?","options":["Only a school assignment","A formal document presenting findings and often recommendations on a specific topic","A personal letter","An invoice"],"correctIndex":1},
  {"question":"What does 'ergonomics' mean in an office context?","options":["Office decoration","Designing the workplace to suit the worker to improve comfort and productivity","Office cleaning","Scheduling meetings"],"correctIndex":1},
  {"question":"What is 'time management' in the workplace?","options":["Watching clocks","Planning and organising tasks to use time productively and meet deadlines","Only punctuality","Working overtime"],"correctIndex":1}
],

"arts_culture_l1.json": [
  {"question":"What is 'calypso' music?","options":["A type of classical music","Caribbean musical form originating in Trinidad with topical, often humorous lyrics","A type of jazz","European folk music"],"correctIndex":1},
  {"question":"What is the term for a building designed for viewing plays and performances?","options":["Museum","Library","Theatre","Gallery"],"correctIndex":2},
  {"question":"Who painted the Mona Lisa?","options":["Michelangelo","Raphael","Leonardo da Vinci","Picasso"],"correctIndex":2},
  {"question":"What is 'reggae' music associated with?","options":["Trinidad","Barbados","Jamaica","Cuba"],"correctIndex":2},
  {"question":"What is 'sculpture'?","options":["Painting on canvas","Three-dimensional artwork created by carving, molding or assembling materials","Photography","Drawing"],"correctIndex":1},
  {"question":"What is 'carnival' in the Caribbean?","options":["Only a fairground","A major cultural festival involving music, costumes and street parades","A religious ceremony only","A sports event"],"correctIndex":1},
  {"question":"What is a 'mural'?","options":["A small painting","A large artwork painted directly on a wall","A type of sculpture","A digital artwork"],"correctIndex":1},
  {"question":"What is 'steelpan'?","options":["A kitchen utensil","A musical instrument invented in Trinidad from oil drums","A type of drum from Africa","A wind instrument"],"correctIndex":1},
  {"question":"What does 'literature' include?","options":["Only novels","Written works including fiction, poetry, drama and non-fiction","Only poetry","Only newspapers"],"correctIndex":1},
  {"question":"What is 'batik'?","options":["A type of dance","A wax-resist fabric dyeing technique producing patterned textiles","A musical style","A painting technique"],"correctIndex":1},
  {"question":"What is 'choreography'?","options":["Writing music","The art of designing and arranging dance movements","Painting a scene","Writing a play"],"correctIndex":1},
  {"question":"What is a 'folk tale'?","options":["A news article","A traditional story passed down orally through generations","A modern novel","A historical document"],"correctIndex":1},
  {"question":"What is the Sistine Chapel famous for?","options":["Its architecture only","Michelangelo's ceiling paintings depicting biblical scenes","Being the largest church","Its location"],"correctIndex":1},
  {"question":"What is 'soca' music?","options":["A type of American jazz","An energetic Caribbean music genre evolving from calypso","A type of reggae","Classical Caribbean music"],"correctIndex":1},
  {"question":"What does 'indigenous art' refer to?","options":["Art from Europe","Artworks created by the original peoples of a region","Modern digital art","Only pottery"],"correctIndex":1}
],

"cxc_integrated_science_l1.json": [
  {"question":"What is matter?","options":["Only solids","Anything that has mass and takes up space","Only liquids and gases","Only living things"],"correctIndex":1},
  {"question":"What are the three states of matter?","options":["Hot, warm and cold","Solid, liquid and gas","Hard, soft and fluid","Heavy, medium and light"],"correctIndex":1},
  {"question":"What is photosynthesis?","options":["Animals breathing","Process where plants produce food using sunlight, water and carbon dioxide","Plants drinking water","Animals eating plants"],"correctIndex":1},
  {"question":"What does the heart do?","options":["Digest food","Pump blood throughout the body","Filter waste","Produce hormones"],"correctIndex":1},
  {"question":"What is an atom?","options":["The largest particle","The smallest unit of a chemical element","A type of molecule","A compound"],"correctIndex":1},
  {"question":"What force keeps planets orbiting the sun?","options":["Magnetism","Electricity","Gravity","Wind"],"correctIndex":2},
  {"question":"What is 'reproduction' in living things?","options":["Getting food","Process by which organisms produce offspring","Growing larger","Moving around"],"correctIndex":1},
  {"question":"What is the chemical symbol for water?","options":["WA","HO","H2O","W2O"],"correctIndex":2},
  {"question":"What is 'energy'?","options":["A type of matter","The capacity to do work or cause change","Only electricity","Only heat"],"correctIndex":1},
  {"question":"What are 'vertebrates'?","options":["Animals without a backbone","Animals with a backbone or spinal column","Only mammals","Only fish"],"correctIndex":1},
  {"question":"What is the function of the lungs?","options":["Pump blood","Exchange oxygen and carbon dioxide during breathing","Digest food","Filter blood"],"correctIndex":1},
  {"question":"What is 'friction'?","options":["A type of energy","Force that opposes motion between two surfaces in contact","A type of wave","Magnetic force"],"correctIndex":1},
  {"question":"What is 'nutrition' in biology?","options":["Only eating","Process of obtaining and using food for energy, growth and repair","Only drinking water","Only breathing"],"correctIndex":1},
  {"question":"What is a 'food chain'?","options":["A restaurant chain","Sequence showing how energy passes from one organism to another through feeding","A type of ecosystem","A farming method"],"correctIndex":1},
  {"question":"What does 'biodegradable' mean?","options":["Never breaks down","Can be broken down naturally by bacteria or other living organisms","Only plastic","Only metal"],"correctIndex":1}
],

"cxc_pe_l1.json": [
  {"question":"What does 'Physical Education' aim to develop?","options":["Only sports skills","Physical fitness, motor skills, health knowledge and social skills","Only academic knowledge","Only teamwork"],"correctIndex":1},
  {"question":"What is 'aerobic exercise'?","options":["Exercise without oxygen","Sustained exercise requiring oxygen like running and swimming","Weightlifting only","Stretching only"],"correctIndex":1},
  {"question":"What is the function of the skeletal system?","options":["Only movement","Support, protection of organs, movement and blood cell production","Only protection","Only storing minerals"],"correctIndex":1},
  {"question":"What is 'flexibility' in fitness?","options":["Being able to run fast","Range of motion available at a joint","Muscular strength","Cardiovascular endurance"],"correctIndex":1},
  {"question":"What is a 'warm-up'?","options":["Drinking hot water","Light activity preparing the body for exercise by increasing heart rate and loosening muscles","The cooling down phase","Only stretching"],"correctIndex":1},
  {"question":"What does the heart rate measure?","options":["Blood pressure","Number of times the heart beats per minute","Breathing rate","Body temperature"],"correctIndex":1},
  {"question":"What is 'muscular endurance'?","options":["Maximum strength of a muscle","Ability of a muscle to repeat contractions over a period of time","Speed of movement","Flexibility"],"correctIndex":1},
  {"question":"What is the main muscle used in breathing?","options":["Bicep","Heart","Diaphragm","Quadriceps"],"correctIndex":2},
  {"question":"What does FITT stand for in exercise planning?","options":["Fast Intense Total Training","Frequency Intensity Time Type","Fitness Interval Training Technique","Full Intensity Timed Training"],"correctIndex":1},
  {"question":"What is 'cool-down' after exercise?","options":["Drinking cold water","Gentle activity gradually lowering heart rate and stretching muscles after exercise","Taking a cold shower","Resting immediately"],"correctIndex":1},
  {"question":"What is 'sportsmanship'?","options":["Only winning","Fair, ethical and generous behaviour in sport","Aggressive play","Only following rules"],"correctIndex":1},
  {"question":"What is 'cardiovascular fitness'?","options":["Strength of muscles","Efficiency of the heart and lungs in delivering oxygen during sustained exercise","Flexibility","Balance"],"correctIndex":1},
  {"question":"What is a 'sprain'?","options":["A broken bone","Injury to a ligament caused by overstretching","A muscle tear","A skin cut"],"correctIndex":1},
  {"question":"What is 'BMI'?","options":["Body Mass Index — ratio of weight to height used to assess healthy weight","Best Muscle Indicator","Body Measurement Index","Basic Movement Indicator"],"correctIndex":0},
  {"question":"Which of these is a benefit of regular physical activity?","options":["Weakens the heart","Reduces risk of chronic diseases and improves mental health","Decreases flexibility","Weakens bones"],"correctIndex":1}
],

"cxc_maths_l1.json": [
  {"question":"What is the probability of rolling an even number on a standard die?","options":["1/6","1/3","1/2","2/3"],"correctIndex":2},
  {"question":"What is the value of 2³ × 3²?","options":["36","54","72","48"],"correctIndex":2},
  {"question":"Express 0.35 as a fraction in its simplest form.","options":["35/100","7/20","7/10","1/3"],"correctIndex":1},
  {"question":"What is the perimeter of a rectangle with length 12 cm and width 5 cm?","options":["30 cm","34 cm","60 cm","17 cm"],"correctIndex":1},
  {"question":"What is the LCM of 4, 6 and 8?","options":["12","16","24","48"],"correctIndex":2},
  {"question":"Factorise x² - 9.","options":["(x-9)(x+1)","(x-3)²","(x+3)(x-3)","(x+9)(x-1)"],"correctIndex":2},
  {"question":"Convert 3/4 to a percentage.","options":["34%","70%","75%","80%"],"correctIndex":2},
  {"question":"What is the area of a circle with radius 7 cm? (Use π ≈ 22/7)","options":["44 cm²","154 cm²","49 cm²","22 cm²"],"correctIndex":1},
  {"question":"Simplify 4x² + 3x - 2x² + x.","options":["2x² + 4x","6x² + 4x","2x² + 2x","4x² + 2x"],"correctIndex":0},
  {"question":"What is 15% of 200?","options":["15","25","30","35"],"correctIndex":2},
  {"question":"If a = 3 and b = -2, what is the value of 2a - 3b?","options":["0","6","12","2"],"correctIndex":2},
  {"question":"Solve: 3x + 7 = 22.","options":["x = 3","x = 4","x = 5","x = 6"],"correctIndex":2},
  {"question":"What is the HCF of 24 and 36?","options":["6","8","12","18"],"correctIndex":2},
  {"question":"What is the gradient of a line passing through (0, 2) and (4, 10)?","options":["1","2","3","4"],"correctIndex":1},
  {"question":"A triangle has angles of 90° and 35°. What is the third angle?","options":["45°","55°","65°","75°"],"correctIndex":1}
]

}

count = 0
for filename, questions in fixes.items():
    filepath = os.path.join(OUT, filename)
    with open(filepath, 'w') as f:
        json.dump(questions, f, indent=2)
    print(f"Fixed: {filename}")
    count += 1

print(f"\nAll done! Fixed {count} files.")
