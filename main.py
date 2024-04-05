import tkinter as tk
from tkinter import Frame, Button
from PIL import Image, ImageTk,ImageFont,ImageDraw
from tkinter import *
from tkinter import filedialog,messagebox
import cv2
from numpy import *
import os
from PIL import Image, ImageTk,ImageEnhance
from tkinter import Label

'''   Globel Veriables  '''

always_keep_orignel_image = ""
image_globel = ""
sec_lab = ""
save_object = ""
image_filename = ""
image_save_main = ""
image_save_icon_1 = ""
image_save_icon_2 = ""
image_save_icon_3 = ""
image_save_passport_1 = ""
image_save_passport_2 = ""
image_save_passport_3 = ""
video_path_globle=""
video_savepath_globle=""
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
final_image=""
three_setimages=[]

'''        Functions           '''

def win_seting(win,w,h):
    app_weidth = w
    app_height = h
    win.iconbitmap("res/logoicon.ico")
    screen_width = win.winfo_screenwidth()
    screen_height = win.winfo_screenheight()
    x = (screen_width / 2) - (app_weidth / 2)
    y = (screen_height / 2) - (app_height / 2)
    y = y - 40
    win.geometry(f'{app_weidth}x{app_height}+{int(x)}+{int(y)}')
    win.geometry(f"{w}x{h}")
    win.title("AK Editors")
    win.maxsize(w, h)
    win.minsize(w, h)
    return 1

def location(event):
    print("x = ",event.x,", y = ",event.y)
    return 1

def img_create(screen, imgp, w, h, xx, yy):
    img = Image.open(imgp)
    raiseimg = img.resize((w, h))
    imgtk = ImageTk.PhotoImage(raiseimg)
    lab = Label(screen, image=imgtk)
    lab.image = imgtk
    lab.place(x=xx, y=yy) 
    return lab

def img_create_lab(imgp, lab, w, h):
    raiseimg = imgp.resize((w, h))
    imgtk = ImageTk.PhotoImage(raiseimg)
    lab.config(image=imgtk)
    lab.image = imgtk
    return lab

def default_fun(win,img):
    global image_final,image_globel,image_filename
    img_lab=img_create(win,img,300, 410,65,85)
    image_final = ""
    image_globel = ""
    image_filename=""
    return img_lab

def brows_fun(win):
    global image_filename,always_keep_orignel_image,image_final,image_globel
    image_filename = filedialog.askopenfilename(initialdir="/", title="Select Image",filetypes=(("JPG files", "*.jpg*"),("PNG Files", "*.png"),("All Files", "*.*")))
    if  len(image_filename)>0 :
        print("in")
        always_keep_orignel_image = image_filename
        image_globel = image_filename
        img_create(win, image_filename, 300, 410, 65, 85)
        print(image_filename)
    else:
        print(image_filename)
        image_filename=""
        default_fun(win,"res/f1.jpg")
    return 1

def text_en(frms):
    global sec_lab
    img_create(frms, always_keep_orignel_image, 312, 514, 90, 94)
    sec_lab=img_create(frms, image_globel, 312, 514, 494, 94)
    return sec_lab

def img_en(frms):
    global sec_lab
    img_create(frms, always_keep_orignel_image, 330, 494, 82, 104)
    sec_lab=img_create(frms, image_globel, 330, 494, 500, 103)
    return sec_lab

