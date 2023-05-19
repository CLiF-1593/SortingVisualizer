import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QComboBox, QSlider, QCheckBox
from PyQt5.QtCore import Qt


class GuiWindow(QWidget):

    def __init__(self):
        super().__init__()
        self.data_size = 1
        self.shuffle_method = 'Random'
        self.sort_method = 'Bubble Sort'
        self.sorting_speed = 1
        self.sorting_delay = 0.5
        self.sfx = True
        self.running = False

        self._init_ui()

    def _init_ui(self):
        # data_size_slider
        self.data_size_slider = QSlider(Qt.Horizontal, self)
        self.data_size_slider.move(100, 100)
        self.data_size_slider.setRange(1, 1000)
        self.data_size_slider.setSingleStep(1)

        # shuffle_select_comboBox
        self.shuffle_select_comboBox = QComboBox(self)
        self.shuffle_select_comboBox.move(100, 200)

        shuffle_method_list = ['Random', 'Reversed', 'Sorted']
        for i in shuffle_method_list:
            self.shuffle_select_comboBox.addItem(i)
        del shuffle_method_list

        # sort_select_comboBox
        self.sort_select_comboBox = QComboBox(self)
        self.sort_select_comboBox.move(100, 300)

        sort_method_list = ['Bubble Sort', 'Insertion Sort', 'Selection Sort']
        for i in sort_method_list:
            self.sort_select_comboBox.addItem(i)
        del sort_method_list

        # sorting_speed_slider
        self.sorting_speed_slider = QSlider(Qt.Horizontal, self)
        self.sorting_speed_slider.move(100, 400)
        self.sorting_speed_slider.setRange(1, 1000)

        # sound_toggle_checkBox
        self.sound_toggle_checkBox = QCheckBox('Sound', self)
        self.sound_toggle_checkBox.move(100, 500)
        self.sound_toggle_checkBox.toggle()

        # start_btn
        self.start_btn = QPushButton('START', self)
        self.start_btn.move(100, 600)
        self.start_btn.setEnabled(True)

        # reset_btn
        self.reset_btn = QPushButton('RESET', self)
        self.reset_btn.move(100, 650)
        self.reset_btn.setEnabled(False)


        # connecting
        self.data_size_slider.valueChanged.connect(self._setDataSize)
        self.shuffle_select_comboBox.activated[str].connect(self._setShuffleMethod)
        self.sort_select_comboBox.activated[str].connect(self._setSortMethod)
        self.sorting_speed_slider.valueChanged.connect(self._setSortingDelay)
        self.sound_toggle_checkBox.stateChanged.connect(self._setSFX)
        self.start_btn.clicked.connect(self._sortingStart)
        self.reset_btn.clicked.connect(self._sortingReset)

        # if setting is done, then show window
        self.setWindowTitle('Sorting Visualizer')
        self.resize(400, 800)
        self.show()

    def _setDataSize(self, val):
        self.data_size = val
        print(val)

    def _setShuffleMethod(self, method):
        self.shuffle_method = method
        print(method)

    def _setSortMethod(self, method):
        self.sort_method = method
        print(method)

    def _setSortingDelay(self, speed):
        self.sorting_speed = speed
        self.sorting_delay = 0.5 / speed
        print(self.sorting_speed, round(self.sorting_delay, 6))

    def _setSFX(self, state):
        self.sfx = True if state == 2 else False
        print(self.sfx)

    def _sortingStart(self):
        self.running = True
        self.data_size_slider.setEnabled(False)
        self.shuffle_select_comboBox.setEnabled(False)
        self.sort_select_comboBox.setEnabled(False)
        self.start_btn.setEnabled(False)

        self.reset_btn.setEnabled(True)

    def _sortingReset(self):
        self.running = False
        self.data_size_slider.setEnabled(True)
        self.shuffle_select_comboBox.setEnabled(True)
        self.sort_select_comboBox.setEnabled(True)
        self.start_btn.setEnabled(True)

        self.reset_btn.setEnabled(False)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = GuiWindow()
    sys.exit(app.exec_())
