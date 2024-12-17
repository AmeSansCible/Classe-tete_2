import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from MainWindow import Ui_MainWindow  # Importez la classe générée dans le fichier MainWindow.py
from ui_window2 import Ui_Window2  # Importation de la classe de la deuxième fenêtre


class MyApp(QMainWindow):
    def __init__(self):
        super(MyApp, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        # Crée un bouton pour ouvrir la fenêtre 2
        self.ui.Bouton_ListeContraintes.clicked.connect(self.open_window2)

        # Initialisation de la fenêtre 2
        self.window2 = None

    def open_window2(self):
        if self.window2 is None:  # Crée une nouvelle instance si elle n'existe pas
            self.window2 = Window2()
        self.window2.show()
class Window2(QMainWindow):
    def __init__(self):
        super(Window2, self).__init__()
        self.ui = Ui_Window2()
        self.ui.setupUi(self)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())