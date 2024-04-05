
import time
from tkinter import *
from tkinter import filedialog
from tkinter import messagebox
import cv2
from numpy import *
import os
import numpy as np
from PIL import Image, ImageTk
from PIL import ImageEnhance
from PIL import Image,ImageFont,ImageDraw

'''    ------------------------  Globel Veriables  '''

always_keep_orignel_image = ""
image_globel = ""
image_final = ""
save_object = ""
image_filename = ""
image_save_main = ""
image_save_icon_1 = ""
image_save_icon_2 = ""
image_save_icon_3 = ""
image_save_passport_1 = ""
image_save_passport_2 = ""
image_save_passport_3 = ""
video_path_globle="---------------------------------> Select Video <---------------------------------"
video_savepath_globle="---------------------------------> Select Destination <---------------------------------"
start_framing=""
end_framing=""
window=""
window_main_all_cap=""
size_one= ""
size_two= ""
win_manual=""
x_current_axis = 0
y_current_axis = 0
center_screen_quardenate_x=0
center_screen_quardenate_y=0

'''    ------------------------     Functions           '''

window_main_all=Tk()
def main_init():
    window_main_all.maxsize(0,0)
    window_main_all.minsize(0, 0)
    window_main_all.geometry(f'{int(0)}x{int(0)}+{int(-10)}+{int(-10)}')
def main_init2():
    window_main_all.maxsize(0,0)
    window_main_all.minsize(0, 0)
    window_main_all.geometry(f'{int(0)}x{int(0)}+{0}+{0}')

main_init()

def save_fun(key):
    if key == 1:
        if image_save_main != "":
            path_name = filedialog.asksaveasfile(mode='w', defaultextension=".jpg")
            if not path_name:
                return
            else:
                image_save_main.save(path_name)
        else:
            messagebox.showerror("Error", "Image note Found")
    elif key == 2:
        if image_save_icon_1 != "":
            path_name = filedialog.asksaveasfile(mode='w', defaultextension=".jpg")
            if not path_name:
                return
            else:
                image_save_icon_1.save(path_name)
        else:
            messagebox.showerror("Error", "Image note Found")
    elif key == 3:
        if image_save_icon_2 != "":
            path_name = filedialog.asksaveasfile(mode='w', defaultextension=".jpg")
            if not path_name:
                return
            else:
                image_save_icon_2.save(path_name)
        else:
            messagebox.showerror("Error", "Image note Found")
    elif key == 4:
        if image_save_icon_3 != "":
            path_name = filedialog.asksaveasfile(mode='w', defaultextension=".jpg")
            if not path_name:
                return
            else:
                image_save_icon_3.save(path_name)
        else:
            messagebox.showerror("Error", "Image note Found")
    elif key == 5:
        if image_save_passport_3 != "":
            path_name = filedialog.asksaveasfile(mode='w', defaultextension=".jpg")
            if not path_name:
                return
            else:
                image_save_passport_3.save(path_name)
        else:
            messagebox.showerror("Error", "Image note Found")
    elif key == 6:
        if image_save_passport_2 != "":
            path_name = filedialog.asksaveasfile(mode='w', defaultextension=".jpg")
            if not path_name:
                return
            else:
                image_save_passport_2.save(path_name)
        else:
            messagebox.showerror("Error", "Image note Found")
    elif key == 7:
        if image_save_passport_1 != "":
            path_name = filedialog.asksaveasfile(mode='w', defaultextension=".jpg")
            if not path_name:
                return
            else:
                image_save_passport_1.save(path_name)
        else:
            messagebox.showerror("Error", "Image note Found")
    return 1

def default_fun():
    global image_final,image_globel,image_filename
    background_panal_image = Image.open("f1.jpg")
    resize_background_panal_image = background_panal_image.resize((300, 410))
    final_backgroung_panal_image = ImageTk.PhotoImage(resize_background_panal_image)
    background_image_panal_label = Label(window, borderwidth=4, relief=SUNKEN)
    background_image_panal_label.configure(image=final_backgroung_panal_image)
    background_image_panal_label.image = final_backgroung_panal_image
    background_image_panal_label.place(x=65, y=85)
    image_final = ""
    image_globel = ""
    image_filename=""

def brows_fun():
    global image_filename
    image_filename = filedialog.askopenfilename(initialdir=os.getcwd(), title="Select Image",filetypes=(("JPG files", "*.jpg*"),
                                                           ("PNG Files", "*.png"),
                                                           ("All Files", "*.*")))

    if image_filename != "":
        global always_keep_orignel_image
        global image_final
        global image_globel
        always_keep_orignel_image = image_filename
        image_globel = image_filename
        img = Image.open(image_filename)
        resize_image = img.resize((265, 369))
        image_final = ImageTk.PhotoImage(resize_image)
        picture_lable = Label(window, borderwidth=4,relief=SUNKEN)
        picture_lable.configure(image=image_final)
        picture_lable.image = image_final
        picture_lable.place(x=85, y=100)
    else:
        default_fun()
    return 1

def save_brows_function():
    path=filedialog.asksaveasfilename(initialdir='\ ',title='Save File', filetypes=(('JPEG','*.jpeg'),('icon','*.ico')))
    cv2.imwrite('processed_saveobject_image.png', save_object)

def feltered_image_frame_1(key):
    global image_globel
    if key == 1:
        filter_try_one(image_globel)
    elif key == 2:
        filter_try_two(image_globel)
    elif key == 3:
        filter_try_three(image_globel)
    elif key == 4:
        filter_try_four(image_globel)

    path = "processed_abc_image.png"
    image_globel = path
    filtered_image2 = Image.open(path)
    resize_image2 = filtered_image2.resize((330, 494))
    final_image2 = ImageTk.PhotoImage(resize_image2)
    return final_image2

def feltered_image_frame_2(key):
    global image_globel

    if key==1:
       filter_text_image_1(image_globel)
    elif key==2:
       filter_text_image_2(image_globel)
    elif key==3:
       filter_text_image_3(image_globel)
    elif key==4:
       filter_text_image_4(image_globel)


    path = "processed_abc_image.png"
    image_globel = path
    filtered_image2 = Image.open(path)
    resize_image2 = filtered_image2.resize((320,514))
    final_image2 = ImageTk.PhotoImage(resize_image2)
    return final_image2

def filter_try_one(raw_image):
    img = cv2.imread(raw_image)


    #cv2.imwrite('processed_abc_image.png', processed_image)

    return 1

