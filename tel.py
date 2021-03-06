from tkinter import *
import numpy as np
import pandas as pd
import smtplib
from tkinter import ttk
import urllib.request
import re
import requests
import json
# from gui_stuff import *

l1=['back_pain','constipation','abdominal_pain','diarrhoea','mild_fever','yellow_urine',
'yellowing_of_eyes','acute_liver_failure','fluid_overload','swelling_of_stomach',
'swelled_lymph_nodes','malaise','blurred_and_distorted_vision','phlegm','throat_irritation',
'redness_of_eyes','sinus_pressure','runny_nose','congestion','chest_pain','weakness_in_limbs',
'fast_heart_rate','pain_during_bowel_movements','pain_in_anal_region','bloody_stool',
'irritation_in_anus','neck_pain','dizziness','cramps','bruising','obesity','swollen_legs',
'swollen_blood_vessels','puffy_face_and_eyes','enlarged_thyroid','brittle_nails',
'swollen_extremeties','excessive_hunger','extra_marital_contacts','drying_and_tingling_lips',
'slurred_speech','knee_pain','hip_joint_pain','muscle_weakness','stiff_neck','swelling_joints',
'movement_stiffness','spinning_movements','loss_of_balance','unsteadiness',
'weakness_of_one_body_side','loss_of_smell','bladder_discomfort','foul_smell_of urine',
'continuous_feel_of_urine','passage_of_gases','internal_itching','toxic_look_(typhos)',
'depression','irritability','muscle_pain','altered_sensorium','red_spots_over_body','belly_pain',
'abnormal_menstruation','dischromic _patches','watering_from_eyes','increased_appetite','polyuria','family_history','mucoid_sputum',
'rusty_sputum','lack_of_concentration','visual_disturbances','receiving_blood_transfusion',
'receiving_unsterile_injections','coma','stomach_bleeding','distention_of_abdomen',
'history_of_alcohol_consumption','fluid_overload','blood_in_sputum','prominent_veins_on_calf',
'palpitations','painful_walking','pus_filled_pimples','blackheads','scurring','skin_peeling',
'silver_like_dusting','small_dents_in_nails','inflammatory_nails','blister','red_sore_around_nose',
'yellow_crust_ooze']

disease=['Fungal infection','Allergy','GERD','Chronic cholestasis','Drug Reaction',
'Peptic ulcer diseae','AIDS','Diabetes','Gastroenteritis','Bronchial Asthma','Hypertension',
' Migraine','Cervical spondylosis',
'Paralysis (brain hemorrhage)','Jaundice','Malaria','Chicken pox','Dengue','Typhoid','hepatitis A',
'Hepatitis B','Hepatitis C','Hepatitis D','Hepatitis E','Alcoholic hepatitis','Tuberculosis',
'Common Cold','Pneumonia','Dimorphic hemmorhoids(piles)',
'Heartattack','Varicoseveins','Hypothyroidism','Hyperthyroidism','Hypoglycemia','Osteoarthristis',
'Arthritis','(vertigo) Paroymsal  Positional Vertigo','Acne','Urinary tract infection','Psoriasis',
'Impetigo']

l2=[]
for x in range(0,len(l1)):
    l2.append(0)

# TESTING DATA df -------------------------------------------------------------------------------------
df=pd.read_csv("Training.csv")

df.replace({'prognosis':{'Fungal infection':0,'Allergy':1,'GERD':2,'Chronic cholestasis':3,'Drug Reaction':4,
'Peptic ulcer diseae':5,'AIDS':6,'Diabetes ':7,'Gastroenteritis':8,'Bronchial Asthma':9,'Hypertension ':10,
'Migraine':11,'Cervical spondylosis':12,
'Paralysis (brain hemorrhage)':13,'Jaundice':14,'Malaria':15,'Chicken pox':16,'Dengue':17,'Typhoid':18,'hepatitis A':19,
'Hepatitis B':20,'Hepatitis C':21,'Hepatitis D':22,'Hepatitis E':23,'Alcoholic hepatitis':24,'Tuberculosis':25,
'Common Cold':26,'Pneumonia':27,'Dimorphic hemmorhoids(piles)':28,'Heart attack':29,'Varicose veins':30,'Hypothyroidism':31,
'Hyperthyroidism':32,'Hypoglycemia':33,'Osteoarthristis':34,'Arthritis':35,
'(vertigo) Paroymsal  Positional Vertigo':36,'Acne':37,'Urinary tract infection':38,'Psoriasis':39,
'Impetigo':40}},inplace=True)

