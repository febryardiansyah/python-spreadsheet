import sys
from PyQt5.QtCore import*
from PyQt5.QtWidgets import*
from PyQt5.QtWidgets import QApplication
from quickstart import QuickStart


class MainWindow(QWidget):    
    def __init__(self):
        super().__init__()        
        self.app = main()
        #self.app.main()
        self.setup()
        self.parse()
    
    def parse(self, index = 0):
        message = self.app.main()
        print(message)
        for data in message:
            print(f'nilainya adalah :{data}')
        return message[index]

    def setup(self):
        print('this got rendered after spreadsheet')
        self.resize(400,300)
        self.move(300,300)
        self.setWindowTitle('Dame Dayo')

        self.label1 = QLabel(f'{self.parse(0)}')
        self.label2 = QLabel(f'{self.parse(1)}')
        layout = QGridLayout()

        layout.addWidget(self.label1,0,0)
        layout.addWidget(self.label2,1,0)
        self.setLayout(layout)


if __name__ == '__main__':
	a= QApplication(sys.argv)
	
	minform = MainWindow()
	minform.show()
	
	a.exec()