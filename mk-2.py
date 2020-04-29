#STATEWISE GRAPHICAL REPRESENTATION OF THE COVID-19 effected people

import numpy as np
import pandas as pd
import json
import requests
import matplotlib.pyplot as plt
import plotly.express as px
import plotly.graph_objects as go
from tkinter import *
import webbrowser


root = Tk()
root.title("COVID-19 Alert!")
url = 'https://api.covid19india.org/data.json'

#data in json format
jsn = requests.get(url).json()
#extract statewise informations in a list
statewise = jsn['statewise']
#created a dataframe of the list
df = pd.DataFrame(statewise)
df = df.drop(df.index[0])
#change the values to int
df['active'] = df['active'].apply(lambda x : int(x))
df['deaths'] = df['deaths'].apply(lambda x : int(x))
df['confirmed'] = df['confirmed'].apply(lambda x : int(x))
df['recovered'] = df['recovered'].apply(lambda x : int(x))
def graph():
    
    fig = px.treemap(df, path=['state', 'confirmed', 'active' , 'recovered'], values='active',
                      color='active', hover_data=['confirmed' , 'recovered'],
                      color_continuous_scale='RdBu',
                      color_continuous_midpoint=np.average(df['confirmed'], weights=df['active']),
                      title = 'Statewise Cases',
                        )
    fig.show()

def bar_graph():
  states =df['state']
  fig = go.Figure(data=[
      go.Bar(name='confirmed', x=states, y=df['confirmed']),
      go.Bar(name='active', x=states, y=df['active']),
      go.Bar(name='recovered', x=states, y=df['recovered'])
  ])
  # Change the bar mode
  fig.update_layout(barmode='group')
  fig.show()