# print(df.head())

X= df[l1]

y = df[["prognosis"]]
np.ravel(y)
# print(y)

# TRAINING DATA tr --------------------------------------------------------------------------------
tr=pd.read_csv("Testing.csv")
tr.replace({'prognosis':{'Fungal infection':0,'Allergy':1,'GERD':2,'Chronic cholestasis':3,'Drug Reaction':4,
'Peptic ulcer diseae':5,'AIDS':6,'Diabetes ':7,'Gastroenteritis':8,'Bronchial Asthma':9,'Hypertension ':10,
'Migraine':11,'Cervical spondylosis':12,
'Paralysis (brain hemorrhage)':13,'Jaundice':14,'Malaria':15,'Chicken pox':16,'Dengue':17,'Typhoid':18,'hepatitis A':19,
'Hepatitis B':20,'Hepatitis C':21,'Hepatitis D':22,'Hepatitis E':23,'Alcoholic hepatitis':24,'Tuberculosis':25,
'Common Cold':26,'Pneumonia':27,'Dimorphic hemmorhoids(piles)':28,'Heart attack':29,'Varicose veins':30,'Hypothyroidism':31,
'Hyperthyroidism':32,'Hypoglycemia':33,'Osteoarthristis':34,'Arthritis':35,
'(vertigo) Paroymsal  Positional Vertigo':36,'Acne':37,'Urinary tract infection':38,'Psoriasis':39,
'Impetigo':40}},inplace=True)

X_test= tr[l1]
y_test = tr[["prognosis"]]
np.ravel(y_test)
# ------------------------------------------------------------------------------------------------------

def cloude(disease_p):
    print(disease_p)
    print([Symptom1.get(),Symptom2.get(),Symptom3.get()])
    print(Name.get())
    print(age.get())
    print(number.get())
    print(details.get())
    print(doctor_name.get())
    print(resprate.get())
    print(bp.get())


    token="1769774111:AAGtg8c6_p3XIZ_oZSC4rnsTaXZmj26Wwnc"
    if doctor_name.get() == 'Rahul' :
        email_id ='beingunique2000@gmail.com'
        chat_id="562934559"
    elif doctor_name.get() == 'Sreenidhi' :
        email_id ='sreenidhishreya@gmail.com'
        chat_id="926817137"
    elif doctor_name.get() == 'Neha' :
        email_id ='nehavrindavan@gmail.com'
        chat_id="1002173513"
    elif doctor_name.get() == 'Ashwin' :
        email_id='ashwincsuresh@gmail.com'
        chat_id="629545180"
    else :
        email_id='vyju.j.s@gmail.com'
        chat_id="1639103107"
    #datafromwebsite=urllib.request.urlopen("https://api.thingspeak.com/channels/526585/fields/1.json?results=1")
    #print(datafromwebsite.read())
    
    

    body="Dear Doc, "+ doctor_name.get() +"\n\nThe medical report of pateint\n\n"+Name.get()+"     \nage:" +str(age.get())+ "\ncontact no: "+ str(number.get())+"\n\nwith Syptoms\n\n"+ Symptom1.get()+" , " + Symptom2.get()+" , "+Symptom3.get()+"\n\nvital readings --->\n\n temp: "+ str(vital_temp) + "\n blood oxy: "+ vital_bloodoxy +"\n heart rate: " +vital_bpm + "\n respiratory rate:  "+str(resprate.get()) +" \n Blood pressure : "+ str(bp.get()) +"\n\n\npossible disease :" + disease_p +"\n\n\nadditional details from patient : "+ details.get() +"\n\n\n" +"\n\n\n please contact the patient @ " +number.get()
    url_req ="https://api.telegram.org/bot"+ token+"/sendMessage"+"?chat_id="+chat_id +"&text="+body

    result=requests.get(url_req)
    print(result.json())

def vital():
    oxylvl=0







