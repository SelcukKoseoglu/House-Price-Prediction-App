# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from ui import Ui_SalePrice
import numpy as np
from Model import model

# Press the green button in the gutter to run the script.

def Error():
    QtWidgets.QMessageBox.about(SalePrice,"Error","Please enter all blocks")

def get_item():
    datas = [ui.lineEdit.text(), ui.lineEdit_2.text(), ui.lineEdit_3.text(), ui.lineEdit_4.text(),
             ui.lineEdit_5.text(), ui.lineEdit_6.text(), ui.lineEdit_7.text(), ui.lineEdit_8.text(),
             ui.lineEdit_9.text(), ui.lineEdit_10.text(), ui.comboBox.currentIndex(),
             ui.comboBox_2.currentIndex(), ui.comboBox_3.currentIndex()]
    flag = [string for string in datas[:10] if not string.isdigit()]
    if len(flag) != 0:
        return Error()
    flag = all(datas[10:])
    if not flag:
        return Error()

    dictionary = {
        'OverallQual': float(ui.lineEdit.text()),
        'GrLivArea': float(ui.lineEdit_2.text()),
        'GarageCars': float(ui.lineEdit_3.text()),
        'GarageArea': float(ui.lineEdit_4.text()),
        'TotalBsmtSF': float(ui.lineEdit_5.text()),
        '1stFlrSF': float(ui.lineEdit_6.text()),
        'FullBath': float(ui.lineEdit_7.text()),
        'TotRmsAbvGrd': float(ui.lineEdit_8.text()),
        'YearBuilt': float(ui.lineEdit_9.text()),
        'YearRemodAdd': float(ui.lineEdit_10.text()),

        'BsmtQual_Ex':0,
        'BsmtQual_Fa': 0,
        'BsmtQual_Gd': 0,
        'BsmtQual_TA': 0,

        'KitchenQual_Ex':0,
        'KitchenQual_Fa': 0,
        'KitchenQual_Gd': 0,
        'KitchenQual_TA': 0,

        'Foundation_BrkTil':0,
        'Foundation_CBlock': 0,
        'Foundation_PConc': 0,
        'Foundation_Slab': 0,
        'Foundation_Stone': 0,
        'Foundation_Wood': 0,
    }
    if ui.comboBox.currentIndex() == 1: dictionary['BsmtQual_Ex'] = 1
    if ui.comboBox.currentIndex() == 2: dictionary['BsmtQual_Fa'] = 1
    if ui.comboBox.currentIndex() == 3: dictionary['BsmtQual_Gd'] = 1
    if ui.comboBox.currentIndex() == 4: dictionary['BsmtQual_TA'] = 1

    if ui.comboBox_2.currentIndex() == 1: dictionary['KitchenQual_Ex'] = 1
    if ui.comboBox_2.currentIndex() == 2: dictionary['KitchenQual_Fa'] = 1
    if ui.comboBox_2.currentIndex() == 3: dictionary['KitchenQual_Gd'] = 1
    if ui.comboBox_2.currentIndex() == 4: dictionary['KitchenQual_TA'] = 1

    if ui.comboBox_3.currentIndex() == 1: dictionary['Foundation_BrkTil'] = 1
    if ui.comboBox_3.currentIndex() == 2: dictionary['Foundation_CBlock'] = 1
    if ui.comboBox_3.currentIndex() == 3: dictionary['Foundation_PConc'] = 1
    if ui.comboBox_3.currentIndex() == 4: dictionary['Foundation_Slab'] = 1
    if ui.comboBox_3.currentIndex() == 5: dictionary['Foundation_Stone'] = 1
    if ui.comboBox_3.currentIndex() == 6: dictionary['Foundation_Wood'] = 1


    values = np.array(list(dictionary.values())).reshape((1,24))

    return Predict(values)


def Predict(values):
    prediction = model.predict(values)
    return label_writer(int(prediction[0][0]))

def label_writer(prediction):
    ui.label.setText(str('Sale Price Prediction:'))
    ui.label_2.setText(str(prediction))

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    SalePrice = QtWidgets.QMainWindow()
    ui = Ui_SalePrice()
    ui.setupUi(SalePrice)
    ui.pushButton.clicked.connect(get_item)
    SalePrice.show()
    sys.exit(app.exec_())
