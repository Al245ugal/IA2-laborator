import customtkinter as ctk
import tkinter as tk
import tkintermapview as tkm



ctk.set_appearance_mode('dark')

window = ctk.CTk()

window.geometry('1200x600')
window.title('Fleet Manager')


#pagini

def vehicles_page():
    vehicles_frame = tk.Frame(main_frame)
#continut pagina vehicles


    button=ctk.CTkButton(main_frame, text='BMW',
                       fg_color='#1A64EF',
                       text_color='white',)
    button.place(x=20,y=50)

    button = ctk.CTkButton(main_frame, text='vw',
                           fg_color='#1A64EF',
                           text_color='white', )
    button.place(x=20, y=90)

    button = ctk.CTkButton(main_frame, text='Audi',
                           fg_color='#1A64EF',
                           text_color='white', )
    button.place(x=20, y=130)


    vehicles_frame.pack(pady=20)


def live_page():
    live_frame = tk.Frame(main_frame)
    # continut pagina live

    #map widget
    map_widget = tkm.TkinterMapView(main_frame,width=965,height=600,corner_radius=0)
    #set startup coordinates
    map_widget.set_position(45.653221, 25.604870)
    #startup zoom
    map_widget.set_zoom(7)


    map_widget.pack()




    live_frame.pack(pady=20)


def clients_page():
    clients_frame = tk.Frame(main_frame)
    # continut pagina clients cu dictionare

    lb = tk.Label(clients_frame, text="clients Page\n\nPage : 3", font=('Bold', 30),background='#21618C')
    lb.pack()



    clients_frame.pack(pady=20)


def drivers_page():
    drivers_frame = tk.Frame(main_frame)
    # continut pagina vehicles

    lb = tk.Label(drivers_frame, text="drivers Page\n\nPage : 4", font=('Bold', 30),background='#21618C')
    lb.pack()

    drivers_frame.pack(pady=20)

def job_page():
    job_frame = tk.Frame(main_frame)
    # continut pagina vehicles

    lb = tk.Label(job_frame, text="home Page\n\nPage : 5", font=('Bold', 30),background='#21618C')
    lb.pack()

    job_frame.pack(pady=20)


def service_page():
    service_frame = tk.Frame(main_frame)
    # continut pagina service

    lb = tk.Label(service_frame, text="service Page\n\nPage : 6", font=('Bold', 30),background='#21618C')
    lb.pack()

    service_frame.pack(pady=20)


def add_page():
    add_frame = tk.Frame(main_frame)
    # continut pagina add

    lb = tk.Label(add_frame, text="add Page\n\nPage : 7", font=('Bold', 30),background='#21618C')
    lb.pack()

    add_frame.pack(pady=20)



def hide_indicators():
    vehicles_indicate.config(bg='black')
    live_indicate.config(bg='black')
    clients_indicate.config(bg='black')
    drivers_indicate.config(bg='black')
    job_indicate.config(bg='black')
    service_indicate.config(bg='black')
    add_indicate.config(bg='black')


def delete_pages():
    for frame in main_frame.winfo_children():
        frame.destroy()

#functie indicatori ce se afiseaza si se distruge
def indicate(lb,page):    #lb vine de la label
    hide_indicators()
    lb.config(bg='#74FC09')
    delete_pages()
    page()


#pagina de afisare

options_frame = tk.Frame(window , bg='black')
#verde #74FC09



# b1
button = ctk.CTkButton(window,
                       text='Vehicles',
                       fg_color='#1A64EF',
                       text_color='white',
                       command=lambda :indicate(vehicles_indicate,vehicles_page)
                       )
button.place(x=50, y=50)
#indicator buton
vehicles_indicate = tk.Label(options_frame , text = '',bg = 'black'  )
vehicles_indicate.place(x=40, y=50 , width = '5', height= '27')



# b2
button = ctk.CTkButton(window,
                       text='Live tracking',
                       fg_color='#1A64EF',
                       text_color='white',
                       command=lambda :indicate(live_indicate,live_page)
                       )
button.place(x=50, y=90)
#indicator buton2
live_indicate = tk.Label(options_frame , text = '',bg = 'black'  )
live_indicate.place(x=40, y=90 , width = '5', height= '27')


# b3
button = ctk.CTkButton(window,
                       text='Clients',
                       fg_color='#1A64EF',
                       text_color='white',
                       command=lambda :indicate(clients_indicate,clients_page)
                       )
button.place(x=50, y=130)
#indicator buton3
clients_indicate = tk.Label(options_frame , text = '',bg = 'black'  )
clients_indicate.place(x=40, y=130 , width = '5', height= '27')


# b4
button = ctk.CTkButton(window,
                       text='Drivers',
                       fg_color='#1A64EF',
                       text_color='white',
                       command=lambda :indicate(drivers_indicate,drivers_page)
                       )
button.place(x=50, y=170)
#indicator buton4
drivers_indicate = tk.Label(options_frame , text = '',bg = 'black'  )
drivers_indicate.place(x=40, y=170 , width = '5', height= '27')


# b5
button = ctk.CTkButton(window,
                       text='Current job',
                       fg_color='#1A64EF',
                       text_color='white',
                       command=lambda :indicate(job_indicate,job_page)
                       )
button.place(x=50, y=210)
#indicator buton5
job_indicate = tk.Label(options_frame , text = '',bg = 'black'  )
job_indicate.place(x=40, y=210 , width = '5', height= '27')


# b6
button = ctk.CTkButton(window,
                       text='Service',
                       fg_color='#1A64EF',
                       text_color='white',
                       command=lambda :indicate(service_indicate, service_page)
                       )
button.place(x=50, y=250)
#indicator buton6
service_indicate = tk.Label(options_frame , text = '',bg = 'black'  )
service_indicate.place(x=40, y=250 , width = '5', height= '27')



#b7
button = ctk.CTkButton(window,
                       text='Add a new vehicle',
                       fg_color='#1A64EF',
                       text_color='white',
                       command=lambda :indicate(add_indicate, add_page)
                       )
button.place(x=50, y=500)
#indicator buton7
add_indicate = tk.Label(options_frame , text = '',bg = 'black'  )
add_indicate.place(x=40, y=500 , width = '5', height= '27')




#options frame
options_frame.pack(side=ctk.LEFT)
options_frame.pack_propagate(False)
options_frame.configure(width=235, height=650)

#main frame
main_frame = tk.Frame(window)
main_frame.pack(side=tk.LEFT)
main_frame.pack_propagate(False)
main_frame.configure(height=600,width=965,background='#21618C'
                     )

window.mainloop()



