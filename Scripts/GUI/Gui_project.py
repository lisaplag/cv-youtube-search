from tkinter import *
from tkinter import messagebox #To be able to have pop up message
from tkinter import filedialog
from tkinter import ttk
from Scripts.WebScraping.ModuleYT import search_and_store
from Scripts.WebScraping.FilterTerms import SortBy, Features, UploadDate, Duration

# Global filter Variables
SORTBY = SortBy.Default.value  # String
FEATURES = []  # List<string>
UPLOADDATE = UploadDate.Default.value  # String
DURATION = Duration.Default.value  # String

SORTBY_DICT = {
    'Default': SortBy.Default.value,
    'Relevance': SortBy.Relevance.value,
    'Upload Time': SortBy.UploadTime.value,
    'View Count': SortBy.ViewCount.value,
    'Rating': SortBy.Rating.value
}
FEATURES_DICT = {
    'Subtitles': Features.Subtitles.value,
    'Live': Features.Live.value,
    '4K': Features.FourKResolution.value,
    'High Definition': Features.HighDefinition.value
}
UPLOADDATE_DICT = {
    'Default': UploadDate.Default.value,
    'Past hour': UploadDate.ThisHour.value,
    'Today': UploadDate.ThisDay.value,
    'This week': UploadDate.ThisWeek.value,
    'This month': UploadDate.ThisMonth.value,
    'This year': UploadDate.ThisYear.value
}
DURATION_DICT = {
    'Default': Duration.Default.value,
    'Long': Duration.Long.value,
    'Short': Duration.Short.value
}

# Main lay out choices
main_bg_colour = '#e1c793'
main_button_colour = '#ead7b2'
main_font = 'Comfortaa'
side_bar_colour = '#e5cfa3'

# Lay out main window
root = Tk()
root.geometry("800x600")  # You want the size of the app to be 600x600
root.resizable(0, 0)  # Don't allow resizing in the x or y direction
root.configure(bg=main_bg_colour)
root.title('Name')


# def window_transition(deletions):
#     print (deletions)
#     for label in deletions:
#         print(label)
#         try:
#             label.place_forget()
#         except:
#             pass

def clear_window():
    empty_window = Frame(root,
                         height=800,
                         width=600,
                         bg=main_bg_colour)
    empty_window.place(x=0,
                       y=0)

# def show_main_window():
#     clear_window()
#     main_window()


def show_result_window():
    clear_window()
    result_window()


def main_window():
    # Button placements
    take_picture_button.place(x=300,
                              y=300,
                              anchor='center',
                              width=120,
                              height=120)

    upload_picture_button.place(x=500,
                                y=300,
                                anchor='center',
                                width=120,
                                height=120)



def pic_from_gallery():
    file1=filedialog.askopenfile()


def make_pic():
    pass


def print_URL(entry):
    print('Search')
    print(search_and_store(entry.get(), 'unused', SORTBY, UPLOADDATE, DURATION, FEATURES))


# Description: Sets the global variable SORTBY everytime the combobox is updated
def sort_combo_func(event=None):
    global SORTBY
    SORTBY = SORTBY_DICT[event.widget.get()]
    print(f'event.widget: {event.widget.get()}')


def feature_func(feature_string):
    global FEATURES
    if feature_string in FEATURES:
        FEATURES.remove(feature_string)
    else:
        FEATURES.append(feature_string)
    print(f'Feature string: {feature_string}')

# Description: Sets the global variable UPLOADDATE everytime the combobox is updated
def upload_combo_func(event=None):
    global UPLOADDATE
    UPLOADDATE = UPLOADDATE_DICT[event.widget.get()]
    print(f'event.widget: {event.widget.get()}')


# Description: Sets the global variable DURATION everytime the combobox is updated
def duration_combo_func(event=None):
    global DURATION
    DURATION = DURATION_DICT[event.widget.get()]
    print(f'event.widget: {event.widget.get()}')