def icon_set(frms):
    global three_setimages
    save_buttons = [None, None, None]  
    img = Image.open(always_keep_orignel_image)
    three_setimages = [img.resize((96, 96)), img.resize((48, 48)), img.resize((16, 16))]
    img_label1 = Label(frms)
    img_label1.image = ImageTk.PhotoImage(three_setimages[0])
    img_label1.config(image=img_label1.image)
    img_label1.place(x=60, y=200)
    img_label1.bind("<Button-1>", lambda event, index=0: toggle_save_option(index))
    img_label2 = Label(frms)
    img_label2.image = ImageTk.PhotoImage(three_setimages[1])
    img_label2.config(image=img_label2.image)
    img_label2.place(x=200, y=350)
    img_label2.bind("<Button-1>", lambda event, index=1: toggle_save_option(index))
    img_label3 = Label(frms)
    img_label3.image = ImageTk.PhotoImage(three_setimages[2])
    img_label3.config(image=img_label3.image)
    img_label3.place(x=310, y=430)
    img_label3.bind("<Button-1>", lambda event, index=2: toggle_save_option(index))
    def toggle_save_option(index):
        nonlocal save_buttons
        if save_buttons[index] is None:  # If save button is not visible, create it
            save_buttons[index] = Button(frms, text="Save", command=lambda: save_fun_img_set(index))
            save_buttons[index].place(x=60 + (index * 140), y=300)
        else:  
            save_buttons[index].destroy()
            save_buttons[index] = None
    return 1

def pasport_set(frms):
    global sec_lab, three_setimages
    three_setimages = []
    img = Image.open(always_keep_orignel_image)
    medium_size = (130, 180) 
    total_width = 2 * medium_size[0]
    total_height = 2 * medium_size[1]
    start_x = (600 - total_width) // 2  
    start_y = (700 - total_height) // 2  
    for i in range(2):
        for j in range(2):
            three_setimages.append(img.resize(medium_size))
            img_create(frms, always_keep_orignel_image, medium_size[0], medium_size[1],start_x + j * medium_size[0], start_y + i * medium_size[1])
    return 1

def filter_try_two(img_lab):
    global final_image
    image = Image.open(image_globel)
    enh_sha = ImageEnhance.Sharpness(image)
    sharpness = 2.0
    processed_image_e = enh_sha.enhance(sharpness)
    processed_image=asarray(processed_image_e)
    cv2.imwrite('res/processed_abc_image.png', processed_image)
    im=cv2.imread('res/processed_abc_image.png')
    final_filtered_image = cv2.cvtColor(im, cv2.COLOR_BGR2RGB)
    image_save_main = Image.fromarray(final_filtered_image)
    final_image = image_save_main
    img_create_lab(image_save_main, img_lab, 330, 494)
    return 1

def filter_try_three(img_lB):
    global final_image
    image=cv2.imread(image_globel)
    image2 = cv2.cvtColor(image, cv2.COLOR_HSV2BGR)
    image2 = cv2.cvtColor(image2, cv2.COLOR_BGR2GRAY)
    figure_size = 9
    new_image = cv2.blur(image2, (figure_size, figure_size))
    processed_image=cv2.cvtColor(new_image,cv2.COLOR_GRAY2RGB)
    image_save_main = Image.fromarray(processed_image)
    final_image = image_save_main
    img_create_lab(image_save_main, img_lB, 330, 494 )
    return 1

def filter_text_image_1(imlab):
    global final_image
    image=cv2.imread(image_globel,0)
    _,processed_1=cv2.threshold(image,130,160,cv2.THRESH_BINARY)
    image_save_main = Image.fromarray(processed_1)
    final_image=image_save_main
    img_create_lab(image_save_main,imlab,312, 514,)
    return 1

def filter_text_image_2(imlab):
    global final_image
    image = cv2.imread(image_globel, 0)
    _, processed_1 = cv2.threshold(image,150, 200, cv2.THRESH_BINARY)
    image_save_main = Image.fromarray(processed_1)
    final_image=image_save_main
    img_create_lab(image_save_main,imlab,312, 514,)
    return 1

def filter_text_image_3(imlab):
    global final_image
    image=cv2.imread(image_globel,0)
    _,processed_1=cv2.threshold(image,100,180,cv2.THRESH_BINARY)
    image_save_main = Image.fromarray(processed_1)
    final_image=image_save_main
    img_create_lab(image_save_main,imlab,312, 514,)
    return 1

