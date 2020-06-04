# Programa para poder subir/bajar el volumen con un sólo click. (25/04/2020)

import tkinter as tk
from pynput.keyboard import Key, Controller, KeyCode
from ctypes import POINTER, cast
from comtypes import CLSCTX_ALL
from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume

gui = tk.Tk()
gui.title("Volume Manager")
gui.geometry("150x270")
gui.resizable(0, 0)
gui.iconbitmap("icon.ico")
play_photo, backwards_photo, forward_photo, decor_photo = tk.PhotoImage(file = "PlayStop.PNG"), tk.PhotoImage(file = "Backwards.PNG"), tk.PhotoImage(file = "Forward.png"), tk.PhotoImage(file = "Decor.png")

var_check1 = tk.BooleanVar()
def TopMost():
     if var_check1.get() == True:
          gui.wm_attributes("-topmost", True)
     else:
          gui.wm_attributes("-topmost", False)

keyboard = Controller()
def playpause_music():
    keyboard.press(Key.media_play_pause)
def backwards_music():
    keyboard.press(Key.media_previous)
def forward_music():
    keyboard.press(Key.media_next)
def volume_up():
    keyboard.press(Key.media_volume_up)
    slider.set(slider.get() + 2)
def volume_down():
    keyboard.press(Key.media_volume_down)
    slider.set(slider.get() - 2)
def mute():
    keyboard.press(Key.media_volume_mute)

var_check2 = tk.BooleanVar()
def widget_value(widget):
     if widget == spinbox:
          if var_check2.get() == True:
               keyboard.press(KeyCode.from_vk(0xB2))
          volume.SetMasterVolumeLevel(scale[str(widget.get()) + "%"], None)
          slider.set(spinbox.get())
     else:
          if var_check2.get() == True:
               keyboard.press(KeyCode.from_vk(0xB2))
          volume.SetMasterVolumeLevel(scale[str(widget) + "%"], None)
          spinbox.delete(0, "end")
          spinbox.insert(0, slider.get())

def enter_volume(event):
     if var_check2.get() == True:
               keyboard.press(KeyCode.from_vk(0xB2))
     volume.SetMasterVolumeLevel(scale[str(spinbox.get()) + "%"], None)
     slider.set(spinbox.get())

scale = {
            '100%': 0.0000000000000000, '99%': -0.15066957473754883, '98%': -0.30284759402275085, '97%': -0.4565645754337311, '96%': -0.6118528842926025, '95%': -0.768743097782135,
               '94%': -0.9272695183753967, '93%': -1.0874667167663574, '92%': -1.2493702173233032, '91%': -1.4130167961120605, '90%': -1.5784454345703125,
               '89%': -1.7456932067871094, '88%': -1.9148017168045044, '87%': -2.08581280708313, '86%': -2.2587697505950928, '85%': -2.4337174892425537,
               '84%': -2.610703229904175, '83%': -2.7897727489471436, '82%': -2.970977306365967, '81%': -3.1543679237365723, '80%': -3.339998245239258,
               '79%': -3.527923583984375, '78%': -3.718202590942383, '77%': -3.9108924865722656, '76%': -4.1060566902160645, '75%': -4.3037590980529785,
               '74%': -4.5040669441223145, '73%': -4.707049369812012, '72%': -4.912779808044434, '71%': -5.121333599090576, '70%': -5.33278751373291,
               '69%': -5.547224998474121, '68%': -5.764730453491211, '67%': -5.98539400100708, '66%': -6.209307670593262, '65%': -6.436570644378662,
               '64%': -6.6672821044921875, '63%': -6.901548862457275, '62%': -7.1394829750061035, '61%': -7.381200790405273, '60%': -7.626824855804443,
               '59%': -7.876484394073486, '58%': -8.130311965942383, '57%': -8.388449668884277, '56%': -8.651047706604004, '55%': -8.918261528015137,
               '54%': -9.190258026123047, '53%': -9.46721076965332, '52%': -9.749302864074707, '51%': -10.036728858947754, '50%': -10.329694747924805,
               '49%': -10.62841796875, '48%': -10.933131217956543, '47%': -11.2440767288208, '46%': -11.561516761779785, '45%': -11.88572883605957,
               '44%': -12.217005729675293, '43%': -12.555663108825684, '42%': -12.902039527893066, '41%': -13.256492614746094, '40%': -13.61940860748291,
               '39%': -13.991202354431152, '38%': -14.372318267822266, '37%': -14.763236045837402, '36%': -15.164472579956055, '35%': -15.576590538024902,
               '34%': -16.000192642211914, '33%': -16.435937881469727, '32%': -16.884546279907227, '31%': -17.3467960357666, '30%': -17.82354736328125,
               '29%': -18.315736770629883, '28%': -18.824398040771484, '27%': -19.350669860839844, '26%': -19.895822525024414, '25%': -20.461252212524414,
               '24%': -21.048532485961914, '23%': -21.6594181060791, '22%': -22.295886993408203, '21%': -22.960174560546875, '20%': -23.654823303222656,
               '19%': -24.38274574279785, '18%': -25.147287368774414, '17%': -25.95233154296875, '16%': -26.80240821838379, '15%': -27.70285415649414,
               '14%': -28.66002082824707, '13%': -29.681535720825195, '12%': -30.77667808532715, '11%': -31.956890106201172, '10%': -33.23651123046875,
               '9%': -34.63383865356445, '8%': -36.17274856567383, '7%': -37.88519287109375, '6%': -39.81534194946289, '5%': -42.026729583740234,
               '4%': -44.61552047729492, '3%': -47.73759078979492, '2%': -51.671180725097656, '1%': -56.992191314697266, '0%': -65.25}

