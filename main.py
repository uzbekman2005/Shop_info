from PyQt6.QtWidgets import QApplication, QMainWindow, QMessageBox
from list import *
from Sotorage import *
import sys


class Window(QMainWindow):
    def __init__(self, parent=None):
        super(Window, self).__init__(parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.tProducts.autoScrollMargin()
        self.ui.btnAdd.clicked.connect(self.addPressed)
        self.loadDataToTable()
        self.ui.btnsearch.clicked.connect(self.search)
        self.ui.deleteSearch.clicked.connect(self.deleteProduct)
        self.ui.btnshowall.clicked.connect(self.showAllProducts)
        self.ui.linesearch.textChanged.connect(self.search)
        self.ui.btnSort.clicked.connect(self.sortButton)

    def sortButton(self):
        if self.ui.combosort.currentText() == "Name":
            products_in.sort(key=lambda x:x["product"])
        if self.ui.combosort.currentText() == "Price":
            products_in.sort(key=lambda x:int(x["price"]), reverse=True)
        if self.ui.combosort.currentText() == "Amount":
            products_in.sort(key=lambda x:int(x["amount"]), reverse=True)
        self.showAllProducts()

    def input_msg(self):
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Icon.Information)
        msg.setText("Siz ma'lumotlarni noto'g'ri kiritdingiz\nMa'lumotlarni to'g'ri kiriting😊")
        msg.setWindowTitle("Error")
        msg.setStandardButtons(QMessageBox.StandardButton.Ok | QMessageBox.StandardButton.Cancel)
        res = msg.exec()
        if res == QMessageBox.StandardButton.Cancel:
            self.ui.linePrice.setText("")
            self.ui.lineAmount.setText("")
            self.ui.lineProduct.setText("")

    def deleteProduct(self):
        txtsearch = self.ui.linesearch.text()
        for prod in products_in:
            if prod["product"] == txtsearch:
                products_in.remove(prod)
                self.loadDataToTable()
                self.ui.linesearch.setText("")
        updateProductInfo()

    def search(self):
        txtSearch = self.ui.linesearch.text().lower()
        if txtSearch != "":
            res = []
            if self.ui.rbproduct.isChecked():
                res = list(filter(lambda item: txtSearch in item["product"].lower(), products_in))
            if self.ui.rbprice.isChecked():
                res = list(filter(lambda item: (txtSearch) in str(item["price"]), products_in))
            if self.ui.rbamount.isChecked():
                res = list(filter(lambda item: (txtSearch) in str(item["amount"]), products_in))
            self.ui.tProducts.setRowCount(len(res))
            row = 0
            for prod in res:
                self.ui.tProducts.setItem(row, 0, QtWidgets.QTableWidgetItem(prod["product"]))
                self.ui.tProducts.setItem(row, 1, QtWidgets.QTableWidgetItem(str(prod["price"])))
                self.ui.tProducts.setItem(row, 2, QtWidgets.QTableWidgetItem(str(prod["amount"])))
                row += 1
            # self.ui.linesearch.setText("")
        else:
            self.showAllProducts()


    def showAllProducts(self):
        self.loadDataToTable()

    def loadDataToTable(self):
        row = 0
        self.ui.tProducts.setRowCount(len(products_in))
        for prod in products_in:
            self.ui.tProducts.setItem(row, 0, QtWidgets.QTableWidgetItem(prod["product"]))
            self.ui.tProducts.setItem(row, 1, QtWidgets.QTableWidgetItem(str(prod["price"])))
            self.ui.tProducts.setItem(row, 2, QtWidgets.QTableWidgetItem(str(prod["amount"])))
            row+=1

    def addPressed(self):
        txtProduct = self.ui.lineProduct.text()
        txtPrice = self.ui.linePrice.text()
        txtAmount = self.ui.lineAmount.text()

        if txtProduct != "" and txtPrice != "" and txtAmount != "" and txtPrice.isdigit() and txtAmount.isdigit():
            dict1 = {}
            dict1["product"] = txtProduct
            dict1["price"] = txtPrice
            dict1["amount"] = txtAmount
            products_in.append(dict1)
            self.loadDataToTable()
            self.ui.linePrice.setText("")
            self.ui.lineAmount.setText("")
            self.ui.lineProduct.setText("")
        else:
            self.input_msg()

        updateProductInfo()


def main():
    app = QApplication([])
    window = Window()
    window.show()
    sys.exit(app.exec())


if __name__ == "__main__":
    main()
