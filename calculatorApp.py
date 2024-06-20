from PyQt5.QtWidgets import QMainWindow, QApplication
from PyQt5.QtCore import *
import sys
from calculatorUI import *

class Naveen(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui =Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.clearB.clicked.connect(self.reset)
        self.ui.delB.clicked.connect(self.delete)
        
        self.ui.oneB.clicked.connect(self.one)
        self.ui.twoB.clicked.connect(self.two)
        self.ui.threeB.clicked.connect(self.three)

        self.ui.fourB.clicked.connect(self.four)
        self.ui.fiveB.clicked.connect(self.five)
        self.ui.sixB.clicked.connect(self.six)

        self.ui.sevenB.clicked.connect(self.seven)
        self.ui.eightB.clicked.connect(self.eight)
        self.ui.nineB.clicked.connect(self.nine)
        self.ui.zeroB.clicked.connect(self.zero)
        self.ui.dotB.clicked.connect(self.dot)
        self.ui.plusB.clicked.connect(self.plus)
        self.ui.minusB.clicked.connect(self.minus)
        self.ui.mulB.clicked.connect(self.mul)
        self.ui.divB.clicked.connect(self.div)
        self.ui.byxB.clicked.connect(self.onebyx)
        self.ui.sqrB.clicked.connect(self.sqr)
        self.ui.sqrtB.clicked.connect(self.sqrt)
        self.ui.perB.clicked.connect(self.per)
        self.ui.eqlB.clicked.connect(self.equals)
        
    def reset(self):
        self.ui.label.clear()
    def delete(self):
        data = self.ui.label.text()
        self.ui.label.setText(data[:-1])
    def dot(self):
        data = self.ui.label.text()
        self.ui.label.setText(data+".")
    def one(self):
        data = self.ui.label.text()
        self.ui.label.setText(data+"1")
    def two(self):
        data = self.ui.label.text()
        self.ui.label.setText(data+"2")
    def three(self):
        data = self.ui.label.text()
        self.ui.label.setText(data+"3")
    def four(self):
        data = self.ui.label.text()
        self.ui.label.setText(data+"4")
    def five(self):
        data = self.ui.label.text()
        self.ui.label.setText(data+"5")
    def six(self):
        data = self.ui.label.text()
        self.ui.label.setText(data+"6")
    def seven(self):
        data = self.ui.label.text()
        self.ui.label.setText(data+"7")
    def eight(self):
        data = self.ui.label.text()
        self.ui.label.setText(data+"8")
    def nine(self):
        data = self.ui.label.text()
        self.ui.label.setText(data+"9")
    def zero(self):
        data = self.ui.label.text()
        self.ui.label.setText(data+"0")
    def plus(self):
        data = self.ui.label.text()
        self.ui.label.setText(data+"+")
    def minus(self):
        data = self.ui.label.text()
        self.ui.label.setText(data+"-")
    def mul(self):
        data = self.ui.label.text()
        self.ui.label.setText(data+"*")
    def div(self):
        data = self.ui.label.text()
        self.ui.label.setText(data+"/")
    def per(self):
        try:
            data = eval(self.ui.label.text())/100
            self.ui.label.setText("{}".format(data))
        except:
            self.ui.label.setText("Invalid Input")
    def sqr(self):
        data = float(self.ui.label.text())
        self.ui.label.setText("{}".format(data**2))
    def sqrt(self):
        data = float(self.ui.label.text())
        self.ui.label.setText("{}".format(data**0.5))
    def onebyx(self):
        data = float(self.ui.label.text())
        self.ui.label.setText("{}".format(1/data))
    def equals(self):
        data = self.ui.label.text()
        try:
            self.ui.label.setText("{}".format(eval(data)))
        except:
            self.ui.label.setText("Invalid Input")

if __name__=="__main__":
    app = QApplication(sys.argv)
    w = Naveen()
    w.show()
    sys.exit(app.exec_())

