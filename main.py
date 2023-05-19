from SortingAlgorithm.Sort import Sort
from SortingAlgorithm.Sort import ArrayType
from SortingAlgorithm.Bubble_Sort import BubbleSort

if __name__ == '__main__':
    sort = BubbleSort()
    sort.SetArray(50, ArrayType.RANDOM)
    sort.SetSpeed(0.01)
    sort.Sort()