def filter_try_two(raw_image):
    global image_save_main
    image = Image.open(raw_image)
    enh_sha = ImageEnhance.Sharpness(image)
    sharpness = 2.0
    processed_image_e = enh_sha.enhance(sharpness)
    processed_image=np.asarray(processed_image_e)
    cv2.imwrite('processed_abc_image.png', processed_image)
    im=cv2.imread('processed_abc_image.png')
    final_filtered_image = cv2.cvtColor(im, cv2.COLOR_BGR2RGB)
    image_save_main = Image.fromarray(final_filtered_image)
    return 1

def filter_try_three(raw_image):
    image=cv2.imread(raw_image)
    image2 = cv2.cvtColor(image, cv2.COLOR_HSV2BGR)
    image2 = cv2.cvtColor(image2, cv2.COLOR_BGR2GRAY)
    figure_size = 9
    new_image = cv2.blur(image2, (figure_size, figure_size))

    processed_image=cv2.cvtColor(new_image,cv2.COLOR_GRAY2RGB)
    cv2.imwrite('processed_abc_image.png', processed_image)

    return 1

def filter_try_four(raw_image):
    global  image_save_main
    source = cv2.imread(raw_image)
    denoised_image = cv2.fastNlMeansDenoisingColored(source, None, h=5)
    final_filtered_image=cv2.cvtColor(denoised_image,cv2.COLOR_BGR2RGB)
    image_save_main=Image.fromarray(final_filtered_image)
    cv2.imwrite('processed_abc_image.png', denoised_image)
    return 1

def filter_text_image_1(raw_image):
    global image_save_main
    image=cv2.imread(raw_image,0)
    _,processed_1=cv2.threshold(image,130,160,cv2.THRESH_BINARY)
    image_save_main = Image.fromarray(processed_1)
    cv2.imwrite('processed_abc_image.png', processed_1)
    return 1

def filter_text_image_2(raw_image):
    global image_save_main
    image = cv2.imread(raw_image, 0)
    _, processed_1 = cv2.threshold(image,150, 200, cv2.THRESH_BINARY)
    image_save_main = Image.fromarray(processed_1)
    cv2.imwrite('processed_abc_image.png', processed_1)
    return 1

def filter_text_image_3(raw_image):
    global image_save_main
    image=cv2.imread(raw_image,0)
    _,processed_1=cv2.threshold(image,100,180,cv2.THRESH_BINARY)
    image_save_main = Image.fromarray(processed_1)
    cv2.imwrite('processed_abc_image.png', processed_1)
    return 1

def filter_text_image_4(raw_image):
    global image_save_main
    image=cv2.imread(raw_image,0)
    _,processed_1=cv2.threshold(image,130,190,cv2.THRESH_BINARY)
    image_save_main = Image.fromarray(processed_1)
    cv2.imwrite('processed_abc_image.png', processed_1)
    return 1

def show_frames(key):
    count=str(key)
    show_lab2= Label(window_main_all_cap,text="Prossing : "+count+" Frames  Saved",fg="blue",bg="#E0F7CC",font=("Constantia",15,"bold")).place(x=100,y=470)
    return 1

def making_path(raw_path):
    d=str(raw_path)
    print(d)
    i=25
    r_new_path=""
    while(d[i]!="'"):
        r_new_path=r_new_path+d[i]
        i=i+1
    return r_new_path

def video_cap(video_address,start_mod,end_mod):
    cap = cv2.VideoCapture(f'{video_address}')
    i = 1
    display_fram_num=1
    if (start_mod == "0") & (end_mod == "0"):
        while (cap.isOpened()):
            ret, frame = cap.read()
            if ret == True:

                asd=cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
                frame_image=Image.fromarray(asd)
                secname=".jpg"
                j=f'{video_savepath_globle}{display_fram_num}{secname}'
                frame_image.save(j)
                show_frames(display_fram_num)
                i = i + 1
                display_fram_num=display_fram_num+1
            else:
               break
        cap.release()
    elif(start_mod!="0")&(end_mod=="0"):
        while (cap.isOpened()):
            ret, frame = cap.read()
            if ret == True:
                if i >= int(start_mod):

                    asd=cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
                    frame_image=Image.fromarray(asd)
                    secname=".jpg"
                    j=f'{video_savepath_globle}{display_fram_num}{secname}'
                    frame_image.save(j)
                    show_frames(display_fram_num)
                    display_fram_num=display_fram_num+1

            else:
                break
            i = i + 1
        cap.release()

    elif (start_mod == "0") & (end_mod != "0"):
        while (cap.isOpened()):
            ret, frame = cap.read()
            if ret == True:
                if i <= int(end_mod):

                    asd=cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
                    frame_image=Image.fromarray(asd)
                    secname=".jpg"
                    j=f'{video_savepath_globle}{display_fram_num}{secname}'
                    frame_image.save(j)
                    show_frames(display_fram_num)
                    display_fram_num=display_fram_num+1

            else:
                break
            i = i + 1
        cap.release()

    elif (start_mod != "0") & (end_mod != "0"):
        while (cap.isOpened()):
            ret, frame = cap.read()
            if ret == True:
                if ((i >= int(start_mod))&((i <= int(end_mod)))):

                    asd=cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
                    frame_image=Image.fromarray(asd)
                    secname=".jpg"
                    j=f'{video_savepath_globle}{display_fram_num}{secname}'
                    frame_image.save(j)
                    show_frames(display_fram_num)
                    display_fram_num=display_fram_num+1

            else:
                break
            i = i + 1
    cap.release()

    return 1

def video_brows():
    global video_path_globle
    video_path_globle=filedialog.askopenfilename(initialdir=os.getcwd(), title="Select Video",
                                                filetypes=(("mp4", "*.mp4"),
                                                           ("avi", "*.avi"),
                                                           ("All Files", "*.*")))

def video_save_brows():
    global video_savepath_globle
    if  video_path_globle!="---------------------------------> Select Video <---------------------------------":
        path =filedialog.asksaveasfile(mode='w')
        print(path)
        video_savepath_globle=making_path(path)
        print(video_savepath_globle)
    else:
        messagebox.showerror("Error","Video Not Selected")
    return 1