#---------------------------------------FUN-----------------------------------------------------------------------------------------------------------------
def Home():
	frame1.grid_forget()
	#--------------------------------------FRAME-9-----------------------------------------------------------------------------------------------------------------------
	frame9 = LabelFrame(root, padx=5, pady=5, bg="#323232")
	frame9.grid(row=0, column=0)
	#---------------------------------------------------------------
	#--------------------------START-------------------------------------
	#---------------------------------------------------------------
	#--------------------------TITLE-------------------------------------
	f9label1 = Label(frame9, text="\n\nStay Home, Stay Safe!\n\n", font=("Arial Bold", 15), bg="#323232", fg="#ff971d")
	f9label1.grid(row=0, column=1, columnspan=3)
	#---------------------------------------------------------------
	#---------------------------Button1-------------------------------------
	#----------------------------------------------------------------
	f9label2 = Label(frame9, text="", bg="#323232")
	f9label2.grid(row=2, column=1)
	#---------------------------Button2-------------------------------------
	#----------------------------------------------------------------
	f9label3 = Label(frame9, text="", bg="#323232")
	f9label3.grid(row=4, column=1)
	#---------------------------Button3------------------------------------
	#----------------------------------------------------------------
	f9label4 = Label(frame9, text="", bg="#323232")
	f9label4.grid(row=6, column=1)
	#---------------------------Button4------------------------------------
	#----------------------------------------------------------------
	f9label5 = Label(frame9, text="", bg="#323232")
	f9label5.grid(row=8, column=1)
	#---------------------------Button5------------------------------------
	#----------------------------------------------------------------
	f9label6 = Label(frame9, text="\n\n\n", bg="#323232")
	f9label6.grid(row=10, column=1)
	#---------------------------Exit-Button------------------------------------
	#----------------------------------------------------------------
	f9label7 = Label(frame9, text="\n\n", bg="#323232")
	f9label7.grid(row=12, column=1)
	#-----------------------------END-----------------------------------

	#------------------------------Column-Space---------------------------------
	f9label8 = Label(frame9, text="", bg="#323232")
	f9label8.grid(row=0, column=0)
	f9label9 = Label(frame9, text="", bg="#323232")
	f9label9.grid(row=0, column=4)
	#----------------------------------------------------------------

	#*****************************BUTTONS**********************************************************************************************************************************
	f9button1 = Button(frame9, text="Home", command=Home, padx=54, pady=5, fg="#363636", bg="#ff971d", state=DISABLED, activeforeground="#ff971d", activebackground="#323232")
	f9button2 = Button(frame9, text="Symptoms", command=Symptoms, padx=39, pady=5, fg="#363636", bg="#ff971d", activeforeground="#ff971d", activebackground="#323232")
	f9button3 = Button(frame9, text="Prevention", command=Prevention, padx=40, pady=5, fg="#363636", bg="#ff971d", activeforeground="#ff971d", activebackground="#323232")
	f9button4 = Button(frame9, text="Treatments", command=Treatments, padx=38, pady=5, fg="#363636", bg="#ff971d", activeforeground="#ff971d", activebackground="#323232")
	f9button5 = Button(frame9, text="Learn More on who.int", command=Learn, padx=5, pady=5, fg="#363636", bg="#ff971d", activeforeground="#ff971d", activebackground="#323232")
	f9button6 = Button(frame9, text="Exit", command=root.quit, padx=61, pady=5, fg="#363636", bg="#ff5722", activeforeground="#ff5722", activebackground="#323232")

	f9button1.grid(row=1, column=2)
	f9button2.grid(row=3, column=2)
	f9button3.grid(row=5, column=2)
	f9button4.grid(row=7, column=2)
	f9button5.grid(row=9, column=2)
	f9button6.grid(row=11, column=2)
	#**********************************************************************************************************************************************************************
	#FRAME-10--------------------------------------------------------------------------------------------------------------------------------------------------------------
	frame2.grid_forget()
	frame10 = LabelFrame(root, padx=5, pady=5, bg="#fefdca")
	frame10.grid(row=0, column=1)
	#---------------------------------------------------------------
	#--------------------------START-------------------------------------
	#---------------------------------------------------------------


	f10label1 = Label(frame10, text="Statewise Graphical Representation\nOf\nThe COVID-19 Effected People", font=("Liberation Serif", 13), bg="#fefdca", fg="#f95959", anchor=CENTER, width=70, height=9)
	f10label1.grid(row=0, column=0)
	f10label2 = Label(frame10, text="***A Tree Map showing number of COVID-19 effected people***", font=("Liberation Serif", 11), bg="#fefdca", fg="#363636", anchor=CENTER, width=70, height=6)
	f10label2.grid(row=1, column=0)
	main_button1 = Button(frame10, text="Tree Map", padx=40, font=("Arial Black", 8), fg="#363636", bg="#ff971d", activeforeground="#ff971d", activebackground="#fefdca", command=graph)
	main_button1.grid(row=2, column=0)
	f10label3 = Label(frame10, text="***A Bar Graph showing number of COVID-19 effected people***", font=("Liberation Serif", 11), bg="#fefdca", fg="#363636", anchor=CENTER, width=70, height=6)
	f10label3.grid(row=3, column=0)
	main_button2 = Button(frame10, text="Bar Graph", padx=40, font=("Arial Black", 8), fg="#363636", bg="#ff971d", activeforeground="#ff971d", activebackground="#fefdca", command=bar_graph)
	main_button2.grid(row=4, column=0)

	f10label4 = Label(frame10, text="\n", bg="#fefdca")
	f10label4.grid(row=5, column=0)
	

