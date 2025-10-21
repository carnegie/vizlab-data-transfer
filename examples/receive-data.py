import vizlab
import numpy as np

# Let VizLab software send back data on socket...
# (need to trigger this after the VizLab software is set to 'send' state)
receivedData = vizlab.receive()
print(receivedData.shape)