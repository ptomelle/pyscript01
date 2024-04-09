from pyscript import document, when, display
from library.domdict import DOMDict
from math import pi

class App:
    # Applicazione = dizionario
    dizModel = {}     # dizionario delle variabili ( .. )
    dom = {}          # dizionario view  è il dom del browser
    dizControl = {}    # dizionario Control => CallBack


def init_app_Model():
    dizModel = {
    # Variabili dell'applicazione
    'conta_tst02': 0,
    'toggle_tst04': True,
    'txtb01_tst05': '',
    'txtb02_tst06': 0,

    }

    return dizModel

def init_app_Control():

# ogni def interna ha il collegamento con il suo tasto di attivazione


    # chiavi-valore CallBack
    dizCallback = {
    'cb_tst01': callback_tst01,
    'cb_tst02': callback_tst02,
    'cb_tst03': callback_tst03,
    'cb_tst04': callback_tst04,
    'cb_tst05': callback_tst05,
    'cb_tst06': callback_tst06
    }

    return  dizCallback


# Callback tasto tst01
# Cambia la label del tasto tst01
@when("click", "#tst01")
def callback_tst01(event = None):
    # lettura valore del tasto
    dom_tst01 = App.dom["tst01"]
    testo = "Label cambiata dalla pressione del tasto"
    dom_tst01.innerHTML = testo
    print(f"Sono nella callback_tst01 -> {testo}")
    display(f"Sono nella callback_tst01 -> {testo}")

# Callback tasto tst02
    # Conta quante volte è stato premuto il tasto tst02

@when("click", "#tst02")
def callback_tst02(event = None):
    dom_tst02 = App.dom["tst02"]
    label_tst02 = "Tasto premuto: "
    App.dizModel['conta_tst02'] += 1
    # cambio testo del tasto
    testo = f"{label_tst02} {App.dizModel['conta_tst02']} volte"
    dom_tst02.innerHTML = testo
    print(f"Sono nella callback_tst02 -> {testo}")
    display(f"Sono nella callback_tst02 -> {testo}")

# Callback tasto tst03
# Modifica una proprietà CSS

@when("click", "#tst03")
def callback_tst03(event = None):
    dom_tst03 = App.dom["tst03"]
    dom_tst03.style.fontSize = "28px"
    print(f"Sono nella callback_tst03 -> fontSize 28px")
    display(f"Sono nella callback_tst03 -> fontSize 28px")

# Callback tasto tst04
        # Modifica alcune proprietà CSS in modo alternato

@when("click", "#tst04")
def callback_tst04(event = None):
    dom_tst04 = App.dom["tst04"]
    if App.dizModel['toggle_tst04']:
        App.dizModel['toggle_tst04'] = False
        dom_tst04.style.backgroundColor = "yellow"
        dom_tst04.style.borderRadius = "6px"
    else:
        App.dizModel['toggle_tst04'] = True
        dom_tst04.style.backgroundColor = "green"
        dom_tst04.style.borderRadius = "1px"
    print(f"Sono nella callback_tst04 -> cambio il colore ed il raggio del bordo -> {App.dizModel['toggle_tst04']}")
    display(f"Sono nella callback_tst04 -> cambio il colore ed il raggio del bordo -> {App.dizModel['toggle_tst04']}")

# Callback input box tstb05
# Recupera un testo da una textbox e lo ricopia modificato in un paragrafo

@when("click", "#tst05")
def callback_tst05(event = None):
    dom_txtb01 = App.dom["txtb01"]
    dom_p01 = App.dom["p01"]
    testo = "Ciao "
    App.dizModel['txtb01_tst05'] = dom_txtb01.value
    risposta = f"{testo} {App.dizModel['txtb01_tst05']} !"
    dom_p02 = App.dom["p01"]
    dom_p02.innerHTML = risposta
    print(f"Sono nella callback_tst05 -> recupero il testo da inputbox -> {risposta}")
    display(f"Sono nella callback_tst05 -> recupero il testo da inputbox -> {risposta}")

# Callback input box tstb06
# Recupera un testo da una textbox, e verifica se essa è numerica o meno

@when("click", "#tst06")
def callback_tst06(event = None):
    dom_txtb02 = App.dom["txtb02"]
    dom_p02 = App.dom["p02"]
    App.dizModel['txtb02_tst06'] = dom_txtb02.value
    if not App.dizModel['txtb02_tst06'].isnumeric():
        risposta = f"{App.dizModel['txtb02_tst06']} non è un numero intero!"
    else:
        intero = int(App.dizModel['txtb02_tst06'])
        risposta = f"{App.dizModel['txtb02_tst06']} è un numero intero!"
    dom_p02.innerHTML = risposta
    display(f"Sono nella callback_tst06 -> recupero il testo da inputbox -> {risposta}")
    print(f"Sono nella callback_tst06 -> recupero il testo da inputbox -> {risposta}")


def canvas():
    canvas = App.dom["myCanvas"]
    ctx = canvas.getContext("2d")
    ctx.moveTo(0, 0)
    ctx.lineTo(200, 100)
    ctx.stroke()
    ctx.beginPath()
    ctx.arc(95, 50, 40, 0, 2 * pi)
    ctx.stroke()


def main():
   App.dizModel = init_app_Model()
   App.dom = DOMDict()
   App.dizControl = init_app_Control()
   canvas()


if __name__ == "__main__":
    main()
