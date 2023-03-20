class TextToMorse:

    def __init__(self):
        self.alphabet = [' ','a','b','c','d','e','f','g','h','i','j','k','l','m','n','ñ','o','p','q','r','s','t','u','v','w','x','y','z', '.', ',']
        self.morse = ['   ', '.-','-...','-.-.','-..','.','..-.','--.','....','..','.---','-.-','.-..','--','-.','--.--','---','.--.','--.-','.-.','...','-','..-','...-','.--','-..-','-.--','--..', '.-.-.-', '--..--']

    def texttomorse(self, text):
        result = ''
        for letter in text.lower():
            result += self.morse[self.alphabet.index(letter)] + " "
        return result