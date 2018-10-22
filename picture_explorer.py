
from PIL import Image
import sys
from PIL.ImageQt import ImageQt
from PyQt5.QtWidgets import QMainWindow, QWidget, QApplication, qApp, QLabel, QGridLayout, QAction, QFileDialog
from PyQt5.QtGui import QPixmap, QImage, QFont, QIcon

class PictureExplorer(QMainWindow):
    def __init__(self):
        super().__init__()
        self.img_file = 'beach.jpg'
        self.img = Image.open(self.img_file)
        self.pixmap = self.img.load()
        self.initUI()
        
        
    def initUI(self):
        '''
        setup UI components
        '''
        
        # File menu
        
        quitAct = QAction('&Quit',self)
        quitAct.setShortcut('Ctrl+Q')
        quitAct.setStatusTip('Exit application')
        quitAct.triggered.connect(qApp.quit)
        
        openAct = QAction('&Open...',self)
        openAct.setShortcut('Ctrl+O')
        openAct.setStatusTip('Open image file')
        openAct.triggered.connect(self.open_file)
    
        
        menubar = self.menuBar()
        file_menu = menubar.addMenu('&File')
        file_menu.addAction(openAct)
        file_menu.addAction(quitAct)
        
        
        # Top bar
        clr_txt = QLabel("Pixel Color",self)
        clr_txt.setFont(QFont('SansSerif',22))
        self.clr_lbl = QLabel(self)
        self.color = ImageQt(Image.new("RGB",(50,50)))
        pixmap = QPixmap.fromImage(self.color)
        self.clr_lbl.setPixmap(pixmap)
        self.rgb_lbl = QLabel("R: 0\tG: 0\tB: 0\t",self)
        self.rgb_lbl.setFont(QFont('SansSerif',22))
        
        # Picture
        self.pic_lbl = QLabel(self)
        pixmap = QPixmap(self.img_file)
        self.pic_lbl.setPixmap(pixmap)
        self.pic_lbl.mousePressEvent = self.getPos
        
        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)
        grid = QGridLayout(self.central_widget)
        
        grid.addWidget(clr_txt,1,1)
        grid.addWidget(self.clr_lbl,1,2)
        grid.addWidget(self.rgb_lbl,1,3)
        grid.addWidget(self.pic_lbl,2,0,1,4)
        
        self.setGeometry(300,300,640,480)
        self.setWindowTitle("Picture Explorer")
        self.setWindowIcon(QIcon('explorer.png'))
        
        self.statusbar = self.statusBar()
        self.statusbar.showMessage("Click in the picture to examine the colors")
        
        self.show()
       
    def getPos(self, e):
        '''
        get position of click and place a yellow + at position
        '''
        x = e.pos().x()
        y = e.pos().y()
        #print(x,y)
        
        #pixmap = QPixmap(self.img_file)
        #self.pic_lbl.setPixmap(pixmap)
        r,g,b = self.pixmap[x,y]
        self.img.close()
        self.img = Image.open(self.img_file)
        self.pixmap = self.img.load()
        try:
            for i in range(1,4):
                self.pixmap[x-i,y] = (255,255,0)
                self.pixmap[x+i,y] = (255,255,0)
                self.pixmap[x,y-i] = (255,255,0)
                self.pixmap[x,y+i] = (255,255,0)
        except:
            pass
        
        r_img = ImageQt(self.img)
        pixmap = QPixmap.fromImage(r_img)
        self.pic_lbl.setPixmap(pixmap)
        
        self.color = ImageQt(Image.new("RGB",(50,50),(r,g,b)))
        pixmap = QPixmap.fromImage(self.color)
        self.clr_lbl.setPixmap(pixmap)
        self.rgb_lbl.setText(f"R: {r: <3}\tG: {g: <3}\tB: {b: <3}\t")
        self.statusbar.showMessage(f"x:{x}\ty:{y}")
        
        
    def open_file(self):
        '''
        open image file dialog
        '''
        fname = QFileDialog.getOpenFileName(self,'Open file', 'home', "Image Files(*.png *.jpg *.jpeg);;All Files (*)")
        
        if fname[0]:
            self.img_file = fname[0]
            pixmap = QPixmap(fname[0])
            self.pic_lbl.setPixmap(pixmap)
            self.img = Image.open(self.img_file)
            self.pixmap = self.img.load()
            #self.setFixedSize(self.central_widget.sizeHint())
            self.show()
            
if __name__ == "__main__":
    app = QApplication(sys.argv)
    pe = PictureExplorer()
    sys.exit(app.exec_())
        