import sys
from PyQt5.QtWidgets import QMainWindow, QApplication, QWidget, QAction, QTableWidget,QTableWidgetItem,QVBoxLayout, QStackedWidget
from PyQt5 import uic, QtCore, QtGui, QtWidgets 
from PyQt5.QtGui import QIcon, QPixmap
import psycopg2 

qtCreatorFile = "Code/MimsChrisMilestone1.ui" # Enter file here.

Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)

class milestone1(QMainWindow):
    def __init__(self):
        super(milestone1, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.loadStateList()
        self.ui.stateList.currentTextChanged.connect(self.stateChanged)
        self.ui.cityList.itemSelectionChanged.connect(self.cityChanged)
        self.ui.bname.textChanged.connect(self.getBusinessName)
        self.ui.businesses.itemSelectionChanged.connect(self.displayBusinessCity)

        # Go to page 1 Button
        self.ui.goToPage1.clicked.connect(lambda: self.ui.stackedWidget.setCurrentIndex(0))
        # Go to page 2 Button
        self.ui.goToPage2.clicked.connect(lambda: self.ui.stackedWidget.setCurrentIndex(1))


    def executeQuery(self, sql_str):
        try:
            conn = psycopg2.connect(
                                    host="localhost",
                                    database="milestone1db",
                                    user="cmims451",
                                    password="JV6_buLc8*z*GUvJNoqNRB3B!Ncr6Giw")
        except:
            print('Unable to connect to the database!')
        cur = conn.cursor()
        cur.execute(sql_str)
        conn.commit()
        result = cur.fetchall()
        conn.close()
        return result 

    def loadStateList(self):
        self.ui.stateList.clear()
        sql_str = "SELECT DISTINCT b_state FROM business ORDER BY b_state;"
        try:
            results = self.executeQuery(sql_str)
            for row in results:
                self.ui.stateList.addItem(row[0])
        except:
            print('Query failed at loadStateList!')
        self.ui.stateList.setCurrentIndex(-1)
        self.ui.stateList.clearEditText()

    def stateChanged(self):
        self.ui.cityList.clear()
        state = self.ui.stateList.currentText()
        if (self.ui.stateList.currentIndex() >= 0):
            sql_str = "SELECT DISTINCT b_city FROM business WHERE b_state ='" + state + "' ORDER BY b_city;"
            try:
                results = self.executeQuery(sql_str)
                for row in results:
                    self.ui.cityList.addItem(row[0]) 
            except:
                print("Query has failed at stateChanged!")
            for i in reversed(range(self.ui.businessTable.rowCount())):
                self.ui.businessTable.removeRow(i)
            sql_str = "SELECT b_name, b_city, b_state FROM business WHERE b_state = '" + state + "' ORDER BY b_name;"
            try:
                results = self.executeQuery(sql_str)
                style = "::section {""background-color: #f3f3f3; }"
                self.ui.businessTable.horizontalHeader().setStyleSheet(style)
                self.ui.businessTable.setColumnCount(len(results[0]))
                self.ui.businessTable.setRowCount(len(results))
                self.ui.businessTable.setHorizontalHeaderLabels(['Business Name', 'City', 'State'])
                self.ui.businessTable.resizeColumnsToContents()
                self.ui.businessTable.setColumnWidth(0, 300)
                self.ui.businessTable.setColumnWidth(1, 100)
                self.ui.businessTable.setColumnWidth(2, 50)
                currentRowCount = 0 
                for row in results:
                    for colCount in range(0, len(results[0])):
                        self.ui.businessTable.setItem(currentRowCount, colCount, QTableWidgetItem(row[colCount]))
                    currentRowCount += 1
            except:
                print("Query has failed at businessTable fill!")
    
    def cityChanged(self):
        if (self.ui.stateList.currentIndex() >= 0) and (len(self.ui.cityList.selectedItems()) > 0):
            state = self.ui.stateList.currentText()
            city = self.ui.cityList.selectedItems()[0].text()
            sql_str = "SELECT b_name, b_city, b_state FROM business WHERE b_state = '" + state + "' AND b_city = '" + city + "' ORDER BY b_name;"
            results = self.executeQuery(sql_str)
            try:
                    results = self.executeQuery(sql_str)
                    style = "::section {""background-color: #f3f3f3; }"
                    self.ui.businessTable.horizontalHeader().setStyleSheet(style)
                    self.ui.businessTable.setColumnCount(len(results[0]))
                    self.ui.businessTable.setRowCount(len(results))
                    self.ui.businessTable.setHorizontalHeaderLabels(['Business Name', 'City', 'State'])
                    self.ui.businessTable.resizeColumnsToContents()
                    self.ui.businessTable.setColumnWidth(0, 300)
                    self.ui.businessTable.setColumnWidth(1, 100)
                    self.ui.businessTable.setColumnWidth(2, 50)
                    currentRowCount = 0 
                    for row in results:
                        for colCount in range(0, len(results[0])):
                            self.ui.businessTable.setItem(currentRowCount, colCount, QTableWidgetItem(row[colCount]))
                        currentRowCount += 1
            except:
                print("Query has failed at businessTable - cityUpdate fill!")
    def getBusinessName(self):
        self.ui.businesses.clear()
        businessname = self.ui.bname.text()
        sql_str = "SELECT b_name FROM business WHERE b_name LIKE '%" + businessname + "%' ORDER BY b_name;"
        try:
            results = self.executeQuery(sql_str)
            for row in results:
                self.ui.businesses.addItem(row[0])
        except:
            print("Query failed at business search fill!")

    def displayBusinessCity(self):
        businessname = self.ui.businesses.selectedItems()[0].text()
        sql_str = "SELECT b_city FROM business WHERE b_name = '" + businessname + "';"
        try:
            results = self.executeQuery(sql_str)
            self.ui.bcity.setText(results[0][0])
        except:
            print("Query failed at ")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = milestone1()
    window.show()
    sys.exit(app.exec_())