def stream_main_control():
    global video_path_globle,video_savepath_globle,start_framing,end_framing
    if video_path_globle == "---------------------------------> Select Video <---------------------------------":
        messagebox.showerror("Error", "Video Not Selected")
    elif video_savepath_globle == "---------------------------------> Select Destination <---------------------------------":
        messagebox.showerror("Error", "Destination Not Selected")
    else:
        show_lab = Label(window_main_all_cap, text="Prossing : Please Wait", fg="blue", bg="#E0F7CC",
                         font=("Constantia", 15, "bold")).place(x=100, y=470)
        messagebox.showinfo("Information", "Framing Start ")
        if((start_framing=="0")&(end_framing=="0")):# complete video frames
            video_cap(video_path_globle, "0", "0")
            video_savepath_globle = "---------------------------------> Select Destination <---------------------------------"
            video_path_globle = "---------------------------------> Select Video <---------------------------------"


        elif ((start_framing != "0") & (end_framing != "0")):# specfic periods frame
            start=int(start_framing)
            endr=int(end_framing)
            finel_s_res=str(1800*start)
            finel_e_res=str(1800*endr)
            video_cap(video_path_globle, finel_s_res, finel_e_res)
            video_savepath_globle = "---------------------------------> Select Destination <---------------------------------"
            video_path_globle = "---------------------------------> Select Video <---------------------------------"
            start_framing="0"
            end_framing="0"

        elif ((start_framing == "0") & (end_framing != "0")):# frams from Specfic Ending Point
            endr = int(end_framing)
            finel_e_res = str(1800 * endr)
            video_cap(video_path_globle, "0", finel_e_res)
            video_savepath_globle = "---------------------------------> Select Destination <---------------------------------"
            video_path_globle = "---------------------------------> Select Video <---------------------------------"
            start_framing = "0"
            end_framing = "0"

        elif ((start_framing != "0") & (end_framing == "0")):# frams from Specfic starting Point
            start = int(start_framing)
            finel_s_res = str(1800 * start)
            video_cap(video_path_globle, finel_s_res, "0")
            video_savepath_globle = "---------------------------------> Select Destination <---------------------------------"
            video_path_globle = "---------------------------------> Select Video <---------------------------------"
            start_framing = "0"
            end_framing = "0"
        messagebox.showinfo("Information", "Completed Successfully")
    return 1



'''   ------------------------   Windows   '''

def window_imgage_contanor(switchkey):
    global window
    app_weidth = 600
    app_height = 700
    window_main_all.iconbitmap("logoicon.ico")
    screen_width = window_main_all.winfo_screenwidth()
    screen_height = window_main_all.winfo_screenheight()
    x = center_screen_quardenate_x
    y = center_screen_quardenate_y
    y = y - 40
    window_main_all.geometry(f'{app_weidth}x{app_height}+{int(x)}+{int(y)}')
    window_main_all.maxsize(600, 700)
    window_main_all.minsize(600, 700)
    background_image = Image.open("br2.jpg")
    resize_background_image = background_image.resize((600, 700))
    final_backgroung_image = ImageTk.PhotoImage(resize_background_image)
    background_image_label = Label(window_main_all)
    background_image_label.configure(image=final_backgroung_image)
    background_image_label.image = final_backgroung_image
    background_image_label.place(x=0, y=0)
    default_fun()

    def switch_fun():
        if int(switchkey)==1:
            window_noice_connect_l()

        elif int(switchkey)==2:
            window_main_allsport_connect_l()

        elif int(switchkey) == 3:
            window_icon_connect_l()

        elif int(switchkey) == 4:
            window_text_connect_l()
        elif int(switchkey)==5:
            window_manual_conect_l()
        return 1

    def window_noice_connect_l():
        if image_filename!="":
            window_noice()
        else:
            messagebox.showerror("Error", "Image Not found")
        return 1

    def window_main_allsport_connect_l():
        if image_filename != "":
            window_main_pasport()
        else:
            messagebox.showerror("Error", "Image Not found")
        return 1

    def window_icon_connect_l():
        if image_filename != "":
            window_icon()
        else:
            messagebox.showerror("Error", "Image Not found")
        return 1
    def window_manual_conect_l():
        if image_filename!="":
            win_manual_size()
        else:
            messagebox.showerror("Error", "Image Not found")

    def window_text_connect_l():
        if image_filename != "":
            window_text()
        else:
            messagebox.showerror("Error", "Image Not found")
        return 1


    # text_lable = Label(window_main_all, text="- - P I C T U R E - -   ", bg="orange", fg="#0000A0", font="Algerian 20").place(x=171,
    #                                                                                                             y=30)
    button_brows = Button(window_main_all, text="B r o w s e", width=40, height=2, bg="white", command=brows_fun).place(x=73,
                                                                                                            y=520)
    buttonclear = Button(window_main_all, text="N E X T", width=19, height=2, bg="white", command=switch_fun).place(x=73, y=650)
    buttonconversion = Button(window_main_all, text="C L E A R", width=19, height=2, bg="white", command=default_fun).place(x=222, y=650)
    button_brows2 = Button(window_main_all, text="B a c k", width=10, height=2, bg="white", command=win_one).place(x=460, y=650)
    return 1