def filter_text_image_4(imlab):
    global final_image
    image=cv2.imread(image_globel,0)
    _,processed_1=cv2.threshold(image,130,190,cv2.THRESH_BINARY)
    image_save_main = Image.fromarray(processed_1)
    final_image=image_save_main
    img_create_lab(image_save_main,imlab,312, 514,)
    return 1

def filter_try_four(imglab):
    global  final_image
    source = cv2.imread(image_globel)
    denoised_image = cv2.fastNlMeansDenoisingColored(source, None, h=5)
    final_filtered_image=cv2.cvtColor(denoised_image,cv2.COLOR_BGR2RGB)
    image_save_main=Image.fromarray(final_filtered_image)
    final_image = image_save_main
    img_create_lab(image_save_main, imglab, 330, 494)
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

def resetfun(w,h):
    global sec_lab,image_globel
    sec_lab=img_create_lab(Image.open(image_globel), sec_lab, w, h)
    return 1

def save_fun():
        global final_image
        if final_image != "":
            path_name = filedialog.asksaveasfile(mode='w', defaultextension=".jpg")
            if not path_name:
                return
            else:
                final_image.save(path_name)
        else:
            messagebox.showerror("Error", "Image not Found")
        return 1

def save_fun_img_set(num):
    global three_setimages
    if num < len(three_setimages) and three_setimages[num] != "":
        path_name = filedialog.asksaveasfile(mode='w', defaultextension=".jpg")
        if not path_name:
            return
        else:
            three_setimages[num].save(path_name)
            messagebox.showinfo("Information", "Image Saved Successfully")
    else:
        messagebox.showerror("Error", "Image not Found")
    return 1

def video_brows(lab,mode):
    global video_path_globle,video_savepath_globle
    temp_path=""
    if mode==1:
        temp_path = filedialog.askopenfilename(initialdir=os.getcwd(), title="Select Video",filetypes=(("mp4", "*.mp4"),("avi", "*.avi"),("All Files", "*.*")))
        print(temp_path)
        if temp_path!="":
            video_path_globle=temp_path
            lab.config(text=f"{temp_path}")
    else:
        temp_path=filedialog.askdirectory()
        video_savepath_globle = temp_path
        lab.config(text=f"{temp_path}")
    return 1

def stream_main_control(lab,f1,f2):
    global video_path_globle,video_savepath_globle
    if video_path_globle=="" and video_savepath_globle=="":
        messagebox.showerror("Error","Select Video And Destination . . .")
    else:
            lab.config(text="Prossing : Please Wait")
            messagebox.showinfo("Information", "Framing Start ")
            try:
                print("in---> 1")
                start=int(f1.get())
                endr=int(f2.get())
                finel_s_res = 1800 * start
                finel_e_res =1800 * endr
                video_cap(video_path_globle, finel_s_res, finel_e_res, lab)
            except:
                start=0
                endr=0
                print("xception")
            messagebox.showinfo("Information", "Completed Successfully")
    return 1

def video_cap(video_address,start_mod,end_mod,lab):
    cap = cv2.VideoCapture(f'{video_address}')
    i = 1
    display_fram_num=1
    print("in --> 2 -- ",start_mod," -- ",end_mod )
    if (start_mod == 0) and (end_mod == 0):
        pass
    else:
        print("ffffffffff")
        while (cap.isOpened()):
            ret, frame = cap.read()
            if i>=start_mod and i<=end_mod:
                if ret == True:
                    asd=cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
                    frame_image=Image.fromarray(asd)
                    j=f'{video_savepath_globle}/ {display_fram_num}.jpg'
                    frame_image.save(j)
                    display_fram_num=display_fram_num+1
                    lab.config(text=f"Status : {display_fram_num}")
                    lab.update()
                else:
                   break
            i = i + 1
        cap.release()
    return 1

def save_manual(tw, th, selected_image_path):
    try:
        w = int(tw.get())
        h = int(th.get())
        path = filedialog.askdirectory()
        if path == "":
            pass
        else:
            img = Image.open(selected_image_path)
            imgr = img.resize((w, h))
            imgr.save(f"{path}/resized Image.jpg")
            messagebox.showinfo("Information", "Image Saved Successfully . . .")
    except ValueError:
        messagebox.showerror("Error", "Size must be numbers")

