from src.ui.defolt.commander_ui import Ui_MainWindow
from src.ui.update_ui.polipotok.load import PoliLoad


class UiMainWindowUpdate(Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

    def setupUi(self, MainWindow):
        super().setupUi(MainWindow)
        self.pb_update.clicked.connect(self.pb_update_action)
        self.pb_load.clicked.connect(self.pb_load_action)
        self.pb_close.clicked.connect(self.pb_close_action)

    def pb_update_action(self):
        print("update")

    def pb_load_action(self):
        PoliLoad()


    def pb_close_action(self):
        self.close()