def Symptoms():
	#-----FRAME-3---------------
	frame1.grid_forget()
	frame3 = LabelFrame(root, padx=5, pady=5, bg="#323232")
	frame3.grid(row=0, column=0)
	#---------------------------------------------------------------
	#--------------------------START-------------------------------------
	#---------------------------------------------------------------
	#--------------------------TITLE-------------------------------------
	f3label1 = Label(frame3, text="\n\nStay Home, Stay Safe!\n\n", font=("Arial Bold", 15), bg="#323232", fg="#ff971d")
	f3label1.grid(row=0, column=1, columnspan=3)
	#---------------------------------------------------------------
	#---------------------------Button1-------------------------------------
	#----------------------------------------------------------------
	f3label2 = Label(frame3, text="", bg="#323232")
	f3label2.grid(row=2, column=1)
	#---------------------------Button2-------------------------------------
	#----------------------------------------------------------------
	f3label3 = Label(frame3, text="", bg="#323232")
	f3label3.grid(row=4, column=1)
	#---------------------------Button3------------------------------------
	#----------------------------------------------------------------
	f3label4 = Label(frame3, text="", bg="#323232")
	f3label4.grid(row=6, column=1)
	#---------------------------Button4------------------------------------
	#----------------------------------------------------------------
	f3label5 = Label(frame3, text="", bg="#323232")
	f3label5.grid(row=8, column=1)
	#---------------------------Button5------------------------------------
	#----------------------------------------------------------------
	f3label6 = Label(frame3, text="\n\n\n", bg="#323232")
	f3label6.grid(row=10, column=1)
	#---------------------------Exit-Button------------------------------------
	#----------------------------------------------------------------
	f3label7 = Label(frame3, text="\n\n", bg="#323232")
	f3label7.grid(row=12, column=1)
	#-----------------------------END-----------------------------------

	#------------------------------Column-Space---------------------------------
	f3label8 = Label(frame3, text="", bg="#323232")
	f3label8.grid(row=0, column=0)
	f3label9 = Label(frame3, text="", bg="#323232")
	f3label9.grid(row=0, column=4)
	#----------------------------------------------------------------

	#*****************************BUTTONS**********************************************************************************************************************************
	f3button1 = Button(frame3, text="Home", command=Home, padx=54, pady=5, fg="#363636", bg="#ff971d", activeforeground="#ff971d", activebackground="#323232")
	f3button2 = Button(frame3, text="Symptoms", command=Symptoms, padx=39, pady=5, fg="#363636", bg="#ff971d", state=DISABLED, activeforeground="#ff971d", activebackground="#323232")
	f3button3 = Button(frame3, text="Prevention", command=Prevention, padx=40, pady=5, fg="#363636", bg="#ff971d", activeforeground="#ff971d", activebackground="#323232")
	f3button4 = Button(frame3, text="Treatments", command=Treatments, padx=38, pady=5, fg="#363636", bg="#ff971d", activeforeground="#ff971d", activebackground="#323232")
	f3button5 = Button(frame3, text="Learn More on who.int", command=Learn, padx=5, pady=5, fg="#363636", bg="#ff971d", activeforeground="#ff971d", activebackground="#323232")
	f3button6 = Button(frame3, text="Exit", command=root.quit, padx=61, pady=5, fg="#363636", bg="#ff5722", activeforeground="#ff5722", activebackground="#323232")

	f3button1.grid(row=1, column=2)
	f3button2.grid(row=3, column=2)
	f3button3.grid(row=5, column=2)
	f3button4.grid(row=7, column=2)
	f3button5.grid(row=9, column=2)
	f3button6.grid(row=11, column=2)


	#-----FRAME-4---------------
	frame2.grid_forget()
	frame4 = LabelFrame(root, padx=5, pady=5, bg="#fefdca")
	frame4.grid(row=0, column=1)
	#---------------------------------------------------------------
	#--------------------------START-------------------------------------
	#---------------------------------------------------------------
	f4label1 = Label(frame4, text="----SYMPTOMS----\n\nCommon symptoms:\ni) Fever.\nii) Tiredness.\niii) Dry cough.\n\nSome people may experience:\ni) Aches and pains.\nii) Nasal congestion.\niii) Runny nose.\niv) Sore throat.\nv) Diarrhoea.\n\nOn average it takes 5–6 days from when someone\nis infected with the virus for symptoms to show, however it can take up to 14 days.\n\nPeople with mild symptoms who are otherwise healthy should self-isolate.\nSeek medical attention if you have a fever, a cough, and difficulty breathing.\n\nCALL AHEAD.", font=("Arial Bold", 10), bg="#fefdca", fg="#363636", anchor=CENTER, width=79, height=29)
	f4label1.grid(row=0, column=0)


