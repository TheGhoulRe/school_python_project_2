from tkinter import Text, Tk, Button, Listbox, Event
from api_interaction import search_movie, show_pie_chart

def main(root):
    setup_window(root)
    search_bar = setup_search_bar(root)
    list_box = setup_list_box(root)
    setup_search_button(root, search_bar, list_box)
    setup_view_pie_chart_button(root, search_bar)
    root.mainloop()

def setup_window(root: Tk):
    root.geometry("500x500")
    root.configure(bg="white")
    root.resizable(False, False)

def setup_search_bar(root):
    search_bar = Text(root, borderwidth=1)
    search_bar.place(x=20, y=17, width=342, height=28)
    return search_bar

def setup_search_button(root, search_bar, listbox):
    button = Button(root, text="Search", background="#D9D9D9", borderwidth=1, command=lambda: search_movie(search_bar, listbox))
    button.place(x=368, y=17, width=112, height=28)

def setup_list_box(root):
    list_box = Listbox(root)
    list_box.place(width=460, height=348, x=20, y=64)
    return list_box

def setup_view_pie_chart_button(root, search_bar):
    button = Button(root, text="VIEW PIE CHART", background="#D9D9D9", borderwidth=1, command=lambda: show_pie_chart(search_bar))
    button.place(x=145, y=424, width=209, height=60)


main(Tk())