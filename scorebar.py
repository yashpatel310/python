import numpy as np
import matplotlib.pyplot as plt
 
  
# creating the dataset
data = {'1st year':70, '2nd year':75, '3rd year':85,
        '4th year':95}
Years = list(data.keys())
Score = list(data.values())
  
fig = plt.figure(figsize = (10, 5))
 
# creating the bar plot
plt.bar(Year, Score, color ='b',
        width = 0.4)
 
plt.xlabel("Student Year")
plt.ylabel("Student Score")
plt.title("My score in all the cycle tests in your previous year of college")
plt.show()