def window_text():
    if  image_filename !="":
        app_weidth = 900
        app_height = 700
        window_main_all.iconbitmap("logoicon.ico")
        screen_width = window_main_all.winfo_screenwidth()
        screen_height = window_main_all.winfo_screenheight()
        x = (screen_width / 2) - (app_weidth / 2)
        y = (screen_height / 2) - (app_height / 2)
        y = y - 40
        background_pick = Image.open("tf.png")
        resize_background = background_pick.resize((900, 700))
        final_image = ImageTk.PhotoImage(resize_background)
        frame_noice_wiz = Label(window_main_all)
        frame_noice_wiz.configure(image=final_image)
        frame_noice_wiz.image = final_image
        frame_noice_wiz.place(x=0, y=0)

        window_main_all.geometry(f'{app_weidth}x{app_height}+{int(x)}+{int(y)}')
        window_main_all.maxsize(900, 700)
        window_main_all.minsize(900, 700)
        window_main_all.title("ButterFly Production")
        frame_noice_win = Frame(window_main_all).place(x=0, y=0)

        open_image = Image.open(always_keep_orignel_image)
        image_size = open_image.resize((312, 514))
        final_imagetk = ImageTk.PhotoImage(image_size)
        image_lable = Label(frame_noice_win, relief=SUNKEN)
        image_lable.configure(image=final_imagetk)
        image_lable.image = final_imagetk
        image_lable.place(x=90, y=94)
        # -------------------After Filter-----------------
        image_size2=open_image.resize((320,514))
        final_image2=ImageTk.PhotoImage(image_size2)
        image_lable2 = Label(frame_noice_win, relief=SUNKEN)
        image_lable2.configure(image=final_image2)
        image_lable2.image = final_image2
        image_lable2.place(x=489, y=94)

        def direct_call_1():

                final_image_return = feltered_image_frame_2(1)
                filter_display_result(final_image_return)

        def direct_call_2():

                    final_image_return = feltered_image_frame_2(2)
                    filter_display_result(final_image_return)

        def direct_call_3():

                final_image_return = feltered_image_frame_2(3)
                filter_display_result(final_image_return)

        def direct_call_4():

                for i in range(1):
                    final_image_return = feltered_image_frame_2(4)
                    filter_display_result(final_image_return)

        def save_fun_direct_call():
                save_fun(1)
                return 1

        def filter_display_result(filtered_image_catcher):
                global save_object
                save_object = filtered_image_catcher
                image_lable2 = Label(window_main_all,relief=SUNKEN)
                image_lable2.configure(image=filtered_image_catcher)
                image_lable2.image = filtered_image_catcher
                image_lable2.place(x=489, y=94)

        def resetfun():
                global image_globel,image_save_main
                image_save_main=""
                image_globel = always_keep_orignel_image
                img = Image.open(always_keep_orignel_image)
                resize_image = img.resize((320,514))
                final_image = ImageTk.PhotoImage(resize_image)
                image_lable2 = Label(window_main_all,relief=SUNKEN)
                image_lable2.configure(image=final_image)
                image_lable2.image = final_image
                image_lable2.place(x=489, y=94)
                return 1

        def destroy_fun():
                default_fun()
                window_main_all.destroy()
            # ---------------------  Algorithm Controls Buttons

        algo_level1_button = Button(window_main_all, text="Try 1", height=2, width=7, bg="#C77826",fg="white",
                                    command=direct_call_1).place(x=95, y=640)
        algo_level2_button = Button(window_main_all, text="Try 2", height=2, width=7, bg="#C77826",fg="white",
                                    command=direct_call_2).place(x=175, y=640)
        algo_level3_button = Button(window_main_all, text="Try 3", height=2, width=7, bg="#C77826",fg="white",
                                    command=direct_call_3).place(x=255, y=640)
        algo_level4_button = Button(window_main_all, text="Try 4", height=2, width=7, bg="#C77826",fg="white",
                                    command=direct_call_4).place(x=335, y=640)
        algo_level5_button = Button(window_main_all, text="Reset", height=2, width=10, bg="#E0A15F",fg="white",
                                    command=resetfun).place(x=510, y=640)
        # --------------------- ------------------------ -------------- --------------- ------------------
        buttonquit = Button(window_main_all, text="Back", width=10, height=2, bg="#E0A15F",fg="white",
                            command=lambda:window_imgage_contanor(4)).place(x=710, y=640)
        button_Save_pic = Button(window_main_all, text="S a v e", width=10, height=2, bg="#E0A15F",fg="white",
                                 command=save_fun_direct_call).place(x=610, y=640)
    else:
        messagebox.showerror("Error", "Image Not found")
    return 1

def window_noice():
    if image_filename != "":
        app_weidth = 900
        app_height = 700
        window_main_all.iconbitmap("logoicon.ico")
        screen_width = window_main_all.winfo_screenwidth()
        screen_height = window_main_all.winfo_screenheight()
        x = (screen_width / 2) - (app_weidth / 2)
        y = (screen_height / 2) - (app_height / 2)
        y = y - 40

        background_pick=Image.open("f4.jpg")
        resize_background=background_pick.resize((900,700))
        final_image=ImageTk.PhotoImage(resize_background)
        frame_noice_wiz = Label(window_main_all)
        frame_noice_wiz.configure(image=final_image)
        frame_noice_wiz.image=final_image
        frame_noice_wiz.place(x=0,y=0)

        window_main_all.geometry(f'{app_weidth}x{app_height}+{int(x)}+{int(y)}')
        window_main_all.maxsize(900, 700)
        window_main_all.minsize(900, 700)
        window_main_all.title("ButterFly Production")
        frame_noice_win= Frame(window_main_all).place(x=0,y=0)

        # text_lable1 =  Label(frame_noice_win , text="B e f o r e", bg="orange", fg="#0000A0", font="Algerian 20").place(x=171,
        #                                                                                                         y=70)
        # text_lable2 =  Label(frame_noice_win , text="A f t e r", bg="orange", fg="#0000A0", font="Algerian 20").place(x=590,
        #                                                                                                       y=70)
        open_image=Image.open(always_keep_orignel_image)
        image_size=open_image.resize((330, 494))
        final_imagetk=ImageTk.PhotoImage(image_size)
        image_lable =  Label(frame_noice_win ,relief=SUNKEN)
        image_lable.configure(image=final_imagetk)
        image_lable.image = final_imagetk
        image_lable.place(x=82, y=104)
        # -------------------After Filter-----------------

        image_lable2 =  Label(frame_noice_win ,relief=SUNKEN)
        image_lable2.configure(image=final_imagetk)
        image_lable2.image = final_imagetk
        image_lable2.place(x=500, y=103)

        def direct_call_1():

            final_image_return = feltered_image_frame_1(1)
            filter_display_result(final_image_return)

        def direct_call_2():
            for x in range(2):
                final_image_return = feltered_image_frame_1(2)
                filter_display_result(final_image_return)

        def direct_call_3():

            final_image_return = feltered_image_frame_1(3)
            filter_display_result(final_image_return)

        def direct_call_4():
                final_image_return = feltered_image_frame_1(4)
                filter_display_result(final_image_return)

        def save_fun_direct_call():
            save_fun(1)
            return 1

        def filter_display_result(filtered_image_catcher):
            global save_object
            save_object = filtered_image_catcher
            image_lable2 = Label(frame_noice_win,relief=SUNKEN)
            image_lable2.configure(image=filtered_image_catcher)
            image_lable2.image = filtered_image_catcher
            image_lable2.place(x=500, y=103)

        def resetfun():
            global image_globel,image_save_main
            image_save_main=""
            image_globel = always_keep_orignel_image
            img = Image.open(always_keep_orignel_image)
            resize_image = img.resize((330, 494))
            final_image = ImageTk.PhotoImage(resize_image)
            image_lable2 = Label(frame_noice_win ,relief=SUNKEN)
            image_lable2.configure(image=final_image)
            image_lable2.image = final_image
            image_lable2.place(x=500, y=103)
            return 1

        def destroy_fun():
            default_fun()
            frame_noice_win .destroy()
            # ---------------------  Algorithm Controls Buttons

        # algo_level1_button =  Button(frame_noice_win , text="Normal", width=19, height=2, bg="white",
        #                             command=direct_call_1).place(x=110, y=640)

        algo_level3_button =  Button(frame_noice_win , text=" Black & White", width=13, height=2, bg="white",
                                    command=direct_call_3).place(x=80, y=640)

        algo_level4_button = Button(frame_noice_win, text="Remove Noice", width=13, height=2, bg="white",
                                    command=direct_call_4).place(x=190, y=640)

        algo_level2_button = Button(frame_noice_win, text="sharp", width=13, height=2, bg="white",
                                    command=direct_call_2).place(x=300, y=640)

        algo_level5_button =  Button(frame_noice_win , text="Reset", width=13, height=2, bg="white", command=resetfun).place(
            x=490, y=640)
        # --------------------- ------------------------ -------------- --------------- ------------------
        buttonquit =  Button(frame_noice_win , text="Back", width=13, height=2, bg="white", command=lambda:window_imgage_contanor(1)).place(
            x=740, y=640)
        # button_orignal_pic = Button(window_main_all, text="Orignel", width=30, height=2, bg="gold", command=default_fun).place(
        #    x=130, y=510)
        button_Save_pic =  Button(frame_noice_win , text="S a v e", width=13, height=2, bg="white",
                                 command=save_fun_direct_call).place(x=610, y=640)
    else:
        messagebox.showerror("Error", "Image Not found")
    return 1

