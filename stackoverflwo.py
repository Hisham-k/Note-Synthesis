import numpy as np
import simpleaudio as sa
import sys
from PyQt5 import QtWidgets, QtGui
from piano import Ui_MainWindow



class ApplicationWindow(QtWidgets.QMainWindow):
    
    def __init__(self):
        super(ApplicationWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        
        self.sample_rate = 44100
        self.damping = 0.98

        self.ui.c4.clicked.connect(lambda: self.noteSelect(-22)) 
        self.ui.d4.clicked.connect(lambda: self.noteSelect(-20))
        self.ui.e4.clicked.connect(lambda: self.noteSelect(-18))
        self.ui.f4.clicked.connect(lambda: self.noteSelect(-17))
        self.ui.g4.clicked.connect(lambda: self.noteSelect(-15))
        self.ui.a4.clicked.connect(lambda: self.noteSelect(-13))
        self.ui.b4.clicked.connect(lambda: self.noteSelect(-11))
        
        self.ui.c40.clicked.connect(lambda: self.noteSelect(-21)) 
        self.ui.d40.clicked.connect(lambda: self.noteSelect(-19))
        self.ui.f40.clicked.connect(lambda: self.noteSelect(-16))
        self.ui.g40.clicked.connect(lambda: self.noteSelect(-14))
        self.ui.a40.clicked.connect(lambda: self.noteSelect(-12))

        self.ui.c5.clicked.connect(lambda: self.noteSelect(-10)) 
        self.ui.d5.clicked.connect(lambda: self.noteSelect(-8))
        self.ui.e5.clicked.connect(lambda: self.noteSelect(-6))
        self.ui.f5.clicked.connect(lambda: self.noteSelect(-5))
        self.ui.g5.clicked.connect(lambda: self.noteSelect(-3))
        self.ui.a5.clicked.connect(lambda: self.noteSelect(-1))
        self.ui.b5.clicked.connect(lambda: self.noteSelect(1))

        self.ui.c50.clicked.connect(lambda: self.noteSelect(-9)) 
        self.ui.d50.clicked.connect(lambda: self.noteSelect(-7))
        self.ui.f50.clicked.connect(lambda: self.noteSelect(-4))
        self.ui.g50.clicked.connect(lambda: self.noteSelect(-2))
        self.ui.a50.clicked.connect(lambda: self.noteSelect(0))

        self.ui.c6.clicked.connect(lambda: self.noteSelect(2))    
        


    def noteSelect(self,number):
        frequency=int(2 ** (number/12) * 440) #440 is base frequency for A4
        self.playNote(frequency)

    def playNote(self,frequency):
        strum = self.generate( frequency ,0.5, self.sample_rate * 1)
        strum *= 32767 / np.max(np.abs(strum))
        strum=strum.astype(np.int16)
        
        try:
            sa.play_buffer(strum,2,2,22050)
        except:
            print("unable to play")
     
       
    def generate(self,noteFrequency, vol, nsamples):
        
        minDelay = self.sample_rate // noteFrequency
        buf = np.random.rand(minDelay) * 2 -1
        samples = np.empty(nsamples, dtype=float)

        for i in range(0, nsamples - minDelay, minDelay):
            samples[i: i + minDelay] = buf[:]
            buf = self.damping * 0.5 * (buf + (np.roll(buf, -1)))
        
        i += minDelay
        k = nsamples - i
        if k: #if samples is missing values, fill from buffer
            samples[i:] = buf[:k]
        
        return samples * vol


    def generate_chord(self,listOfFrequencies, nsamples):
    
        samples = np.zeros(nsamples, dtype=float)
        for note in listOfFrequencies:
            samples += self.generate(note, 0.5, nsamples)
        return samples

def main():
    app = QtWidgets.QApplication(sys.argv)
    application = ApplicationWindow()
    application.show()
    app.exec_()

        

if __name__ == "__main__":
    main()
        
        
        


    