from flask import Flask
from flask import render_template
from flask import Response, request, jsonify
app = Flask(__name__)

# buttons: text-action pairs
#           actions: {sound - play sound, w - wrong choice (checkpoint), r - right choice (checkpoint)}
learningdata={
    "1":
    {
        "id":"1",
        "navbefore":[],
        "bold":"Spanish Accents",
        "navafter":["Checkpoint 1","Words that end in Consonants: When don't you need an accent?","Words that end in Consonants: When do you need an accent?","Checkpoint 2","Words that end in vowels: When don't you need an accent?","Words that end in vowels: When do you need an accent?", "Checkpoint 3", "Words that end in 'mente'" ],
        "header":"á é í ó ú",
        "content":["Spanish accents or 'tildes' are written above vowels from the lower left to the upper right."," They indicate a stressed syllable in a word."],
        "instructions": "Click on each word below to hear how the syllables are stressed.",
        "buttons":[["árbol", "sound"],["está", "sound"]],
        "hear":[],
        "prev_question_id": "start",
        "next_question_id": "2",
    },
            "2":
    {
        "id":"2",
        "navbefore":["Spanish Accents"],
        "bold":"Checkpoint 1",
        "navafter":["Words that end in Consonants: When don't you need an accent?","Words that end in Consonants: When do you need an accent?","Checkpoint 2","Words that end in vowels: When don't you need an accent?","Words that end in vowels: When do you need an accent?", "Checkpoint 3", "Words that end in 'mente'" ],
        "header":"Checkpoint 1: ",
        "content":["Which is the stressed syllable in \"apréndetelo\"?"],
        "instructions": "",
        "buttons":[["a","w"],["prén","r"],["de","w"],["te","w"],["lo","w"]],
        "hear":["..\\static\\audio\\apréndetelo.mp3"],
        "prev_question_id": "1",
        "next_question_id": "3",
    },
        "3":
    {
        "id":"3",
        "navbefore":["Spanish Accents","Checkpoint 1"],
        "bold":"Words that end in Consonants: When don't you need an accent?",
        "navafter":["Words that end in Consonants: When do you need an accent?","Checkpoint 2","Words that end in vowels: When don't you need an accent?","Words that end in vowels: When do you need an accent?", "Checkpoint 3", "Words that end in 'mente'" ],
        "header":"Words that end in consonants ",
        "content":["Conventionally, the last syllable is stressed in spanish words that end in consonants.","The consonants 'n' and 's' are an exception!(more on those later)When a word follows this convention, we assume the stressed syllable and do not need to include an accent mark. "],
        "instructions": "Click on each word below to hear how the syllables are stressed.",
        "buttons":[["comer","sound"],["profesor","sound"],["animal","sound"],["Madrid","sound"]],
        "hear":[],
        "prev_question_id": "2",
        "next_question_id": "4",
    },
        "4":
    {
        "id":"4",
        "navbefore":["Spanish Accents","Checkpoint 1","Words that end in Consonants: When don't you need an accent?"],
        "bold":"Words that end in Consonants: When do you need an accent?",
        "navafter":["Checkpoint 2","Words that end in vowels: When don't you need an accent?","Words that end in vowels: When do you need an accent?", "Checkpoint 3", "Words that end in 'mente'" ],
        "header":" Words that end in consonants other than 'n' or 's'",
        "content":["A word ending in a consonant needs an accent mark when it does not follow the convention - when the stressed syllable is not the last syllable."],
        "instructions": "Click on each word below to hear how the syllables are stressed.",
        "buttons":[["cárcel","sound"],["árbol","sound"], ["césped","sound"],["débil","sound"]],
        "hear":[],
        "prev_question_id": "3",
        "next_question_id": "5",
    },
                "5":
    {
        "id":"5",
        "navbefore":["Spanish Accents","Checkpoint 1","Words that end in Consonants: When don't you need an accent?","Words that end in Consonants: When do you need an accent?",],
        "bold":"Checkpoint 2",
        "navafter":["Words that end in vowels: When don't you need an accent?","Words that end in vowels: When do you need an accent?", "Checkpoint 3", "Words that end in 'mente'" ],
        "header":"Checkpoint 2:",
        "content":["Which is correct?"],
        "instructions": "",
        "buttons":[["ciudad","r"],["ciudád","w"]],
        "hear":["..\\static\\audio\\ciudad.mp3"],
        "prev_question_id": "4",
        "next_question_id": "6",
    },
        "6":
    {
        "id":"6",
        "navbefore":["Spanish Accents","Checkpoint 1","Words that end in Consonants: When don't you need an accent?","Words that end in Consonants: When do you need an accent?","Checkpoint 2",],
        "bold":"Words that end in vowels: When don't you need an accent?",
        "navafter":["Words that end in vowels: When do you need an accent?", "Checkpoint 3", "Words that end in 'mente'" ],
        "header":"Words that end in vowels",
        "content":["Conventionally, the second to last syllable is stressed in spanish words that end in a vowel, or in 'n' or 's'.","When a word follows this convention, we assume the stressed syllable and do not need to include an accent mark. "],
        "instructions": "Click on each word below to hear how the syllables are stressed.",
        "buttons":[["todo","sound"],["inteligente","sound"],["examen","sound"],["joven","sound"],["lunes","sound"],["calcetines","sound"]],
        "hear":[],
        "prev_question_id": "5",
        "next_question_id": "7",
    },
        "7":
    {
        "id":"7",
        "navbefore":["Spanish Accents","Checkpoint 1","Words that end in Consonants: When don't you need an accent?","Words that end in Consonants: When do you need an accent?","Checkpoint 2","Words that end in vowels: When don't you need an accent?",],
        "bold":"Words that end in vowels: When do you need an accent?",
        "navafter":[ "Checkpoint 3", "Words that end in 'mente'" ],
        "header":" Words that end in vowels",
        "content":["A word that ends in a vowel or in 'n' or 's' needs an accent mark when it does not follow the convention - when the stressed syllable is not the second to last syllable. "],
        "instructions": "Click on each word below to hear how the syllables are stressed.",
        "buttons":[["cambiará","sound"],["comeré","sound"],["apréndetelo","sound"],["océano","sound"], ["háganselo","sound"]],
        "hear":[],
        "prev_question_id": "6",
        "next_question_id": "8",
    },
                    "8":
    {
        "id":"8",
        "navbefore":["Spanish Accents","Checkpoint 1","Words that end in Consonants: When don't you need an accent?","Words that end in Consonants: When do you need an accent?","Checkpoint 2","Words that end in vowels: When don't you need an accent?","Words that end in vowels: When do you need an accent?",],
        "bold":"Checkpoint 3", 
        "navafter":[ "Words that end in 'mente'" ],
        "header":" Checkpoint 3: ",
        "content":["Which is correct?"],
        "instructions": "",
        "buttons":[["ubicacion","w"],["ubicación","r"]],
        "hear":["..\\static\\audio\\ubicación.mp3"],
        "prev_question_id": "7",
        "next_question_id": "9",
    },
    

        "9":
    {
        "id":"9",
        "navbefore":["Spanish Accents","Checkpoint 1","Words that end in Consonants: When don't you need an accent?","Words that end in Consonants: When do you need an accent?","Checkpoint 2","Words that end in vowels: When don't you need an accent?","Words that end in vowels: When do you need an accent?", "Checkpoint 3",],
        "bold": "Words that end in 'mente'",
        "navafter":[ ],
        "header":"Special Case: words that end in 'mente'",
        "content":["In Spanish, adverbs that end in 'mente' are the only words that have two stressed syllables.","In this case, consider the part of the word before 'mente' independently and apply the accent mark rules to it."],
        "instructions": "Click on each word below to hear how the syllables are stressed.",
        "buttons":[["alfabéticamente","sound"],["artísticamente","sound"],["paralelamente","sound"],["solamente","sound"]],
        "hear":[],
        "prev_question_id": "8",
        "next_question_id": "end",
    },
}
word_data = {
    "además": {
        "id": "1",
        "word": "además",
        "audio": "..\\static\\audio\\además.mp3",
    },
    "alfabéticamente": {
        "id": "2",
        "word": "alfabéticamente",
        "audio": "..\\static\\audio\\alfabéticamente.mp3",
    },
    "animal": {
        "id": "3",
        "word": "animal",
        "audio": "..\\static\\audio\\animal.mp3",
    },
    "apréndetelo": {
        "id": "4",
        "word": "apréndetelo",
        "audio": "..\\static\\audio\\apréndetelo.mp3",
    },
    "árbol": {
        "id": "5",
        "word": "árbol",
        "audio": "..\\static\\audio\\árbol.mp3",
    },
    "artísticamente": {
        "id": "6",
        "word": "artísticamente",
        "audio": "..\\static\\audio\\artísticamente.mp3",
    },
    "calcetines": {
        "id": "7",
        "word": "calcetines",
        "audio": "..\\static\\audio\\calcetines.mp3",
    },
    "cambiará": {
        "id": "8",
        "word": "cambiará",
        "audio": "..\\static\\audio\\cambiará.mp3",
    },
    "cárcel": {
        "id": "9",
        "word": "cárcel",
        "audio": "..\\static\\audio\\cárcel.mp3",
    },
    "césped": {
        "id": "10",
        "word": "césped",
        "audio": "..\\static\\audio\\césped.mp3",
    },
    "ciudad": {
        "id": "11",
        "word": "ciudad",
        "audio": "..\\static\\audio\\ciudad.mp3",
    },
    "comer": {
        "id": "12",
        "word": "comer",
        "audio": "..\\static\\audio\\comer.mp3",
    },
    "comeré": {
        "id": "13",
        "word": "comeré",
        "audio": "..\\static\\audio\\comeré.mp3",
    },
    "débil": {
        "id": "14",
        "word": "débil",
        "audio": "..\\static\\audio\\débil.mp3",
    },
    "está": {
        "id": "15",
        "word": "está",
        "audio": "..\\static\\audio\\está.mp3",
    },
    "examen": {
        "id": "16",
        "word": "examen",
        "audio": "..\\static\\audio\\examen.mp3",
    },
    "fantástico": {
        "id": "17",
        "word": "fantástico",
        "audio": "..\\static\\audio\\fantástico.mp3",
    },
    "háganselo": {
        "id": "18",
        "word": "háganselo",
        "audio": "..\\static\\audio\\háganselo.mp3",
    },
    "inteligente": {
        "id": "19",
        "word": "inteligente",
        "audio": "..\\static\\audio\\inteligente.mp3",
    },
    "joven": {
        "id": "20",
        "word": "joven",
        "audio": "..\\static\\audio\\joven.mp3",
    },
    "lágrima": {
        "id": "21",
        "word": "lágrima",
        "audio": "..\\static\\audio\\lágrima.mp3",
    },
    "lunes": {
        "id": "22",
        "word": "lunes",
        "audio": "..\\static\\audio\\lunes.mp3",
    },
    "Madrid": {
        "id": "23",
        "word": "Madrid",
        "audio": "..\\static\\audio\\madrid.mp3",
    },
    "océano": {
        "id": "24",
        "word": "océano",
        "audio": "..\\static\\audio\\océano.mp3",
    },
    "paralelamente": {
        "id": "25",
        "word": "paralelamente",
        "audio": "..\\static\\audio\\paralelamente.mp3",
    },
    "pasarás": {
        "id": "26",
        "word": "pasarás",
        "audio": "..\\static\\audio\\pasarás.mp3",
    },
    "profesor": {
        "id": "27",
        "word": "profesor",
        "audio": "..\\static\\audio\\profesor.mp3",
    },
    "solamente": {
        "id": "28",
        "word": "solamente",
        "audio": "..\\static\\audio\\solamente.mp3",
    },
    "todo": {
        "id": "29",
        "word": "todo",
        "audio": "..\\static\\audio\\todo.mp3",
    },
    "ubicación": {
        "id": "30",
        "word": "ubicación",
        "audio": "..\\static\\audio\\ubicación.mp3",
    },
}

