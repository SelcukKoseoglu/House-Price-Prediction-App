# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_SalePrice(object):
    def setupUi(self, SalePrice):
        SalePrice.setObjectName("SalePrice")
        SalePrice.resize(500, 625)
        SalePrice.setMaximumSize(QtCore.QSize(500, 625))
        SalePrice.setStyleSheet("background-color:rgb(200, 200, 200);")
        self.centralwidget = QtWidgets.QWidget(SalePrice)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(40, 530, 151, 71))
        font = QtGui.QFont()
        font.setPointSize(-1)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.pushButton.setFont(font)
        self.pushButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton.setStyleSheet("QPushButton#pushButton {\n"
"    background-color: rgb(72,178,121);\n"
"    border-style: outset;\n"
"    border-width: 2px;\n"
"    border-radius: 20px;\n"
"    border-color: beige;\n"
"    font: bold 25px;\n"
"    padding: 6px;\n"
"    cursor:pointer;\n"
"}\n"
"")
        self.pushButton.setObjectName("pushButton")
        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(20, 20, 455, 478))
        self.widget.setObjectName("widget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.widget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.OverallQual_L = QtWidgets.QLabel(self.widget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.OverallQual_L.setFont(font)
        self.OverallQual_L.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.OverallQual_L.setObjectName("OverallQual_L")
        self.verticalLayout.addWidget(self.OverallQual_L)
        self.GrLivArea_L = QtWidgets.QLabel(self.widget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.GrLivArea_L.setFont(font)
        self.GrLivArea_L.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.GrLivArea_L.setObjectName("GrLivArea_L")
        self.verticalLayout.addWidget(self.GrLivArea_L)
        self.GarageCars_L = QtWidgets.QLabel(self.widget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.GarageCars_L.setFont(font)
        self.GarageCars_L.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.GarageCars_L.setObjectName("GarageCars_L")
        self.verticalLayout.addWidget(self.GarageCars_L)
        self.GarageArea_L = QtWidgets.QLabel(self.widget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.GarageArea_L.setFont(font)
        self.GarageArea_L.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.GarageArea_L.setObjectName("GarageArea_L")
        self.verticalLayout.addWidget(self.GarageArea_L)
        self.TotalBsmtSF_L = QtWidgets.QLabel(self.widget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.TotalBsmtSF_L.setFont(font)
        self.TotalBsmtSF_L.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.TotalBsmtSF_L.setObjectName("TotalBsmtSF_L")
        self.verticalLayout.addWidget(self.TotalBsmtSF_L)
        self.FirstFlrSF_L = QtWidgets.QLabel(self.widget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.FirstFlrSF_L.setFont(font)
        self.FirstFlrSF_L.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.FirstFlrSF_L.setObjectName("FirstFlrSF_L")
        self.verticalLayout.addWidget(self.FirstFlrSF_L)
        self.FullBath_L = QtWidgets.QLabel(self.widget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.FullBath_L.setFont(font)
        self.FullBath_L.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.FullBath_L.setObjectName("FullBath_L")
        self.verticalLayout.addWidget(self.FullBath_L)
        self.TotRmsAbvGrd_L = QtWidgets.QLabel(self.widget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.TotRmsAbvGrd_L.setFont(font)
        self.TotRmsAbvGrd_L.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.TotRmsAbvGrd_L.setObjectName("TotRmsAbvGrd_L")
        self.verticalLayout.addWidget(self.TotRmsAbvGrd_L)
        self.YearBuilt_L = QtWidgets.QLabel(self.widget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.YearBuilt_L.setFont(font)
        self.YearBuilt_L.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.YearBuilt_L.setObjectName("YearBuilt_L")
        self.verticalLayout.addWidget(self.YearBuilt_L)
        self.YearRemodAdd_L = QtWidgets.QLabel(self.widget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.YearRemodAdd_L.setFont(font)
        self.YearRemodAdd_L.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.YearRemodAdd_L.setObjectName("YearRemodAdd_L")
        self.verticalLayout.addWidget(self.YearRemodAdd_L)
        self.BsmtQual_L = QtWidgets.QLabel(self.widget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.BsmtQual_L.setFont(font)
        self.BsmtQual_L.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.BsmtQual_L.setObjectName("BsmtQual_L")
        self.verticalLayout.addWidget(self.BsmtQual_L)
        self.KitchenQual_L = QtWidgets.QLabel(self.widget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.KitchenQual_L.setFont(font)
        self.KitchenQual_L.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.KitchenQual_L.setObjectName("KitchenQual_L")
        self.verticalLayout.addWidget(self.KitchenQual_L)
        self.Foundation_L = QtWidgets.QLabel(self.widget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.Foundation_L.setFont(font)
        self.Foundation_L.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.Foundation_L.setObjectName("Foundation_L")
        self.verticalLayout.addWidget(self.Foundation_L)
        self.horizontalLayout.addLayout(self.verticalLayout)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.lineEdit = QtWidgets.QLineEdit(self.widget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEdit.sizePolicy().hasHeightForWidth())
        self.lineEdit.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lineEdit.setFont(font)
        self.lineEdit.setObjectName("lineEdit")
        self.verticalLayout_2.addWidget(self.lineEdit)
        self.lineEdit_2 = QtWidgets.QLineEdit(self.widget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEdit_2.sizePolicy().hasHeightForWidth())
        self.lineEdit_2.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lineEdit_2.setFont(font)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.verticalLayout_2.addWidget(self.lineEdit_2)
        self.lineEdit_3 = QtWidgets.QLineEdit(self.widget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEdit_3.sizePolicy().hasHeightForWidth())
        self.lineEdit_3.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lineEdit_3.setFont(font)
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.verticalLayout_2.addWidget(self.lineEdit_3)
        self.lineEdit_4 = QtWidgets.QLineEdit(self.widget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEdit_4.sizePolicy().hasHeightForWidth())
        self.lineEdit_4.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lineEdit_4.setFont(font)
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.verticalLayout_2.addWidget(self.lineEdit_4)
        self.lineEdit_5 = QtWidgets.QLineEdit(self.widget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEdit_5.sizePolicy().hasHeightForWidth())
        self.lineEdit_5.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lineEdit_5.setFont(font)
        self.lineEdit_5.setObjectName("lineEdit_5")
        self.verticalLayout_2.addWidget(self.lineEdit_5)
        self.lineEdit_6 = QtWidgets.QLineEdit(self.widget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEdit_6.sizePolicy().hasHeightForWidth())
        self.lineEdit_6.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lineEdit_6.setFont(font)
        self.lineEdit_6.setObjectName("lineEdit_6")
        self.verticalLayout_2.addWidget(self.lineEdit_6)
        self.lineEdit_7 = QtWidgets.QLineEdit(self.widget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEdit_7.sizePolicy().hasHeightForWidth())
        self.lineEdit_7.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lineEdit_7.setFont(font)
        self.lineEdit_7.setObjectName("lineEdit_7")
        self.verticalLayout_2.addWidget(self.lineEdit_7)
        self.lineEdit_8 = QtWidgets.QLineEdit(self.widget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEdit_8.sizePolicy().hasHeightForWidth())
        self.lineEdit_8.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lineEdit_8.setFont(font)
        self.lineEdit_8.setObjectName("lineEdit_8")
        self.verticalLayout_2.addWidget(self.lineEdit_8)
        self.lineEdit_9 = QtWidgets.QLineEdit(self.widget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEdit_9.sizePolicy().hasHeightForWidth())
        self.lineEdit_9.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lineEdit_9.setFont(font)
        self.lineEdit_9.setObjectName("lineEdit_9")
        self.verticalLayout_2.addWidget(self.lineEdit_9)
        self.lineEdit_10 = QtWidgets.QLineEdit(self.widget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEdit_10.sizePolicy().hasHeightForWidth())
        self.lineEdit_10.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lineEdit_10.setFont(font)
        self.lineEdit_10.setObjectName("lineEdit_10")
        self.verticalLayout_2.addWidget(self.lineEdit_10)
        self.comboBox = QtWidgets.QComboBox(self.widget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.comboBox.setFont(font)
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.verticalLayout_2.addWidget(self.comboBox)
        self.comboBox_2 = QtWidgets.QComboBox(self.widget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.comboBox_2.setFont(font)
        self.comboBox_2.setObjectName("comboBox_2")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.verticalLayout_2.addWidget(self.comboBox_2)
        self.comboBox_3 = QtWidgets.QComboBox(self.widget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.comboBox_3.setFont(font)
        self.comboBox_3.setObjectName("comboBox_3")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.verticalLayout_2.addWidget(self.comboBox_3)
        self.horizontalLayout.addLayout(self.verticalLayout_2)
        self.widget1 = QtWidgets.QWidget(self.centralwidget)
        self.widget1.setGeometry(QtCore.QRect(250, 530, 215, 65))
        self.widget1.setObjectName("widget1")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.widget1)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.label = QtWidgets.QLabel(self.widget1)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.verticalLayout_3.addWidget(self.label)
        self.label_2 = QtWidgets.QLabel(self.widget1)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_2.setFont(font)
        self.label_2.setText("")
        self.label_2.setObjectName("label_2")
        self.verticalLayout_3.addWidget(self.label_2)
        SalePrice.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(SalePrice)
        self.statusbar.setObjectName("statusbar")
        SalePrice.setStatusBar(self.statusbar)

        self.retranslateUi(SalePrice)
        QtCore.QMetaObject.connectSlotsByName(SalePrice)

    def retranslateUi(self, SalePrice):
        _translate = QtCore.QCoreApplication.translate
        SalePrice.setWindowTitle(_translate("SalePrice", "Sale Price Prediction"))
        self.pushButton.setText(_translate("SalePrice", "Calculate"))
        self.OverallQual_L.setText(_translate("SalePrice", "Overall Quality:"))
        self.GrLivArea_L.setText(_translate("SalePrice", "Above Ground Living Area:"))
        self.GarageCars_L.setText(_translate("SalePrice", "Garage Cars:"))
        self.GarageArea_L.setText(_translate("SalePrice", "Garage Area:"))
        self.TotalBsmtSF_L.setText(_translate("SalePrice", "Total of Basement Area: "))
        self.FirstFlrSF_L.setText(_translate("SalePrice", "First Floor:"))
        self.FullBath_L.setText(_translate("SalePrice", "Full Bathrooms:"))
        self.TotRmsAbvGrd_L.setText(_translate("SalePrice", " Total Rooms:"))
        self.YearBuilt_L.setText(_translate("SalePrice", "Year Built:"))
        self.YearRemodAdd_L.setText(_translate("SalePrice", "Remodel Date:"))
        self.BsmtQual_L.setText(_translate("SalePrice", "Basement Quality:"))
        self.KitchenQual_L.setText(_translate("SalePrice", "Kitchen Quality:"))
        self.Foundation_L.setText(_translate("SalePrice", "Foundation:"))
        self.comboBox.setItemText(0, _translate("SalePrice", "Choose"))
        self.comboBox.setItemText(1, _translate("SalePrice", "Excellent"))
        self.comboBox.setItemText(2, _translate("SalePrice", "Good"))
        self.comboBox.setItemText(3, _translate("SalePrice", "Typical"))
        self.comboBox.setItemText(4, _translate("SalePrice", "Fair"))
        self.comboBox.setItemText(5, _translate("SalePrice", "No Basement"))
        self.comboBox_2.setItemText(0, _translate("SalePrice", "Choose"))
        self.comboBox_2.setItemText(1, _translate("SalePrice", "Excellent"))
        self.comboBox_2.setItemText(2, _translate("SalePrice", "Good"))
        self.comboBox_2.setItemText(3, _translate("SalePrice", "Typical"))
        self.comboBox_2.setItemText(4, _translate("SalePrice", "Fair"))
        self.comboBox_2.setItemText(5, _translate("SalePrice", "Poor"))
        self.comboBox_3.setItemText(0, _translate("SalePrice", "Choose"))
        self.comboBox_3.setItemText(1, _translate("SalePrice", "Brick & Tile"))
        self.comboBox_3.setItemText(2, _translate("SalePrice", "Cinder Block"))
        self.comboBox_3.setItemText(3, _translate("SalePrice", "Poured Contrete"))
        self.comboBox_3.setItemText(4, _translate("SalePrice", "Slab"))
        self.comboBox_3.setItemText(5, _translate("SalePrice", "Stone"))
        self.comboBox_3.setItemText(6, _translate("SalePrice", "Wood"))
        # self.label.setText(_translate("SalePrice", "Sale Price Prediction:"))