def switch(win, num, selected_image_path=None):
    win.destroy()
    if num == 0:
        obj = front_end()
        obj.menu()
    elif num == 123:
        obj = front_end()
        obj.window_cam()
    else:
        window_main_all = Tk()
        win_seting(window_main_all, 600, 700)
        img_create(window_main_all, "res/br2.jpg", 600, 700, 0, 0)
        default_fun(window_main_all, "res/f1.jpg")
        if num == 5:
            selected_image_path = None 
            def select_image():
                nonlocal selected_image_path
                selected_image_path = filedialog.askopenfilename()
                if selected_image_path:
                    img = Image.open(selected_image_path)
                    img = img.resize((200, 200))
                    img_create(window_main_all, selected_image_path, 300, 410, 65, 85)
            Button(window_main_all, text="B r o w s e", width=40, height=2, bg="white", command=select_image).place(x=73, y=520)
        else:
            Button(window_main_all, text="B r o w s e", width=40, height=2, bg="white",command=lambda: brows_fun(window_main_all)).place(x=73,y=520)
        def switch_fun():
            obj = front_end()
            window_main_all.destroy()
            if int(num) == 1:
                obj.text_enhancement()
            elif int(num) == 2:
                obj.img_enhancement()
            elif int(num) == 3:
                obj.window_icon()
            elif int(num) == 4:
                obj.window_main_pasport()
            elif int(num) == 5:
                obj.win_manual_size(selected_image_path)  
            return 1
        Button(window_main_all, text="N E X T", width=19, height=2, bg="white", command=switch_fun).place(x=73, y=650)
        Button(window_main_all, text="C L E A R", width=19, height=2, bg="white", command=lambda: default_fun(window_main_all, "res/f1.jpg")).place(x=222, y=650)
        Button(window_main_all, text="B a c k", width=10, height=2, bg="white", command=lambda: switch(window_main_all, 0)).place(x=460, y=650)
        window_main_all.mainloop()
    return 1

