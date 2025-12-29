# import time
# for _ in range (10):
#         print('🍎'*_ +"happy 2026")
# time.sleep(0.2)
      #macOS: Press Control + Command + Space for emoji
""" output:
happy 2026
🍎happy 2026
🍎🍎happy 2026
🍎🍎🍎happy 2026
🍎🍎🍎🍎happy 2026
🍎🍎🍎🍎🍎happy 2026
🍎🍎🍎🍎🍎🍎happy 2026
🍎🍎🍎🍎🍎🍎🍎happy 2026
🍎🍎🍎🍎🍎🍎🍎🍎happy 2026"""
#==============circuit ========
import schemdraw
import schemdraw.elements as elm

d = schemdraw.Drawing()
V = d.add(elm.SourceV().label('V',loc='left'))
R = d.add(elm.Resistor().label('R').right())
R1 = d.add(elm.Resistor().label('R1').right())
C = d.add(elm.Capacitor().label('C').right())
L = d.add(elm.Inductor().label('L').right())
C1 = d.add(elm.Capacitor().label('C1').right())

d.add(elm.Ground().at(V.start))
d.add(elm.Ground().at(L.end))
d.draw()
