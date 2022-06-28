import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

import scipy.stats as st

x=pd.read_csv('/Users/naderelzik/Desktop/cell2celltrain.csv')
y = x.replace([np.inf, -np.inf], np.nan).dropna(axis=0)
#Removes the rows which contains NAN or INF

#a=y.Occupation
#b=(a.value_counts()/49752)
##Calculates the probability of a string field (Occupation)
#
#s=y.groupby(["Churn", "Occupation"]).size()/49752
##Calculates the joint probability between two fields and results a table with the data & prob
#
#v=s.loc['Yes','Professional']
#Locates the probability of the two fields (Yes and professional) like indexing
#condprob=v/b.Professional

#From Bayes' rule P(A\B)=(P(A,B)/P(B)) so the joint probability already calculated by the fn groupby
#and the probability of a field already calculated in the 2nd step so only remains the division

#d=y.MonthlyRevenue
#plt.hist(d,bins=20)
#plt.xlabel('MonthlyRevenueRange')
#plt.ylabel('Number of customer')
#plt.show()
#Draw a histogram given a column and the y axis is the occurences of the customers

#hist , histedges=np.histogram(d,bins=20,density=True)
#e=plt.plot(histedges[1:],hist,linewidth=3)
#plt.axis([250,3000,0,0.0002])
#plt.xlabel("MonthlyRevenueRange")
#plt.ylabel("Probabilties of the customers")
#plt.show()
#Takes the y-values of the histogram and draw it as a curve not histogram bars

#cdf = np.cumsum (hist)
#plt.plot(histedges[1:], cdf/cdf[-1])
#plt.xlabel("MonthlyRevenueRange")
#plt.ylabel("Cumulative Probabilities")
#plt.show()
#Calculates the CDF using 11 elements of the histedges array to maintain the dimensions

#mean=np.mean(d)
#var=np.var(d)
#Calculates the mean and the variance

#plt.hist2d(x=y.ThreewayCalls,y=y.MonthsInService,density=True,bins=(10,10),cmap='Blues')
#plt.xlabel('ThreewayCalls')
#plt.ylabel('MonthsInService')
#plt.colorbar()
#plt.show()
#Calculates the 2D PDF between two fields
#t=np.cov(y.TotalRecurringCharge, y=y.DirectorAssistedCalls)
#print(t)
#print(np.cov(y.TotalRecurringCharge))
y=y.reset_index(drop=True)

Y=y.drop(["PercChangeMinutes","PercChangeRevenues","CustomerID","ServiceArea","ChildrenInHH","HandsetRefurbished","HandsetWebCapable","TruckOwner","RVOwner","Homeownership","BuysViaMailOrder","RespondsToMailOffers","OptOutMailings","NonUSTravel","OwnsComputer","HasCreditCard","RetentionCalls","RetentionOffersAccepted","NewCellphoneUser","NotNewCellphoneUser","ReferralsMadeBySubscriber","OwnsMotorcycle","AdjustmentsToCreditRating","HandsetPrice","MadeCallToRetentionTeam","CreditRating","PrizmCode","Occupation","MaritalStatus","CallForwardingCalls"],axis = 1)
indexofbestfit=[]
indexofbestfit2=[]
for column in Y.columns[1:]:
    hist , histedges=np.histogram(Y[column],bins=20,density=True)
    e=plt.plot(histedges[1:],hist,linewidth=3)
for column in Y.columns[1:]:
  
#pdf
    DISTRIBUTIONS=[st.expon,st.norm,st.beta]
    index=0
    error_array=[]
    while(index<3):
        fitpar=DISTRIBUTIONS[index].fit(Y[column])
        arg=fitpar[:-2]
        loc=fitpar[-2]
        scale=fitpar[-1]
        fitted_pdf=DISTRIBUTIONS[index].pdf(histedges[1:],loc=loc,scale=scale, *arg)
        g=plt.plot(histedges[1:], fitted_pdf)
        error=hist[index]-fitted_pdf
        error=np.power(error, 2.0)
        mean_error=np.mean(error)
        error_array.append(mean_error)
        index=index+1
    indexofbestfit.append(error_array.index(min(error_array)))  

yes_churn=Y[Y['Churn'].str.match('Yes')]
indexofbestfit2=[]
for column in yes_churn.columns[1:]: 
   
    DISTRIBUTIONS=[st.expon,st.norm,st.beta]
    index=0
    error_array=[]
    while(index<3):
        fitpar=DISTRIBUTIONS[index].fit(yes_churn[column])
        arg=fitpar[:-2]
        loc=fitpar[-2]
        scale=fitpar[-1]
        fitted_pdf=DISTRIBUTIONS[index].pdf(histedges[1:],loc=loc,scale=scale, *arg)
        g=plt.plot(histedges[1:], fitted_pdf)
        error=hist[index]-fitted_pdf
        error=np.power(error, 2.0)
        mean_error=np.mean(error)
        error_array.append(mean_error)
        index=index+1
    indexofbestfit2.append(error_array.index(min(error_array)))
    #best fit pdf given that yes churn
