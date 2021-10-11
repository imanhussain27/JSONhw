
from plotly.graph_objs import Scattergeo, Layout
from plotly import offline
import json


infile=open("US_fires_9_1.json","r")
outfile=open("readable_fires_9_1_data.json","w")
firedata=json.load(infile)
json.dump(firedata,outfile,indent=4)

f=[x for x in firedata if x["brightness"]>450]
brightness=[x["brightness"] for x in f]
lat=[x["latitude"] for x in f]
lon=[x["longitude"] for x in f]

from plotly.graph_objs import Scattergeo, Layout
from plotly import offline

data = [
    {
        "type":"scattergeo","lon":lon,"lat":lat,"text":brightness,
        "marker":{"size":[.05*b for b in brightness],"color":brightness,"colorscale":"Viridis","reversescale":True,"colorbar":{"title":"Magnitude"},
        }
    }
]

my_layout=Layout(title="Global Earthquake 3 Day")
fig={"data":data,"layout":my_layout}
offline.plot(fig,filename="globalearthquake3day.html")
print(brightness)
print(lon)