def Prevention():
	#-----FRAME-5---------------
	frame1.grid_forget()
	frame5 = LabelFrame(root, padx=5, pady=5, bg="#323232")
	frame5.grid(row=0, column=0)
	#---------------------------------------------------------------
	#--------------------------START-------------------------------------
	#---------------------------------------------------------------
	#--------------------------TITLE-------------------------------------
	f5label1 = Label(frame5, text="\n\nStay Home, Stay Safe!\n\n", font=("Arial Bold", 15), bg="#323232", fg="#ff971d")
	f5label1.grid(row=0, column=1, columnspan=3)
	#---------------------------------------------------------------
	#---------------------------Button1-------------------------------------
	#----------------------------------------------------------------
	f5label2 = Label(frame5, text="", bg="#323232")
	f5label2.grid(row=2, column=1)
	#---------------------------Button2-------------------------------------
	#----------------------------------------------------------------
	f5label3 = Label(frame5, text="", bg="#323232")
	f5label3.grid(row=4, column=1)
	#---------------------------Button3------------------------------------
	#----------------------------------------------------------------
	f5label4 = Label(frame5, text="", bg="#323232")
	f5label4.grid(row=6, column=1)
	#---------------------------Button4------------------------------------
	#----------------------------------------------------------------
	f5label5 = Label(frame5, text="", bg="#323232")
	f5label5.grid(row=8, column=1)
	#---------------------------Button5------------------------------------
	#----------------------------------------------------------------
	f5label6 = Label(frame5, text="\n\n\n", bg="#323232")
	f5label6.grid(row=10, column=1)
	#---------------------------Exit-Button------------------------------------
	#----------------------------------------------------------------
	f5label7 = Label(frame5, text="\n\n", bg="#323232")
	f5label7.grid(row=12, column=1)
	#-----------------------------END-----------------------------------

	#------------------------------Column-Space---------------------------------
	f5label8 = Label(frame5, text="", bg="#323232")
	f5label8.grid(row=0, column=0)
	f5label9 = Label(frame5, text="", bg="#323232")
	f5label9.grid(row=0, column=4)
	#----------------------------------------------------------------

	#*****************************BUTTONS**********************************************************************************************************************************
	f5button1 = Button(frame5, text="Home", command=Home, padx=54, pady=5, fg="#363636", bg="#ff971d", activeforeground="#ff971d", activebackground="#323232")
	f5button2 = Button(frame5, text="Symptoms", command=Symptoms, padx=39, pady=5, fg="#363636", bg="#ff971d", activeforeground="#ff971d", activebackground="#323232")
	f5button3 = Button(frame5, text="Prevention", command=Prevention, padx=40, pady=5, fg="#363636", bg="#ff971d", state=DISABLED, activeforeground="#ff971d", activebackground="#323232")
	f5button4 = Button(frame5, text="Treatments", command=Treatments, padx=38, pady=5, fg="#363636", bg="#ff971d", activeforeground="#ff971d", activebackground="#323232")
	f5button5 = Button(frame5, text="Learn More on who.int", command=Learn, padx=5, pady=5, fg="#363636", bg="#ff971d", activeforeground="#ff971d", activebackground="#323232")
	f5button6 = Button(frame5, text="Exit", command=root.quit, padx=61, pady=5, fg="#363636", bg="#ff5722", activeforeground="#ff5722", activebackground="#323232")

	f5button1.grid(row=1, column=2)
	f5button2.grid(row=3, column=2)
	f5button3.grid(row=5, column=2)
	f5button4.grid(row=7, column=2)
	f5button5.grid(row=9, column=2)
	f5button6.grid(row=11, column=2)

	#-----FRAME-6---------------
	frame2.grid_forget()
	frame6 = LabelFrame(root, padx=5, pady=5, bg="#fefdca")
	frame6.grid(row=0, column=1)
	#---------------------------------------------------------------
	#--------------------------START-------------------------------------
	#---------------------------------------------------------------
	f6label1 = Label(frame6, text="----PREVENTION----\n\nSTAY HOME.\nSAVE LIVES.\n\nHelp stop coronavirus\n1) STAY home\n2) KEEP a safe distance\n3) WASH hands often\n4) COVER your cough\n5) SICK? Call the helpline", font=("Arial Bold", 10), bg="#fefdca", fg="#363636", anchor=CENTER, width=79, height=29)
	f6label1.grid(row=0, column=0)

