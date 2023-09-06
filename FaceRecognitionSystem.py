from PyQt5 import QtCore, QtGui, QtWidgets
import sys
import cv2
import numpy as np
import sqlite3
from PIL import Image
import pickle
import os
from PyQt5.QtGui import QPixmap
from time import sleep
from random import randint
import resourcefile

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setEnabled(True)
        MainWindow.resize(1920, 1080)
        MainWindow.setStyleSheet("background-image: url(:/images/backgroundImage.jpg);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.frameVideo = QtWidgets.QFrame(self.centralwidget)
        self.frameVideo.setGeometry(QtCore.QRect(220, 9, 971, 591))
        self.frameVideo.setStyleSheet("background: rgb(47,100,178);")
        self.frameVideo.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frameVideo.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frameVideo.setObjectName("frameVideo")
        self.groupBoxTrain = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBoxTrain.setGeometry(QtCore.QRect(1240, 580, 411, 291))
        self.groupBoxTrain.setStyleSheet("background-color: rgb(247, 247, 247);\n"
"font: 9pt \"MS Shell Dlg 2\";\n"
"border:none;\n"
"color:rgb(255, 255, 255);")
        self.groupBoxTrain.setTitle("")
        self.groupBoxTrain.setObjectName("groupBoxTrain")
        self.pushButtonCaptureData = QtWidgets.QPushButton(self.groupBoxTrain)
        self.pushButtonCaptureData.setGeometry(QtCore.QRect(190, 140, 151, 31))
        self.pushButtonCaptureData.setStyleSheet("color:white;\n"
"background: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0.011, stop:0.0547264 rgba(62, 130, 10, 255), stop:1 rgba(100, 183, 2, 255));\n"
"border-radius:6px;")
        self.pushButtonCaptureData.setObjectName("pushButtonCaptureData")
        self.Surnametrain = QtWidgets.QLabel(self.groupBoxTrain)
        self.Surnametrain.setGeometry(QtCore.QRect(20, 60, 71, 21))
        self.Surnametrain.setStyleSheet("background:none;\n"
"color: #ffffff")
        self.Surnametrain.setObjectName("Surnametrain")
        self.Nintrain = QtWidgets.QLabel(self.groupBoxTrain)
        self.Nintrain.setGeometry(QtCore.QRect(20, 100, 55, 21))
        self.Nintrain.setStyleSheet("background:none;\n"
"color: #ffffff")
        self.Nintrain.setObjectName("Nintrain")
        self.waitTrain = QtWidgets.QLabel(self.groupBoxTrain)
        self.waitTrain.setGeometry(QtCore.QRect(20, 180, 111, 16))
        self.waitTrain.setStyleSheet("background:none;\n"
"color: rgb(85, 255, 0);")
        self.waitTrain.setObjectName("waitTrain")
        self.SurnameInput = QtWidgets.QTextEdit(self.groupBoxTrain)
        self.SurnameInput.setGeometry(QtCore.QRect(90, 50, 281, 31))
        self.SurnameInput.setStyleSheet("background: transparent;\n"
"border:1px solid #99a1bc;\n"
"border-radius:6px")
        self.SurnameInput.setObjectName("SurnameInput")
        self.NinInput = QtWidgets.QTextEdit(self.groupBoxTrain)
        self.NinInput.setGeometry(QtCore.QRect(90, 90, 281, 31))
        self.NinInput.setStyleSheet("background: transparent;\n"
"border:1px solid #99a1bc;\n"
"border-radius:6px")
        self.NinInput.setObjectName("NinInput")
        self.pushButtonTrainFile = QtWidgets.QPushButton(self.groupBoxTrain)
        self.pushButtonTrainFile.setGeometry(QtCore.QRect(190, 250, 151, 28))
        self.pushButtonTrainFile.setStyleSheet("background: rgb(63, 69, 157);\n"
"background-color: qlineargradient(spread:pad, x1:0.01, y1:0.006, x2:1, y2:0, stop:0 rgba(4, 0, 133, 255), stop:1 rgba(0, 19, 176, 255));\n"
"color:white;\n"
"border-radius:8px")
        self.pushButtonTrainFile.setObjectName("pushButtonTrainFile")
        self.words1 = QtWidgets.QLabel(self.groupBoxTrain)
        self.words1.setGeometry(QtCore.QRect(20, 200, 381, 21))
        self.words1.setStyleSheet("background:none;\n"
"color: #ffffff")
        self.words1.setObjectName("words1")
        self.words2 = QtWidgets.QLabel(self.groupBoxTrain)
        self.words2.setGeometry(QtCore.QRect(10, 220, 301, 21))
        self.words2.setStyleSheet("background:none;\n"
"color:#ffffff")
        self.words2.setObjectName("words2")
        self.label_2 = QtWidgets.QLabel(self.groupBoxTrain)
        self.label_2.setGeometry(QtCore.QRect(20, 20, 81, 16))
        self.label_2.setStyleSheet("color: rgb(255, 255, 255);\n"
"font: 10pt \"MS Shell Dlg 2\";\n"
"background:transparent")
        self.label_2.setObjectName("label_2")
        self.groupBoxDectect = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBoxDectect.setGeometry(QtCore.QRect(170, 620, 1051, 251))
        self.groupBoxDectect.setStyleSheet("background: transparent;\n"
"color: rgb(255, 255, 255);\n"
"font: 9pt \"MS Shell Dlg 2\";\n"
"border:none;\n"
"border-bottom:0.5px solid #9ca9ff\n"
"")
        self.groupBoxDectect.setObjectName("groupBoxDectect")
        self.Surname = QtWidgets.QLabel(self.groupBoxDectect)
        self.Surname.setGeometry(QtCore.QRect(210, 80, 241, 21))
        self.Surname.setObjectName("Surname")
        self.Givenname = QtWidgets.QLabel(self.groupBoxDectect)
        self.Givenname.setGeometry(QtCore.QRect(210, 120, 241, 18))
        self.Givenname.setObjectName("Givenname")
        self.Nationality = QtWidgets.QLabel(self.groupBoxDectect)
        self.Nationality.setGeometry(QtCore.QRect(210, 150, 241, 21))
        self.Nationality.setObjectName("Nationality")
        self.Nin = QtWidgets.QLabel(self.groupBoxDectect)
        self.Nin.setGeometry(QtCore.QRect(210, 180, 241, 31))
        self.Nin.setObjectName("Nin")
        self.ImageFace = QtWidgets.QLabel(self.groupBoxDectect)
        self.ImageFace.setGeometry(QtCore.QRect(50, 60, 141, 151))
        self.ImageFace.setStyleSheet("color: rgb(218, 218, 218);\n"
"border-color:1px solid #d5ecff;\n"
"background-color: rgb(47, 108, 188);")
        self.ImageFace.setFrameShape(QtWidgets.QFrame.Box)
        self.ImageFace.setText("")
        self.ImageFace.setObjectName("ImageFace")
        self.DateOfBirth = QtWidgets.QLabel(self.groupBoxDectect)
        self.DateOfBirth.setGeometry(QtCore.QRect(480, 70, 271, 31))
        self.DateOfBirth.setObjectName("DateOfBirth")
        self.Gender = QtWidgets.QLabel(self.groupBoxDectect)
        self.Gender.setGeometry(QtCore.QRect(480, 120, 271, 21))
        self.Gender.setObjectName("Gender")
        self.Village = QtWidgets.QLabel(self.groupBoxDectect)
        self.Village.setGeometry(QtCore.QRect(480, 150, 271, 21))
        self.Village.setObjectName("Village")
        self.Parish = QtWidgets.QLabel(self.groupBoxDectect)
        self.Parish.setGeometry(QtCore.QRect(480, 190, 271, 21))
        self.Parish.setObjectName("Parish")
        self.SubCounnty = QtWidgets.QLabel(self.groupBoxDectect)
        self.SubCounnty.setGeometry(QtCore.QRect(780, 70, 261, 31))
        self.SubCounnty.setObjectName("SubCounnty")
        self.county = QtWidgets.QLabel(self.groupBoxDectect)
        self.county.setGeometry(QtCore.QRect(780, 120, 261, 21))
        self.county.setObjectName("county")
        self.District = QtWidgets.QLabel(self.groupBoxDectect)
        self.District.setGeometry(QtCore.QRect(780, 150, 261, 21))
        self.District.setObjectName("District")
        self.groupBoxTopMatches_2 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBoxTopMatches_2.setGeometry(QtCore.QRect(1240, 0, 411, 571))
        self.groupBoxTopMatches_2.setStyleSheet("font: 9pt \"MS Shell Dlg 2\";\n"
"border:none;\n"
"color: rgb(85, 170, 0);")
        self.groupBoxTopMatches_2.setTitle("")
        self.groupBoxTopMatches_2.setObjectName("groupBoxTopMatches_2")
        self.tabWidget = QtWidgets.QTabWidget(self.groupBoxTopMatches_2)
        self.tabWidget.setGeometry(QtCore.QRect(10, 40, 411, 541))
        self.tabWidget.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"")
        self.tabWidget.setObjectName("tabWidget")
        self.Details = QtWidgets.QWidget()
        self.Details.setObjectName("Details")
        self.Occupation = QtWidgets.QLabel(self.Details)
        self.Occupation.setGeometry(QtCore.QRect(10, 300, 161, 31))
        self.Occupation.setStyleSheet("color: rgb(204, 255, 176);\n"
"background:transparent")
        self.Occupation.setObjectName("Occupation")
        self.NextOfKin = QtWidgets.QLabel(self.Details)
        self.NextOfKin.setGeometry(QtCore.QRect(10, 210, 161, 21))
        self.NextOfKin.setStyleSheet("color: rgb(204, 255, 176);\n"
"background:transparent")
        self.NextOfKin.setObjectName("NextOfKin")
        self.physicalAddress = QtWidgets.QLabel(self.Details)
        self.physicalAddress.setGeometry(QtCore.QRect(10, 270, 151, 21))
        self.physicalAddress.setStyleSheet("color: rgb(204, 255, 176);\n"
"background:transparent")
        self.physicalAddress.setObjectName("physicalAddress")
        self.telephone = QtWidgets.QLabel(self.Details)
        self.telephone.setGeometry(QtCore.QRect(10, 240, 161, 21))
        self.telephone.setStyleSheet("color: rgb(204, 255, 176);\n"
"background:transparent")
        self.telephone.setObjectName("telephone")
        self.Relative1Image = QtWidgets.QLabel(self.Details)
        self.Relative1Image.setGeometry(QtCore.QRect(10, 10, 141, 151))
        self.Relative1Image.setStyleSheet("color: rgb(255, 255, 255);")
        self.Relative1Image.setFrameShape(QtWidgets.QFrame.Box)
        self.Relative1Image.setText("")
        self.Relative1Image.setObjectName("Relative1Image")
        self.Relative2Image = QtWidgets.QLabel(self.Details)
        self.Relative2Image.setGeometry(QtCore.QRect(210, 10, 141, 151))
        self.Relative2Image.setStyleSheet("color: rgb(255, 255, 255);")
        self.Relative2Image.setFrameShape(QtWidgets.QFrame.Box)
        self.Relative2Image.setText("")
        self.Relative2Image.setObjectName("Relative2Image")
        self.NextOfKin_2 = QtWidgets.QLabel(self.Details)
        self.NextOfKin_2.setGeometry(QtCore.QRect(220, 210, 171, 21))
        self.NextOfKin_2.setStyleSheet("color: rgb(204, 255, 176);\n"
"background:transparent")
        self.NextOfKin_2.setObjectName("NextOfKin_2")
        self.physicalAddress_2 = QtWidgets.QLabel(self.Details)
        self.physicalAddress_2.setGeometry(QtCore.QRect(220, 270, 171, 21))
        self.physicalAddress_2.setStyleSheet("color: rgb(204, 255, 176);\n"
"background:transparent")
        self.physicalAddress_2.setObjectName("physicalAddress_2")
        self.telephone_2 = QtWidgets.QLabel(self.Details)
        self.telephone_2.setGeometry(QtCore.QRect(220, 240, 161, 21))
        self.telephone_2.setStyleSheet("color: rgb(204, 255, 176);\n"
"background:transparent")
        self.telephone_2.setObjectName("telephone_2")
        self.Occupation_2 = QtWidgets.QLabel(self.Details)
        self.Occupation_2.setGeometry(QtCore.QRect(220, 300, 171, 31))
        self.Occupation_2.setStyleSheet("color: rgb(204, 255, 176);\n"
"background:transparent")
        self.Occupation_2.setObjectName("Occupation_2")
        self.relation = QtWidgets.QLabel(self.Details)
        self.relation.setGeometry(QtCore.QRect(10, 180, 151, 21))
        self.relation.setStyleSheet("color: rgb(204, 255, 176);\n"
"background:transparent")
        self.relation.setObjectName("relation")
        self.relation_2 = QtWidgets.QLabel(self.Details)
        self.relation_2.setGeometry(QtCore.QRect(220, 180, 161, 21))
        self.relation_2.setStyleSheet("color: rgb(204, 255, 176);\n"
"background:transparent")
        self.relation_2.setObjectName("relation_2")
        self.tabWidget.addTab(self.Details, "")
        self.Upload = QtWidgets.QWidget()
        self.Upload.setObjectName("Upload")
        self.uploadImage = QtWidgets.QPushButton(self.Upload)
        self.uploadImage.setGeometry(QtCore.QRect(180, 10, 151, 31))
        self.uploadImage.setStyleSheet("color:white;\n"
"background: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0.011, stop:0.0547264 rgba(62, 130, 10, 255), stop:1 rgba(100, 183, 2, 255));\n"
"border-radius:6px;")
        self.uploadImage.setObjectName("uploadImage")
        self.uploadedImage = QtWidgets.QLabel(self.Upload)
        self.uploadedImage.setGeometry(QtCore.QRect(180, 50, 161, 131))
        self.uploadedImage.setStyleSheet("background:transparent;\n"
"border: 1px solid #3c78b4;")
        self.uploadedImage.setFrameShape(QtWidgets.QFrame.Box)
        self.uploadedImage.setText("")
        self.uploadedImage.setObjectName("uploadedImage")
        self.NextOfKin_3 = QtWidgets.QLabel(self.Upload)
        self.NextOfKin_3.setGeometry(QtCore.QRect(20, 290, 111, 21))
        self.NextOfKin_3.setStyleSheet("background:none;\n"
"color: #ffffff")
        self.NextOfKin_3.setObjectName("NextOfKin_3")
        self.telephone_3 = QtWidgets.QLabel(self.Upload)
        self.telephone_3.setGeometry(QtCore.QRect(20, 330, 131, 21))
        self.telephone_3.setStyleSheet("background:none;\n"
"color: #ffffff")
        self.telephone_3.setObjectName("telephone_3")
        self.Occupation_3 = QtWidgets.QLabel(self.Upload)
        self.Occupation_3.setGeometry(QtCore.QRect(20, 410, 131, 31))
        self.Occupation_3.setStyleSheet("background:none;\n"
"color: #ffffff")
        self.Occupation_3.setObjectName("Occupation_3")
        self.relation_3 = QtWidgets.QLabel(self.Upload)
        self.relation_3.setGeometry(QtCore.QRect(20, 250, 111, 21))
        self.relation_3.setStyleSheet("background:none;\n"
"color: #ffffff")
        self.relation_3.setObjectName("relation_3")
        self.physicalAddress_3 = QtWidgets.QLabel(self.Upload)
        self.physicalAddress_3.setGeometry(QtCore.QRect(20, 370, 121, 21))
        self.physicalAddress_3.setStyleSheet("background:none;\n"
"color: #ffffff")
        self.physicalAddress_3.setObjectName("physicalAddress_3")
        self.textEditRelatedNin = QtWidgets.QTextEdit(self.Upload)
        self.textEditRelatedNin.setGeometry(QtCore.QRect(160, 247, 201, 31))
        self.textEditRelatedNin.setStyleSheet("background: transparent;\n"
"border:1px solid #99a1bc;\n"
"border-radius:6px;color:#ffffff")
        self.textEditRelatedNin.setObjectName("textEditRelatedNin")
        self.textEditRelatedKin = QtWidgets.QTextEdit(self.Upload)
        self.textEditRelatedKin.setGeometry(QtCore.QRect(160, 287, 201, 31))
        self.textEditRelatedKin.setStyleSheet("background: transparent;\n"
"border:1px solid #99a1bc;\n"
"border-radius:6px;color:#ffffff")
        self.textEditRelatedKin.setObjectName("textEditRelatedKin")
        self.textEditRelatedTel = QtWidgets.QTextEdit(self.Upload)
        self.textEditRelatedTel.setGeometry(QtCore.QRect(160, 327, 201, 31))
        self.textEditRelatedTel.setStyleSheet("background: transparent;\n"
"border:1px solid #99a1bc;\n"
"border-radius:6px;color:#ffffff")
        self.textEditRelatedTel.setObjectName("textEditRelatedTel")
        self.textEditRelatedAddress = QtWidgets.QTextEdit(self.Upload)
        self.textEditRelatedAddress.setGeometry(QtCore.QRect(160, 367, 201, 31))
        self.textEditRelatedAddress.setStyleSheet("background: transparent;\n"
"border:1px solid #99a1bc;\n"
"border-radius:6px;color:#ffffff")
        self.textEditRelatedAddress.setObjectName("textEditRelatedAddress")
        self.textEditRelatedOccupation = QtWidgets.QTextEdit(self.Upload)
        self.textEditRelatedOccupation.setGeometry(QtCore.QRect(160, 407, 201, 31))
        self.textEditRelatedOccupation.setStyleSheet("background: transparent;\n"
"border:1px solid #99a1bc;\n"
"border-radius:6px;color:#ffffff")
        self.textEditRelatedOccupation.setObjectName("textEditRelatedOccupation")
        self.pushButtonSaveRelative = QtWidgets.QPushButton(self.Upload)
        self.pushButtonSaveRelative.setGeometry(QtCore.QRect(180, 457, 151, 28))
        self.pushButtonSaveRelative.setStyleSheet("background: rgb(63, 69, 157);\n"
"background-color: qlineargradient(spread:pad, x1:0.01, y1:0.006, x2:1, y2:0, stop:0 rgba(4, 0, 133, 255), stop:1 rgba(0, 19, 176, 255));\n"
"color:white;\n"
"border-radius:8px")
        self.pushButtonSaveRelative.setObjectName("pushButtonSaveRelative")
        self.textEdit = QtWidgets.QTextEdit(self.Upload)
        self.textEdit.setGeometry(QtCore.QRect(160, 200, 201, 31))
        self.textEdit.setStyleSheet("background: transparent;\n"
"border:1px solid #99a1bc;\n"
"border-radius:6px;\n"
"color:#ffffff")
        self.textEdit.setObjectName("textEdit")
        self.relation_4 = QtWidgets.QLabel(self.Upload)
        self.relation_4.setGeometry(QtCore.QRect(20, 210, 111, 21))
        self.relation_4.setStyleSheet("background:none;\n"
"color: #ffffff")
        self.relation_4.setObjectName("relation_4")
        self.tabWidget.addTab(self.Upload, "")
        self.label = QtWidgets.QLabel(self.groupBoxTopMatches_2)
        self.label.setGeometry(QtCore.QRect(10, 10, 81, 16))
        self.label.setStyleSheet("color: rgb(255, 255, 255);\n"
"font: 10pt \"MS Shell Dlg 2\";\n"
"background:transparent")
        self.label.setObjectName("label")
        self.groupBoxTopMatches = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBoxTopMatches.setGeometry(QtCore.QRect(480, 600, 551, 61))
        self.groupBoxTopMatches.setStyleSheet("border:none;\n"
"background-color: rgb(47, 100, 178);")
        self.groupBoxTopMatches.setTitle("")
        self.groupBoxTopMatches.setObjectName("groupBoxTopMatches")
        self.play = QtWidgets.QPushButton(self.groupBoxTopMatches)
        self.play.setGeometry(QtCore.QRect(232, 20, 131, 28))
        self.play.setStyleSheet("background: rgb(63, 69, 157);\n"
"color:black;\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0.011, stop:0 rgba(201, 201, 201, 255), stop:1 rgba(255, 255, 255, 255));\n"
"border-radius:6px")
        self.play.setObjectName("play")
        self.pause = QtWidgets.QPushButton(self.groupBoxTopMatches)
        self.pause.setGeometry(QtCore.QRect(400, 20, 121, 28))
        self.pause.setStyleSheet("background: rgb(63, 69, 157);\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0.011, stop:0 rgba(201, 201, 201, 255), stop:1 rgba(255, 255, 255, 255));\n"
"color:black;\n"
"border-radius:6px")
        self.pause.setObjectName("pause")
        self.buttonUpload = QtWidgets.QPushButton(self.groupBoxTopMatches)
        self.buttonUpload.setGeometry(QtCore.QRect(30, 20, 141, 31))
        self.buttonUpload.setStyleSheet("color:white;\n"
"background: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0.011, stop:0.0547264 rgba(62, 130, 10, 255), stop:1 rgba(100, 183, 2, 255));\n"
"border-radius:6px;")
        self.buttonUpload.setObjectName("buttonUpload")
        self.groupBoxDectect.raise_()
        self.frameVideo.raise_()
        self.groupBoxTrain.raise_()
        self.groupBoxTopMatches_2.raise_()
        self.groupBoxTopMatches.raise_()
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1920, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)


        #working with face QVBox
        fp = "cascades/data/haarcascade_frontalface_alt2.xml"
        self.face_detection_widget = FaceDetectionWidget(fp)
        self.record_video = RecordVideo()

        image_data_slot = self.face_detection_widget.image_data_slot

        self.record_video.image_data.connect(image_data_slot)
        self.record_video.start_recording()
        layout = QtWidgets.QVBoxLayout()
        layout.addWidget(self.face_detection_widget)

        self.frameVideo.setLayout(layout)

        
        #details
        self.face_detection_widget.got_profileName.connect(self.shown)
        self.face_detection_widget.got_givenname.connect(self.showGivename)
        self.face_detection_widget.got_nationality.connect(self.showNationality)
        self.face_detection_widget.got_nin.connect(self.showNin)
        self.face_detection_widget.got_dataOfBith.connect(self.showDateofBirth)
        self.face_detection_widget.got_gender.connect(self.showGender)
        self.face_detection_widget.got_village.connect(self.showVillage)
        self.face_detection_widget.got_parish.connect(self.showParish)
        self.face_detection_widget.got_subcounty.connect(self.showSubCounty)
        self.face_detection_widget.got_county.connect(self.showCounty)
        self.face_detection_widget.got_district.connect(self.showDistrict)
        self.face_detection_widget.got_image_id.connect(self.ImageId)
        self.face_detection_widget.got_trainnerString.connect(self.showTrainString)

        # self.face_detection_widget.got_image_id.connect(self.ImageId)
        # self.face_detection_widget.got_image_id.connect(self.ImageId)


        self.face_detection_widget.got_relativeDetail.connect(self.shownRelative)
        self.face_detection_widget.got_relativePhone.connect(self.showRelativePhone)
        self.face_detection_widget.got_relativeAddress.connect(self.showRelativeAddress)
        self.face_detection_widget.got_relativeOccupation.connect(self.showRelativeOccupation)
        self.face_detection_widget.got_relativeRelation.connect(self.showRelativeRelation)
        

        # self.face_detection_widget.got_image_id.connect(self.ImageId)

        self.face_detection_widget.got_relativeDetailB.connect(self.shownRelativeB)
        self.face_detection_widget.got_relativePhoneB.connect(self.showRelativePhoneB)
        self.face_detection_widget.got_relativeAddressB.connect(self.showRelativeAddressB)
        self.face_detection_widget.got_relativeOccupationB.connect(self.showRelativeOccupationB)
        self.face_detection_widget.got_relativeRelationB.connect(self.showRelativeRelationB)

        # self.face_detection_widget.got_image_id.connect(self.ImageId)

        #method links
        callFunc=self.face_detection_widget.userDetails
        name=self.record_video.image_data.connect(callFunc)

        callRelativeFunc=self.face_detection_widget.relativeDetail
        nameR=self.record_video.image_data.connect(callRelativeFunc)

        callTrainer=self.face_detection_widget.trainingMethod
        nameT=self.record_video.image_data.connect(callTrainer)

        callTrainerFile=self.face_detection_widget.trainer
        fileT=self.record_video.image_data.connect(callTrainerFile)

        #buttons
        self.pushButtonTrainFile.clicked.connect(self.trainerButton)
        self.pushButtonCaptureData.clicked.connect(self.insertion)
        self.pushButtonSaveRelative.clicked.connect(self.insertRelative)
        # self.buttonUpload.clicked.connect(self.startTime)
        self.play.clicked.connect(self.videoWorkStream)
        # self.pause.clicked.connect(self.saveSnap)
    
        self.pause.clicked.connect(self.saveSnap)
        # self.record_video.start_recording()
        self.buttonUpload.clicked.connect(self.uploadVideoFile)
        self.uploadImage.clicked.connect(self.imageUpload)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButtonCaptureData.setText(_translate("MainWindow", "Capture data"))
        self.Surnametrain.setText(_translate("MainWindow", "Surname"))
        self.Nintrain.setText(_translate("MainWindow", "Nin"))
        self.waitTrain.setText(_translate("MainWindow", "Wait to train"))
        self.pushButtonTrainFile.setText(_translate("MainWindow", "Train file"))
        self.words1.setText(_translate("MainWindow", "After capturing the data you will need to train the image"))
        self.words2.setText(_translate("MainWindow", " from the main window"))
        self.label_2.setText(_translate("MainWindow", "Train"))
        self.groupBoxDectect.setTitle(_translate("MainWindow", "               Face Detected"))
        self.Surname.setText(_translate("MainWindow", "Surname"))
        self.Givenname.setText(_translate("MainWindow", "Givenname"))
        self.Nationality.setText(_translate("MainWindow", "Nationality"))
        self.Nin.setText(_translate("MainWindow", "Nin"))
        self.DateOfBirth.setText(_translate("MainWindow", "Date of Birth"))
        self.Gender.setText(_translate("MainWindow", "Gender"))
        self.Village.setText(_translate("MainWindow", "Village"))
        self.Parish.setText(_translate("MainWindow", "Parish"))
        self.SubCounnty.setText(_translate("MainWindow", "Sub county"))
        self.county.setText(_translate("MainWindow", "County"))
        self.District.setText(_translate("MainWindow", "District"))
        self.Occupation.setText(_translate("MainWindow", "Occupation"))
        self.NextOfKin.setText(_translate("MainWindow", "Next of kin"))
        self.physicalAddress.setText(_translate("MainWindow", "Physical Address"))
        self.telephone.setText(_translate("MainWindow", "Telephone Number"))
        self.NextOfKin_2.setText(_translate("MainWindow", "Next of kin"))
        self.physicalAddress_2.setText(_translate("MainWindow", "Physical Address"))
        self.telephone_2.setText(_translate("MainWindow", "Telephone Number"))
        self.Occupation_2.setText(_translate("MainWindow", "Occupation"))
        self.relation.setText(_translate("MainWindow", "relation"))
        self.relation_2.setText(_translate("MainWindow", "relation2"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.Details), _translate("MainWindow", "Tab 1"))
        self.uploadImage.setText(_translate("MainWindow", "Upload Image"))
        self.NextOfKin_3.setText(_translate("MainWindow", "Relations"))
        self.telephone_3.setText(_translate("MainWindow", "Telephone Number"))
        self.Occupation_3.setText(_translate("MainWindow", "Occupation"))
        self.relation_3.setText(_translate("MainWindow", "Related to Nin"))
        self.physicalAddress_3.setText(_translate("MainWindow", "Physical Address"))
        self.pushButtonSaveRelative.setText(_translate("MainWindow", "Save"))
        self.relation_4.setText(_translate("MainWindow", "Name"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.Upload), _translate("MainWindow", "Tab 2"))
        self.label.setText(_translate("MainWindow", "Relations"))
        self.play.setText(_translate("MainWindow", "VideoStream"))
        self.pause.setText(_translate("MainWindow", "SnapShot"))
        self.buttonUpload.setText(_translate("MainWindow", "Upload file"))

    def flick(self):
        pass

    def controls(self):
        # cv2.setTrackbarPos('S','image',0)
        cv2.createTrackbar('S','image', 0,100, self.flick)

    def uploadVideoFile(self):
        filename,_=QtWidgets.QFileDialog.getOpenFileName(None,"Select Video","","Video Files (*.mp4)")
        fileVideo="videoUploaded"
        if filename:
            self.record_video.videoFileUpload(filename)
            self.record_video.getVideoFile(fileVideo) 
            # self.record_video.keyShoots()    

    def imageUpload(self):

        fileName,_=QtWidgets.QFileDialog.getOpenFileName(None,"Select Image for Upload")
        if fileName:
            global pix
            pix=QtGui.QPixmap(fileName)
            pix=pix.scaled(self.uploadedImage.width(),self.uploadedImage.height(),QtCore.Qt.KeepAspectRatio)
            self.uploadedImage.setPixmap(pix)
            self.uploadedImage.setAlignment(QtCore.Qt.AlignCenter)

    def saveSnap(self):
        options = QtWidgets.QFileDialog.Options()
        options |= QtWidgets.QFileDialog.DontUseNativeDialog
        fileName, _ = QtWidgets.QFileDialog.getSaveFileName(None,"Save Image","","All Files (*);;Image Files (*.jpg)", options=options)
        if fileName:
            self.record_video.snap(fileName)

    def videoWorkStream(self):
        self.record_video.switchVideo()


    def trainerButton(self):
        signal='train'
        self.face_detection_widget.buttonTrainer(signal)
        print("Hello Me")
    def shown(self,theWord):
        self.Surname.setText("Surname: "+theWord) 
    def showGivename(self,theword):
        self.Givenname.setText("Givename: "+theword)
    def showNationality(self,theword):
        self.Nationality.setText("Nationality: "+theword)
    def showNin(self,theword):
        self.Nin.setText("Nin: "+theword)
    def showDateofBirth(self,theword):
        self.DateOfBirth.setText("Date of Birth: "+theword)
    def showGender(self,theword):
        self.Gender.setText("Gender: "+theword)
    def showVillage(self,theword):
        self.Village.setText("Village: "+theword)
    def showParish(self,theword):
        self.Parish.setText("Parish: "+theword)
    def showSubCounty(self,theword):
        self.SubCounnty.setText("Sub County: "+theword)
    def showCounty(self,theword):
        self.county.setText("County: "+theword)
    def showDistrict(self,theword):
        self.District.setText("District: "+theword)

    def shownRelative(self,theword):
        self.NextOfKin.setText(theword)

        if(theword!=""):
            self.im=QPixmap("./relatives/"+theword+".jpg")
            self.im=self.im.scaled(self.Relative1Image.width(),self.Relative1Image.height(),QtCore.Qt.KeepAspectRatio)
            self.Relative1Image.setPixmap(self.im)
            self.Relative1Image.setAlignment(QtCore.Qt.AlignCenter)   
        else:
            self.im=QPixmap("./defaultImage/person.jpg")
            self.im=self.im.scaled(self.Relative1Image.width(),self.Relative1Image.height(),QtCore.Qt.KeepAspectRatio)
            self.Relative1Image.setPixmap(self.im)
            self.Relative1Image.setAlignment(QtCore.Qt.AlignCenter) 

    def showRelativePhone(self,theword):
        self.telephone.setText("Tel: "+theword)
    def showRelativeAddress(self,theword):
        self.physicalAddress.setText("Address: "+theword)
    def showRelativeOccupation(self,theword):
        self.Occupation.setText("Job: "+theword)
    def showRelativeRelation(self,theword):
        self.relation.setText(theword)

    def showTrainString(self, theword):
        self.waitTrain.setText(theword)

    def shownRelativeB(self,theword):
        self.NextOfKin_2.setText(theword)

        if(theword!=""):
            self.im=QPixmap("./relatives/"+theword+".jpg")
            self.im=self.im.scaled(self.Relative2Image.width(),self.Relative2Image.height(),QtCore.Qt.KeepAspectRatio)
            self.Relative2Image.setPixmap(self.im)
            self.Relative2Image.setAlignment(QtCore.Qt.AlignCenter)   
        else:
            self.im=QPixmap("./defaultImage/person.jpg")
            self.im=self.im.scaled(self.Relative2Image.width(),self.Relative2Image.height(),QtCore.Qt.KeepAspectRatio)
            self.Relative2Image.setPixmap(self.im)
            self.Relative2Image.setAlignment(QtCore.Qt.AlignCenter) 

    def showRelativePhoneB(self,theword):
        self.telephone_2.setText("Tel "+theword)
    def showRelativeAddressB(self,theword):
        self.physicalAddress_2.setText("Address "+theword)
    def showRelativeOccupationB(self,theword):
        self.Occupation_2.setText("Job "+theword)
    def showRelativeRelationB(self,theword):
        self.relation_2.setText(theword)

    def ImageId(self,theword):
        print(theword)
        if(theword!=""):
            self.im=QPixmap("./dataSet/User."+str(theword)+".1.jpg")
            self.im=self.im.scaled(self.ImageFace.width(),self.ImageFace.height(),QtCore.Qt.KeepAspectRatio)
            self.ImageFace.setPixmap(self.im)
            self.ImageFace.setAlignment(QtCore.Qt.AlignCenter)

        else:
            self.im=QPixmap("./defaultImage/person.jpg").scaled(180,150)
            self.im=self.im.scaled(self.ImageFace.width(),self.ImageFace.height(),QtCore.Qt.KeepAspectRatio)
            self.ImageFace.setPixmap(self.im)
            self.ImageFace.setAlignment(QtCore.Qt.AlignCenter)


    def insertion(self):
        name=self.SurnameInput.toPlainText()
        Id=self.NinInput.toPlainText()
        randomInt=randint(1,100000);
        # print(random)

        self.face_detection_widget.setId(Id)
        self.face_detection_widget.get_random(randomInt)
        self.face_detection_widget.setName(name)
        # self.face_detection_widget.quickD()
        self.face_detection_widget.insertOrUpdate()
        # self.face_detection_widget.insertOrUpdate(Id,name)

    def dataCapture(self):
        name=self.SurnameInput.toPlainText()
        Id=self.NinInput.toPlainText()
        randomInt=randint(1,100000);
        self.face_detection_widget.captureData(name,Id,randomInt)

    def insertRelative(self):
        nameRelated=self.textEdit.toPlainText()
        ninRelated=self.textEditRelatedNin.toPlainText()
        nextKin=self.textEditRelatedKin.toPlainText()
        telRelated=self.textEditRelatedTel.toPlainText()
        addressRelated=self.textEditRelatedAddress.toPlainText()
        occupationRelated=self.textEditRelatedOccupation.toPlainText()

        self.face_detection_widget.dataBaseInsertRelative(nameRelated,ninRelated,nextKin,telRelated,addressRelated,occupationRelated)
        pix.save("relatives/"+str(nameRelated)+".jpg")


