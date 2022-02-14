from tkinter import *
from tkinter import messagebox
import webbrowser
#load vô link 
def toan():
	with open('myfile1.txt', 'r' ,encoding='UTF-8') as f:
	    datalist = f.readlines() 
	    line2 = datalist[3]
	url=line2
	runprf = webbrowser.open_new_tab(url)
def li():
	with open('myfile1.txt', 'r' ,encoding='UTF-8') as f:
	    datalist = f.readlines() 
	    line2 = datalist[6]
	url=line2
	runprf = webbrowser.open_new_tab(url)
def anh():
	with open('myfile1.txt', 'r' ,encoding='UTF-8') as f:
	    datalist = f.readlines() 
	    line2 = datalist[9]
	url=line2
	runprf = webbrowser.open_new_tab(url)
def tin():
	with open('myfile1.txt', 'r' ,encoding='UTF-8') as f:
	    datalist = f.readlines() 
	    line2 = datalist[12]
	url=line2
	runprf = webbrowser.open_new_tab(url)
def hoa():
	with open('myfile1.txt', 'r' ,encoding='UTF-8') as f:
	    datalist = f.readlines() 
	    line2 = datalist[15]
	url=line2
	runprf = webbrowser.open_new_tab(url)
def sinh():
	with open('myfile1.txt', 'r' ,encoding='UTF-8') as f:
	    datalist = f.readlines() 
	    line2 = datalist[18]
	url=line2
	runprf = webbrowser.open_new_tab(url)
def dia():
	with open('myfile1.txt', 'r' ,encoding='UTF-8') as f:
	    datalist = f.readlines() 
	    line2 = datalist[21]
	url=line2
	runprf = webbrowser.open_new_tab(url)
def su():
	with open('myfile1.txt', 'r' ,encoding='UTF-8') as f:
	    datalist = f.readlines() 
	    line2 = datalist[24]
	url=line2
	runprf = webbrowser.open_new_tab(url)
def gdcd():
	with open('myfile1.txt', 'r' ,encoding='UTF-8') as f:
	    datalist = f.readlines() 
	    line2 = datalist[27]
	url=line2
	runprf = webbrowser.open_new_tab(url)
def cn():
	with open('myfile1.txt', 'r' ,encoding='UTF-8') as f:
	    datalist = f.readlines() 
	    line2 = datalist[30]
	url=line2
	runprf = webbrowser.open_new_tab(url)
def van():
	with open('myfile1.txt', 'r' ,encoding='UTF-8') as f:
	    datalist = f.readlines() 
	    line2 = datalist[33]
	url=line2
	runprf = webbrowser.open_new_tab(url)
def error():
	url="https://www.facebook.com/PCTPC57/"
	runprf = webbrowser.open_new_tab(url)
def out():
	messagebox.showinfo("thông báo","bấm x để thoát")
#môn học 
def lh_click():
	top = Toplevel(nice)  
	top.title("toán")
	top.geometry("400x300")
	with open('myfile1.txt', 'r' ,encoding='UTF-8') as f:
	    datalist = f.readlines() 
	    line2 = datalist[3]
	lb3= Label(top, text="bạn có chắc chắn muốn vào link này:",font=("Time New Roman",16, ),fg='green')
	lb3.pack()
	lb2= Label(top,text=line2,font=(15),fg='red')
	lb2.pack()
	om=Button(top , text="Yes",font=("consolas",14,"bold"),width=10,height=1,command=toan)
	om.place(x=100, y=70)
	gg=Button(top , text="No",font=("consolas",14,"bold"),width=10,height=1,command=out)
	gg.place(x=200, y=70)
	f.close()
	top.mainloop() 
def lj_click():
	top = Toplevel(nice)
	top.title("lí")
	top.geometry("400x300")
	with open('myfile1.txt', 'r' ,encoding='UTF-8') as f:
	    datalist = f.readlines() 
	    line2 = datalist[6]
	lb3= Label(top, text="bạn có chắc chắn muốn vào link này:",font=("Time New Roman",16, ),fg='green')
	lb3.pack()
	lb2= Label(top,text=line2,font=(15),fg='red')
	lb2.pack()
	om=Button(top , text="Yes",font=("consolas",14,"bold"),width=10,height=1,command=li)
	om.place(x=100, y=70)
	gg=Button(top , text="No",font=("consolas",14,"bold"),width=10,height=1,command=out)
	gg.place(x=200, y=70)
	f.close()
	top.mainloop()
def lk_click():
	top = Toplevel(nice)
	top.geometry("400x300")
	top.title("anh")
	with open('myfile1.txt', 'r' ,encoding='UTF-8') as f:
	    datalist = f.readlines() 
	    line2 = datalist[9]
	lb3= Label(top, text="bạn có chắc chắn muốn vào link này:",font=("Time New Roman",16, ),fg='green')
	lb3.pack()
	lb2= Label(top,text=line2,font=(15),fg='red')
	lb2.pack()
	om=Button(top , text="Yes",font=("consolas",14,"bold"),width=10,height=1,command=anh)
	om.place(x=100, y=70)
	gg=Button(top , text="No",font=("consolas",14,"bold"),width=10,height=1,command=out)
	gg.place(x=200, y=70)
	f.close()
	top.mainloop()