def result_window():
    # Build elements
    side_bar = Frame(root,
                     height = 600,
                     width = 200,
                     bg= side_bar_colour )

    search_term_label= Label(root,
                             text= 'Search term',
                             font = (main_font,15),
                             bg= side_bar_colour)

    sort_by_label = Label(root,
                          text= 'Sort by',
                          font= (main_font,10),
                          bg= side_bar_colour)

    sort_combobox = ttk.Combobox(root,
                                 values=('Default', 'Relevance', 'Upload Time', 'View Count', 'Rating'),
                                 width=20,
                                 font=(main_font,10),
                                 )
    sort_combobox.bind('<<ComboboxSelected>>', sort_combo_func)

    upload_date_label = Label(root,
                              text='Upload Date',
                              font=(main_font,10),
                              bg= side_bar_colour)

    upload_date_combobox = ttk.Combobox(root,
                                        values=('Default', 'Past hour', 'Today', 'This week', 'This month', 'This year'),
                                        width=20,
                                        font=(main_font, 10))
    upload_date_combobox.bind('<<ComboboxSelected>>', upload_combo_func)

    duration_label = Label(root,
                           text='Duration',
                           font=(main_font, 10),
                           bg=side_bar_colour)

    duration_combobox = ttk.Combobox(root,
                                     values=('Default', 'Long', 'Short'),
                                     width=20,
                                     font=(main_font, 10))
    duration_combobox.bind('<<ComboboxSelected>>', duration_combo_func)

    filter_label = Label(root,
                         text='Filter',
                         font=(main_font, 10),
                         bg=side_bar_colour)

    Subtitle_checkbox = Checkbutton(root,
                                    text='Subtitles',
                                    width=20,
                                    bg=side_bar_colour,
                                    command=lambda: feature_func(Features.Subtitles.value))

    live_checkbox = Checkbutton(root,
                                text='Live',
                                width=20,
                                bg=side_bar_colour,
                                command=lambda: feature_func(Features.Live.value))

    FourKResolution_checkbox= Checkbutton(root,
                                    text='4K',
                                    width=20,
                                    bg=side_bar_colour,
                                    command=lambda: feature_func(Features.FourKResolution.value))

    HighDefinition_checkbox = Checkbutton(root,
                                 text='High Definition',
                                 width=20,
                                 bg=side_bar_colour,
                                 command=lambda: feature_func(Features.HighDefinition.value))
    go_back_button = Button(root,
                            width=5,
                            height=2,
                            bg= main_button_colour)
    result_label =Label (root,
                         text= 'Results',
                         font=(main_font,25),
                         bg= main_bg_colour)

    input_searchterm = Entry(root,
                             textvariable= StringVar)
    search_button = Button(root,
                           command=lambda: print_URL(input_searchterm))




    #Place elements

    search_term_label.place(x=10,
                            y=10)

    sort_by_label.place(x=10,
                        y=60)

    sort_combobox.place(x=10,
                        y=90)

    upload_date_label.place(x=10,
                            y=120)

    upload_date_combobox.place(x=10,
                               y=150)

    duration_label.place(x=10,
                         y=180)

    duration_combobox.place(x=10,
                            y=210)

    filter_label.place(x=10,
                       y=240)

    Subtitle_checkbox.place(x=10,
                            y=260)

    FourKResolution_checkbox.place(x=-6,
                                   y=280)

    HighDefinition_checkbox.place(x=28,
                                  y=300)

    live_checkbox.place(x=-2,
                        y= 320)

    side_bar.place(x=0,
                   y=0)

    go_back_button.place(x=710,
                         y=20)

    result_label.place(x=300,
                       y=10)

    input_searchterm.place(x=300,
                           y=100)

    search_button.place(x=450,
                        y=100)


#Create Buttons
take_picture_button = Button(root,
                             text = 'Take picture',
                             bg= main_button_colour,
                             font = main_font,
                             command = show_result_window)


upload_picture_button =  Button(root,
                                text='Upload picture',
                                bg = main_button_colour,
                                font = main_font,
                                command = pic_from_gallery)

# Import pictures
# camera_picture = PhotoImage(file = 'C:\\Users\Daniek\camera.png')
# take_picture_button.config(image = camera_picture)
#
# gallery_picture = PhotoImage(file = 'C:\\Users\Daniek\Afbeelding3.png')
# upload_picture_button.config(image = gallery_picture)

main_window()

# Close window function
def close_win():
    root.destroy()

def close_window():
    close_que = messagebox.askquestion('Exit', 'Are you sure you want to exit?')
    if close_que == 'yes':
        close_win()


# Dropdown menu

menu = Menu(root)
root.config(menu=menu)

picture_menu = Menu(menu)
menu.add_cascade(label='Picture',
                 menu =  picture_menu)

picture_menu.add_command(label = 'Camera')

picture_menu.add_command(label = 'From gallery')

settings = Menu(menu)
menu.add_command(label='Settings')

exit = Menu(menu)
menu.add_command(label = 'Exit',command =  close_window)


root.mainloop()