class RecordVideo(QtCore.QObject):
    image_data = QtCore.pyqtSignal(np.ndarray)
    global camera
    global read
    global data
    global cap

    def __init__(self,parent=None):
        super().__init__(parent)
        self.timer=QtCore.QBasicTimer()
        self.videoSignal=None
        # default video stream
        self.camera=cv2.VideoCapture(0)

    def videoFileUpload(self,videoFile):
        #uploaded video file
        self.camera=cv2.VideoCapture(videoFile)

    def snap(self,picName):
        # cv2.imwrite("dataSet/AC."+str(sampleNum)+".jpg",grayImg[y:y+h,x:x+w])
        s,img=self.camera.read()
        cv2.imwrite(picName+".jpg",img)
   

    def switchVideo(self):
        self.camera=cv2.VideoCapture(0)

    def getVideoFile(self,videoSig):
        self.videoSignal=videoSig


#frame arrangement from timer
    def start_recording(self):
        self.timer.start(0,self)

#events on each frame
    def timerEvent(self,event):
        if(event.timerId()!=self.timer.timerId()):
            return

        read,data=self.camera.read()
        # data=cv2.resize(dat,(940,560))

        if read:

#send signal to UI_Maindow class, for face detection
            self.image_data.emit(data)

    def flick(self,x):
        pass
    def process(im):
        return cv2.cvtColor(im,cv2.COLOR_BGR2GRAY)

    def start_videoUpload(self):
        print("He")


