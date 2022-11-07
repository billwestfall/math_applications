from pyflowsheet import Flowsheet, UnitOperation, Distillation, Vessel, BlackBox, Pump, Stream, StreamFlag, Valve,HeatExchanger, SvgContext, Table, Figure, TextElement
from pyflowsheet.internals import Tubes,RandomPacking
from IPython.core.display import SVG, HTML

import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

#Turn the interactive plotting option off to prohibit the plot to be shown twice
plt.ioff()

pfd= Flowsheet("V100-DS20","Simple Distillation", "Demo Flowsheet for testing functionality")

Feed= StreamFlag("Feed", "Feed", position=(0,400))
HX=Vessel("HX","Condenser", position=(260,200),  size=(40,140), internals=[Tubes()])
P2= StreamFlag("P2", "Product 2", position=(300,000))

pfd.addUnits( [Feed,HX,P2] )
pfd.connect("S01", Feed["Out"], HX["In"] ) 
pfd.connect("S02", HX["Out"], P2["In"] ) 

#Create your pandas dataframe
df = pd.DataFrame(np.random.randn(10, 4), columns=list('ABCD'))

#Create a new table object and pass the pandas table as the data argument. It will internally be rendered as a  matplotlib Table
T1 = Table("T1", "DemoTable", data=df, position=(500,100), size=(500,200),figsize=(12,5))

#Create your plot. Pass it to the Figure annotation. Pass the figure object as the fig parameter. It will internally be rendered into a base64 encoded string and embedded into the SVG drawing.
fig=df.plot(kind="line",figsize=(5,5))
F1 = Figure("Profile", "DemoFigure", fig=plt.gcf(), position=(00,50), size=(250,250))

#You can also create very simple tables on your own by creating callouts. In a real application the numbers would of course come from a real data source (simulation or plant data)
for i in range(1,6):
    pfd.callout(f"T{i} = {123+5*i} Â°C", (320,220+15*i) )

pfd.addAnnotations([F1,T1])

ctx= SvgContext("img/plots_and_tables.svg")
img = pfd.draw(ctx)
SVG(img.render(scale=1))
