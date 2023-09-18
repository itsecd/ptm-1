from annotation import Annotation
from creat_ann import creat_annotation


class AnnotationIterator:

    def __init__(self, annotation: Annotation) -> None:
        """Constructor"""
        self.ann = annotation
        self.counter = 0

    def __next__(self, label: str) -> str:
        """Returns the next instance of annotation 
        by label without repetition
        """
        if self.counter < (self.ann.number_lines-1):
            copy = self.ann.next(label)
            self.counter = self.ann.viewed_files
            return copy
        else:
            raise StopIteration


if __name__ == "__main__":
    path_main = 'C:/Users/user/Desktop/dataset_copy' 
    annotation_main = Annotation("task1_csv.csv")
    creat_annotation(path_main, annotation_main)
    iter = AnnotationIterator(annotation_main)