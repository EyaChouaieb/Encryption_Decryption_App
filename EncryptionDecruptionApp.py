import kivy
from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.image import Image
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.core.clipboard import Clipboard


def decoding(C,Q):
    D={".-":"a","-...":"b","-.-.":"c","-..":"d",".":"e","..-.":"f","--.":"g","....":"h","..":"i",".---":"j","-.-":"k",".-..":"l","--":"m","-.":"n","---":"o",".--.":"p","--.-":"q",".-.":"r","...":"s","-":"t","..-":"u","...-":"v",".--":"w","-..-":"x","-.--":"y","--..":"z","-----":"0",".----":"1","..---":"2","...--":"3","....-":"4",".....":"5","-....":"6","--...":"7","---..":"8","----.":"9","-.-.--":"!",".-..-.":'"',"...-..-":"$",".-...":"&",".----.":"'","-.--.":"(","-.--.-":")",".-.-.":"+","--..--":",","-....-":"-",".-.-.-":".","-..-.":"/","---...":":","-.-.-.":";","-...-":"=","..--..":"?",".--.-.":"@","..--.-":"_"}
    B=str(Q)*1000
    L=[]
    K=C
    i=K.find("    ")
    while i>=0:
         W=K[:i+4]
         L.append(K[:i])
         K=K.replace(W,"")
         i=K.find("    ")

    Y=C.split("    ")
    ch=""
    for cl in Y:
         O=cl.split()
         for cm in O:
              ch+=D[cm]
         if cl in L:
              ch+=" "
    #print(ch)
    def code2(ch,B):
        A=["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]*2
        N=["0","1","2","3","4","5","6","7","8","9"]*3
        Symb=["!",'"',"$","&","'","(",")","+",",","-",".","/",":",";","=","?","@","_"]*2
        E=[]
        for i in range(len(ch)):
            if ch[i]==" ":
                E.append(i)
        R=""
        T1=ch.replace(" ","")
        for c in range(len(T1)):
            if c%2!=0:
                if T1[c].isalpha():
                    R+=A[(A.index(T1[c].lower()))-int(B[c])]
                elif T1[c].isnumeric():
                    R+=N[N.index(T1[c])-int(B[c])]
                else:
                    R+=Symb[Symb.index(T1[c])-int(B[c])]
            else:
                if T1[c].isalpha():
                    R+=A[A.index(T1[c].lower())+int(B[c])]
                elif T1[c].isnumeric():
                    R+=N[N.index(T1[c])+int(B[c])]
                else:
                    R+=Symb[Symb.index(T1[c])+int(B[c])]
        L2=[]
        for n in R:
            L2.append(n)
        for z in E:
            L2.insert(z," ")
        Rf="".join(L2)
        return Rf
    Z=code2(ch,B)
    return Z


def coding(T,L):
    B=str(L)*1000
    def code1(T,B):
        A=["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]*2
        N=["0","1","2","3","4","5","6","7","8","9"]*3
        Symb=["!",'"',"$","&","'","(",")","+",",","-",".","/",":",";","=","?","@","_"]*2
        E=[]
        for i in range(len(T)):
            if T[i]==" ":
                E.append(i)
        R=""
        T1=T.replace(" ","")
        for c in range(len(T1)):
            if c%2==0:
                if T1[c].lower() in A:
                    R+=A[(A.index(T1[c].lower()))-int(B[c])]
                if T1[c] in N:
                    R+=N[N.index(T1[c])-int(B[c])]
                if T1[c] in Symb:
                    R+=Symb[Symb.index(T1[c])-int(B[c])]
            else:
                if T1[c].lower() in A:
                    R+=A[A.index(T1[c].lower())+int(B[c])]
                if T1[c] in N:
                    R+=N[N.index(T1[c])+int(B[c])]
                if T1[c] in Symb:
                    R+=Symb[Symb.index(T1[c])+int(B[c])]
        L2=[]
        for n in R:
            L2.append(n)
        for z in E:
            L2.insert(z," ")
        Rf="".join(L2)
        return Rf
    R=code1(T,B)
    print(R)

    def code(T):
        D={"a":".-","b":"-...","c":"-.-.","d":"-..","e":".","f":"..-.","g":"--.","h":"....","i":"..","j":".---","k":"-.-","l":".-..","m":"--","n":"-.","o":"---","p":".--.","q":"--.-","r":".-.","s":"...","t":"-","u":"..-","v":"...-","w":".--","x":"-..-","y":"-.--","z":"--.."," ":"    ","0":"-----","1":".----","2":"..---","3":"...--","4":"....-","5":".....","6":"-....","7":"--...","8":"---..","9":"----.","!":"-.-.--",'"':".-..-.","$":"...-..-","&":".-...","'":".----.","(":"-.--.",")":"-.--.-","+":".-.-.",",":"--..--","-":"-....-",".":".-.-.-","/":"-..-.",":":"---...",";":"-.-.-.","=":"-...-","?":"..--..","@":".--.-.","_":"..--.-"}
        ch=""
        for e in T:
            ch+=D[e]+" "
        return(ch)

    RS=code(R)
    return RS

class encryption_and_decryption(App):
    def build(self):
        self.window = GridLayout()
        self.window.cols=1
        self.window.size_hint=(0.6,0.7)
        self.window.pos_hint={"center_x":0.5,"center_y":0.5}
        self.window.add_widget(Image(source="pngwing.com.png",size_hint=(2.5,2.5)))
        self.space=Label(text="")
        self.window.add_widget(self.space)
        self.choiceq=Label(text="Do you want to encrypt or decrypt your message?",size_hint=(1,1),font_size=35,bold=True)
        self.window.add_widget(self.choiceq)
        self.space1=Label(text="",size_hint=(0.3,0.3),font_size=35,bold=True)
        self.window.add_widget(self.space1)
        self.choice=TextInput(padding_y=(10,10),size_hint=(1,0.9))
        self.window.add_widget(self.choice)
        self.question1=Label(text="Type the text you want to translate:",font_size=35,bold=True)
        self.window.add_widget(self.question1)
        self.message=TextInput(padding_y=(10,10),size_hint=(1,0.9))
        self.window.add_widget(self.message)
        self.question2=Label(text="Type your secret code:",font_size=35,bold=True)
        self.window.add_widget(self.question2)
        self.secretcode=TextInput(padding_y=(10,10),size_hint=(1,0.9))
        self.window.add_widget(self.secretcode)
        self.space2=Label(text="",font_size=2)
        self.window.add_widget(self.space2)
        self.button=Button(text="TRANSLATE",size_hint=(0.5,0.9),bold=True,background_color="#1e5687", background_normal = "")
        #self.button=Button(background_normal="pngwing.com.png",size_hint=(0.1,4))
        self.window.add_widget(self.button)
        self.button.bind(on_press=self.callback)
        
        return self.window

          
    def callback(self,instance):
        if (self.choice.text=="Decrypt" or self.choice.text=="DECRYPT" or self.choice.text=="decrypt") and (self.secretcode.text.isnumeric()):
            C=self.message.text
            Q=self.secretcode.text
            A=decoding(C,Q)
            self.choiceq.text="Your decrypted message is:\n"+ A+ "\n"+"\n"
            self.choiceq.text_size=(950,None)
            self.question1.text=""
            self.question2.text=""
            Clipboard.copy(A)
        elif (self.choice.text=="Encrypt" or self.choice.text=="ENCRYPT" or self.choice.text=="encrypt") and (self.secretcode.text.isnumeric()):
            T=self.message.text
            L=self.secretcode.text
            N=coding(T,L)
            self.choiceq.text="Your encrypted message is:\n"+ N + "\n"+"\n"
            self.choiceq.text_size=(950,None)
            self.question1.text=""
            self.question2.text=""
            Clipboard.copy(N)
            


if __name__ == "__main__":
    encryption_and_decryption().run()
