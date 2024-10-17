import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from MainWindow import Ui_MainWindow  # Importez la classe générée dans le fichier MainWindow.py

class MyApp(QMainWindow):
    def __init__(self):
        super(MyApp, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())