def window_main_pasport():
    if image_filename != "":
        window_main_all_lab = Label(window_main_all,bg="orange",width=500,height=600).place(x=0,y=0)
        window_main_all.title("ButterFly Production")
        window_main_all.iconbitmap('logoicon.ico')
        window_weidth = 600
        window_heigth = 700
        window_main_all.minsize(600, 700)
        window_main_all.maxsize(600, 700)
        screen_width2 = window_main_all.winfo_screenwidth()
        screen_height2 = window_main_all.winfo_screenheight()
        x = (screen_width2 / 2) - (window_weidth / 2)
        y = (screen_height2 / 2) - (window_heigth / 2)
        y = y - 40
        window_main_all.configure(bg="gold")

        window_main_all.geometry(f'{window_weidth}x{window_heigth}+{int(x)}+{int(y)}')
        background_image_three = Image.open("iconback.jpeg")
        background_image_win_three = Image.open(image_filename)
        resized_background_image = background_image_three.resize((600, 700))
        large_passport = background_image_win_three.resize((140, 210))
        mediam_passport = background_image_win_three.resize((130, 180))
        small_passport = background_image_win_three.resize((100, 130))
        background_final_image = ImageTk.PhotoImage(resized_background_image)
        final_large_passport = ImageTk.PhotoImage(large_passport)
        final_mediam_passport = ImageTk.PhotoImage(mediam_passport)
        final_small_passport = ImageTk.PhotoImage(small_passport)
        global image_save_passport_1, image_save_passport_2,image_save_passport_3

        image_array_passport_small = np.asarray(small_passport)
        image_save_passport_1 = Image.fromarray(image_array_passport_small)

        image_array_passport_medum = np.asarray(mediam_passport)
        image_save_passport_2 = Image.fromarray(image_array_passport_medum)

        image_array_passport_large=np.asarray(large_passport)
        image_save_passport_3=Image.fromarray(image_array_passport_large)

        background_image_label0 = Label(window_main_all)
        background_image_label0.configure(image=background_final_image)
        background_image_label0.image = background_final_image
        background_image_label0.place(x=0, y=0)

        frame_image = Image.open("f5.jpg.")
        frame1_resize = frame_image.resize((153, 223))
        frame2_resize = frame_image.resize((143, 193))
        frame3_resize = frame_image.resize((113, 143))

        final_frame1_tk = ImageTk.PhotoImage(frame1_resize)
        final_frame2_tk = ImageTk.PhotoImage(frame2_resize)
        final_frame3_tk = ImageTk.PhotoImage(frame3_resize)

        frame_lable1 = Label(window_main_all)
        frame_lable1.configure(image=final_frame1_tk)
        frame_lable1.image = final_frame1_tk
        frame_lable1.place(x=34, y=74)

        frame_lable2 = Label(window_main_all)
        frame_lable2.configure(image=final_frame2_tk)
        frame_lable2.image = final_frame2_tk
        frame_lable2.place(x=154, y=324)

        frame_lable3 = Label(window_main_all)
        frame_lable3.configure(image=final_frame3_tk)
        frame_lable3.image = final_frame3_tk
        frame_lable3.place(x=304, y=514)

        background_image_label1 = Label(window_main_all)
        background_image_label1.configure(image=final_large_passport)
        background_image_label1.image = final_large_passport
        background_image_label1.place(x=40, y=80)

        background_final_label2 = Label(window_main_all)
        background_final_label2.configure(imag=final_mediam_passport)
        background_final_label2.image = final_mediam_passport
        background_final_label2.place(x=160, y=330)

        background_final_label3 = Label(window_main_all)
        background_final_label3.configure(image=final_small_passport)
        background_final_label3.image = final_small_passport
        background_final_label3.place(x=310, y=520)

        def save_fun_direct_call_pasport_large():
            save_fun(5)
            return 1

        def save_fun_direct_call_pasport_medum():
            save_fun(6)
            return 1
        def save_fun_direct_call_pasport_small():
            save_fun(7)
            return 1

        text_lable_win_three1 = Label(window_main_all, text="Large", bg="white", fg="#0000A0",
                                      font="Algerian 17").place(x=66, y=30)
        text_lable_win_three2 = Label(window_main_all, text="Mediam", bg="white", fg="#0000A0",
                                      font="Algerian 13").place(x=190, y=300)
        text_lable_win_three3 = Label(window_main_all, text="Small", bg="white", fg="#0000A0",
                                      font="Algerian 10").place(x=330, y=490)
        weidthpp = window_main_all.winfo_screenwidth()
        y_width = weidthpp / 2
        button1_winthree = Button(window_main_all, text="S a v e ", bg="White", width=10,
                                  command=save_fun_direct_call_pasport_large).place(x=56, y=665)
        button2_winthree = Button(window_main_all, text="S a v e ", bg="White", width=10,
                                  command=save_fun_direct_call_pasport_medum).place(x=180, y=665)
        button3_winthree = Button(window_main_all, text="S a v e ", bg="White", width=10,
                                  command=save_fun_direct_call_pasport_small).place(x=323, y=665)
        button4_winthree = Button(window_main_all, text="Back", bg="White", width=5,
                                  command=lambda:window_imgage_contanor(2)).place(x=523, y=665)
    else:
        messagebox.showerror("Error", "Image Not Found")

