#!/usr/bin/env python

__author__ = "Claudiu Persoiu"
__copyright__ = "Copyright 2014, Claudiu Persoiu"
__license__ = "GPL"
__email__ = "claudiu@claudiupersoiu.ro"

from Tkinter import *
from ttk import *
from unserializer.DumpPHPUnserialized import *

class selectAllEntry(Entry):
    def __init__(self, master=None):
        Entry.__init__(self,master=master, width=70)
        self.bind("<Control-Key-a>", self.select_all)
        
    def select_all(self,event):
        self.selection_range(0, END)
        return "break"

def focus_find(event = False):
    edit.focus_set()

def callback_serialize(event = False):
    text.delete(0.0, END)
    
    try:
        tmp = DumpPHPUnserialized(unser.get()).unserialize()
        text.insert(INSERT, tmp)
    except Exception:
        pass

find_str = ''
find_results = []
find_idx = False
    
def find(event = False):
    global find_str, find_results, find_idx
    
    find_str_new = edit.get()

    if find_str == find_str_new and len(find_results):
        find_focus(find_idx + 1)
        return
    
    find_str = find_str_new
    
    if find_str:
        
        find_results = []
        text.tag_remove('found', '1.0', END)
        text.tag_remove('found_h', '1.0', END)
        idx = '1.0'
        
        while 1:
            idx = text.search(find_str, idx, nocase=1, stopindex=END)
            if not idx: break
            lastidx = '%s+%dc' % (idx, len(find_str))
            text.tag_add('found', idx, lastidx)
            find_results.append(idx)
            idx = lastidx
            if len(find_results):
                find_focus(0)
                
        text.tag_config('found', foreground='red', background='yellow')
        text.tag_config('found_h', foreground='blue', background='yellow')
    edit.focus_set()

def find_focus(idx):
    global find_str, find_results, find_idx
    find_idx = (idx) % len(find_results)
    text.tag_remove('found_h', '1.0', END)
    text.tag_add('found_h', find_results[find_idx], '%s+%dc' % (find_results[find_idx], len(find_str)))
    text.see(find_results[find_idx])

root = Tk()

# scrollbar
scrollbar = Scrollbar(root)
scrollbar.pack(side=RIGHT, fill=Y)

# top section
fram = Frame(root)
Label(fram,text='Unserialize:').pack(side=LEFT)
unser = selectAllEntry(fram)
unser.bind("<Return>", callback_serialize)
unser.pack(side=LEFT, fill=BOTH, expand=1)

butt = Button(fram, text='Dump')
butt.pack(side=RIGHT)
fram.pack(side=TOP)

butt.config(command=callback_serialize)

text = Text(root,height=30,width=100, font=("Helvetica", 12), wrap=WORD, yscrollcommand=scrollbar.set)
text.pack(side=TOP)
text.bind("<Control-Key-f>", focus_find)
scrollbar.config(command=text.yview)

# bottom section
fram = Frame(root)
Label(fram,text='Text to find:').pack(side=LEFT)
edit = selectAllEntry(fram)
edit.bind("<Return>", find)
edit.pack(side=LEFT, fill=BOTH, expand=1)

butt = Button(fram, text='Find')
butt.pack(side=RIGHT)
fram.pack(side=TOP)

butt.config(command=find)

root.title('Python unserializer')
root.mainloop()
