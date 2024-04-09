## Pyscript01

Progetto scheletro per usare il browser come UI di un programma python scaricato in formato Wasm secondo
il progetto Pyiodide.

Il progetto usa un MVC con un dizionario
App che è l'applicationContext
dell'applicazione con i tre dizionari
dizModel, dom , dizControl

dizModel => Model
dom del browser  = > View
dizControl , callBack => Control

Il python contenuto nel wasm è quasi completo
dei moduli più usati.

Per far partire il programma dopo aver
eseguito un fork, posizionarsi nella dir
del file index.html

e da terminale lanciare 
python3 -m http.server 

quindi puntare con il browser 
localhost:8000
oppure
0.0.0.0:8000

Nota: questa versione una annotazione 
che esegue il binding di un evento associato
all' #id  di un elemento del dom
alla funzione scritta a seguire l'annotazione.

La prossima versione dovrebbe togliere
questa annotazione, molto utile, per esporre 
il binding dell'elemento del dom con l'evento 
atteso e la sua callback. 