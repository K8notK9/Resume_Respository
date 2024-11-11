import matplotlib.pyplot as plt
 # Data to plot
labels = ['Apples', 'Bananas', 'Cherries', 'Dates']
sizes = [10, 10, 10, 10]
colors = ['gold', 'yellowgreen', 'lightcoral', 'lightskyblue']
explode = (0.1, 0, 0, 0) # explode the 1st slice (i.e. 'Apples')
 # Plot
 # autopct: A string that formats the percentage label for each slice. '%1.1f%%' means one decimal
#place followed by a percent sign.
plt.pie(sizes, explode=explode, labels=labels, colors=colors,
autopct='%1.1f%%', shadow=True)
plt.axis('equal') # Equal aspect ratio ensures that pie is drawn as a circle.
plt.show()