import pandas as pd
import statsmodels.api as sm

df = pd.read_csv('loansData_clean.csv')

# add column to df to show interest rate is if < 12%
# derive column from interest rate column & name it IR_TF
# contains binary values, i.e., '0' when interest<12% or
# '1' when interest is >=12%
df['IR_TF'] = df['Interest.Rate'].map(lambda x: x<0.12)

# add column with constant intercept of 1.0
df['Intercept'] = 1

# create list of column names of independent variables,
# including the intercept, and call it ind_vars

ind_vars = ['Intercept', 'FICO.Score', 'Amount.Requested']

# define logistic regression
logit = sm.Logit(df['IR_TF'], df[ind_vars])

# fit the model
result = logit.fit()

# get fitted coefficients from results
coeff = result.params
print coeff


#there seems to be discrepancy between amount requested as part of printed coeff variable
#and when it is shown in summary

#also, do i need to fit a linear model first before using logit in statmodels?

# print logit regression results
result.summary()

import numpy as np

# fico and loan amount to the logistic function
fico = 720
loan_amt = 10000

# define logistic function
def logistic_function(c, FS, LA):
    z = c[0] + c[1]*FS + c[2]*LA # linear part of predictor
    p = 1/(1+np.e**z) # logistic function
    print "logistic function is %d" % p + "\n" # see value for logistic function
    return p, FS, LA
   
# define pred function
def pred(pv, FS, LA):
    print "pv is {0}".format(pv) # see pv value for pred function
    print "\n"
    if pv < 0.7:
        print "Given the Loan Amount, {1}, and the FICO Score, {0}, you are UNLIKELY to get this loan <=12% interest.".format(FS, LA)
    else: 
        print "Given the Loan Amount, {1}, and the FICO Score, {0}, you are LIKELY to get this loan <=12% interest.".format(FS, LA)


pval = logistic_function(coeff, fico, loan_amt) # this defines pval
pred(pval, fico, loan_amt) # what does this do? puts pval, fico, loan_amt values for pv, FS, LA?       

#not sure how this code works
#logistic function prints out zero--what does that mean?
#pv value doesn't make sense when i print it
