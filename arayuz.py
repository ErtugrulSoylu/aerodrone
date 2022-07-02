from re import S
from dronekit import connect, VehicleMode
from pymavlink import mavutil
from time import sleep
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtCore import Qt, pyqtSignal, pyqtSlot, QObject
from ui_drone import Ui_MainWindow
import threading
import math
import sys
from ucus_komutlari import aero

connection_string="127.0.0.1:14550"
vehicle = connect(connection_string,wait_ready=True,timeout=100)
ui = Ui_MainWindow()

class Attributes(QObject):
    bataryaGonder = pyqtSignal(list)
    hizGonder = pyqtSignal(list)

def bataryaGuncelle(value):
    ui.CekilenAkim.display(value[0])
    ui.pilSeviyesi.setValue(value[1])

def hizGuncelle(value):
    ui.dikeyHiz.display(-value[2])
    ui.yatayHiz.display(math.sqrt(value[0]**2 + value[1]**2))

# Signals
attr = Attributes()
attr.bataryaGonder.connect(bataryaGuncelle)
attr.hizGonder.connect(hizGuncelle)

class MainWindow:
    def __init__(self):
        self.drone = aero(vehicle)
        self.main_win = QMainWindow()
        ui.setupUi(self.main_win)
        self.main_win.m_flag = False
        self.droneThreadFlag = False
        
        # Buttons
        ui.armTestButon.clicked.connect(self.armTestButon)
        ui.otoKalkisButon.clicked.connect(self.otoKalkisButon)
        ui.acilInisButon.clicked.connect(self.acilInisButon)
        ui.yukselButon.clicked.connect(self.yukselButon)
        
        ui.guidedButon.clicked.connect(self.guidedMode)
        ui.loiterButon.clicked.connect(self.loiterMode)
        ui.posholdButon.clicked.connect(self.pos_holdMode)
        ui.landButon.clicked.connect(self.landMode)
        ui.stabilizeButon.clicked.connect(self.stabilizeMode)
        
    ############################################################################################################
    ######################################            NECESSARY            #####################################
    ############################################################################################################

    def show(self):
        self.main_win.show()

    def mousePressEvent(self, event):
        if event.button()==Qt.LeftButton:
            self.main_win.m_flag=True
            self.main_win.m_Position=event.globalPos()-self.main_win.pos()
            event.accept()

    def mouseMoveEvent(self, QMouseEvent):
        if Qt.LeftButton and self.main_win.m_flag:  
            self.main_win.move(QMouseEvent.globalPos()-self.main_win.m_Position)
            QMouseEvent.accept()
            
    def mouseReleaseEvent(self, QMouseEvent):
        self.main_win.m_flag=False

    ############################################################################################################
    #####################################            ATTRIBUTES            #####################################
    ############################################################################################################

    @vehicle.on_attribute('velocity')
    def hizOku(self, attr_name, value):
        attr.hizGonder.emit(value)

    @vehicle.on_attribute('battery')
    def bataryaOku(self, attr_name, value):
        attr.bataryaGonder.emit([value.current, value.level])
    
    def ucusSuresiGuncelle(self):
        return

    def durumGuncelle(self, text = ""):
        return

    def kameraGuncelle(self, image):
        return

    def modGuncelle(self, image):
        return

    ############################################################################################################
    ######################################            BUTTONS            #######################################
    ############################################################################################################

    ## SCRIPTS ##

    def armTestButon(self):
        threading.Thread(target=self.armTest).start()

    def armTest(self):
        if self.droneThreadFlag is False:
            self.droneThreadFlag = True
            self.drone.test()
            self.droneThreadFlag = False

    def otoKalkisButon(self):
        threading.Thread(target=self.otoKalkis).start()

    def otoKalkis(self):
        if self.droneThreadFlag is False:
            self.droneThreadFlag = True
            self.drone.otonom_kalkis_inis()
            self.droneThreadFlag = False
        
    def acilInisButon(self):
        threading.Thread(target=self.acilInis).start()

    def acilInis(self):
        self.droneThreadFlag = True
        self.drone.acil_inis()
        self.droneThreadFlag = False
    
    def yukselButon(self):
        threading.Thread(target=self.yuksel).start()

    def yuksel(self):
        if self.droneThreadFlag is False:
            self.droneThreadFlag = True
            self.drone.otonom_yuksel()
            self.droneThreadFlag = False

    ## MODES ##

    def stabilizeMode(self):
        self.drone.vehicle.mode = VehicleMode('STABILIZE')

    def loiterMode(self):
        self.drone.vehicle.mode = VehicleMode('LOITER')

    def guidedMode(self):
        self.drone.vehicle.mode = VehicleMode('GUIDED')

    def landMode(self):
        self.drone.vehicle.mode = VehicleMode('LAND')

    def pos_holdMode(self):
        self.drone.vehicle.mode = VehicleMode('POS_HOLD')
    

if __name__ == '__main__':
    app = QApplication(sys.argv)
    main_win = MainWindow()
    main_win.show()
    sys.exit(app.exec_())
