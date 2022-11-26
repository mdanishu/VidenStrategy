import sys

import yfinance as yf
import pandas as pd
import PyQt6 as pyqt6
import matplotlib as plt
from datetime import datetime
#plt.style.use('seaborn')
from PyQt6.QtWidgets import QApplication, QWidget, QLineEdit, QPushButton, QTextEdit, QVBoxLayout
from PyQt6.QtGui import QIcon

tickers = 'TSLA'

class MyApp(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('DSquared Ticker App')
        self.setWindowIcon(QIcon('maps.ico'))
        self.resize(500,400)

        layout = QVBoxLayout()
        self.setLayout(layout)

        self.inputField = QLineEdit()
        button = QPushButton('&Pick Ticker',clicked=self.sayHello)
        button.clicked.connect(self.sayHello)
        self.output = QTextEdit()

        layout.addWidget(self.inputField)
        layout.addWidget(button)
        layout.addWidget(self.output)
    def sayHello(self):
        inputText = self.inputField.text()
        #self.output.setText('Hello {0}'.format(inputText))
        tickers = '{0}'.format(inputText)
        self.output.setText(analysisout(tickers))

app = QApplication(sys.argv)
app.setStyleSheet('''
    QWidget {
        font-size: 25px;
    }
   QPushButton {
        font-size: 20px;
    } 
        
''')

#tickers = input("ticker please:")

#df = pd.head(f'"recs)
#df = pd.DataFrame.index.values(stock.info)
#pd.DataFrame.head (f'(stock.info),2)

def analysisout (tickers):
    stock = yf.Ticker(tickers)
    stockinfo = stock.info
    twohundred = stock.info['twoHundredDayAverage']
    recs = stock.recommendations
    lastClose = stock.info['previousClose']
    percentBelow200 = (lastClose - twohundred) / twohundred * 100
    print(stock.info.get('shortName'))
    #print(stockinfo.keys())
    print("Two Hundred Day Price:", twohundred)
    print("Previous Close Price:", stock.info.get('previousClose'))
    print("Percent Difference:", percentBelow200, "%")

#analysisout(tickers)

#for key,value in stockinfo.items():
    #print(key,":",value)

window = MyApp()
window.show()
app.exec()