class front_end:
    def animation(self):
        window_welcome_all = tk.Tk()
        window_welcome_all.title("AK Editors")
        lab = Label(window_welcome_all)
        lab.place(x=0, y=0)
        app_width = 800
        app_height = 500
        win_width = window_welcome_all.winfo_screenwidth() 
        win_height = window_welcome_all.winfo_screenheight()  
        x = (win_width / 2) - (app_width / 2)
        y = (win_height / 2) - (app_height / 2)
        y = y - 40
        window_welcome_all.geometry(f'{app_width}x{app_height}+{int(x)}+{int(y)}')
        window_welcome_all.iconbitmap("res/logoicon.ico")
        frame_number = 175
        gif_label = Label(window_welcome_all) 
        lab = Label(window_welcome_all)
        frame_number = 175
        self.animation_frame(window_welcome_all, frame_number, lab)
        window_welcome_all.mainloop()

    def animation_frame(self, window, frame_number, lab):
        if frame_number == 1000:
            self.win_one(window)
            window.destroy() 
            return
        else:
            print("in", frame_number)
            frame_count = str(frame_number)
            open_frame = Image.open(f'res/animation/a{frame_count}.jpg')
            resize_frame = open_frame.resize((800, 500))
            font = ImageFont.truetype("res/FFF_Tusj.ttf", 80)
            font2 = ImageFont.truetype("res/Antonio-Bold.ttf", 40)
            draw = ImageDraw.Draw(resize_frame)
            draw2 = ImageDraw.Draw(resize_frame)
            text = "A . K   EDITORS"
            text2 = " P   h   o   t   o      F   i   x "
            draw.text((85, 300), text, (0, 200, 255), font=font)
            draw2.text((240, 430), text2, (0, 50, 255), font=font2)
            print("-----------------------")
            frame_tk = ImageTk.PhotoImage(resize_frame)
            lab.configure(image=frame_tk)
            lab.image = frame_tk
            lab.place(x=0, y=0)
            frame_number += 1
            if frame_number == 245:
                frame_number = 1000
                window.after(1000, window.destroy)  
            window.after(30, self.animation_frame, window, frame_number, lab)

    def win_one(self, window):
        window_one = tk.Toplevel(window)
        window_one.title("Window One")
        window_one.geometry("400x300")
        label_one = Label(window_one, text="This is Window One")
        label_one.pack(pady=20)
        button_close = Button(window_one, text="Close Window", command=window_one.destroy)
        button_close.pack()

    def menu(self):
        global center_screen_quardenate_x, center_screen_quardenate_y
        window_main_all=Tk()
        win_seting(window_main_all,620,700)
        img_create(window_main_all,"res/manupic.jpg",620,700,0,0)
        Button(window_main_all, text="Text Enhancing", bg="white", font="Rockwell", width=20,height=3, command=lambda: switch(window_main_all,1)).place(x=50, y=20)
        Button(window_main_all, text="Pasport Size", bg="white", font="Rockwell", width=20, height=3, command=lambda: switch(window_main_all,4)).place(x=330, y=115)
        Button(window_main_all, text="Icon Size", bg="white", font="Rockwell", width=20,  height=3, command=lambda: switch(window_main_all,3)).place(x=50, y=220)
        Button(window_main_all, text="Image Seting", bg="white", font="Rockwell", width=20, height=3, command=lambda: switch(window_main_all,2)).place(x=330, y=320)
        Button(window_main_all, text="Video To Framing", bg="white", font="Rockwell", width=20, height=3,command=lambda: switch(window_main_all,123) ).place(x=50, y=420)
        Button(window_main_all, text="Manual Size Converter", bg="white", font="Rockwell", width=20, height=3, command=lambda: switch(window_main_all,5)).place(x=330, y=520)
        Button(window_main_all, text="Q u i t", bg="white", font="Rockwell", width=59, height=2, command=window_main_all.destroy).place(x=40, y=630)
        window_main_all.mainloop()

    def text_enhancement(self):
        global image_globel
        window_main_all=Tk()
        win_seting(window_main_all,900,700)
        img_create(window_main_all, "res/tf.png", 900, 700, 0, 0)
        img_lab=text_en(window_main_all)

        def direct_call_1():
            filter_text_image_1(img_lab)

        def direct_call_2():
            filter_text_image_2(img_lab)

        def direct_call_3():
            filter_text_image_3(img_lab)

        def direct_call_4():
            filter_text_image_4(img_lab)

        Button(window_main_all, text="Try 1", height=2, width=7, bg="#C77826", fg="white",command=direct_call_1).place(x=95, y=640)
        Button(window_main_all, text="Try 2", height=2, width=7, bg="#C77826", fg="white",  command=direct_call_2).place(x=175, y=640)
        Button(window_main_all, text="Try 3", height=2, width=7, bg="#C77826", fg="white", command=direct_call_3).place(x=255, y=640)
        Button(window_main_all, text="Try 4", height=2, width=7, bg="#C77826", fg="white", command=direct_call_4).place(x=335, y=640)
        Button(window_main_all, text="Reset", height=2, width=10, bg="#E0A15F", fg="white",command=lambda :resetfun(312, 514)).place(x=510, y=640)
        Button(window_main_all, text="S a v e", width=10, height=2, bg="#E0A15F", fg="white",command=save_fun).place(x=610, y=640)
        Button(window_main_all, text="B A C K", width=10, height=2, bg="#E0A15F", fg="white",command=lambda: switch(window_main_all,0)).place(x=740, y=640)
        window_main_all.mainloop()

    def img_enhancement(self):
        global image_filename
        window_main_all=Tk()
        win_seting(window_main_all, 900, 700)
        img_create(window_main_all, "res/f4.jpg", 900, 700, 0, 0)
        frame_noice_win = Frame(window_main_all).place(x=0, y=0)
        Label(frame_noice_win , text="B e f o r e", bg="orange", fg="#0000A0", font="Algerian 20").place(x=171,y=70)
        Label(frame_noice_win , text="A f t e r", bg="orange", fg="#0000A0", font="Algerian 20").place(x=590,y=70)
        img_lab=img_en(frame_noice_win)

        def direct_call_2():
            filter_try_two(img_lab)

        def direct_call_3():
            filter_try_three(img_lab)

        def direct_call_4():
            filter_try_four(img_lab)

        def filter_display_result(filtered_image_catcher):
            global save_object
            save_object = filtered_image_catcher
            image_lable2 = Label(frame_noice_win, relief=SUNKEN)
            image_lable2.configure(image=filtered_image_catcher)
            image_lable2.image = filtered_image_catcher
            image_lable2.place(x=500, y=103)

        def destroy_fun():
            default_fun()
            frame_noice_win.destroy()
        Button(frame_noice_win, text=" Black & White", width=13, height=2, bg="white",command=direct_call_3).place(x=80, y=640)
        Button(frame_noice_win, text="Remove Noice", width=13, height=2, bg="white",command=direct_call_4).place(x=190, y=640)
        Button(frame_noice_win, text="sharp", width=13, height=2, bg="white",command=direct_call_2).place(x=300, y=640)
        Button(frame_noice_win, text="Reset", width=13, height=2, bg="white",command=lambda :resetfun(330, 494)).place(x=490, y=640)
        Button(frame_noice_win, text="Back", width=13, height=2, bg="white",command=lambda: switch(window_main_all,0)).place(x=740, y=640)
        Button(frame_noice_win, text="S a v e", width=13, height=2, bg="white",command=save_fun).place(x=610, y=640)
        window_main_all.mainloop()

    def window_icon(self):
            global image_filename
            window_main_all = Tk()
            win_seting(window_main_all, 500, 600)
            img_create(window_main_all, "res/iconback.jpeg", 500, 600, 0, 0)
            img_create(window_main_all, "res/f5.jpg", 106, 106, 55, 195)
            img_create(window_main_all, "res/f5.jpg", 58, 58, 195, 345)
            img_create(window_main_all, "res/f5.jpg", 22, 22, 306, 427)
            icon_set(window_main_all)
            Label(window_main_all, text="Large", bg="white", fg="#0000A0",font="Algerian 17").place(x=70, y=160)
            Label(window_main_all, text="Med", bg="white", fg="#0000A0", font="Algerian 13").place(x=210, y=320)
            Label(window_main_all, text="S", bg="white", fg="#0000A0",font="Algerian 10").place(x=315, y=405)
            Button(window_main_all, text="Back ", bg="White",command=lambda: switch(window_main_all,0)).place(x=415, y=540)
            window_main_all.mainloop()
            return 1

    def window_main_pasport(self):
        global image_filename
        window_main_all = Tk()
        win_seting(window_main_all, 600, 700)
        img_create(window_main_all, "res/iconback.jpeg", 600, 700, 0, 0)
        pasport_set(window_main_all)
        text_lable_win_three1 = Label(window_main_all, text="Passport Size", bg="white", fg="#0000A0",font="Algerian 17")
        text_lable_win_three1.place(x=300, y=100, anchor=CENTER)
        button2_winthree = Button(window_main_all, text="S a v e ", bg="White", width=10,command=lambda: save_fun_img_set(1))
        button2_winthree.place(x=300, y=610, anchor=CENTER) 
        button4_winthree = Button(window_main_all, text="Back", bg="White", width=5,command=lambda: switch(window_main_all, 0))
        button4_winthree.place(x=300, y=650, anchor=CENTER) 
        window_main_all.mainloop()

    def window_cam(self):
        global window_main_all_cap,video_path_globle,video_savepath_globle
        window_main_all_cap = Tk()
        win_seting(window_main_all_cap, 700, 600)
        img_create(window_main_all_cap, "res/iconback.jpeg", 700, 600, 0, 0)
        field_1 = Entry(window_main_all_cap, width=5)
        field_1.insert(0, "0")
        field_1.place(x=130, y=225)
        field_2 = Entry(window_main_all_cap, width=5)
        field_2.insert(0, "0")
        field_2.place(x=130, y=255)
        Path_text_lable = Label(window_main_all_cap, text=f'Select . . . ',fg="blue", bg="#E0F7CC", font="Forte 15")
        Path_text_lable.place(x=40, y=100)
        Path_text_lable2 = Label(window_main_all_cap, text=f'Select . . . ',fg="blue", bg="#E0F7CC", font="Forte 15")
        Path_text_lable2.place(x=40, y=330)
        show_lab = Label(window_main_all_cap, text="Status", fg="blue", bg="#E0F7CC",font=("Constantia", 15, "bold"))
        show_lab.place(x=100, y=470)
        Label(window_main_all_cap, text="Enter Mniuts From Framing Starts", bg="#E0F7CC", fg="blue",font=("Constantia", 10, "bold")).place(x=165, y=225)
        Label(window_main_all_cap, text="Enter Mniuts where Fraims End", bg="#E0F7CC", fg="blue",font=("Constantia", 10, "bold")).place(x=165, y=255)
        Button(window_main_all_cap, text="Brows", bg="#E0F7CC",font="Algerian 15", command=lambda :video_brows(Path_text_lable,1)).place(x=240, y=150)
        Button(window_main_all_cap, text="Brows", bg="#E0F7CC",font="Algerian 15", command=lambda :video_brows(Path_text_lable2,2)).place(x=240, y=385)
        Button(window_main_all_cap, text="Start Framing", bg="#E0F7CC",font="Algerian 15", command=lambda :stream_main_control(show_lab,field_1,field_2)).place(x=190, y=530)
        button_video_frames = Button(window_main_all_cap, text="B a c k", bg="#E0F7CC",font="Algerian 15", command=lambda :switch(window_main_all_cap,0)).place(x=490, y=530)
        return 1
    
    def win_manual_size(self, selected_image_path=None):
        global image_filename  
        win_manual = Tk()
        win_seting(win_manual, 800, 600)
        img_create(win_manual, "res/manualbackpick.jpeg", 1000, 600, 0, 0)
        Label(win_manual, text="Manual Size Converter", font=("Arial", 20)).place(x=330, y=32)
        Button(win_manual, text="S A V E", width=50, height=4, command=lambda: save_manual(entery_lable, entery_lable2, selected_image_path)).place(x=300, y=400)
        Button(win_manual, text="B A C K", width=70, height=4, command=lambda: switch(win_manual, 0)).place(x=240, y=490)
        entery_lable = Entry(win_manual, width=8)
        entery_lable.insert(0, "200")
        entery_lable.place(x=5, y=67)
        Label(win_manual, text="x").place(x=69, y=67)
        entery_lable2 = Entry(win_manual, width=8)
        entery_lable2.insert(0, "200")
        entery_lable2.place(x=90, y=67)
        frame = Frame(win_manual, width=400, height=200)
        frame.place(x=360, y=150)
        canvas = Canvas(frame, width=200, height=200)
        canvas.pack(fill="both", expand=True)
        print("Selected Image Path:", selected_image_path) 
        if selected_image_path:
            try:
                print("Trying to load image...")  
                img = Image.open(selected_image_path)
                print("Image Loaded Successfully") 
                img = img.resize((200, 200)) 
                img = ImageTk.PhotoImage(img)
                canvas.create_image(0, 0, anchor="nw", image=img)
            except Exception as e:
                print("Error loading image:", e)  
        win_manual.bind("<Button-1>", lambda event: location(event))
        win_manual.mainloop() 

if __name__ == "__main__":       
    obj = front_end()
    obj.animation() 
    obj.menu()