def window_icon():
    if image_filename != "":
        window_main_all_lab =  Label(window_main_all,bg="orange",width=500,height=600).place(x=0,y=0)
        window_main_all.title("ButterFly Production")
        window_main_all.iconbitmap('logoicon.ico')
        window_weidth = 500
        window_heigth = 600
        window_main_all.minsize(500, 600)
        window_main_all.maxsize(500, 600)
        screen_width2 = window_main_all.winfo_screenwidth()
        screen_height2 = window_main_all.winfo_screenheight()
        x = (screen_width2 / 2) - (window_weidth / 2)
        y = (screen_height2 / 2) - (window_heigth / 2)
        y = y - 40
        window_main_all.configure(bg="gold")

        window_main_all.geometry(f'{window_weidth}x{window_heigth}+{int(x)}+{int(y)}')
        background_image_three = Image.open("iconback.jpeg")
        background_image_win_three = Image.open(image_filename)
        resized_background_image = background_image_three.resize((500, 600))
        large_icon = background_image_win_three.resize((96, 96))
        mediam_icon = background_image_win_three.resize((48, 48))
        small_icon = background_image_win_three.resize((16, 16))
        background_final_image = ImageTk.PhotoImage(resized_background_image)
        final_large_icon = ImageTk.PhotoImage(large_icon)
        final_mediam_icon = ImageTk.PhotoImage(mediam_icon)
        final_small_icon = ImageTk.PhotoImage(small_icon)
        global image_save_icon_1, image_save_icon_2,image_save_icon_3
        image_array_icon_small = np.asarray(small_icon)
        image_save_icon_1 = Image.fromarray(image_array_icon_small)
        image_array_icon_medum = np.asarray(mediam_icon)
        image_save_icon_2 = Image.fromarray(image_array_icon_medum)
        image_array_icon_large=np.asarray(large_icon)
        image_save_icon_3=image_array_icon_large

        background_image_label0 = Label(window_main_all)
        background_image_label0.configure(image=background_final_image)
        background_image_label0.image = background_final_image
        background_image_label0.place(x=0, y=0)

        frame_image = Image.open("f5.jpg.")
        frame1_resize = frame_image.resize((106, 106))
        frame2_resize = frame_image.resize((58, 58))
        frame3_resize = frame_image.resize((22, 22))

        final_frame1_tk = ImageTk.PhotoImage(frame1_resize)
        final_frame2_tk = ImageTk.PhotoImage(frame2_resize)
        final_frame3_tk = ImageTk.PhotoImage(frame3_resize)

        frame_lable1 = Label(window_main_all)
        frame_lable1.configure(image=final_frame1_tk)
        frame_lable1.image = final_frame1_tk
        frame_lable1.place(x=55, y=195)

        frame_lable2 = Label(window_main_all)
        frame_lable2.configure(image=final_frame2_tk)
        frame_lable2.image = final_frame2_tk
        frame_lable2.place(x=195, y=345)

        frame_lable3 = Label(window_main_all)
        frame_lable3.configure(image=final_frame3_tk)
        frame_lable3.image = final_frame3_tk
        frame_lable3.place(x=306, y=427)

        background_image_label1 = Label(window_main_all)
        background_image_label1.configure(image=final_large_icon)
        background_image_label1.image = final_large_icon
        background_image_label1.place(x=60, y=200)

        background_final_label2 = Label(window_main_all)
        background_final_label2.configure(imag=final_mediam_icon)
        background_final_label2.image = final_mediam_icon
        background_final_label2.place(x=200, y=350)

        background_final_label3 = Label(window_main_all)
        background_final_label3.configure(image=final_small_icon)
        background_final_label3.image = final_small_icon
        background_final_label3.place(x=310, y=430)

        def save_fun_direct_call_icon_large():
            save_fun(2)
            return 1

        def save_fun_direct_call_icon_medum():
            save_fun(3)
            return 1
        def save_fun_direct_call_icon_small():
            save_fun(4)
            return 1

        text_lable_win_three1 = Label(window_main_all, text="Large", bg="white", fg="#0000A0",
                                      font="Algerian 17").place(x=70, y=160)
        text_lable_win_three2 = Label(window_main_all, text="Med", bg="white", fg="#0000A0",
                                      font="Algerian 13").place(x=210, y=320)
        text_lable_win_three3 = Label(window_main_all, text="S", bg="white", fg="#0000A0",
                                      font="Algerian 10").place(x=315, y=405)
        weidthpp = window_main_all.winfo_screenwidth()
        y_width = weidthpp / 2
        button1_winthree = Button(window_main_all, text="S a v e ", bg="White", width=10,
                                  command=save_fun_direct_call_icon_large).place(x=66, y=540)
        button2_winthree = Button(window_main_all, text="S a v e ", bg="White",  width=5,
                                  command=save_fun_direct_call_icon_medum).place(x=210, y=540)
        button3_winthree = Button(window_main_all, text="S a v e ", bg="White", width=4,
                                  command=save_fun_direct_call_icon_small).place(x=315, y=540)
        button3_winfour = Button(window_main_all, text="Back ", bg="White",
                                  command=lambda:window_imgage_contanor(3)).place(x=415, y=540)

    else:
        messagebox.showerror("Error", "Image Not Found")

