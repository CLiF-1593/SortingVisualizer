import random
import sys
from SylTimer import SylTimer

from PyQt5.QtCore import Qt, QTimer
from PyQt5.QtGui import QFont, QPainter, QColor
from PyQt5.QtWidgets import *

from SortingAlgorithm.Bogo_Sort import BogoSort
from SortingAlgorithm.Bubble_Sort import BubbleSort
from SortingAlgorithm.CombSort import CombSort
from SortingAlgorithm.Counting_Sort import CountingSort
from SortingAlgorithm.Gnome_Sort import GnomeSort
from SortingAlgorithm.Heap_Sort import HeapSort
from SortingAlgorithm.Insertion_Sort import InsertionSort
from SortingAlgorithm.Intro_Sort import IntroSort
from SortingAlgorithm.Merge_Sort import MergeSort
from SortingAlgorithm.Odd_Even_Sort import OddEvenSort
from SortingAlgorithm.Quick_Sort import QuickSort
from SortingAlgorithm.Radix_Sort import RadixSort
from SortingAlgorithm.Selection_Sort import SelectionSort
from SortingAlgorithm.Shell_Sort import ShellSort
from SortingAlgorithm.Tim_Sort import TimSort
from SortingAlgorithm.Adaptive_Partition_Sort import AdaptivePartitionSort