def DecisionTree():

    from sklearn import tree

    clf3 = tree.DecisionTreeClassifier()   # empty model of the decision tree
    clf3 = clf3.fit(X,y)

    # calculating accuracy-------------------------------------------------------------------
    from sklearn.metrics import accuracy_score
    y_pred=clf3.predict(X_test)
    print(accuracy_score(y_test, y_pred))
    print(accuracy_score(y_test, y_pred,normalize=False))
    # -----------------------------------------------------

    psymptoms = [Symptom1.get(),Symptom2.get(),Symptom3.get()]

    for k in range(0,len(l1)):
        # print (k,)
        for z in psymptoms:
            if(z==l1[k]):
                l2[k]=1

    inputtest = [l2]
    predict = clf3.predict(inputtest)
    predicted=predict[0]

    h='no'
    for a in range(0,len(disease)):
        if(predicted == a):
            h='yes'
            break


    if (h=='yes'):
        send_disease=disease[a]
        cloude(send_disease)
        t1.delete("1.0", END)
        t1.insert(END, disease[a])
    else:
        t1.delete("1.0", END)
        t1.insert(END, "Not Found")


# gui_stuff------------------------------------------------------------------------------------

root = Tk()
root.configure(background='green')

# entry variables
Symptom1 = StringVar()
Symptom1.set(None)
Symptom2 = StringVar()
Symptom2.set(None)
Symptom3 = StringVar()
Symptom3.set(None)
Name = StringVar()
doctor_name=StringVar()
doctor_name.set(None)
age=IntVar()
number=StringVar()
details=StringVar()
resprate=IntVar()
bp=IntVar()


datafromwebsite=urllib.request.urlopen("https://api.thingspeak.com/channels/526585/feeds.json?results=1")
json_data =json.loads(datafromwebsite.read())
vital_temp=json_data["feeds"][0]["field1"]
vital_bpm=json_data["feeds"][0]["field2"]
vital_bloodoxy =json_data["feeds"][0]["field3"]

# Heading
w2 = Label(root, justify=LEFT, text="Team Zendaya", fg="white", bg="green")
w2.config(font=("Elephant", 20))
w2.grid(row=1, column=1, columnspan=2, padx=100)

w4 = Label(root, justify=LEFT, text="Rahul,Neha,Vyjayanthi,Sreenidhi", fg="white", bg="green")
w4.config(font=("Aharoni", 15))
w4.grid(row=5, column=1, columnspan=2, padx=100)
w5 = Label(root,  text="Enter your details", fg="white", bg="green")
w5.config(font=("Aharoni", 10))
w5.grid(row=6, column=1, columnspan=2, padx=100)

w6 = Label(root,  text="choose doctor to consult", fg="white", bg="green")
w6.config(font=("Aharoni", 10))
w6.grid(row=9, column=1, columnspan=2, padx=100)

w7 = Label(root,  text="choose symptoms", fg="white", bg="green")
w7.config(font=("Aharoni", 10))
w7.grid(row=13, column=1, columnspan=2, padx=100)


w8 = Label(root,  text="vitals:", fg="white", bg="green")
w8.config(font=("Aharoni", 10))
w8.grid(row=9, column=2, columnspan=2, padx=100)

w9 = Label(root,  text=" bloode oxylevel :"+ str(vital_bloodoxy), fg="white", bg="green")
w9.config(font=("Aharoni", 10))
w9.grid(row=10, column=2, columnspan=2, padx=100)

w10 = Label(root,  text=" temp :"+ str(vital_temp), fg="white", bg="green")
w10.config(font=("Aharoni", 10))
w10.grid(row=11, column=2, columnspan=2, padx=100)

w11 = Label(root,  text=" heartrate :"+ str(vital_bpm), fg="white", bg="green")
w11.config(font=("Aharoni", 10))
w11.grid(row=12, column=2, columnspan=2, padx=100)

w12 = Label(root,  text=" manual vital---> respiration rate:", fg="white", bg="green")
w12.config(font=("Aharoni", 10))
w12.grid(row=14, column=2, columnspan=2, padx=100)