def Treatments():
	#-----FRAME-7---------------
	frame1.grid_forget()
	frame7 = LabelFrame(root, padx=5, pady=5, bg="#323232")
	frame7.grid(row=0, column=0)
	#---------------------------------------------------------------
	#--------------------------START-------------------------------------
	#---------------------------------------------------------------
	#--------------------------TITLE-------------------------------------
	f7label1 = Label(frame7, text="\n\nStay Home, Stay Safe!\n\n", font=("Arial Bold", 15), bg="#323232", fg="#ff971d")
	f7label1.grid(row=0, column=1, columnspan=3)
	#---------------------------------------------------------------
	#---------------------------Button1-------------------------------------
	#----------------------------------------------------------------
	f7label2 = Label(frame7, text="", bg="#323232")
	f7label2.grid(row=2, column=1)
	#---------------------------Button2-------------------------------------
	#----------------------------------------------------------------
	f7label3 = Label(frame7, text="", bg="#323232")
	f7label3.grid(row=4, column=1)
	#---------------------------Button3------------------------------------
	#----------------------------------------------------------------
	f7label4 = Label(frame7, text="", bg="#323232")
	f7label4.grid(row=6, column=1)
	#---------------------------Button4------------------------------------
	#----------------------------------------------------------------
	f7label5 = Label(frame7, text="", bg="#323232")
	f7label5.grid(row=8, column=1)
	#---------------------------Button5------------------------------------
	#----------------------------------------------------------------
	f7label6 = Label(frame7, text="\n\n\n", bg="#323232")
	f7label6.grid(row=10, column=1)
	#---------------------------Exit-Button------------------------------------
	#----------------------------------------------------------------
	f7label7 = Label(frame7, text="\n\n", bg="#323232")
	f7label7.grid(row=12, column=1)
	#-----------------------------END-----------------------------------

	#------------------------------Column-Space---------------------------------
	f7label8 = Label(frame7, text="", bg="#323232")
	f7label8.grid(row=0, column=0)
	f7label9 = Label(frame7, text="", bg="#323232")
	f7label9.grid(row=0, column=4)
	#----------------------------------------------------------------

	#*****************************BUTTONS**********************************************************************************************************************************
	f7button1 = Button(frame7, text="Home", command=Home, padx=54, pady=5, fg="#363636", bg="#ff971d", activeforeground="#ff971d", activebackground="#323232")
	f7button2 = Button(frame7, text="Symptoms", command=Symptoms, padx=39, pady=5, fg="#363636", bg="#ff971d", activeforeground="#ff971d", activebackground="#323232")
	f7button3 = Button(frame7, text="Prevention", command=Prevention, padx=40, pady=5, fg="#363636", bg="#ff971d", activeforeground="#ff971d", activebackground="#323232")
	f7button4 = Button(frame7, text="Treatments", command=Treatments, padx=38, pady=5, fg="#363636", bg="#ff971d", state=DISABLED, activeforeground="#ff971d", activebackground="#323232")
	f7button5 = Button(frame7, text="Learn More on who.int", command=Learn, padx=5, pady=5, fg="#363636", bg="#ff971d", activeforeground="#ff971d", activebackground="#323232")
	f7button6 = Button(frame7, text="Exit", command=root.quit, padx=61, pady=5, fg="#363636", bg="#ff5722", activeforeground="#ff5722", activebackground="#323232")

	f7button1.grid(row=1, column=2)
	f7button2.grid(row=3, column=2)
	f7button3.grid(row=5, column=2)
	f7button4.grid(row=7, column=2)
	f7button5.grid(row=9, column=2)
	f7button6.grid(row=11, column=2)


	#-----FRAME-8---------------
	frame2.grid_forget()
	frame8 = LabelFrame(root, padx=5, pady=5, bg="#fefdca")
	frame8.grid(row=0, column=1)
	#---------------------------------------------------------------
	#--------------------------START-------------------------------------
	#---------------------------------------------------------------
	f8label1 = Label(frame8, text="----TREATMENTS----\n\nTo date, there are no specific vaccines or medicines for COVID-19.\nTreatments are under investigation, and will be tested through clinical trials.\n\nSelf-care\n\nIf you feel sick you should rest, drink plenty of fluid, and eat nutritious food.\nStay in a separate room from other family members, and use a dedicated bathroom if possible.\nClean and disinfect frequently touched surfaces.\nEveryone should keep a healthy lifestyle at home.\nMaintain a healthy diet, sleep, stay active, and make social\ncontact with loved ones through the phone or internet.\nChildren need extra love and attention from adults during difficult times.\nKeep to regular routines and schedules as much as possible.\nIt is normal to feel sad, stressed, or confused during a crisis.\nTalking to people you trust, such as friends and family, can help.\nIf you feel overwhelmed, talk to a health worker or counsellor.\n", font=("Arial Bold", 10), bg="#fefdca", fg="#363636", anchor=CENTER, width=79, height=29)
	f8label1.grid(row=0, column=0)



def Learn():
	webbrowser.open("https://www.who.int/", new=1)


#--------------------------------------FRAME-1-----------------------------------------------------------------------------------------------------------------------
frame1 = LabelFrame(root, padx=5, pady=5, bg="#323232")
frame1.grid(row=0, column=0)
#---------------------------------------------------------------
#--------------------------START-------------------------------------
#---------------------------------------------------------------
#--------------------------TITLE-------------------------------------
f1label1 = Label(frame1, text="\n\nStay Home, Stay Safe!\n\n", font=("Arial Bold", 15), bg="#323232", fg="#ff971d")
f1label1.grid(row=0, column=1, columnspan=3)
#---------------------------------------------------------------
#---------------------------Button1-------------------------------------
#----------------------------------------------------------------
f1label2 = Label(frame1, text="", bg="#323232")
f1label2.grid(row=2, column=1)
#---------------------------Button2-------------------------------------
#----------------------------------------------------------------
f1label3 = Label(frame1, text="", bg="#323232")
f1label3.grid(row=4, column=1)
#---------------------------Button3------------------------------------
#----------------------------------------------------------------
f1label4 = Label(frame1, text="", bg="#323232")
f1label4.grid(row=6, column=1)
#---------------------------Button4------------------------------------
#----------------------------------------------------------------
f1label5 = Label(frame1, text="", bg="#323232")
f1label5.grid(row=8, column=1)
#---------------------------Button5------------------------------------
#----------------------------------------------------------------
f1label6 = Label(frame1, text="\n\n\n", bg="#323232")
f1label6.grid(row=10, column=1)
#---------------------------Exit-Button------------------------------------
#----------------------------------------------------------------
f1label7 = Label(frame1, text="\n\n", bg="#323232")
f1label7.grid(row=12, column=1)
#-----------------------------END-----------------------------------

