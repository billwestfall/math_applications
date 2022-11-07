from pyflowsheet import Flowsheet, BlackBox, Stream, StreamFlag, Port, SvgContext,VerticalLabelAlignment, HorizontalLabelAlignment
from IPython.core.display import SVG, HTML

pfd= Flowsheet("V100","Block Flow Diagram", "Demo Flowsheet for showing block-flow diagram style")

SP1=BlackBox("Pretreatment","Removal of catalyst poisons", position=(100,180), size=(80,60))
SP2=BlackBox("Reaction","Catalytic reaction", position=(240,180), size=(80,60))
SP3=BlackBox("Gas-Recovery","Recycling of unconverted gaseous feedstock", position=(380,180), size=(80,60))
SP4=BlackBox("Separation","Recycling of solvent", position=(520,180), size=(80,60))
SP5=BlackBox("Purification","Removal of side product", position=(660,180), size=(80,60))

Feed= StreamFlag("Feed", "", position=(0,190))
Product= StreamFlag("Product", "", position=(800,190))
Waste= StreamFlag("Waste", "", position=(120,360))
SideProduct= StreamFlag("SideProduct", "", position=(680,360))

steps=[SP1,SP2,SP3,SP4,SP5]

for sp in steps:
    sp.setTextAnchor(HorizontalLabelAlignment.Center,VerticalLabelAlignment.Center,(0,5) )

Waste.rotate(90)
SideProduct.rotate(90)

#Add additional ports to the process steps for recycles and removal of unwanted components
SP1.ports["Out2"] = Port("Out2", SP1, (0.5, 1), (0, 1), intent="out")
SP5.ports["Out2"] = Port("Out2", SP5, (0.5, 1), (0, 1), intent="out")
SP3.ports["Out2"] = Port("Out2", SP3, (0.5, 0), (0, -1), intent="out")
SP4.ports["Out2"] = Port("Out2", SP4, (0.5, 1), (0, 1), intent="out")
SP2.ports["In2"] = Port("In2", SP2, (0.5, 0), (0, -1))
SP2.ports["In3"] = Port("In3", SP2, (0.5, 1), (0, 1))

#Add all units to the diagram
pfd.addUnits( [Feed,Product,Waste, SideProduct, SP1,SP2, SP3, SP4, SP5] )

#Create stream connectivity
pfd.connect("S01", Feed["Out"], SP1["In"] ) 
pfd.connect("S02", SP1["Out"], SP2["In"] ) 
pfd.connect("S03", SP2["Out"], SP3["In"] ) 
pfd.connect("S04", SP3["Out"], SP4["In"] ) 
pfd.connect("S05", SP4["Out"], SP5["In"] ) 
pfd.connect("S06", SP5["Out"], Product["In"] ) 
pfd.connect("S07", SP1["Out2"], Waste["In"] ) 
pfd.connect("S08", SP5["Out2"], SideProduct["In"] ) 
pfd.connect("S09", SP3["Out2"], SP2["In2"] ) 
pfd.connect("S10", SP4["Out2"], SP2["In3"] ) 

#Change the label offset for stream S09 to make it more readable
pfd.streams["S09"].labelOffset=(0,-5)

#Create a rendering context for the flowsheet and display it. pfd.draw(ctx) will also save the file to disc.
ctx= SvgContext("img/blockflowprocess.svg")
img = pfd.draw(ctx)
SVG(img.render(scale=1))