w12 = Label(root,  text=" manual vital---> Blood Pressure:", fg="white", bg="green")
w12.config(font=("Aharoni", 10))
w12.grid(row=16, column=2, columnspan=2, padx=100)

# labels
NameLb = Label(root, text="Name :", fg="black", bg="green")
NameLb.grid(row=7, column=0, pady=10, sticky=W)
ageLb = Label(root, text="Age", fg="black", bg="green")
ageLb.grid(row=7, column=1)

numLb = Label(root, text="contact no:", fg="black", bg="green")
numLb.grid(row=7, column=3, )


S1Lb = Label(root, text="Symptom 1", fg="yellow", bg="green")
S1Lb.grid(row=14, column=1, pady=10, sticky=W)

S2Lb = Label(root, text="Symptom 2", fg="yellow", bg="green")
S2Lb.grid(row=15, column=1, pady=10, sticky=W)

S3Lb = Label(root, text="Symptom 3", fg="yellow", bg="green")
S3Lb.grid(row=16, column=1, pady=10, sticky=W)

#S4Lb = Label(root, text="Symptom 4", fg="yellow", bg="black")
#S4Lb.grid(row=10, column=0, pady=10, sticky=W)

#S5Lb = Label(root, text="Symptom 5", fg="yellow", bg="black")
#S5Lb.grid(row=11, column=0, pady=10, sticky=W)


lrLb = Label(root, text="possible disease---->", fg="white", bg="green")
lrLb.grid(row=22, column=0, pady=10,sticky=W)

#destreeLb = Label(root, text="RandomForest", fg="white", bg="red")
#destreeLb.grid(row=17, column=0, pady=10, sticky=W)

#ranfLb = Label(root, text="NaiveBayes", fg="white", bg="red")
#ranfLb.grid(row=19, column=0, pady=10, sticky=W)

# entries
OPTIONS = sorted(l1)

NameEn = Entry(root, textvariable=Name)
NameEn.grid(row=8, column=0)

ageEn = Entry(root, textvariable=age)
ageEn.grid(row=8, column=1)

numEn = Entry(root, textvariable=number)
numEn.grid(row=8, column=3)

S1En = OptionMenu(root, Symptom1,*OPTIONS)
S1En.grid(row=14, column=1)

S2En = OptionMenu(root, Symptom2,*OPTIONS)
S2En.grid(row=15, column=1)

S3En = OptionMenu(root, Symptom3,*OPTIONS)
S3En.grid(row=16, column=1)

respEn = Entry(root, textvariable=resprate)
respEn.grid(row=15, column=3,columnspan=5)

bpEn = Entry(root, textvariable=bp)
bpEn.grid(row=17, column=3,columnspan=5)

#S4En = OptionMenu(root, Symptom4,*OPTIONS)
#S4En.grid(row=10, column=1)

#S5En = OptionMenu(root, Symptom5,*OPTIONS)
#F:\projects\final\program_trial\mainS5En.grid(row=11, column=1)


dst = Button(root, text="RUN", command=DecisionTree,bg="blue",fg="yellow")
dst.grid(row=20, column=1,padx=8)

#rnf = Button(root, text="Randomforest", command=randomforest,bg="green",fg="yellow")
#rnf.grid(row=9, column=3,padx=10)

#lr = Button(root, text="NaiveBayes", command=NaiveBayes,bg="green",fg="yellow")
#lr.grid(row=10, column=3,padx=10)

#textfileds
t1 = Text(root, height=1, width=40,bg="orange",fg="black")
t1.grid(row=22, column=1, padx=10)

#t2 = Text(root, height=1, width=40,bg="orange",fg="black")
#t2.grid(row=17, column=1 , padx=10)

#t3 = Text(root, height=1, width=40,bg="orange",fg="black")
#t3.grid(row=19, column=1 , padx=10)

additionnal = Label(root, text="additional details", fg="black", bg="green")
additionnal.grid(row=18, column=1, pady=10, sticky=W)
additionaen = Entry(root, textvariable=details)
additionaen.grid(row=18, column=0,columnspan=3, rowspan=1)


choices = { 'Rahul','Neha','Ashwin','Sreenidhi','Vyju'}
S2En = OptionMenu(root, doctor_name,*choices)
S2En.grid(row=11, column=1)

root.mainloop()