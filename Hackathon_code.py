import pandas as pd
from tkinter import *

csvreader = pd.read_csv('C:/Users/sroux/Downloads/Hackathon/Hackathon_data.csv')

already_searched=[]
nbr=0
first=True
indices=[]
valid_symptoms=[]
refuted_symptoms=[]
first=True
fen=Tk()
fen.title("Healing Together")
fen.state('normal')
text=StringVar(fen)
ans=StringVar(fen)

#Designing the possible indices with condition
def indices_format(condition, a):
    global next_key
    global nbr
    global indices
    global csvreader
    global valid_symptoms
    global refuted_symptoms
    global all_symptoms_valid

    #Defines all possible indices with current condition (validated or refuted) and removes indexes which do not show condition
    if a==True:
      valid_symptoms.append(condition)
      for i in csvreader:
            for j in i:
              if indices==[]:
                if i[j] == condition:
                    indices.append(csvreader.index(i))
              else:
                ok=False
                for k in indices:
                  for l in csvreader[k]:
                    if i[j] == condition and i[j] == l:
                      indices.append(csvreader.index(i))
                      ok=True
                  if ok!=True:
                    del indices[indices.index(k)]
                  ok=False
    elif a==False:
      refuted_symptoms.append(condition)
      if indices!=[]:
        ok=False
        for i in indices:
          for j in csvreader[i]:
              if j==condition:
                ok=True
          if ok==False:
            del indices[indices.index(i)]
    nbr+=1

def most_occurences():
    global indices
    global csvreader
    global counting
    if indices!=[]:
    #Firstly, checking if one of the disease has full symptoms
      for j in csvreader:
        for i in indices:
          for l in counting:
            for k in j:
              if csvreader[i][j.index(k)]!=0 and csvreader[i][j.index(k)]!=6:
                if l==k:
                  ok1=True
            if ok1==True:
              verif=True
            else:
              verif=False
          ok1=False
      if verif==True:
        return 'all_symptoms_valid'
      
    #If not, then making the list that will count each occurence and return symptom with most occurences
      counting=[]

      for j in indices:
            counting.append(csvreader[j][2])
            counting.append(csvreader[j][3])
            try:
                counting.append(csvreader[j][4])
            except:
                break
            try:
                counting.append(csvreader[j][5])
            except:
                break
            try:
                counting.append(csvreader[j][6])
            except:
                break
            try:
                counting.append(csvreader[j][7])
            except:
                break
            try:
                counting.append(csvreader[j][8])
            except:
                break
            try:
                counting.append(csvreader[j][9])
            except:
                break
            try:
                counting.append(csvreader[j][10])
            except:
                break
            try:
                counting.append(csvreader[j][11])
            except:
                break
            try:
                counting.append(csvreader[j][12])
            except:
                break

    #Making a liste that has [{symptom},{occurence}] arguments
      for j in counting:
            for i in counting:
              if j==i and counting.index(j)!=counting.index(i):
                del counting[counting.index(i)]
                n+=1
            j=[j,n]
            n=1

    #Returning symptom with most occurences
      returnidx=0
      for k in counting:
          if counting[returnidx][1] < k[1]:
            returnidx = k
      return counting[returnidx][0]

#Else: if it is the first question
    elif first==True:
      first=False
      jointed=[]
      for liste in csvreader:
        jointed.extend(liste)
      #Making a liste that has [{symptom},{occurence}] arguments
      for j in jointed:
            for i in jointed:
              if j==i and jointed.index(j)!=jointed.index(i):
                del jointed[jointed.index(i)]
                n+=1
            j=[j,n]
            n=1

    #Returning symptom with most occurences
      returnidx=0
      for k in jointed:
          if jointed[returnidx][1] < k[1]:
            returnidx = k
      return jointed[returnidx][0]


def diagnosis_action():
  global nbr
  global indices
  global csvreader
  global all_symptoms_valid
  global first
  if indices_format()=='all_symptoms_valid':
    return ['answer', most_occurences()]
  if len(indices)!=1 and nbr<6:
    if len(indices)==0:
      return ['first',most_occurences()]
    else:
      return ['next', most_occurences()]
  if len(indices)==1:
    return ['answer',csvreader[indices[0]][0]]    #Or just show that answer is found
  if len(indices)==0 and first!=True:
    return ['answer', 0]

#This will probably be edited, depending on how Emna will present the HTML
def presentation(): 
  found_question=diagnosis_action()
  if found_question[0]=='first' or found_question[0]=='next':
    text.set('Are you victim of the following symptom : {} \n Please respond with "Yes" or "No"'.format(most_occurences()))
    if ans.get()=='Yes':
      indices_format(found_question[1], True)
    if ans.get()=='No':
      indices_format(found_question[1], False)
  elif found_question==['answer', 0]:
    text.set('Our datasets were not able to provide a pertinent disease to your symptoms')
  elif found_question[0]=='answer':
    text.set('According to our datasets, you are sick of {}'.format(most_occurences()))      #Here would then be called the localisation function to present nearby practicians

title=Label(fen, text='Welcome to Healing Together!')
title.pack()
desc=Label(fen, text='This quiz allows you to have a general idea of what disease you migt be sick of. However, please note that this does not substitute an official diagnosis from a professional')
desc.pack()
Text=Label(fen, textvariable=text)
Text.pack()

entry=Entry(fen, validatecommand=presentation, textvariable=ans)
entry.pack()

fen.mainloop()