devices = AudioUtilities.GetSpeakers()
interface = devices.Activate(IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
volume = cast(interface, POINTER(IAudioEndpointVolume))
def set_volume(value):
     if var_check2.get() == True:
          keyboard.press(KeyCode.from_vk(0xB2))
     volume.SetMasterVolumeLevel(scale[str(value) + "%"], None)
     slider.set(value)     
    
main_menu = tk.Menu(gui)
gui.config(menu = main_menu)
help_menu = tk.Menu(main_menu, tearoff = 0)
main_menu.add_cascade(label = "Help", menu = help_menu)
instructions_menu = tk.Menu(help_menu, tearoff = 0)
instructions_menu.add_cascade(label = "Pick a widget you like, and manipulate it to change the master volume of this PC.")
about_menu = tk.Menu(help_menu, tearoff = 0) 
about_menu.add_cascade(label = "Program created to change master volume quickly, and in many different ways.")
help_menu.add_cascade(label = "How to use it?", menu= instructions_menu)
help_menu.add_cascade(label = "About this program", menu = about_menu) 
help_menu.add_separator()
help_menu.add_command(label = "Exit", command = gui.quit)
tools_menu = tk.Menu(main_menu, tearoff = 0)
main_menu.add_cascade(label = "Tools", menu = tools_menu)
tools_menu.add_checkbutton(label = "Don't minimize window", command = lambda:TopMost(), variable = var_check1)
tools_menu.add_checkbutton(label = "Show media controls", variable = var_check2)

decoration_label = tk.Label(gui, image = decor_photo).place(x = 125, y = 70)
vol100_button = tk.Button(gui, text = "100", font = ("Arial", "10"), command = lambda:set_volume(100), width = 3, height = 1).place(x = 59, y = 50)
vol80_button = tk.Button(gui, text = "80", font = ("Arial", "10"), command = lambda:set_volume(80), width = 3, height = 1).place(x = 59, y = 78)
vol60_button = tk.Button(gui, text = "60", font = ("Arial", "10"), command = lambda:set_volume(60), width = 3, height = 1).place(x = 59, y = 106)
vol40_button = tk.Button(gui, text = "40", font = ("Arial", "10"), command = lambda:set_volume(40), width = 3, height = 1).place(x = 59, y = 134)
vol20_button = tk.Button(gui, text = "20", font = ("Arial", "10"), command = lambda:set_volume(20), width = 3, height = 1).place(x = 59, y = 162)
vol0_button = tk.Button(gui, text = "Mute", font = ("Arial", "10"), command = lambda:mute(), width = 3, height = 1).place(x = 59, y = 190)
backward_button = tk.Button(gui, image = backwards_photo, command = lambda:backwards_music(), width = 30, height = 30).place(x = 5, y = 5)
play_button = tk.Button(gui, image = play_photo, command = lambda:playpause_music(), width = 30 , height = 30).place(x = 58, y = 5)
forward_button = tk.Button(gui, image = forward_photo, command = lambda:forward_music(), width = 30, height = 30).place(x = 110, y = 5)
decrease_button = tk.Button(gui, text = "-", font = ("Times New Roman", "8"), command = lambda:volume_down()).place(x = 120, y = 193)
increase_button = tk.Button(gui, text = "+", font = ("Times New Roman", "8"), command = lambda:volume_up()).place(x = 120, y = 50)
spinbox = tk.Spinbox(gui, from_ = 0, to = 100, command = lambda:widget_value(spinbox))
spinbox.place(x = 10, y = 225) 
spinbox.bind("<Return>", enter_volume)
slider = tk.Scale(gui, length = 165, sliderlength = 20, from_ = 100, to = 0, command = widget_value)
slider.place(x = -5, y = 50)

gui.mainloop()