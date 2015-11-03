from dxfwrite import DXFEngine as dxf

from dxfwrite.const import CENTER


drawing = dxf.drawing('dia.dxf')

polyline= dxf.polyline(linetype='LINE')

polyline.add_vertices([(6,10), (6,6),(1,6),(1,2),(15,2),(15,6),(10,6),(10,10)])
drawing.add(polyline)
drawing.add(dxf.line((5.5,10),(6.5,10)))

drawing.add(dxf.line((6.5,10),(6,10)))
drawing.add(dxf.line((6.5,10),(7,10.5)))
drawing.add(dxf.line((7,10.5),(7,9.5)))
drawing.add(dxf.line((7,9.5),(7.5,10)))
drawing.add(dxf.line((7.5,10),(8,10)))
drawing.add(dxf.line((9.5,10),(10.5,10)))
drawing.add(dxf.line((1,4),(15,4)))
drawing.add(dxf.line((1,4),(15,4)))
drawing.add(dxf.line((2.5,4),(2.5,2)))
drawing.add(dxf.line((3.5,4),(3.5,2)))
drawing.add(dxf.line((4.5,4),(4.5,2)))
drawing.add(dxf.line((5.5,4),(5.5,2)))
drawing.add(dxf.line((6.5,4),(6.5,2)))
drawing.add(dxf.line((7.5,4),(7.5,2)))
drawing.add(dxf.line((8.5,4),(8.5,2)))
drawing.add(dxf.line((9.5,4),(9.5,2)))
drawing.add(dxf.line((10.5,4),(10.5,2)))
drawing.add(dxf.line((11.5,4),(11.5,2)))
drawing.add(dxf.line((12.5,4),(12.5,2)))
drawing.add(dxf.line((13.5,4),(13.5,2)))
drawing.add(dxf.line((1,4),(1.5,3.5)))
drawing.add(dxf.line((1,4),(0.5,3.5)))
drawing.add(dxf.line((2.5,4),(2,3.5)))
drawing.add(dxf.line((2.5,4),(2.9,3.5)))
drawing.add(dxf.line((3.5,4),(3.9,3.5)))
drawing.add(dxf.line((3.5,4),(3.2,3.5)))
drawing.add(dxf.line((4.5,4),(4.9,3.5)))
drawing.add(dxf.line((4.5,4),(4.2,3.5)))
drawing.add(dxf.line((5.5,4),(5.9,3.5)))
drawing.add(dxf.line((5.5,4),(5.2,3.5)))
drawing.add(dxf.line((6.5,4),(6.9,3.5)))
drawing.add(dxf.line((6.5,4),(6.2,3.5)))
drawing.add(dxf.line((7.5,4),(7.2,3.5)))
drawing.add(dxf.line((7.5,4),(7.9,3.5)))
drawing.add(dxf.line((8.5,4),(8.9,3.5)))
drawing.add(dxf.line((8.5,4),(8.2,3.5)))
drawing.add(dxf.line((9.5,4),(9.9,3.5)))
drawing.add(dxf.line((9.5,4),(9.2,3.5)))
drawing.add(dxf.line((10.5,4),(10.9,3.5)))
drawing.add(dxf.line((10.5,4),(10.2,3.5)))
drawing.add(dxf.line((11.5,4),(11.9,3.5)))
drawing.add(dxf.line((11.5,4),(11.2,3.5)))
drawing.add(dxf.line((12.5,4),(12.9,3.5)))
drawing.add(dxf.line((12.5,4),(12.2,3.5)))
drawing.add(dxf.line((13.5,4),(13.9,3.5)))
drawing.add(dxf.line((13.5,4),(13.2,3.5)))
drawing.add(dxf.line((15,4),(14.5,3.5)))
drawing.add(dxf.line((15,4),(15.5,3.5)))


drawing.add(dxf.text('A', halign=CENTER, alignpoint=(8, 0)))
drawing.add(dxf.text('a', halign=CENTER, alignpoint=(8, 8)))
drawing.add(dxf.text('P(kN)', halign=CENTER, alignpoint=(8, 12)))
drawing.add(dxf.text('D', valign=CENTER, alignpoint=(16, 4)))
drawing.add(dxf.text('Uniformly deep footing', halign=CENTER, alignpoint=(-2, -2)))
drawing.add(dxf.text('p(kN/cm)', halign=CENTER, alignpoint=(-3, 2)))






drawing.save()
