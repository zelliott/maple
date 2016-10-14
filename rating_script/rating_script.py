#!/usr/bin/python

import Tkinter as tki
import os
import tkMessageBox


# http://stackoverflow.com/questions/14771380/how-do-i-make-the-program-wait-for-an-input-using-an-entry-box-in-python-gui
# Frame for displaying abstract and evaluation
class Questionnarie(tki.Frame):
    def __init__(self, parent, readings, ratings_fp):
        tki.Frame.__init__(self, parent)
        self._setup_gui()
        self._readings = readings.keys()[:]
        self._text = readings
        self._current = ""
        self._ratings_fp = ratings_fp
        self._next_abstract()

    def _setup_gui(self):
        self._label_var = tki.StringVar()
        self._label = tki.Label(textvariable=self._label_var)
        self._label_var.set("Please Rate the following passage from 1 to 10 on difficulty. \nWith 1 being completely understandable and 10 being completely foreign.")
        self._label.pack()
        self._textbox = tki.Text(wrap=tki.WORD, padx=15)
        self._textbox.pack(padx=10)
        self._scale = tki.Scale(orient=tki.HORIZONTAL, length=200,
                                sliderlength=10, to=10)
        self._scale.pack(anchor=tki.S)
        self._button = tki.Button(text="Next", command=self._move_next)
        self._button.pack(anchor=tki.SE, padx=10, pady=10)

    def _next_abstract(self):
        self._textbox.config(state=tki.NORMAL)
        self._textbox.delete("1.0", tki.END)
        self._current = self._readings.pop(0)
        self._textbox.insert(tki.INSERT, self._text[self._current])
        self._textbox.config(state=tki.DISABLED)
        self._scale.set(0)

    def _move_next(self):
        if self._get_rating():
            if len(self._readings) > 0:
                self._next_abstract()
            else:
                self._ratings_fp.close()
                self.quit()
                self.destroy()
        else:
            tkMessageBox.showinfo(title="Error", message="Please give a rating greater than 0.")

    def _get_rating(self):
        rating = str(self._scale.get())
        if rating != "0":
            result = '{:<50}  {:>3}'.format(self._current, rating)
            self._ratings_fp.write(result + "\n")
            return True
        else:
            return False


def fetchExistingRating(name):
    rating_fp = open(name + "_rating.txt", "a+")
    rating_fp.seek(0)
    rating_dict = {}
    l = rating_fp.readlines()
    for s in l:
        words = s.split()
        rating_dict[' '.join(words[:-1])] = words[-1]
    rating_fp.close()

    return rating_dict


# start evaluation based on which user selected
def setDirectory(frame, name):
    seperator = os.sep
    directory = os.getcwd() + seperator + name
    file_dict = {}
    rating_dict = fetchExistingRating(name)
    for filename in os.listdir(directory):
        f = open(directory + seperator + filename, "r")
        if filename not in rating_dict:
            file_dict[filename] = f.read()

    for widget in frame.winfo_children():
        widget.destroy()

    if file_dict:
        rating_fp = open(name + "_rating.txt", "a")

        evalPage = Questionnarie(frame, file_dict, rating_fp)
        evalPage.pack()
    else:
        tki.Button(frame, text="Done!", command=lambda: quit()).pack()


def createStart(frame):
    frame = tki.Frame(top)

    nen = tki.Button(
        frame, text="Professor Nenkova", command=lambda: setDirectory(frame, "nenkova"))
    a = tki.Button(
        frame, text="Omar", command=lambda: setDirectory(frame, "omar"))
    b = tki.Button(
        frame, text="Spencer", command=lambda: setDirectory(frame, "spencer"))
    c = tki.Button(
        frame, text="Zack", command=lambda: setDirectory(frame, "zack"))
    d = tki.Button(
        frame, text="Zhi", command=lambda: setDirectory(frame, "zhi"))

    frame.pack()
    nen.pack(pady=10)
    a.pack(pady=10)
    b.pack(pady=10)
    c.pack(pady=10)
    d.pack(pady=10)

top = tki.Tk()
top.minsize(width=200, height=250)
createStart(top)

top.mainloop()
