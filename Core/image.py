#!/usr/bin/env python
#-*-coding:utf-8-*-
#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:     study
# Author:      zhx
# Created:     29/03/2014
# Copyright:   (c) zhx 2014
# Licence:     <>
#-------------------------------------------------------------------------------
#--------------------识别python版本，并导入模块---------------------------------
try:
    from Tkinter import *
    #因为倒入顺序的问题，Image会报错，因为Tkinter里也有Image这个类，但功能不好，所以再导入覆盖就好了
    from PIL import Image,ImageEnhance,ImageFilter,ImageTk
    import tkMessageBox as tkmesbox
    from tkFont import Font
    from ttk import *
    import tkFileDialog
    import os
except ImportError:
    from tkinter import *
    from PIL import Image,ImageEnhance,ImageFilter,ImageTk
    from tkinter.font import Font
    from tkinter.ttk import *
    import tkinter.messagebox as tkmesbox
    import tkinter.filedialog as tkFileDialog
    import tkinter.simpledialog as tkSimpleDialog    #askstring()
    import os


################################################################################
# 弹出对话框
################################################################################
class PopupDialog(Toplevel):

    def __init__(self, parent, callback):
        '''构造函数

        Keyword arguments:
        parent -- 父窗口
        callback -- 回调函数，当点击确定按钮时，会调用这个函数进行相应的图像调节
        '''
        Toplevel.__init__(self, parent)

        self.parent = parent
        self.callback = callback
        
        self.grab_set()
        self.title('请输入数值')

        self.spinbox = Spinbox(self, from_ = 0, to_ = 10, increment = 0.1)
        self.spinbox.grid(row = 0, column = 0)
      
        self.spinbox.delete(0, 'end')
        self.spinbox.insert(0, 1.0)

      
        self.bind('<Return>', lambda x : self.ok())

        self.button = Button(self, text="确定", command=self.ok)
        self.button.grid(row = 0, column = 1)

        self.center()


    def center(self):
        '''居中显示弹出对话框
        '''
        # 获取父窗口的大小以及位置
        parent_geo = self.parent.geometry()
        parent_size, parent_x, parent_y = parent_geo.split('+')
        parent_w, parent_h = [int(i) for i in parent_size.split('x')]
        parent_x, parent_y = int(parent_x), int(parent_y)

        # 计算调节弹出窗口的位置
        w, h = 245, 30
        x = parent_x + (parent_w - w) / 2
        y = parent_y + (parent_h - h) / 2
        self.geometry('%dx%d+%d+%d' % (w, h, x, y))


    def ok(self):
        '''获取值，如果输入的值合法，那么根据值进行图像调节，
        调节完成自动关闭弹出对话框
        '''
        try:
            value = float(self.spinbox.get())
            self.callback(value)
            self.destroy()
        except ValueError as e:
            pass
# END

#-----------------------------功能函数------------------------------------------
class mini_ps_fuc:
    def __init__(self):
        #使用缺省图片，省去了调用前的判断或异常处理
        self.img = Image.open('test.jpg')
        self.img_name = "test.jpg"
    #旋转功能
    def xuanzhuan1_cmd(self):
        #旋转45度
        self.img = self.img.rotate(45)
        self.photo_display()
    def xuanzhuan2_cmd(self):
        #旋转90度
        self.img = self.img.transpose(Image.ROTATE_90)
        self.photo_display()
    def xuanzhuan3_cmd(self):
        #旋转180度
        self.img = self.img.transpose(Image.ROTATE_180)
        self.photo_display()
    def duihuan1_cmd(self):
        #图片上下对换
        self.img = self.img.transpose(Image.FLIP_TOP_BOTTOM)
        self.photo_display()
    def duihuan2_cmd(self):
        #图片左右对换
        self.img = self.img.transpose(Image.FLIP_LEFT_RIGHT)
        self.photo_display()