def ll_click():
	top = Toplevel(nice) 
	top.geometry("400x300") 
	top.title("tin")
	with open('myfile1.txt', 'r' ,encoding='UTF-8') as f:
	    datalist = f.readlines() 
	    line2 = datalist[12]
	lb3= Label(top, text="bạn có chắc chắn muốn vào link này:",font=("Time New Roman",16, ),fg='green')
	lb3.pack()
	lb2= Label(top,text=line2,font=(15),fg='red')
	lb2.pack()
	om=Button(top , text="Yes",font=("consolas",14,"bold"),width=10,height=1,command=tin)
	om.place(x=100, y=70)
	gg=Button(top , text="No",font=("consolas",14,"bold"),width=10,height=1,command=out)
	gg.place(x=200, y=70)
	f.close()
	top.mainloop()
def lz_click():
	top = Toplevel(nice)  
	top.geometry("400x300")
	top.title("hoa")
	with open('myfile1.txt', 'r' ,encoding='UTF-8') as f:
	    datalist = f.readlines() 
	    line2 = datalist[15]
	lb3= Label(top, text="bạn có chắc chắn muốn vào link này:",font=("Time New Roman",16, ),fg='green')
	lb3.pack()
	lb2= Label(top,text=line2,font=(15),fg='red')
	lb2.pack()
	om=Button(top , text="Yes",font=("consolas",14,"bold"),width=10,height=1,command=hoa)
	om.place(x=100, y=70)
	gg=Button(top , text="No",font=("consolas",14,"bold"),width=10,height=1,command=out)
	gg.place(x=200, y=70)
	f.close()
	top.mainloop()
def lx_click():
	top = Toplevel(nice)  
	top.geometry("400x300")
	top.title("sinh")
	with open('myfile1.txt', 'r' ,encoding='UTF-8') as f:
	    datalist = f.readlines() 
	    line2 = datalist[18]
	lb3= Label(top, text="bạn có chắc chắn muốn vào link này:",font=("Time New Roman",16, ),fg='green')
	lb3.pack()
	lb2= Label(top,text=line2,font=(15),fg='red')
	lb2.pack()
	om=Button(top , text="Yes",font=("consolas",14,"bold"),width=10,height=1,command=sinh)
	om.place(x=100, y=70)
	gg=Button(top , text="No",font=("consolas",14,"bold"),width=10,height=1,command=out)
	gg.place(x=200, y=70)
	f.close()
	top.mainloop()
#dãy 2
def qr_click():
	top = Toplevel(nice)
	top.geometry("400x300")  
	top.title("GDCD")
	with open('myfile1.txt', 'r' ,encoding='UTF-8') as f:
	    datalist = f.readlines() 
	    line2 = datalist[21]
	lb3= Label(top, text="bạn có chắc chắn muốn vào link này:",font=("Time New Roman",16, ),fg='green')
	lb3.pack()
	lb2= Label(top,text=line2,font=(15),fg='red')
	lb2.pack()
	om=Button(top , text="Yes",font=("consolas",14,"bold"),width=10,height=1,command=gdcd)
	om.place(x=100, y=70)
	gg=Button(top , text="No",font=("consolas",14,"bold"),width=10,height=1,command=out)
	gg.place(x=200, y=70)
	f.close()
	top.mainloop()
def qw_click():
	top = Toplevel(nice) 
	top.geometry("400x300") 
	top.title("sử")
	with open('myfile1.txt', 'r' ,encoding='UTF-8') as f:
	    datalist = f.readlines() 
	    line2 = datalist[24]
	lb3= Label(top, text="bạn có chắc chắn muốn vào link này:",font=("Time New Roman",16, ),fg='green')
	lb3.pack()
	lb2= Label(top,text=line2,font=(15),fg='red')
	lb2.pack()
	om=Button(top , text="Yes",font=("consolas",14,"bold"),width=10,height=1,command=su)
	om.place(x=100, y=70)
	gg=Button(top , text="No",font=("consolas",14,"bold"),width=10,height=1,command=out)
	gg.place(x=200, y=70)
	f.close()
	top.mainloop()
def uj_click():
	top = Toplevel(nice)  
	top.geometry("400x300")
	top.title("van")
	with open('myfile1.txt', 'r' ,encoding='UTF-8') as f:
	    datalist = f.readlines() 
	    line2 = datalist[27]
	lb3= Label(top, text="bạn có chắc chắn muốn vào link này:",font=("Time New Roman",16, ),fg='green')
	lb3.pack()
	lb2= Label(top,text=line2,font=(15),fg='red')
	lb2.pack()
	om=Button(top , text="Yes",font=("consolas",14,"bold"),width=10,height=1,command=van)
	om.place(x=100, y=70)
	gg=Button(top , text="No",font=("consolas",14,"bold"),width=10,height=1,command=out)
	gg.place(x=200, y=70)
	f.close()
	top.mainloop()