score=0

answers = []
correctanswers = ["además", "césped", "cambiará", "artísticamente", "inteligente", "profesor", "océano", "fantástico", "correct", "correct"]
data = {
   "1":
    {
        "id": "1",
        "question": "Which is correct?",
        "options": ["ademas", "además"],
        "correct": "además",
        "prev_question_id": "start",
        "next_question_id": "2",
        "audio": "/static/audio/además.mp3",
        "explanation": "A word that ends in a vowel or in 'n' or 's' needs an accent mark when it does not follow the convention - when the stressed syllable is not the second to last syllable."
    },
    "2":
    {
        "id": "2",
        "question": "Which is correct?",
        "options": ["cesped", "césped"],
        "correct": "césped",
        "prev_question_id": "1",
        "next_question_id": "3",
        "audio": "/static/audio/césped.mp3",
        "explanation": "A word ending in a consonant needs an accent mark when it does not follow the convention - when the stressed syllable is not the last syllable."
    },
    "3":
    {
        "id": "3",
        "question": "Which is correct?",
        "options": ["cambiara", "cambiará"],
        "correct": "cambiará",
        "prev_question_id": "2",
        "next_question_id": "4",
        "audio": "/static/audio/cambiará.mp3",
        "explanation": "A word that ends in a vowel or in 'n' or 's' needs an accent mark when it does not follow the convention - when the stressed syllable is not the second to last syllable."
    },
    "4":
    {
        "id": "4",
        "question": "Which is correct?",
        "options": ["artisticamente", "artísticamente", "artisticaménte", "artísticaménte"],
        "correct": "artísticamente",
        "prev_question_id": "3",
        "next_question_id": "5",
        "audio": "/static/audio/artísticamente.mp3",
        "explanation": "In Spanish, adverbs that end in 'mente' are the only words that have two stressed syllables. In this case, consider the part of the word before 'mente' independently and apply the accent mark rules to it."
    },
    "5":
    {
        "id": "5",
        "question": "Which is correct?",
        "options": ["inteligente", "ínteligente", "intéligente", "inteligénte"],
        "correct": "inteligente",
        "prev_question_id": "4",
        "next_question_id": "6",
        "audio": "/static/audio/inteligente.mp3",
        "explanation": "The second to last syllable is stressed in spanish words that end in a vowel, or in 'n' or 's'. When a word follows this convention, we assume the stressed syllable and do not need to include an accent mark."
    },
    "6":
    {
        "id": "6",
        "question": "Which is correct?",
        "options": ["profesor", "prófesor", "profésor", "profesór"],
        "correct": "profesor",
        "prev_question_id": "5",
        "next_question_id": "7",
        "audio": "/static/audio/profesor.mp3",
        "explanation": "The last syllable is stressed in spanish words that end in consonants (apart from 'n' and 's'). When a word follows this convention, we assume the stressed syllable and do not need to include an accent mark."
    },
    "7":
    {
        "id": "7",
        "question": "Which is correct?",
        "options": ["oceano", "óceano", "océano", "oceáno"],
        "correct": "océano",
        "prev_question_id": "6",
        "next_question_id": "8",
        "audio": "/static/audio/océano.mp3",
        "explanation": "A word that ends in a vowel or in 'n' or 's' needs an accent mark when it does not follow the convention - when the stressed syllable is not the second to last syllable."
    },
    "8":
    {
        "id": "8",
        "question": "Which is correct?",
        "options": ["fantastico", "fantástico", "fántastico", "fantasticó"],
        "correct": "fantástico",
        "prev_question_id": "7",
        "next_question_id": "9",
        "audio": "/static/audio/fantástico.mp3",
        "explanation": "A word that ends in a vowel or in 'n' or 's' needs an accent mark when it does not follow the convention - when the stressed syllable is not the second to last syllable."
    },
    # Data for drag and drop type questions
    "9":
    {
        "id": "9",
        "question": "Drag and drop the words onto the correct box.",
        "options": ["comer", "pasaras", "lunes", "debil", "examen"],
        "yes_accent": ["pasaras", "debil"],
        "no_accent": ["comer", "lunes", "examen"],
        "prev_question_id": "8",
        "next_question_id": "10",
    },
    "10":
    {
        "id": "10",
        "question": "Drag and drop the words onto the correct box.",
        "options": ["animal", "lagrima", "oceano", "todo", "joven"],
        "yes_accent": ["lagrima", "oceano"],
        "no_accent": ["animal", "todo", "joven"],
        "prev_question_id": "9",
        "next_question_id": "end",
    }
}

