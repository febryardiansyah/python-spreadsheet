import sys
from PyQt5.QtCore import*
from PyQt5.QtWidgets import*
from PyQt5.QtWidgets import QApplication
from quickstart import QuickStart


class MainWindow(QWidget):    
    def __init__(self):
        super().__init__()        
        self.app = QuickStart()
        self.setup()
        print(self.setup())
    
    def setup(self):
        print('this got rendered after spreadsheet')
        self.resize(400,300)
        self.move(300,300)
        self.setWindowTitle('Dame Dayo')

        self.label1 = QLabel(f'{self.app.main()} -- result')
        self.label2 = QLabel('label2')

        layout = QGridLayout()

        layout.addWidget(self.label1,0,0)
        layout.addWidget(self.label2,0,1)
        self.setLayout(layout)

        

if __name__ == '__main__':
	a= QApplication(sys.argv)
	
	minform = MainWindow()
	minform.show()
	
	a.exec()