#------------------------------Column-Space---------------------------------
f1label8 = Label(frame1, text="", bg="#323232")
f1label8.grid(row=0, column=0)
f1label9 = Label(frame1, text="", bg="#323232")
f1label9.grid(row=0, column=4)
#----------------------------------------------------------------

#*****************************BUTTONS**********************************************************************************************************************************
f1button1 = Button(frame1, text="Home", command=Home, padx=54, pady=5, fg="#363636", bg="#ff971d", state=DISABLED, activeforeground="#ff971d", activebackground="#323232")
f1button2 = Button(frame1, text="Symptoms", command=Symptoms, padx=39, pady=5, fg="#363636", bg="#ff971d", activeforeground="#ff971d", activebackground="#323232")
f1button3 = Button(frame1, text="Prevention", command=Prevention, padx=40, pady=5, fg="#363636", bg="#ff971d", activeforeground="#ff971d", activebackground="#323232")
f1button4 = Button(frame1, text="Treatments", command=Treatments, padx=38, pady=5, fg="#363636", bg="#ff971d", activeforeground="#ff971d", activebackground="#323232")
f1button5 = Button(frame1, text="Learn More on who.int", command=Learn, padx=5, pady=5, fg="#363636", bg="#ff971d", activeforeground="#ff971d", activebackground="#323232")
f1button6 = Button(frame1, text="Exit", command=root.quit, padx=61, pady=5, fg="#363636", bg="#ff5722", activeforeground="#ff5722", activebackground="#323232")

f1button1.grid(row=1, column=2)
f1button2.grid(row=3, column=2)
f1button3.grid(row=5, column=2)
f1button4.grid(row=7, column=2)
f1button5.grid(row=9, column=2)
f1button6.grid(row=11, column=2)
#**********************************************************************************************************************************************************************





#FRAME-2--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#---------------------------------------------------------------
#--------------------------START-------------------------------------
#---------------------------------------------------------------
frame2 = LabelFrame(root, padx=5, pady=5, bg="#fefdca")
frame2.grid(row=0, column=1)

f2label1 = Label(frame2, text="Statewise Graphical Representation\nOf\nThe COVID-19 Effected People", font=("Liberation Serif", 13), bg="#fefdca", fg="#f95959", anchor=CENTER, width=70, height=9)
f2label1.grid(row=0, column=0)

f2label2 = Label(frame2, text="***A Tree Map showing number of COVID-19 effected people***", font=("Liberation Serif", 11), bg="#fefdca", fg="#363636", anchor=CENTER, width=70, height=6)
f2label2.grid(row=1, column=0)
main_button1 = Button(frame2, text="Tree Map", padx=40, font=("Arial Black", 8), fg="#363636", bg="#ff971d", activeforeground="#ff971d", activebackground="#fefdca", command=graph)
main_button1.grid(row=2, column=0)
f2label3 = Label(frame2, text="***A Bar Graph showing number of COVID-19 effected people***", font=("Liberation Serif", 11), bg="#fefdca", fg="#363636", anchor=CENTER, width=70, height=6)
f2label3.grid(row=3, column=0)
main_button2 = Button(frame2, text="Bar Graph", padx=40, font=("Arial Black", 8), fg="#363636", bg="#ff971d", activeforeground="#ff971d", activebackground="#fefdca", command=bar_graph)
main_button2.grid(row=4, column=0)

f2label4 = Label(frame2, text="\n", bg="#fefdca")
f2label4.grid(row=5, column=0)
#----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

root.configure(bg="#323232")
root.geometry("897x510")
root.iconphoto(True, PhotoImage(file='alert1.png'))

root.mainloop()