import pickle
from tkinter import filedialog
from os.path import expandvars


class DoodleDAO :
    @staticmethod
    def save_doodle(doodle):
        file = filedialog.asksaveasfilename(filetypes=[('PICKLE', '.pickle')], initialdir=expandvars('$HOME'),
                                            initialfile='my_doodles.pickle')
        try:
            with open(file, 'wb') as saved:
                pickle.dump(doodle,saved)
        except pickle.PickleError as perr:
            print('pickle error!')

    @staticmethod
    def load_doodle():
        file = filedialog.askopenfilename(filetypes=[('PICKLE', '.pickle')], initialdir=expandvars('$HOME'))
        try:
            with open(file, 'rb') as d_file:
                doodles = pickle.load(d_file)
            return doodles
        except IOError as ioerr:
            print('no such file')
        except pickle.PickleError as perr:
            print('pickle error!')
            return None

