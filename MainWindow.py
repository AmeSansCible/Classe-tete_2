# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_interface_MainWindow.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget.setGeometry(QtCore.QRect(20, 150, 151, 71))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(0)
        self.tableWidget.setRowCount(0)
        self.tableWidget_2 = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget_2.setGeometry(QtCore.QRect(20, 230, 151, 71))
        self.tableWidget_2.setObjectName("tableWidget_2")
        self.tableWidget_2.setColumnCount(0)
        self.tableWidget_2.setRowCount(0)
        self.tableWidget_3 = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget_3.setGeometry(QtCore.QRect(20, 310, 151, 71))
        self.tableWidget_3.setObjectName("tableWidget_3")
        self.tableWidget_3.setColumnCount(0)
        self.tableWidget_3.setRowCount(0)
        self.tableWidget_4 = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget_4.setGeometry(QtCore.QRect(200, 230, 151, 71))
        self.tableWidget_4.setObjectName("tableWidget_4")
        self.tableWidget_4.setColumnCount(0)
        self.tableWidget_4.setRowCount(0)
        self.tableWidget_5 = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget_5.setGeometry(QtCore.QRect(200, 310, 151, 71))
        self.tableWidget_5.setObjectName("tableWidget_5")
        self.tableWidget_5.setColumnCount(0)
        self.tableWidget_5.setRowCount(0)
        self.tableWidget_6 = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget_6.setGeometry(QtCore.QRect(200, 150, 151, 71))
        self.tableWidget_6.setObjectName("tableWidget_6")
        self.tableWidget_6.setColumnCount(0)
        self.tableWidget_6.setRowCount(0)
        self.tableWidget_7 = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget_7.setGeometry(QtCore.QRect(380, 230, 151, 71))
        self.tableWidget_7.setObjectName("tableWidget_7")
        self.tableWidget_7.setColumnCount(0)
        self.tableWidget_7.setRowCount(0)
        self.tableWidget_8 = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget_8.setGeometry(QtCore.QRect(380, 310, 151, 71))
        self.tableWidget_8.setObjectName("tableWidget_8")
        self.tableWidget_8.setColumnCount(0)
        self.tableWidget_8.setRowCount(0)
        self.tableWidget_9 = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget_9.setGeometry(QtCore.QRect(380, 150, 151, 71))
        self.tableWidget_9.setObjectName("tableWidget_9")
        self.tableWidget_9.setColumnCount(0)
        self.tableWidget_9.setRowCount(0)

        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setGeometry(QtCore.QRect(600, 0, 16, 551))
        self.line.setFrameShape(QtWidgets.QFrame.VLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")

        self.Titre_Classe = QtWidgets.QLabel(self.centralwidget)
        self.Titre_Classe.setGeometry(QtCore.QRect(670, 10, 47, 13))
        self.Titre_Classe.setObjectName("Titre_Classe")

        self.line_2 = QtWidgets.QFrame(self.centralwidget)
        self.line_2.setGeometry(QtCore.QRect(610, 250, 191, 16))
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")

        self.Titre_Plan = QtWidgets.QLabel(self.centralwidget)
        self.Titre_Plan.setGeometry(QtCore.QRect(670, 270, 47, 13))
        self.Titre_Plan.setObjectName("Titre_Plan")

        self.Bouton_FilleGarcon = QtWidgets.QRadioButton(self.centralwidget)
        self.Bouton_FilleGarcon.setGeometry(QtCore.QRect(620, 300, 82, 17))
        self.Bouton_FilleGarcon.setObjectName("Bouton_FilleGarcon")

        self.Bouton_Niveaux = QtWidgets.QRadioButton(self.centralwidget)
        self.Bouton_Niveaux.setGeometry(QtCore.QRect(620, 320, 131, 17))
        self.Bouton_Niveaux.setObjectName("Bouton_Niveaux")

        self.Bouton_Contraintes = QtWidgets.QRadioButton(self.centralwidget)
        self.Bouton_Contraintes.setGeometry(QtCore.QRect(620, 340, 82, 17))
        self.Bouton_Contraintes.setObjectName("Bouton_Contraintes")

        self.Bouton_Aleatoire = QtWidgets.QRadioButton(self.centralwidget)
        self.Bouton_Aleatoire.setGeometry(QtCore.QRect(620, 360, 82, 17))
        self.Bouton_Aleatoire.setObjectName("Bouton_Aleatoire")

        # Création du QButtonGroup
        self.plan_group1 = QtWidgets.QButtonGroup(self.centralwidget)

        # Ajout des radio buttons au groupe
        self.plan_group1.addButton(self.Bouton_FilleGarcon)
        self.plan_group1.addButton(self.Bouton_Niveaux)
        self.plan_group1.addButton(self.Bouton_Contraintes)
        self.plan_group1.addButton(self.Bouton_Aleatoire)

        # Le mode exclusif (tu peux en sélectionner qu'un)
        self.plan_group1.setExclusive(True)


        self.Bouton_Add_Tables = QtWidgets.QPushButton(self.centralwidget)
        self.Bouton_Add_Tables.setGeometry(QtCore.QRect(640, 50, 75, 23))
        self.Bouton_Add_Tables.setObjectName("Bouton_Add_Tables")

        self.Bouton_Modif = QtWidgets.QPushButton(self.centralwidget)
        self.Bouton_Modif.setGeometry(QtCore.QRect(640, 80, 75, 23))
        self.Bouton_Modif.setObjectName("Bouton_Modif")

        self.Bouton_ListeContraintes = QtWidgets.QPushButton(self.centralwidget)
        self.Bouton_ListeContraintes.setGeometry(QtCore.QRect(640, 120, 131, 23))
        self.Bouton_ListeContraintes.setObjectName("Bouton_ListeContraintes")

        self.Bouton_Generer = QtWidgets.QPushButton(self.centralwidget)
        self.Bouton_Generer.setGeometry(QtCore.QRect(640, 400, 111, 41))
        self.Bouton_Generer.setObjectName("Bouton_Generer")

        self.Bouton_Exporter = QtWidgets.QPushButton(self.centralwidget)
        self.Bouton_Exporter.setGeometry(QtCore.QRect(640, 500, 111, 41))
        self.Bouton_Exporter.setObjectName("Bouton_Exporter")

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.Titre_Classe.setText(_translate("MainWindow", "Classe"))
        self.Titre_Plan.setText(_translate("MainWindow", "Plan"))
        self.Bouton_FilleGarcon.setText(_translate("MainWindow", "Fille/garçon"))
        self.Bouton_Niveaux.setText(_translate("MainWindow", "Niveaux (fort/faible)"))
        self.Bouton_Contraintes.setText(_translate("MainWindow", "Contraintes"))
        self.Bouton_Aleatoire.setText(_translate("MainWindow", "Aléatoire"))
        self.Bouton_Add_Tables.setText(_translate("MainWindow", "+ Tables"))
        self.Bouton_Modif.setText(_translate("MainWindow", "Modifications"))
        self.Bouton_ListeContraintes.setText(_translate("MainWindow", "Liste et contraintes"))
        self.Bouton_Generer.setText(_translate("MainWindow", "Générer"))
        self.Bouton_Exporter.setText(_translate("MainWindow", "Exporter en PDF"))