def window_cam():
    global window_main_all_cap
    main_init()
    window_main_all_cap=Toplevel()
    window_main_all_cap.title("ButterFly Production")
    window_main_all_cap.iconbitmap('logoicon.ico')
    window_weidth = 900
    window_heigth = 700
    window_main_all_cap.minsize(700, 600)
    window_main_all_cap.maxsize(700, 600)
    screen_width2 = window_main_all_cap.winfo_screenwidth()
    screen_height2 = window_main_all_cap.winfo_screenheight()
    x = (screen_width2 / 2) - (window_weidth / 2)
    y = (screen_height2 / 2) - (window_heigth / 2)
    y = y - 40

    background_image=Image.open("iconback.jpeg")
    background_resize=background_image.resize((700,600))
    background_imagetk=ImageTk.PhotoImage(background_resize)
    background_image_lable=Label(window_main_all_cap)
    background_image_lable.configure(image=background_imagetk)
    background_image_lable.image=background_imagetk
    background_image_lable.place(x=0,y=0)

    window_main_all_cap.geometry(f'{window_weidth}x{window_heigth}+{int(x)}+{int(y)}')
    def text_show(address,mod):
        if mod==1:
            Path_text_lable=Label(window_main_all_cap,text=f'{address}',
                           fg="blue",bg="#E0F7CC",font="Forte 15").place(x=40,y=100)
        elif mod==2:
            Path_text_lable2 = Label(window_main_all_cap, text=f'{address}',
                                    fg="blue", bg="#E0F7CC", font="Forte 15").place(x=40, y=330)

        return 14

    def text_control():
        video_brows()
        text_show("------------------------------------------------------------------------------------",1)
        text_show(video_path_globle,1)
        return 1

    def text_control_save():
        video_save_brows()
        text_show("------------------------------------------------------------------------------------",2)
        text_show(video_savepath_globle,2)
        return 1

    def straem_in_control():
        global start_framing,end_framing
        if(((type(int(field_1.get())))==int)&((type(int(field_2.get())))==int)):
            start_framing=field_1.get()
            end_framing=field_2.get()
        if start_framing=="":
            start_framing="0"
        if end_framing=="":
            end_framing="0"

        stream_main_control()
        text_show(video_path_globle,1)
        text_show(video_savepath_globle,2)
    field_1=Entry(window_main_all_cap,width=5)
    field_1.insert(0,"0")
    field_1.place(x=130,y=225)

    field_2 = Entry(window_main_all_cap, width=5)
    field_2.insert(0, "0")
    field_2.place(x=130, y=255)
    def wincont():
        window_main_all_cap.destroy()
        win_one()

    field_text=Label(window_main_all_cap,text="Enter Mniuts From Framing Starts",bg="#E0F7CC",fg="blue",font=("Constantia",10,"bold")).place(x=165,y=225)
    field_text = Label(window_main_all_cap, text="Enter Mniuts where Fraims End", bg="#E0F7CC", fg="blue",font=("Constantia",10,"bold")).place(x=165, y=255)
    text_show(video_path_globle,1)
    text_show(video_savepath_globle,2)

    button_video_path=Button(window_main_all_cap,text="Brows",bg="#E0F7CC",
                           font="Algerian 15",command=text_control).place(x=240,y=150)

    button_video_frames = Button(window_main_all_cap, text="Brows", bg="#E0F7CC",
                                 font="Algerian 15", command=text_control_save).place(x=240, y=385)

    button_video_frames=Button(window_main_all_cap,text="Start Framing",bg="#E0F7CC",
                           font="Algerian 15",command=straem_in_control).place(x=190,y=530)

    button_video_frames = Button(window_main_all_cap, text="B a c k", bg="#E0F7CC",
                                 font="Algerian 15", command=wincont).place(x=490, y=530)
    return 1

def win_one():
    global center_screen_quardenate_x,center_screen_quardenate_y
    app_weidth = 620
    app_height = 700
    window_main_all.iconbitmap("logoicon.ico")
    screen_width = window_main_all.winfo_screenwidth()
    screen_height = window_main_all.winfo_screenheight()
    x = (screen_width / 2) - (app_weidth / 2)
    y = (screen_height / 2) - (app_height / 2)
    y = y - 40
    center_screen_quardenate_x=x
    center_screen_quardenate_y=y
    window_main_all.geometry(f'{app_weidth}x{app_height}+{int(x)}+{int(y)}')
    window_main_all.maxsize(620, 700)
    window_main_all.minsize(620, 700)

    window_main_all.title("ButterFly Production")

    background_pick = Image.open("manupic.jpg")
    resizee_background_pic=background_pick.resize((620,700))
    final_background_pic=ImageTk.PhotoImage(resizee_background_pic)
    frame_pic_back = Label(window_main_all)
    frame_pic_back.configure(image=final_background_pic)
    frame_pic_back.image=final_background_pic
    frame_pic_back.place(x=0,y=0)


    button_lable4 = Button(window_main_all, text="Text Enhancing", bg="white", font="Rockwell", width=25,
                           height=4, command=lambda:window_imgage_contanor(4)).place(x=50, y=20)
    button_lable2 =  Button(window_main_all, text="Pasport Size", bg="white", font="Rockwell", width=25,
                       height=4, command=lambda:window_imgage_contanor(2)).place(x=330, y=115)
    button_lable3 =  Button(window_main_all, text="Icon Size", bg="white", font="Rockwell", width=25,
                       height=4, command=lambda:window_imgage_contanor(3)).place(x=50, y=220)
    button_lable6 = Button(window_main_all, text="Noice Remover", bg="white", font="Rockwell", width=25,
                           height=4, command=lambda:window_imgage_contanor(1)).place(x=330, y=320)
    button_lable5 =  Button(window_main_all, text="Video To Framing", bg="white", font="Rockwell", width=25,
                       height=4, command=window_cam).place(x=50, y=420)
    button_lable5 = Button(window_main_all, text="Manual Size Converter", bg="white", font="Rockwell", width=25,
                           height=4, command=lambda:window_imgage_contanor(5)).place(x=330, y=520)
    button_lable7 =  Button(window_main_all, text="Q u i t", bg="white", font="Rockwell", width=59,
                       height=2, command=window_main_all.destroy).place(x=50, y=630)

    return 1

def wellcome_win():

    window_wellcome_all=Toplevel()
    app_width=800
    app_hight=500
    win_weidth=window_wellcome_all.winfo_screenwidth()
    win_height=window_wellcome_all.winfo_screenheight()
    x=(win_weidth/2)-(app_width/2)
    y=(win_height/2)-(app_hight/2)
    y=y-40
    window_wellcome_all.geometry(f'{app_width}x{app_hight}+{int(x)}+{int(y)}')
    window_wellcome_all.title("Well Come")
    window_wellcome_all.iconbitmap("logoicon.ico")
    frame_number=175
    giflable = Label(window_wellcome_all)

    def inemation(frame_number):

        if frame_number==1000:
            win_one()

            window_wellcome_all.destroy()
        else:
            print("\n in",frame_number)
            fram_count = str(frame_number)
            open_frame = Image.open(f'a{fram_count}.jpg')
            resize_frame = open_frame.resize((800, 500))

            font=ImageFont.truetype("FFF_Tusj.ttf",80)
            font2=ImageFont.truetype("Antonio-Bold.ttf",40)

            draw=ImageDraw.ImageDraw(resize_frame)
            draw2=ImageDraw.ImageDraw(resize_frame)

            text="A . J   Presents"
            text2=" P   h   o   t   o      F   i   x "

            draw.text((85,300),text,(0,200,255),font=font)
            draw2.text((240,430),text2,(0,50,255),font=font2)

            frametk = ImageTk.PhotoImage(resize_frame)
            giflable.configure(image=frametk)
            giflable.image=frametk
            giflable.place(x=0,y=0)
            frame_number=frame_number+1
            if frame_number==245:
                frame_number=1000
                time.sleep(1)
        window_wellcome_all.after(30,lambda : inemation(frame_number))

        return 1
    inemation(frame_number)

