from die import Die
import plotly.express as px

die=Die()
results=[]

# Roll 1000 times
for roll_num in range(1000):
    result=die.roll()
    results.append(result)

# Analyse the results
frequencies=[]
poss_results=range(1,die.num_sides+1)
for value in poss_results:
    frequency=results.count(value)
    frequencies.append(frequency)

# Show the bar map thru Plotly Express
# fig=px.bar(x=poss_results,y=frequencies)
# fig=px.scatter(x=poss_results,y=frequencies)
# fig=px.line(x=poss_results,y=frequencies)
fig.show()