class MainWidget(QWidget):

    class Color:
        default = QColor(255, 255, 255)
        out_of_partition = QColor(150, 150, 150)
        comparing = QColor(214, 71, 71)
        check = QColor(143, 214, 71)
        pivot = QColor(71, 205, 214)

    def __init__(self):
        super().__init__()
        self.data_size = 1
        self.shuffle_method = 'Sorted'
        self.sort_method = 'Bogo Sort'
        self.sorting_speed = 1
        self.sorting_delay = 1.0  # 1 / speed seconds
        self.sfx = True
        self.running = False
        self.init_arr = [0]
        self.is_shuffled = False
        self.sorter = None
        self.sort_timer = SylTimer()

        self.saved_shuffle_method = 'Sorted'
        self.saved_width = 1600
        self.saved_height = 900
        self.saved_shuffle_len = 0

        self.c_xy = 20
        self.c_w = 1240  # width * 4/5 - 2*canvas_xy
        self.c_h = 860  # height - 2*canvas_xy
        self.c_col = QColor(0, 0, 0)
        self.cmp_col = QColor(255, 255, 0)
        self.change_col = QColor(255, 0, 0)

        self.sort_method_list = [AdaptivePartitionSort, BogoSort, BubbleSort, CombSort, CountingSort,
                                 GnomeSort, HeapSort, InsertionSort, IntroSort, MergeSort, OddEvenSort,
                                 QuickSort, QuickSort, RadixSort, SelectionSort, ShellSort, TimSort,]
        self.sort_method_list_str = ['Adaptive Partition Sort', 'Bogo Sort', 'Bubble Sort', 'Comb Sort',
                                     'Counting Sort','Gnome Sort', 'Heap Sort', 'Insertion Sort', 'Intro Sort',
                                     'Merge Sort', 'Odd Even Sort', 'Quick Sort (Left Pivot)',
                                     'Quick Sort (Right Pivot)', 'Radix Sort', 'Selection Sort',
                                     'Shell Sort', 'Tim Sort']

        self._init_ui()

        # graphic update by 125 fps
        self.graphic_timer = QTimer()
        self.graphic_timer.timeout.connect(self.update_graphic)
        self.graphic_timer.start(8)

    def _init_ui(self):

        self.mainFont = QFont('Pretendard Medium', 15)

        # ===================================================================
        # ============================= Widgets =============================
        # ===================================================================

        # data_size_slider_label
        self.data_size_slider_label = QLabel('Data Size : 1')
        self.data_size_slider_label.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.data_size_slider_label.setFont(self.mainFont)

        #

        # data_size_slider
        self.data_size_slider = QSlider(Qt.Horizontal, self)
        self.data_size_slider.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.data_size_slider.setRange(0, 300)
        self.data_size_slider.setSingleStep(1)
        self.data_size_slider.setFont(self.mainFont)

        #

        # shuffle_select_comboBox
        self.shuffle_select_comboBox = QComboBox(self)
        self.shuffle_select_comboBox.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.shuffle_select_comboBox.setFont(self.mainFont)

        shuffle_method_list = ['Sorted', 'Random', 'Reversed']
        for i in shuffle_method_list:
            self.shuffle_select_comboBox.addItem(i)
        del shuffle_method_list

        #

        # shuffle_btn
        self.shuffle_btn = QPushButton('Shuffle')
        self.shuffle_btn.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.shuffle_btn.setFont(self.mainFont)
        self.shuffle_btn.setEnabled(False)
        
        #
        
        # sort_select_comboBox
        self.sort_select_comboBox = QComboBox(self)
        self.sort_select_comboBox.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.sort_select_comboBox.setFont(self.mainFont)

        for i in self.sort_method_list_str:
            self.sort_select_comboBox.addItem(i)

        #

        # sorting_speed_slider_label
        self.sorting_speed_slider_label = QLabel('Speed : 1 (1000.0ms/step)')
        self.sorting_speed_slider_label.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.sorting_speed_slider_label.setFont(self.mainFont)

        #

        # sorting_speed_slider
        self.sorting_speed_slider = QSlider(Qt.Horizontal, self)
        self.sorting_speed_slider.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.sorting_speed_slider.setRange(1, 250)
        self.sorting_speed_slider.setFont(self.mainFont)

        #

        # sound_toggle_checkBox
        self.sound_toggle_checkBox = QCheckBox('Sound', self)
        self.sound_toggle_checkBox.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.sound_toggle_checkBox.toggle()
        self.sound_toggle_checkBox.setFont(self.mainFont)

        #

        # start_btn
        self.start_btn = QPushButton('START', self)
        self.start_btn.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.start_btn.setEnabled(True)
        self.start_btn.setFont(self.mainFont)

        #

        # reset_btn
        self.reset_btn = QPushButton('RESET', self)
        self.reset_btn.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.reset_btn.setEnabled(False)
        self.reset_btn.setFont(self.mainFont)

        #

        # connecting
        self.data_size_slider.valueChanged.connect(self._setDataSize)
        self.shuffle_select_comboBox.activated[str].connect(self._setShuffleMethod)
        self.shuffle_btn.clicked.connect(self._shuffleData)
        self.sort_select_comboBox.activated[str].connect(self._setSortMethod)
        self.sorting_speed_slider.valueChanged.connect(self._setSortingDelay)
        self.sound_toggle_checkBox.stateChanged.connect(self._setSFX)
        self.start_btn.clicked.connect(self._sortingStart)
        self.reset_btn.clicked.connect(self._sortingReset)

        # ===================================================================
        # ============================= Layouts =============================
        # ===================================================================

        # the boxes
        self.stt_rst_hbox = QHBoxLayout()
        self.settings_vbox = QVBoxLayout()
        self.total_hbox = QHBoxLayout()

        #

        # settings' part
        self.settings_vbox.addStretch(1)
        self.settings_vbox.addWidget(self.data_size_slider_label, 1)
        self.settings_vbox.addWidget(self.data_size_slider, 1)
        self.settings_vbox.addWidget(self.shuffle_select_comboBox, 1)
        self.settings_vbox.addWidget(self.shuffle_btn, 1)

        self.settings_vbox.addStretch(1)
        self.settings_vbox.addWidget(self.sort_select_comboBox, 1)
        self.settings_vbox.addWidget(self.sorting_speed_slider_label, 1)
        self.settings_vbox.addWidget(self.sorting_speed_slider, 1)
        self.settings_vbox.addWidget(self.sound_toggle_checkBox, 1)

        self.settings_vbox.addStretch(1)
        self.stt_rst_hbox.addWidget(self.start_btn, 1)
        self.stt_rst_hbox.addWidget(self.reset_btn, 1)
        self.settings_vbox.addLayout(self.stt_rst_hbox, 1)

        self.settings_vbox.addStretch(1)

        #

        # total binding
        self.total_hbox.addStretch(4)  # show data rods here
        self.total_hbox.addLayout(self.settings_vbox, 1)
        self.setLayout(self.total_hbox)

        # ===================================================================
        # ============================= Release =============================
        # ===================================================================

        self.setMinimumSize(1008, 567)
        self.setWindowTitle('Sorting Visualizer')
        self.resize(1600, 900)
        self.show()

    # ============================================================================
    # ============================= Widget Functions =============================
    # ============================================================================

    def _setDataSize(self, val):
        self.data_size = int(4**(val / 50))
        self.data_size_slider_label.setText(f'Data Size : {self.data_size}')
        if self.shuffle_method == 'Random':
            if len(self.init_arr) < self.data_size:
                if self.saved_shuffle_method == 'Sorted':
                    self.init_arr += list(range(len(self.init_arr), self.data_size))
                elif self.saved_shuffle_method == 'Reversed':
                    self.init_arr = list(range(self.data_size - 1, len(self.init_arr) - 1, -1)) + self.init_arr
            elif len(self.init_arr) > self.data_size:
                if self.saved_shuffle_method == 'Sorted':
                    if self.saved_shuffle_len > self.data_size:
                        tmp = self.init_arr
                        self.init_arr = list(range(self.data_size))
                        del tmp
                        self.saved_shuffle_len = 0
                    else:
                        self.init_arr = self.init_arr[:self.data_size]
                elif self.saved_shuffle_method == 'Reversed':
                    if self.saved_shuffle_len > self.data_size:
                        tmp = self.init_arr
                        self.init_arr = list(range(self.data_size - 1, -1, -1))
                        del tmp
                        self.saved_shuffle_len = 0
                    else:
                        self.init_arr = self.init_arr[-self.data_size:]
                self.is_shuffled = False

        self.update()

    def _setShuffleMethod(self, method):
        shuffle = False
        if method == 'Random':
            self.shuffle_btn.setEnabled(True)

            if self.shuffle_method != 'Random':
                self.saved_shuffle_method = self.shuffle_method
                shuffle = True
            if self.shuffle_method == 'Sorted':
                self.init_arr = list(range(0, self.data_size, 1))
            elif self.shuffle_method == 'Reversed':
                self.init_arr = list(range(self.data_size - 1, -1, -1))
        self.shuffle_method = method
        if method != 'Random':
            self.shuffle_btn.setEnabled(False)
            del self.init_arr
            self.init_arr = None
            self.is_shuffled = False
        if shuffle:
            self._shuffleData()
        self.update()

    def _shuffleData(self):
        if self.shuffle_method == 'Random':
            random.shuffle(self.init_arr)
            self.is_shuffled = True
            self.saved_shuffle_len = len(self.init_arr)
            self.update()

    def _setSortMethod(self, method):
        self.sort_method = method

    def _setSortingDelay(self, speed):
        speed = int(4**(speed / 50))
        self.sorting_speed = speed
        self.sorting_delay = 1.0 / speed
        self.sorting_speed_slider_label.setText(
            f'Speed : {speed} ({self.sorting_delay * 10000 // 1 / 10}ms/step)')
        if self.running: self.sorter.SetSpeed(self.sorting_delay)

    def _setSFX(self, state):
        self.sfx = True if state == 2 else False
        if self.running: self.sorter.SetPlaysound(self.sfx)

    def _sortingStart(self):
        self.data_size_slider.setEnabled(False)
        self.shuffle_btn.setEnabled(False)
        self.shuffle_select_comboBox.setEnabled(False)
        self.sort_select_comboBox.setEnabled(False)
        self.start_btn.setEnabled(False)

        self.reset_btn.setEnabled(True)

        if self.shuffle_method == 'Sorted':
            self.init_arr = list(range(self.data_size))
        elif self.shuffle_method == 'Reversed':
            self.init_arr = list(range(self.data_size - 1, -1, -1))
        elif self.is_shuffled is False:
            self._shuffleData()

        index = self.sort_method_list_str.index(self.sort_method)
        self.sorter = self.sort_method_list[index](self.sort_timer)
        if index == 11:
            self.sorter.SetPivot(QuickSort.PivotType.PIVOT_FIRST)
        elif index == 12:
            self.sorter.SetPivot(QuickSort.PivotType.PIVOT_LAST)
        self.sorter.SetArrayDirectly(self.init_arr)
        self.sorter.SetSpeed(self.sorting_delay)
        self.sorter.SetPlaysound(self.sfx)
        self.sorter.Sort()

        self.running = True

    def _sortingReset(self):
        self.data_size_slider.setEnabled(True)
        self.shuffle_btn.setEnabled(True)
        self.shuffle_select_comboBox.setEnabled(True)
        self.sort_select_comboBox.setEnabled(True)
        self.start_btn.setEnabled(True)
        self.reset_btn.setEnabled(False)
        self.running = False
        self.update()

    # ============================================================================
    # ============================ Override Functions ============================
    # ============================================================================

    def paintEvent(self, event):

        painter = QPainter(self)

        # draw canvas bg
        painter.fillRect(self.c_xy - 1, self.c_xy - 1,
                         self.c_w + 2, self.c_h + 2, self.c_col)

        # draw rods
        for i in range(self.data_size):
            if not self.running:
                if self.shuffle_method == 'Random': val = self.init_arr[i]
                if self.shuffle_method == 'Sorted': val = i
                if self.shuffle_method == 'Reversed': val = self.data_size - 1 - i
            else:
                val = self.sorter.arr[i]

            color = self.Color.default
            if self.running:
                partition = self.sorter.GetPartition()
                if partition and not (partition[0] <= i <= partition[1]):
                    color = self.Color.out_of_partition
                comparing = self.sorter.GetComparingIndex()
                if i in comparing:
                    color = self.Color.comparing
                pivot = self.sorter.GetPivot()
                if i == pivot:
                    color = self.Color.pivot
                check = self.sorter.GetCheckedIndex()
                if i <= check:
                    color = self.Color.check

            painter.fillRect(self.c_xy + i * self.c_w // self.data_size,
                             self.c_xy + (self.data_size - val - 1) * self.c_h // self.data_size,
                             (i + 1) * self.c_w // self.data_size - i * self.c_w // self.data_size,
                             self.c_h - (self.data_size - val - 1) * self.c_h // self.data_size,
                             color)

    # ===========================================================================
    # ============================= Other Functions =============================
    # ===========================================================================

    def update_graphic(self):
        if self.update_graphic_related_values() or self.running:
            self.update()

    def update_graphic_related_values(self):
        nw = self.width()
        nh = self.height()

        if nw != self.saved_width or nh != self.saved_height:

            fontSize_by_width = 15 * nw / 1600 // 1
            fontSize_by_height = 15 * nh / 900 // 1
            self.mainFont.setPointSize(min(fontSize_by_width, fontSize_by_height))
            self.data_size_slider_label.setFont(self.mainFont)
            self.shuffle_select_comboBox.setFont(self.mainFont)
            self.shuffle_btn.setFont(self.mainFont)
            self.sort_select_comboBox.setFont(self.mainFont)
            self.sorting_speed_slider_label.setFont(self.mainFont)
            self.sound_toggle_checkBox.setFont(self.mainFont)
            self.start_btn.setFont(self.mainFont)
            self.reset_btn.setFont(self.mainFont)

            self.c_w = nw * 4 / 5 - 2 * self.c_xy
            self.c_h = nh - 2 * self.c_xy

            self.saved_width = nw
            self.saved_height = nh

            return True

        return False


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MainWidget()
    sys.exit(app.exec_())