class FaceDetectionWidget(QtWidgets.QWidget):

    #emiting details of the user as a signal

    name=None
    got_profileName=QtCore.pyqtSignal(str)
    got_image_id=QtCore.pyqtSignal(str)
    got_givenname=QtCore.pyqtSignal(str)
    got_nationality=QtCore.pyqtSignal(str)
    got_nin=QtCore.pyqtSignal(str)
    got_dataOfBith=QtCore.pyqtSignal(str)
    got_gender=QtCore.pyqtSignal(str)
    got_village=QtCore.pyqtSignal(str)
    got_parish=QtCore.pyqtSignal(str)
    got_subcounty=QtCore.pyqtSignal(str)
    got_county=QtCore.pyqtSignal(str)
    got_district=QtCore.pyqtSignal(str)

    got_relativeDetail=QtCore.pyqtSignal(str)
    got_relativePhone=QtCore.pyqtSignal(str)
    got_relativeAddress=QtCore.pyqtSignal(str)
    got_relativeOccupation=QtCore.pyqtSignal(str)
    got_relativeRelation=QtCore.pyqtSignal(str)

    got_trainnerString=QtCore.pyqtSignal(str)
    
    got_relativeDetailB=QtCore.pyqtSignal(str)
    got_relativePhoneB=QtCore.pyqtSignal(str)
    got_relativeAddressB=QtCore.pyqtSignal(str)
    got_relativeOccupationB=QtCore.pyqtSignal(str)
    got_trainnerStringB=QtCore.pyqtSignal(str)
    got_relativeRelationB=QtCore.pyqtSignal(str)


    def __init__(self,haar_cascade_filepath, parent=Ui_MainWindow):
        super(FaceDetectionWidget,self).__init__()
        self.classifier = cv2.CascadeClassifier(haar_cascade_filepath)
        self.recognizer= cv2.face.LBPHFaceRecognizer_create()
        self.recognizer.read('trainer/trainerdata.yml')
        self.path='dataSet'
        self.image = QtGui.QImage()
        self._red = (0, 0, 255)
        self._width = 2
        self._min_size = (30, 30)
        self.color=(255,0,255)
        self.stroke=2
        self.font = cv2.FONT_HERSHEY_SIMPLEX
        self.naming=None
        self.nameId=None
        self.IdName=None
        self.faces=None
        self.grayImg=None
        self.nameperson=None
        self.nameTester=None
        self.counter=0
        self.data_train=None
        self.randNumber=None


    def set_name(self):
        self.nameTester="Hello dada"

    def get_name(self):
        return self.nameTester

    def get_random(self, randomN):
        self.randNumber=randomN
        
    def getProfile(self,id):
        conn=sqlite3.connect("FaceData.db")
        cmd="SELECT * FROM UserDetail WHERE ID='"+str(id)+"'"
        cursor=conn.execute(cmd)

        profile=None
        for row in cursor:
            profile=row
        conn.close()

        return profile

    

    def setName(self,name):
        self.naming=name

    def setId(self,Id):
        self.IdName=Id

    def buttonTrainer(self,train_data):
        self.data_train=train_data

    def quickD(self):
        print(self.naming)
        print(self.IdName)

    def displayName(self):
        # self.nameperson
        print(self.nameperson)

        self.update()

    def detect_faces(self, image: np.ndarray):
        gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        gray_image = cv2.equalizeHist(gray_image)

        faces = self.classifier.detectMultiScale(gray_image,scaleFactor=1.3,minNeighbors=4,flags=cv2.CASCADE_SCALE_IMAGE,minSize=self._min_size)

        return faces

    def detect_Label(self,image: np.ndarray):
        grayImg = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

        return grayImg

    def image_data_slot(self,image_data):
        self.faces=self.detect_faces(image_data)
        self.grayImg=self.detect_Label(image_data) 

        for (x,y,w,h) in self.faces:

            id,conf = self.recognizer.predict(self.grayImg[y:y+h,x:x+w])
            cv2.rectangle(image_data,(x,y),(x+w,y+h),self._red,self._width)

            profile=self.getProfile(id)
            # if(profile!=None):
                # cv2.putText(image_data,str(profile[1]), (x,y+h+30), self.font, 1, self.color, self.stroke, cv2.LINE_AA)
                # cv2.putText(image_data,str(profile[2]), (x,y+h+60), self.font, 1, self.color, self.stroke, cv2.LINE_AA)
                # cv2.putText(image_data,str(profile[3]), (x,y+h+90), self.font, 1, self.color, self.stroke, cv2.LINE_AA)
                # cv2.putText(image_data,str(profile[4]), (x,y+h+120),self.font, 1, self.color, self.stroke, cv2.LINE_AA)
            
        self.image=self.get_qimage(image_data)
        if self.image.size()!=self.size():
            self.setFixedSize(self.image.size())

        self.update()

    def relativeDetail(self,image_data):
        faces=self.detect_faces(image_data)
        gray=self.detect_faces(image_data)

        for(x,y,w,h) in faces:
            id,conf = self.recognizer.predict(self.grayImg[y:y+h,x:x+w])
            profile=self.getProfile(id)

            if(profile!=None):
            	conn=sqlite3.connect("FaceData.db")
            	cmd="SELECT * FROM UserDetail WHERE  ID="+str(profile[0])

            	cursor=conn.execute(cmd)
            	profileData=None

            	for row in cursor:
            		profileData=row

            	profileNin=profileData[5]

            	cmd1="SELECT * FROM RelativeTable WHERE  RelatedTo='"+str(profileNin)+"' AND Relations='Mother'"

            	cursor2=conn.execute(cmd1)

            	relativeProfile=None
            	relativeProfileB=None

            	for row1 in cursor2:
            		relativeProfile=row1

            	cmd2="SELECT * FROM RelativeTable WHERE  RelatedTo='"+str(profileNin)+"' AND Relations='Father'"

            	cursor3=conn.execute(cmd2)

            	for row3 in cursor3:
            		relativeProfileB=row3

            	NameRelativeB=str(relativeProfileB[0])
            	phoneRelativeB=str(relativeProfileB[1])
            	AddressRelativeB=str(relativeProfileB[2])
            	OccupationRelativeB=str(relativeProfileB[3])
            	RelationRelativeB=str(relativeProfileB[5])
            	self.got_relativeDetailB.emit(NameRelativeB)
            	self.got_relativePhoneB.emit(phoneRelativeB)
            	self.got_relativeAddressB.emit(AddressRelativeB)
            	self.got_relativeOccupationB.emit(OccupationRelativeB)
            	self.got_relativeRelationB.emit(RelationRelativeB)


            	NameRelative=str(relativeProfile[0])
            	phoneRelative=str(relativeProfile[1])
            	AddressRelative=str(relativeProfile[2])
            	OccupationRelative=str(relativeProfile[3])
            	RelationRelative=str(relativeProfile[5])
            	self.got_relativeDetail.emit(NameRelative)
            	self.got_relativePhone.emit(phoneRelative)
            	self.got_relativeAddress.emit(AddressRelative)
            	self.got_relativeOccupation.emit(OccupationRelative)
            	self.got_relativeRelation.emit(RelationRelative)



    def userDetails(self,image_data):
        faces=self.detect_faces(image_data)
        gray=self.detect_Label(image_data)
        NameProfile=""
        IdProfile=""
        GivennameProfile=""
        NationalityProfile=""
        NinProfile=""
        DateOfBirthProfile=""
        GenderProfile=""
        VillageProfile=""
        ParishProfile=""
        DistrictProfile=""
        CountyProfile=""
        SubCountyProfile=""


        for (x,y,w,h) in faces:
            id,conf = self.recognizer.predict(self.grayImg[y:y+h,x:x+w])
            profile=self.getProfile(id)

            if(profile!=None):
                conn=sqlite3.connect("FaceData.db")
                cmd="SELECT * FROM UserDetail WHERE  ID="+str(profile[0])

                cursor=conn.execute(cmd)
                profileData=None
                for row in cursor:
                    profileData=row

                NameProfile=str(profileData[1])
                IdProfile=str(profileData[0])
                GivennameProfile=str(profileData[2])
                NationalityProfile=str(profileData[3])
                NinProfile=str(profileData[5])
                DateOfBirthProfile=str(profileData[6])
                GenderProfile=str(profileData[4])
                VillageProfile=str(profileData[7])
                ParishProfile=str(profileData[8])
                DistrictProfile=str(profileData[9])
                CountyProfile=str(profileData[11])
                SubCountyProfile=str(profileData[10])

                self.got_profileName.emit(NameProfile)
                self.got_image_id.emit(IdProfile)
                self.got_givenname.emit(GivennameProfile)
                self.got_nationality.emit(NationalityProfile)
                self.got_nin.emit(NinProfile)
                self.got_dataOfBith.emit(DateOfBirthProfile)
                self.got_gender.emit(GenderProfile)
                self.got_village.emit(VillageProfile)
                self.got_parish.emit(ParishProfile)
                self.got_subcounty.emit(SubCountyProfile)
                self.got_county.emit(CountyProfile)
                self.got_district.emit(DistrictProfile)

    def trainingMethod(self,image_data):
        faces=self.detect_faces(image_data)
        grayImg=self.detect_Label(image_data)
        Id=self.randNumber
        trainerData=self.data_train
        recognize=cv2.face.LBPHFaceRecognizer_create()
        path='dataSet'
        trainString=""

        if(Id!=None):
            for(x,y,w,h) in faces:
                self.counter=self.counter+1
                if(self.counter>20):
                    break
                cv2.imwrite("dataSet/User."+str(Id)+"."+str(self.counter)+".jpg",grayImg[y:y+h,x:x+w])

            if(self.counter==20):
                trainString="Ready to train"
        
        elif(trainerData=='train'):
            
            image_paths=[os.path.join(path,f) for f in os.listdir(path)]
            casPath="cascades/data/haarcascade_frontalface_alt2.xml"
            faceCaspath=cv2.CascadeClassifier(casPath)
            images=[]
            labels=[]

            for image_path in image_paths:
                image_pil=Image.open(image_path).convert('L')
                image=np.array(image_pil,'uint8')

                nbr=int(str(os.path.split(image_path)[-1].split('.')[1]))
                

                # nbr=int(os.path)
                print(nbr)

                faced=faceCaspath.detectMultiScale(image)
                for(x,y,w,h) in faced:
                    images.append(image[y:y+h,x:x+w])
                    labels.append(nbr)

                recognize.train(images,np.array(labels))
                recognize.save('trainer/trainerdata.yml')
            
            self.data_train='stop'
            self.got_trainnerString.emit(trainString)



    def trainer(self,image_data):
        faces=self.detect_faces(image_data)


    def insertOrUpdate(self):
        # print(self.naming)
     #    print(self.IdName)
        Name=self.naming
        Id=self.randNumber
        Nin=self.IdName
        con=sqlite3.connect("FaceData.db")

        cmd="SELECT * FROM UserDetail WHERE Nin='"+str(Nin)+"'"
        cursor=con.execute(cmd)

        isRecordExist=0
        for row in cursor:
            isRecordExist=1
        if(isRecordExist==1):
            cmd="UPDATE UserDetail SET Surname='"+str(Name)+"',ID='"+str(Id)+"' WHERE Nin='"+str(Nin)+"'"
        else:
            cmd="INSERT INTO UserDetail(ID,Surname,Nin) Values("+str(Id)+",'"+str(Name)+"','"+str(Nin)+"')"
        con.execute(cmd)
        con.commit()
        con.close()


    def dataBaseInsertRelative(self,nameRelated,ninRelated,nextKin,telRelated,addressRelated,occupationRelated):

        con=sqlite3.connect("FaceData.db")
        cmd="SELECT * FROM RelativeTable WHERE RelatedTo='"+str(ninRelated)+"' AND Relations='"+str(nextKin)+"'"

        cursor=con.execute(cmd)

        isRecordExist=0
        for row in cursor:
            isRecordExist=1
        if(isRecordExist==1):
            cmd= "UPDATE RelativeTable SET Name='"+str(nameRelated)+"', phone='"+str(telRelated)+"', address='"+str(addressRelated)+"', Occupation='"+str(occupationRelated)+"', RelatedTo='"+str(ninRelated)+"',Relations='"+str(nextKin)+"' WHERE  RelatedTo='"+str(ninRelated)+"' AND Relations='"+str(nextKin)+"'"
        else:
            cmd="INSERT INTO RelativeTable(Name,phone,address,Occupation,RelatedTo,Relations) values('"+str(nameRelated)+"','"+str(telRelated)+"','"+str(addressRelated)+"','"+str(occupationRelated)+"','"+str(ninRelated)+"','"+str(nextKin)+"')"

        con.execute(cmd)
        con.commit()
        con.close()

    def get_qimage(self,image:np.ndarray):
        height, width, colors = image.shape
        bytesPerLine = 3 * width
        QImage = QtGui.QImage

        image = QImage(image.data,width,height,bytesPerLine,QImage.Format_RGB888)
        image=image.rgbSwapped()

        return image

    def paintEvent(self,event):
        painter= QtGui.QPainter(self)
        painter.drawImage(0,0,self.image)
        self.image=QtGui.QImage()


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