# Routes Quiz
@app.route('/quiz')
def home_page():
   global score
   score = 0 
   answers.clear()
   print(answers)
   return render_template('quiz_home_page.html', data=data)

@app.route('/keepscore', methods=['GET', 'POST'])
def keepscore():
    json_data = request.get_json()  
    ans = json_data["ans"] 
    answers.append(ans)
    return ans

@app.route('/quiz1/<id>', methods=['GET', 'POST'])
def quiz_type_1(id=None):
    quiz_id = data[id]
    return render_template('quiz_question1.html', quiz=quiz_id, data=data)  

@app.route('/quiz2/<id>')
def quiz_type_2(id=None):
    quiz_id = data[id]

    return render_template('quiz_question2.html', quiz=quiz_id, data=data)  

@app.route('/quiz2/score')
def quiz_score():
    global score
    print("correctanswers:"+str(correctanswers))
    print("myanswers:"+str(answers))
    for i in range(10):
        if answers[i]==correctanswers[i]:
            score+=1
    return render_template('quiz_score.html', score=score)  

# Routes Learning
@app.route('/learn/<id>', methods=['GET', 'POST'])
def learn(id=None):
    learn_id = learningdata[id]
    return render_template('learn.html', learn=learn_id, learningdata=learningdata, word_data=word_data)  

@app.route('/')
def home():
   return render_template('home.html')   


if __name__ == '__main__':
   app.run(debug = True)