def win_manual_size():
    if image_filename!="":
        global size_one,size_two,win_manual
        win_manual=Toplevel()
        win_manual.state("zoomed")
        win_manual.configure(bg="white")

        weidthapp=int(win_manual.winfo_screenwidth())
        heighapp=int(win_manual.winfo_screenheight())
        win_manual.minsize(weidthapp,heighapp)
        win_manual.maxsize(weidthapp,heighapp)
        print("weidth : ",weidthapp)
        print("height : ",heighapp)
        picture=Image.open("manualbackpick.jpeg")
        resize_pic=picture.resize((weidthapp,heighapp))

        font2=ImageFont.truetype("Antonio-Bold.ttf",20)

        draw=ImageDraw.ImageDraw(resize_pic)
        draw2=ImageDraw.ImageDraw(resize_pic)

        text="Enter photo size"
        text2=" x "

        draw.text((10,20),text,(150,50,150),font=font2)
        draw2.text((60,65),text2,(150,50,150),font=font2)
        background_pictk=ImageTk.PhotoImage(resize_pic)
        back_ground_pic=Label(win_manual)
        back_ground_pic.configure(image=background_pictk)
        back_ground_pic.image=background_pictk
        back_ground_pic.place(x=0,y=0)

        #line_frame=Frame(win_manual,width=700,height=3,bg="black").place(x=50,y=150)
        entery_lable=Entry(win_manual,width=8)
        entery_lable.insert(0,"200")
        entery_lable.place(x=5,y=70)
        # t_lteable = Label(win_manual, text="X", fg="black", bg="white",
        #                    font=("Constantia", 10, "bold")).place(x=235, y=50)
        entery_lable2 = Entry(win_manual, width=8)
        entery_lable2.insert(0, "200")
        entery_lable2.place(x=90, y=67)
        def permint_frame():
            frame_x_axis=weidthapp-500;
            picture_perment_frame = Image.open("f4landscape.jpg")
            resize_pic_perment_frame = picture_perment_frame.resize((410, 210))
            background_pictk_perment_frame = ImageTk.PhotoImage(resize_pic_perment_frame)
            back_ground_pic_perment_frame = Label(win_manual)
            back_ground_pic_perment_frame.configure(image=background_pictk_perment_frame)
            back_ground_pic_perment_frame.image = background_pictk_perment_frame
            back_ground_pic_perment_frame.place(x=frame_x_axis, y=10)
            frame_x_axis2 = frame_x_axis+11;
            picture_current = Image.open(image_filename)
            resize_pic_current = picture_current.resize((388, 189))
            background_pictk_current = ImageTk.PhotoImage(resize_pic_current)
            back_ground_pic_current = Label(win_manual)
            back_ground_pic_current.configure(image=background_pictk_current)
            back_ground_pic_current.image = background_pictk_current
            back_ground_pic_current.place(x=frame_x_axis2, y=20)
        def currentsize():
            global x_current_axis, y_current_axis
            x_size=int(weidthapp/2)+100
            y_size=int(heighapp/2)-20
            x_current_axis=weidthapp-x_size-10
            y_current_axis=heighapp-int(heighapp/2)-50
            print(x_current_axis, "  ", y_current_axis)
            picture_perment_frame = Image.open("f4landscape.jpg")
            resize_pic_perment_frame = picture_perment_frame.resize((x_size,y_size))
            background_pictk_perment_frame = ImageTk.PhotoImage(resize_pic_perment_frame)
            back_ground_pic_perment_frame = Label(win_manual)
            back_ground_pic_perment_frame.configure(image=background_pictk_perment_frame)
            back_ground_pic_perment_frame.image = background_pictk_perment_frame
            back_ground_pic_perment_frame.place(x=x_current_axis, y=y_current_axis)
        def back_control():
            win_manual.destroy()
            save_fun(1)

            window_imgage_contanor(5)




        currentsize()
        permint_frame()

        print(x_current_axis,"  ",y_current_axis)
        def reset():
            global image_save_main
            print("in  reset")
            picture = Image.open("manualbackpickcroped.jpeg")
            resize_pic = picture.resize((weidthapp-215, heighapp))
            background_pictk = ImageTk.PhotoImage(resize_pic)
            back_ground_pic = Label(win_manual)
            back_ground_pic.configure(image=background_pictk)
            back_ground_pic.image = background_pictk
            back_ground_pic.place(x=215, y=0)
            return 1

        def size_concversion():

            size_one = entery_lable.get()
            size_two = entery_lable2.get()
            print("in apply")
            confirm = 1
            try:
                print("in try")
                a = int(size_one)
                d = int(size_two)
            except:
                confirm = 0

            if (confirm == 1):
                global image_save_main
                s_one = int(size_one)
                s_two = int(size_two)
                reset()
                permint_frame()
                currentsize()
                picture = Image.open(image_filename)
                resize_pic = picture.resize((s_one, s_two))
                iamge_array = np.asarray(resize_pic)
                image_save_main = Image.fromarray(iamge_array)
                background_pictk = ImageTk.PhotoImage(resize_pic)
                back_ground_pic = Label(win_manual)
                back_ground_pic.configure(image=background_pictk)
                back_ground_pic.image = background_pictk
                back_ground_pic.place(x=x_current_axis+21, y=y_current_axis+17)
            else:
                messagebox.showerror("Error", "Size is wrong")
            return 1


        button_lable = Button(win_manual, text="Apply", bg="white", width=15, height=2, command=size_concversion).place(
            x=20, y=450)
        button_lable2 = Button(win_manual, text="Save", bg="white", width=15, height=2,command=back_control).place(x=20, y=650)



    else:
        messagebox.showerror("Error","Image Not Found")




'''     ------------------------    Main Window     '''

wellcome_win()

#win_one()



#buttonquit = Button(window, text="Quit", width=6, height=1, bg="gold", command=window.quit).place(x=500, y=647)

#=========================== testing Area=====================
# lableent=Entry(window_main_all,width=7)
# lableent.insert(0,"0")
# lableent.place(x=300,y=300)

# def check_fun():
#
#     if type(int(lableent.get()))==int:
#         print("in")
#         h = int(lableent.get())
#         print(type(h))
#         print(h)
#     else:
#         print("out")
#

#test=Button(window_main_all,text="test image text",command=check_fun).place(x=400,y=530)


window_main_all.mainloop()
