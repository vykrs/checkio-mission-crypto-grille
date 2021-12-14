"""
TESTS is a dict with all of your tests.
Keys for this will be the categories' names.
Each test is a dict with
    "input" -- input data for a user function
    "answer" -- your right answer
    "explanation" -- not necessarily a key, it's used for an additional info in animation.
"""


TESTS = {
    "Basics": [
        {
            'input': ['cardangrilletest', ['.X..', '.X..', '...X', 'X...']],
            'answer': 'actilangeslrdret',
            'explanation': 'basic test'
        },
        {
            'input': ['quickbrownfoxjumpsoverthelazydog',
                      ['X...', '...X', '..X.', '.X..']],
            'answer': 'qxwkbnjufriumcoopyeerldsatoogvhz',
            'explanation': 'long text'
        },
        {
            'input': ['pythonsstandardlibraryisveryextensiveofferingawiderangeofstuffxx',
                       ['XX..', 'X...', '.X..', '....']],
            'answer': 'pyontstsahradlndibryrivseaxeterynseoifefgvarwiindengrefofafsxxtu',
            'explanation': 'even longer text'
        },
        {
            'input': ['quickbrownfoxjumpsoverthelazydog', ['.XX.', '.XX.', '..X.', 'X...']],
            'answer': None,
            'explanation': 'bad key'
        },
        {
            'input': ['qwertyuiopasdfghjklzxcvbnmqwerty', ['...X', '....', '....', '....']],
            'answer': None,
            'explanation': 'bad key'
        },
        {
            'input': ['youshouldreadeliezeryudkowskysrationalityfromaitozombiesitsgreat',
                      ['..X.', '...X', '....', 'X..X']],
            'answer': None,
            'explanation': 'bad key'
        }
        
        
    ],
    "Extra": [
        {
            'input': ['meetmeatelevenpm', ['XX..', 'XX..', '....', '....']],
            'answer': 'memeetatenelpmev'
        },
        {
            'input': ['topsecretmessage', ['X.X.', '.X.X', '....', '....']],
            'answer': 'tsoeapcstgmreees'
        },
        {
            'input': ['jackdawslovesmyblackquartzsphinx', ['XXX.', '....', '..X.', '....']],
            'answer': 'jacdslmaywksbovelacqhtiunakrxzsp'
        },
        {
            'input': ['rotatingcardangrilleisatypeoftranspositioncipherthatusesastencil',
                       ['..X.', '..X.', 'X...', '...X']],
            'answer': 'ctrangoatringdrayiiftrlplesatoaeosnphesnpcitiiroautncihsatseselt'
        },
        {
            'input': ['testtextformymissionaboutgrilles', ['.XX.', '....', '..X.', 'X...']],
            'answer': 'ttefyomeixsttrmsasitlglbeoounris'
        },
        {
            'input': ['pythonsstandardlibraryisveryextensiveofferingawiderangeofstuffxx',
                       ['X.X.', '....', 'X.X.', '....']],
            'answer': 'poynatratshsdnldirbyevxeriastreynesogearifvfwiindnegfffsreaoxtxu'
        },
        {
            'input': ['theexampleaboveisaverysimpleandinsecurecaseofastencilcipherinsuc\
haciphercertainlettersonapagearepartofthesecretmessagetheyarehid', ['....', 'X..X', '..X.', '...X']],
            'answer': 'loxvteehaaebmipemarnspdalyvesiieafuansssereoetcchnlseeunrcciicpi\
capihenarhctelriaeraeprtastgoeneeroepstaefrctmhteegheyisaesrtdha'
        },
        {
            'input': ['inthischapterwelookatanumberofciphersystemswhicharebaseduponadif\
ferentideatothosethatwehavemetsofarinthesesystemseachletterretai\
nsitsownidentityandsothefrequenciesoftheindividuallettersoftheme\
ssagesareunchangedbuttheconstituentlettersofthedigraphsandthehig\
herorderpolygraphsareseparatedandtheiroriginalfrequenciesaregone', ['....', '....', '..XX', 'X.X.']],
            'answer': 'iarptewescinthhltmoberfcanookuaisehmswicysphetrhauapondisearedbf\
netatohotiferdestaevemtsweethhaonssesytethfareimhteerrtaleseatci\
sitdenitownsintyofureqenthandescfivndiidthieseoutshoftemteallree\
eehuncansassarggtctonsitthedbeuuertsofhettenteldpnedthhihsigraag\
rpgolyradeherropeaeratdasehsaprniiaginlfrodthrernsgareonciequeee'
        },
        {
            'input': ['roughlyspeakinganalgorithmisasequenceofinstructionsthatonemustpe\
rforminordertosolveawellformulatedproblemwewillspecifyproblemsin\
termsoftheirinputsandtheiroutputsandthealgorithmwillbethemethodo\
ftranslatingtheinputsintooutputs', ['....', '..X.', 'X..X', '...X']],
            'answer': 'phinegraokluysaghoasmeniasrlitqgneucstuteronfiicnhstepomnuastoet\
rmtodsrefrionoorfwuloalrvmeelltamoilwleedwbplesrofmsbipleeycprni\
hsineptierorftumidtprutosutahetnltitghsoarhneamdebhomdweitelthol\
tnthiefntgsrlaiaospuotnuptiuntst'
        },
        {
            'input': ['youshouldreadeliezeryudkowskysrationalityfromaitozombiesitsgreat',
                      ['...X', '....', '..X.', '.XX.']],
            'answer': 'ddryheelouoiauslyoweyssrudzakerkmyftarailiitoontritobseaieztgoms'
        },
        {
            'input': ['theideaofcognitivebiasinpsychologyworksinananalogouswayacognitiv\
ebiasisasystematicerrorinhowwethinkasopposedtoarandomerrororonet\
hatsmerelycausedbyourignorancewhereasstatisticalbiasskewsasample\
sothatitlesscloselyresemblesalargerpopulationcognitivebiasesskew\
ourbeliefssothattheylessaccuratelyrepresentthefactsandtheyskewou\
rdecisionmakinganditlessreliablyachievesourgoals', ['....', 'X.XX', '....', '...X']],
            'answer': 'fnditthecoegaioiphaovlebsyscioninnraglywankasoiociwtgiouoganyvas\
sesmeabiysitstaanwreitcehoowrhirotsoiankseodprpaoomnaendroerrtro\
lumsheatyceardesocrebwyorainghnutisceareissttlaasmspbliaaskaeews\
lcalsootestsisthbaelealylessermranocgoertipouglpasvkneitseesbwii\
ftehoaurssloitebarlatthecceusesyehpelfyrntrteaseeenwcotsysdktuha\
niinrgdemaskiaocralbnldieleisystooeaalchurvgessi'
        },
        {
            'input': ['cardangrilletest', ['..X.', '..XX', '....', 'X...']],
            'answer': 'atciesarllngdert'
        },
        {
            'input': ['qwertyuiopasdfghjklzxcvbnmqwerty', ['.X..', '..X.', '....', '.X.X']],
            'answer': 'oqpdtfwygauhiesrnjmexrkctqvyblwz'
        },
        {
            'input': ['meetmeatelevenpm', ['XX..', '.X.X', 'X.XX', '..XX']],
            'answer': None
        },
        {
            'input': ['topsecretmessage', ['....', '....', '..X.', '....']],
            'answer': None
        },
        {
            'input': ['quickbrownfoxjumpsoverthelazydog', ['.X..', '.XX.', 'X...', '....']],
            'answer': None
        },
        {
            'input': ['jackdawslovesmyblackquartzsphinx', ['....', '..X.', 'X.X.', '..X.']],
            'answer': None
        },
        {
            'input': ['rotatingcardangrilleisatypeoftranspositioncipherthatusesastencil', 
                      ['....', '..X.', 'X.X.', '.X..']],
            'answer': None
        },
        {
            'input': ['testtextformymissionaboutgrilles', ['...X', 'X...', 'X..X', '....']],
            'answer': None   
        },
        {
            'input': ['pythonsstandardlibraryisveryextensiveofferingawiderangeofstuffxx',
                      ['X...', '.X..', '...X', '...X']],
            'answer': None
        },
        {
            'input': ['theexampleaboveisaverysimpleandinsecurecaseofastencilcipherinsuc\
haciphercertainlettersonapagearepartofthesecretmessagetheyarehid', ['...X', '..X.', '....', '....']],
            'answer': None
        },
        {
            'input': ['inthischapterwelookatanumberofciphersystemswhicharebaseduponadif\
ferentideatothosethatwehavemetsofarinthesesystemseachletterretai\
nsitsownidentityandsothefrequenciesoftheindividuallettersoftheme\
ssagesareunchangedbuttheconstituentlettersofthedigraphsandthehig\
herorderpolygraphsareseparatedandtheiroriginalfrequenciesaregone', ['....', '....', '.X.X', '..X.']],
            'answer': None
        },
        {
            'input': ['roughlyspeakinganalgorithmisasequenceofinstructionsthatonemustpe\
rforminordertosolveawellformulatedproblemwewillspecifyproblemsin\
termsoftheirinputsandtheiroutputsandthealgorithmwillbethemethodo\
ftranslatingtheinputsintooutputs', ['X.X.', '....', '..X.', '....']],
            'answer': None
        },
        {
            'input': ['youshouldreadeliezeryudkowskysrationalityfromaitozombiesitsgreat',
                      ['....', '....', '....', '....']],
            'answer': None
        },
        {
            'input': ['theideaofcognitivebiasinpsychologyworksinananalogouswayacognitiv\
ebiasisasystematicerrorinhowwethinkasopposedtoarandomerrororonet\
hatsmerelycausedbyourignorancewhereasstatisticalbiasskewsasample\
sothatitlesscloselyresemblesalargerpopulationcognitivebiasesskew\
ourbeliefssothattheylessaccuratelyrepresentthefactsandtheyskewou\
rdecisionmakinganditlessreliablyachievesourgoals', ['XXXX', '....', '.X..', '.X..']],
            'answer': None
        },
        {
            'input': ['cardangrilletest', ['.XX.', '.XX.', '..X.', 'X...']],
            'answer': None
        },
        {
            'input': ['qwertyuiopasdfghjklzxcvbnmqwerty', ['X.X.', '.X.X', '..X.', '....']],
            'answer': None
        }
    ]
}