################################################################################
# 增强
################################################################################
    #图像增强
    def zengqiang1_cmd(self):
        #亮度增强
        def zengqiang1(value):
            '''根据value值进行亮度调节
            
           
            '''
            brightness = ImageEnhance.Brightness(self.img)
            self.img = brightness.enhance(value)
            self.photo_display()

        # 将zengqiang1函数传入，当点击确定按钮时会调用这个函数进行调节
        PopupDialog(window, zengqiang1)

    def zengqiang2_cmd(self):
        #图像锐化
        def zengqiang2(value):
            '''根据value值进行图像锐化调节

           
            '''
            sharpness = ImageEnhance.Sharpness(self.img)
            self.img = sharpness.enhance(value)
            self.photo_display()

        PopupDialog(window, zengqiang2)

    def zengqiang3_cmd(self):
        #对比增强
        def zengqiang3(value):
      
            contrast = ImageEnhance.Contrast(self.img)
            self.img = contrast.enhance(value)
            self.photo_display()

        PopupDialog(window, zengqiang3)

    def zengqiang4_cmd(self):
        #色彩增强
        def zengqiang4(value):
      
            enhancer = ImageEnhance.Color(self.img)
            self.img = enhancer.enhance(value)
            self.photo_display()

        PopupDialog(window, zengqiang4)
# END

    def zengqiang5_cmd(self):
        #边缘增强
        self.img = self.img.filter(ImageFilter.EDGE_ENHANCE_MORE)
        self.photo_display()
    #艺术效果
    def yishu1_cmd(self):
        #素雅效果
        self.img = ImageEnhance.Color(self.img)
        self.img = self.img.enhance(0.5)
        self.img = self.img.filter(ImageFilter. SMOOTH_MORE)
        self.photo_display()
    def yishu2_cmd(self):
        #浮雕效果
        self.img = self.img.filter(ImageFilter.EMBOSS)
        self.photo_display()
    def yishu3_cmd(self):
        #铅笔画效果
        self.img = self.img.filter(ImageFilter.CONTOUR)
        self.photo_display()
    def yishu4_cmd(self):
        #底片效果
        self.img = self.img.filter(ImageFilter. FIND_EDGES)
        self.photo_display()
    def yishu5_cmd(self):
        #黑白效果
        self.img = self.img.convert('L')
        self.photo_display()
    def yishu6_cmd(self):
        #模糊效果
        self.img = self.img.filter(ImageFilter.BLUR)
        self.photo_display()
    #文件操作
    def ps_open(self):
        #打开图片
        self.img_path = tkFileDialog.askopenfilename()
        if self.img_path:
            try :
                self.img = Image.open(self.img_path)
                self.img_name = os.path.basename(self.img_path)
                self.img_display = ImageTk.PhotoImage(self.img)
                self.photo_display()
            except IOError :
                tkmesbox.showerror(u'错误',u"这不是一个规范的图像文件")
    def ps_save(self):
        #图片保存
        self.img.save(self.img_name,option={'progression':True,'quality':60,'optimize':True})
    def ps_save_other(self):
        #图片另存为
        pass
    def ps_close(self):
        #关闭图片
        baocun_return = tkmesbox.askyesnocancel(title=u'mini ps',message=u'图像经过修改，是否保存')
        if baocun_return == True:
            self.ps_save()
            self.img = Image.open('test.jpg')
            self.photo_display()
        elif baocun_return ==False:
            self.img = Image.open('test.jpg')
            self.photo_display()
        else :
            pass
    #注意关闭前提示保存
    def ps_tuichu(self):
        #退出窗体
        tuichu_return = tkmesbox.askyesnocancel(title=u'mini ps',message=u'图像经过修改，是否保存')
        if tuichu_return == True:
            self.ps_save()
            window.destroy()
        elif tuichu_return == False:
            window.destroy()
        else :
            pass
    def photo_display(self):
        #显示图片
        self.img_display = ImageTk.PhotoImage(self.img)
        if self.img.size[0] > 350:
            window.geometry(str(self.img.size[0])+'x'+str(self.img.size[1]))
        else :
            window.geometry(str(350)+'x'+str(self.img.size[1]))
        lab['image'] = self.img_display
#-----------------------------事件函数------------------------------------------
def button3_menu_display(event):
    button3_menu.post(event.x_root,event.y_root)

#-----------------------------异常处理------------------------------------------
class ps_bug:
    pass
#-----------------------------窗口形成------------------------------------------
def mini_ps_ui():
    global lab,window,button3_menu
    window = Tk()
    fuc = mini_ps_fuc()
    #初始化窗体
    #print fuc.img.size
    chushidaxiao = str(fuc.img.size[0])+'x'+str(fuc.img.size[1])
    window.geometry(chushidaxiao)
    #菜单
    menubar = Menu(window)