def lo_click():
	top = Toplevel(nice)  
	top.geometry("400x300")
	top.title("Công nghệ")
	with open('myfile1.txt', 'r' ,encoding='UTF-8') as f:
	    datalist = f.readlines() 
	    line2 = datalist[30]
	lb3= Label(top, text="bạn có chắc chắn muốn vào link này:",font=("Time New Roman",16, ),fg='green')
	lb3.pack()
	lb2= Label(top,text=line2,font=(15),fg='red')
	lb2.pack()
	om=Button(top , text="Yes",font=("consolas",14,"bold"),width=10,height=1,command=cn)
	om.place(x=100, y=70)
	gg=Button(top , text="No",font=("consolas",14,"bold"),width=10,height=1,command=out)
	gg.place(x=200, y=70)
	f.close()
	top.mainloop()
def cc_click():
	top = Toplevel(nice)  
	top.geometry("400x300")
	top.title("Địa")
	with open('myfile1.txt', 'r' ,encoding='UTF-8') as f:
	    datalist = f.readlines() 
	    line2 = datalist[33]
	lb3= Label(top, text="bạn có chắc chắn muốn vào link này:",font=("Time New Roman",16, ),fg='green')
	lb3.pack()
	lb2= Label(top,text=line2,font=(15),fg='red')
	lb2.pack()
	om=Button(top , text="Yes",font=("consolas",14,"bold"),width=10,height=1,command=dia)
	om.place(x=100, y=70)
	gg=Button(top , text="No",font=("consolas",14,"bold"),width=10,height=1,command=out)
	gg.place(x=200, y=70)
	f.close()
	top.mainloop()
def ed_click():
	top = Toplevel(nice) 
	top.geometry("400x300")
	top.title("Báo lỗi")
	with open('myfile1.txt', 'r' ,encoding='UTF-8') as f:
	    datalist = f.readlines() 
	    line2 = datalist[36]
	lb3= Label(top, text="bạn có chắc chắn muốn vào link này:",font=("Time New Roman",16, ),fg='green')
	lb3.pack()
	lb2= Label(top,text=line2,font=(15),fg='red')
	lb2.pack()
	om=Button(top , text="Yes",font=("consolas",14,"bold"),width=10,height=1,command=error)
	om.place(x=100, y=70)
	gg=Button(top , text="No",font=("consolas",14,"bold"),width=10,height=1,command=out)
	gg.place(x=200, y=70)	
	f.close()
	top.mainloop()
def ex_click():
	messagebox.showerror("Thông báo","Bấm ok để thoát")
	nice.destroy()

#biến tạo bảng chọn
with open('myfile1.txt', 'r' ,encoding='UTF-8') as f:
	datalist = f.readlines() 
	line2 = datalist[14]
nice=Tk()
nice.title("link học online")
lbName= Label(nice,text=line2,font=("Time New Roman",14),fg="green")
lbName.pack()
nice.geometry("275x400")
menu = Menu(nice)
new_item = Menu(menu)
new_item.add_command(label='Exit',command=ex_click)
menu.add_cascade(label='File', menu=new_item)
nice.config(menu=menu)

#tạo các button
lh=Button(nice , text="Toán",font=("consolas",14,"bold"),width=10,height=1,command=lh_click)
lh.place(x=5, y=70)
lj=Button(nice , text="Lí",font=("consolas",14,"bold"),width=10,height=1,command=lj_click)
lj.place(x=5, y=110)
lk=Button(nice , text="Anh",font=("consolas",14,"bold"),width=10,height=1,command=lk_click)
lk.place(x=5, y=150)
ll=Button(nice , text="Tin",font=("consolas",14,"bold"),width=10,height=1,command=ll_click)
ll.place(x=5, y=190)
lz=Button(nice , text="Hóa",font=("consolas",14,"bold"),width=10,height=1,command=lz_click)
lz.place(x=5, y=230)
lx=Button(nice , text="Sinh",font=("consolas",14,"bold"),width=10,height=1,command=lx_click)
lx.place(x=5, y=270)


qr=Button(nice , text="GDCD",font=("consolas",14,"bold"),width=10,height=1,command=qr_click)
qr.place(x=150, y=70)
qw=Button(nice , text="Sử",font=("consolas",14,"bold"),width=10,height=1,command=qw_click)
qw.place(x=150, y=110)
uj=Button(nice , text="Văn",font=("consolas",14,"bold"),width=10,height=1,command=uj_click)
uj.place(x=150, y=150)
lo=Button(nice , text="Công Nghệ",font=("consolas",14,"bold"),width=10,height=1,command=lo_click)
lo.place(x=150, y=190)
cc=Button(nice , text="Địa",font=("consolas",14,"bold"),width=10,height=1,command=cc_click)
cc.place(x=150, y=230)
ed=Button(nice , text="Báo lỗi",font=("consolas",14,"bold"),width=10,height=1,command=ed_click)
ed.place(x=150, y=270)
lbname2=Label(nice,text="2022-©-Nguyễn Hoàng Phúc",font=("Time New Roman",14),fg="blue")
lbname2.place(x=25,y=350)
nice.mainloop()