no_churn=Y[Y['Churn'].str.match('No')]
indexofbestfit3=[]
for column in no_churn.columns[1:]: 
  
    DISTRIBUTIONS=[st.expon,st.norm,st.beta]
    index=0
    error_array=[]
    while(index<3):
        fitpar=DISTRIBUTIONS[index].fit(no_churn[column])
        arg=fitpar[:-2]
        loc=fitpar[-2]
        scale=fitpar[-1]
        fitted_pdf=DISTRIBUTIONS[index].pdf(histedges[1:],loc=loc,scale=scale, *arg)
        g=plt.plot(histedges[1:], fitted_pdf)
        error=hist[index]-fitted_pdf
        error=np.power(error, 2.0)
        mean_error=np.mean(error)
        error_array.append(mean_error)
        index=index+1
    indexofbestfit3.append(error_array.index(min(error_array)))       
#best fit pdf
Churn_yes=[]
rows=0
F=Y.drop(["Churn"],axis = 1)
Yes_churn=yes_churn.drop(["Churn"],axis = 1)
while rows<5000:
    if(rows==0):
        print ("entered first loop")

    i=0
    customer=[]
    prob=[]
    for column in Y.columns[1:]:
                customer=F.iloc[rows,:]  
                fitpar=DISTRIBUTIONS[indexofbestfit[i]].fit(Y[column])
                arg=fitpar[:-2]
                loc=fitpar[-2]
                scale=fitpar[-1]
                fitted_pdf=DISTRIBUTIONS[indexofbestfit[i]].pdf(customer[i],loc=loc,scale=scale, *arg)
                prob.append(fitted_pdf)
                i=i+1
               
    prob2=[]
    i=0          
    for column in yes_churn.columns[1:]:
                customer=Yes_churn.iloc[rows,:]  
                fitpar=DISTRIBUTIONS[indexofbestfit2[i]].fit(yes_churn[column])
                arg=fitpar[:-2]
                loc=fitpar[-2]
                scale=fitpar[-1]
                fitted_pdf=DISTRIBUTIONS[indexofbestfit2[i]].pdf(customer[i],loc=loc,scale=scale, *arg)
                prob2.append(fitted_pdf)
                i=i+1
   
    def multiplyList(myList) :
                 
                # Multiply elements one by one
                result = 1
                for x in myList:
                     result = result * x 
                return result  
    z=14245/49752
   
    if prob2==0 or prob==0:
        Churn_yes.append(0)
    else:
        churn=(multiplyList(prob2)*z)/(multiplyList(prob))
        Churn_yes.append(churn)
    
    rows=rows+1
    
No_churn=no_churn.drop(["Churn"],axis = 1) 
Churn_no=[]
rows=0
while rows<5000:
    if(rows==0):
        print ("entered second loop")

    i=0
    customer=[]
    prob=[]
    for column in Y.columns[1:]:
                customer=F.iloc[rows,:]  
                fitpar=DISTRIBUTIONS[indexofbestfit[i]].fit(Y[column])
                arg=fitpar[:-2]
                loc=fitpar[-2]
                scale=fitpar[-1]
                fitted_pdf=DISTRIBUTIONS[indexofbestfit[i]].pdf(customer[i],loc=loc,scale=scale, *arg)
                prob.append(fitted_pdf)
                i=i+1
               
    prob2=[]
    i=0          
    for column in no_churn.columns[1:]:
                customer=No_churn.iloc[rows,:]  
                fitpar=DISTRIBUTIONS[indexofbestfit2[i]].fit(no_churn[column])
                arg=fitpar[:-2]
                loc=fitpar[-2]
                scale=fitpar[-1]
                fitted_pdf=DISTRIBUTIONS[indexofbestfit2[i]].pdf(customer[i],loc=loc,scale=scale, *arg)
                prob2.append(fitted_pdf)
                i=i+1
   
    def multiplyList(myList) :
                 
                # Multiply elements one by one
                result = 1
                for x in myList:
                     result = result * x 
                return result  
    z=35507/49752
    if prob2==0 or prob==0:
        Churn_no.append(0)
    else:
        churn=(multiplyList(prob2)*z)/(multiplyList(prob))
        Churn_no.append(churn) 
    rows=rows+1 
   
rows=0
Churn=[]  
while(rows<5000):
    if(rows==0):
        print ("entered third loop")
   
    if(Churn_yes[rows]>Churn_no[rows]) :
        Churn.append('Yes')
       
    if Churn_no[rows]>Churn_yes[rows] or Churn_yes[rows]==Churn_no[rows] :
        Churn.append('No')
   
       
    rows=rows+1
rows=0
accuracy_counter=0

while(rows<5000):
    if Churn[rows]==Y.Churn[rows]:
        accuracy_counter=accuracy_counter+1
    rows=rows+1
          
accuracy=accuracy_counter/5000    