#----------------------------生成文件菜单---------------------------------------
    filemenu = Menu(menubar, tearoff=0)
    filemenu.add_command(label = u'打开',command = fuc.ps_open)
    filemenu.add_command(label = u'保存',command = fuc.ps_save)
    filemenu.add_command(label = u'另存为',command = fuc.ps_save_other)
    filemenu.add_command(label = u'关闭',command = fuc.ps_close)
    filemenu.add_separator()
    filemenu.add_command(label = u'退出',command = fuc.ps_tuichu)
    menubar.add_cascade(label = u"文件", menu = filemenu)
#-----------------------------函数字典--------------------------------------------
    com_xuanzhuan_name_list = [u'旋转45度',u'旋转90度',u'旋转180度']
    com_xuanzhuan_value_list = [fuc.xuanzhuan1_cmd,fuc.xuanzhuan2_cmd,fuc.xuanzhuan3_cmd]
    com_duihuan_name_list = [u'上下对换',u'左右对换']
    com_duihuan_value_list = [fuc.duihuan1_cmd,fuc.duihuan2_cmd]
    com_zengqiang_name_list = [u'亮度增强',u'图像锐化',u'对比增强',u'色彩增强',u'边缘增强']
    com_zengqiang_value_list = [fuc.zengqiang1_cmd,fuc.zengqiang2_cmd,fuc.zengqiang3_cmd,fuc.zengqiang4_cmd,fuc.zengqiang5_cmd]
    com_yishu_name_list = [u'素雅效果',u'浮雕效果',u'铅笔画效果',u'底片效果',u'黑白效果',u'模糊效果']
    com_yishu_value_list = [fuc.yishu1_cmd,fuc.yishu2_cmd,fuc.yishu3_cmd,fuc.yishu4_cmd,fuc.yishu5_cmd,fuc.yishu6_cmd]
    names1 = [zip(com_xuanzhuan_name_list,com_xuanzhuan_value_list ),zip(com_duihuan_name_list,com_duihuan_value_list),zip(com_zengqiang_name_list,com_zengqiang_value_list),zip(com_yishu_name_list,com_yishu_value_list)]
    names2 = [u'旋转',u'对换',u'增强',u'艺术效果']
#------------------------------功能菜单-----------------------------------------
    psmenu = Menu(window)
    ps_menus = []
    for i in range(0,4,1):
        ps_menu = Menu(psmenu,tearoff=0)
        ps_menus.append(ps_menu)
        for biao,ming in names1[i]:
            ps_menus[i].add_command(label=biao,command=ming)
        menubar.add_cascade(label=names2[i],menu=ps_menus[i])
    window.config(menu=menubar)
#-------------------------------------------------------------------------------
#右键菜单
    button3_menu = Menu(window,tearoff=0)
    button3_menu.add_command(label = u'打开',command = fuc.ps_open)
    button3_menu.add_command(label = u'保存',command = fuc.ps_save)
    button3_menu.add_command(label = u'另存为',command = fuc.ps_save_other)
    window.bind("<Button-3>",button3_menu_display)
#--------------------------用label输出图片--------------------------------------
    lab = Label(window,justify = CENTER)
    fuc.photo_display()
    lab.pack(expand=1,fill=BOTH,anchor = CENTER)
    window.mainloop()
#-------------------------------调用--------------------------------------------
if __name__ == '__main__':
    mini_ps_ui()
#command_xuanzhuan_dict={u'旋转45度' : fuc.xuanzhuan1_cmd,u'旋转90度':fuc.xuanzhuan2_cmd,u'旋转180度':fuc.xuanzhuan3_cmd,u'旋转':None}
#command_duihuan_dict = {u'上下对换' : fuc.duihuan1_cmd,u'左右对换':fuc.duihuan2_cmd,u'对换':None}
#command_zengqiang_dict = {u'亮度增强' : fuc.zengqiang1_cmd,u'图像锐化':fuc.zengqiang1_cmd,u'对比增强':fuc.zengqiang2_cmd,u'色彩增强':fuc.zengqiang3_cmd,u'边缘增强':fuc.zengqiang4_cmd,u'增强':None}
#command_yishu_dict = {u'素雅效果' : fuc.yishu1_cmd,u'浮雕效果':fuc.yishu2_cmd,u'铅笔画效果':fuc.yishu3_cmd,u'底片效果':fuc.yishu4_cmd,u'黑白效果':fuc.yishu5_cmd,u'模糊效果':fuc.yishu6_cmd,u'艺术':None}'''
