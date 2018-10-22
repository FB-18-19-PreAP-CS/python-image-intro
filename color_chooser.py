
from PIL import Image
import sys
from PIL.ImageQt import ImageQt
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QMainWindow, QWidget, QLineEdit, QApplication, QFrame, qApp, QLabel, QGridLayout, QSlider
from PyQt5.QtGui import QPixmap, QImage, QFont, QIcon, QColor


class ColorChooser(QWidget):
    
    def __init__(self):
        super().__init__()
        self.red = 0
        self.green = 0
        self.blue = 0
        self.col = QColor(self.red, self.green, self.blue)
        self.initUI()

    def initUI(self):
        self.r_sld = QSlider(Qt.Horizontal, self)
        self.r_sld.valueChanged[int].connect(self.changeRed)
        self.r_sld.setMinimum(0)
        self.r_sld.setMaximum(255)
        
        self.g_sld = QSlider(Qt.Horizontal, self)
        self.g_sld.valueChanged[int].connect(self.changeGreen)
        self.g_sld.setMinimum(0)
        self.g_sld.setMaximum(255)
        
        self.b_sld = QSlider(Qt.Horizontal, self)
        self.b_sld.valueChanged[int].connect(self.changeBlue)
        self.b_sld.setMinimum(0)
        self.b_sld.setMaximum(255)
        
        self.r_lbl = QLineEdit('0',self)
        self.r_lbl.setFixedWidth(40)
        self.r_lbl.textChanged.connect(self.changeRed)
        
        self.g_lbl = QLineEdit('0',self)
        self.g_lbl.setFixedWidth(40)
        self.g_lbl.textChanged.connect(self.changeGreen)
        
        self.b_lbl = QLineEdit('0',self)
        self.b_lbl.setFixedWidth(40)
        self.b_lbl.textChanged.connect(self.changeBlue)
        
        self.grid = QGridLayout()
        self.grid.addWidget(QLabel("Red",self),1,0)
        self.grid.addWidget(self.r_sld,1,1)
        self.grid.addWidget(self.r_lbl,1,2)
        
        self.grid.addWidget(QLabel("Green",self),2,0)
        self.grid.addWidget(self.g_sld,2,1)
        self.grid.addWidget(self.g_lbl,2,2)
        
        self.grid.addWidget(QLabel("Blue",self),3,0)
        self.grid.addWidget(self.b_sld,3,1)
        self.grid.addWidget(self.b_lbl,3,2)
        
        self.square = QFrame(self)
        self.square.setStyleSheet("QWidget { background-color: %s }" % self.col.name())
        
        self.grid.addWidget(self.square,4,0,1,3)
        
        self.setLayout(self.grid)
        
        self.setGeometry(300,300,640,480)
        self.setWindowTitle("Choose a color")
        self.show()
        
    
    def changeRed(self, value):
        try:
            self.r_lbl.setText(f"{value}")
            self.red = int(value)
            self.col = QColor(self.red, self.green, self.blue)
            self.square.setStyleSheet("QWidget { background-color: %s }" % self.col.name())
            self.r_sld.setValue(self.red)
        except:
            pass
        
    def changeBlue(self, value):
        try:
            self.b_lbl.setText(f'{value}')
            self.blue = int(value)
            self.col = QColor(self.red, self.green, self.blue)
            self.square.setStyleSheet("QWidget { background-color: %s }" % self.col.name())
            self.b_sld.setValue(self.blue)
        except:
            pass
    
    def changeGreen(self, value):
        try:
            self.g_lbl.setText(f'{value}')
            self.green = int(value)
            self.col = QColor(self.red, self.green, self.blue)
            self.square.setStyleSheet("QWidget { background-color: %s }" % self.col.name())
            self.g_sld.setValue(self.green)
        except:
            pass
    

if __name__ == "__main__":
    app = QApplication(sys.argv)
    cc = ColorChooser()
    sys.exit(app.exec_())