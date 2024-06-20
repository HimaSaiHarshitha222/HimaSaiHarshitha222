from PyQt5.QtWidgets import QMainWindow, QApplication
from PyQt5.QtCore import *
import sys
from chatcenterUI import *

class Naveen(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui =Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.bilB.clicked.connect(self.bill)
        self.ui.resetB.clicked.connect(self.reset)
        self.ui.exitB.clicked.connect(self.exit)
    def exit(self):
        sys.exit()
    def reset(self):
        self.ui.label_15.clear()
        self.ui.label_16.clear()
        self.ui.label_18.clear()
        self.ui.label_20.clear()

        self.ui.panipuri.setText("0")
        self.ui.dahipuri.setText("0")
        self.ui.masalapuri.setText("0")
        self.ui.gobi.setText("0")
        self.ui.cutlet.setText("0")
        self.ui.bhel.setText("0")
        self.ui.noodles.setText("0")
        self.ui.egg.setText("0")
        self.ui.kachori.setText("0")
        self.ui.paav.setText("0")
        self.ui.cool.setText("0")
    def bill(self):
        pp = int(self.ui.panipuri.text())*20
        dp = int(self.ui.dahipuri.text())*30
        mp = int(self.ui.masalapuri.text())*30
        gm = int(self.ui.gobi.text())*50
        ct = int(self.ui.cutlet.text())*40
        bp = int(self.ui.bhel.text())*30
        gn = int(self.ui.noodles.text())*80
        eggn = int(self.ui.egg.text())*60
        kc = int(self.ui.kachori.text())*40
        pb = int(self.ui.paav.text())*80
        cd = int(self.ui.cool.text())*20

        bill = pp + dp + mp + gm + ct + bp + gn + eggn + kc + pb + cd
        sgst = bill*0.025
        cgst = bill*0.025
        tot_bill = bill + sgst + cgst

        self.ui.label_15.setText("{:.2f}".format(bill))
        self.ui.label_16.setText("{:.2f}".format(sgst))
        self.ui.label_18.setText("{:.2f}".format(cgst))
        self.ui.label_20.setText("{:.2f}".format(tot_bill))
        
        
if __name__=="__main__":
    app = QApplication(sys.argv)
    w = Naveen()
    w.show()
    sys.exit(app.exec_())

