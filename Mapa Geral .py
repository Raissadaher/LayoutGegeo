import random
import math
import os

from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont, QPainter
from qgis.gui import QgsMapCanvas
from qgis.core import *
from qgis.core import QgsProject, QgsCoordinateReferenceSystem
from qgis.utils import iface
from datetime import date
from qgis.core import QgsLayoutItemScaleBar, QgsProject, QgsLayoutItemMapOverview, QgsSimpleFillSymbolLayer, QgsLineSymbol 
from qgis.core import QgsProject, QgsLayoutItemMap, QgsLayoutPoint, QgsLayoutSize, QgsUnitTypes, QgsFillSymbol
from qgis.core import QgsSymbolLayer, QgsSymbolRenderContext, QgsGeometry, Qgis


def imprime_layers():
    names = [mapLayers.name() for mapLayers in QgsProject.instance().mapLayers().values()]
    print(names)



# variaveis globais
project = QgsProject.instance()
manager = project.layoutManager()
layout = QgsPrintLayout(project)
layoutName = f"pagina_1_{random.randint(1, 500)}"
layout.initializeDefaults()
layout.setName(layoutName)
manager.addLayout(layout)

# adicionando segunda pagina
page = QgsLayoutItemPage(layout)
page.setPageSize('A4', QgsLayoutItemPage.Landscape)
layout.pageCollection().addPage(page)

# Adicionando Poligono Maior
rectangle_maior = QgsLayoutItemShape(layout)
rectangle_maior.setShapeType(QgsLayoutItemShape.Rectangle)
rectangle_maior.setRect(0, 0, 0, 0)
layout.addLayoutItem(rectangle_maior)
rectangle_maior.attemptMove(QgsLayoutPoint(6, 3, QgsUnitTypes.LayoutMillimeters))
rectangle_maior.attemptResize(QgsLayoutSize(287.717, 202.350, QgsUnitTypes.LayoutMillimeters))
iface.openLayoutDesigner(layout)

# Adicionando Poligono Titulo
rectangle_titulo = QgsLayoutItemShape(layout)
rectangle_titulo.setShapeType(QgsLayoutItemShape.Rectangle)
rectangle_titulo.setRect(0, 0, 0, 0)
layout.addLayoutItem(rectangle_titulo)
rectangle_titulo.attemptMove(QgsLayoutPoint(212, 8, QgsUnitTypes.LayoutMillimeters))
rectangle_titulo.attemptResize(QgsLayoutSize(77, 193.3, QgsUnitTypes.LayoutMillimeters))

# Renderizar Mapa
area_imovel :QgsMapLayer = project.mapLayersByName('Área do imóvel')[0]
centroides_gerais :QgsMapLayer = project.mapLayersByName('Centroides gerais')[0]
area_de_preservacao_permanente = QgsMapLayer = project.mapLayersByName('Área de preservação permanente')[0]
area_supressao = QgsMapLayer = project.mapLayersByName('Área de supressão')[0]
reserva_legal = QgsMapLayer = project.mapLayersByName('Reserva legal')[0]
mapa = QgsLayoutItemMap(layout)
mapa.setId("mapa_propriedade")
mapa.setAtlasDriven(True)
mapa.setFrameEnabled(True)
mapa.setRect(0, 0, 200, 188)
mapa.setLayers([area_imovel, centroides_gerais, area_de_preservacao_permanente, area_imovel, area_supressao, reserva_legal])
mapa.setExtent(area_imovel.extent())
layout.addLayoutItem(mapa)
mapa.attemptMove(QgsLayoutPoint(10, 8, QgsUnitTypes.LayoutMillimeters))
mapa.attemptResize(QgsLayoutSize(200, 193.3, QgsUnitTypes.LayoutMillimeters))

# Mapa Localização
#frame_symbol = QgsFillSymbol.defaultSymbol(QgsWkbTypes.PolygonGeometry)
#frame_symbol.setColor(QColor(255, 50, 50, 50))
municipios :QgsMapLayer = project.mapLayersByName('Municipios')[0]
pais :QgsMapLayer = project.mapLayersByName('Brasil')[0]
mapa01 = QgsLayoutItemMap(layout)
mapa01.setId("mapa_municipios")
mapa01.setAtlasDriven(True)
mapa01.setFrameEnabled(True)
mapa01.setRect(0, 0, 170, 0)
src_crs = QgsCoordinateReferenceSystem(4674)
mapa01.setCrs(src_crs)
mapa01.setLayers([municipios, pais])
mapa01.setExtent(municipios.extent())
mapa01.overview().setLinkedMap(mapa)
#mapa01.overview().setFrameSymbol(frame_symbol)
props2 = {"color": "0,255,0,100", "color_border": "red", "width_border": "2.0"}
fillSymbol2 = QgsFillSymbol.createSimple(props2)
mapa01.overview().setFrameSymbol(fillSymbol2)
mapa01.setScale(6500000)
layout.addLayoutItem(mapa01)
mapa01.attemptMove(QgsLayoutPoint(216, 70, QgsUnitTypes.LayoutMillimeters))
mapa01.attemptResize(QgsLayoutSize(69.700, 43.109, QgsUnitTypes.LayoutMillimeters))

#adicionando rotunds

#MT
mt = 'MT'
map_label = QgsLayoutItemLabel(layout)
map_label.setText(mt)
map_label.setFont(QFont("Arial", 6))
map_label.setItemOpacity(1.0)
map_label.setBackgroundEnabled(1)
map_label.adjustSizeToText()
layout.addLayoutItem(map_label)
map_label.attemptResize(QgsLayoutSize(5, 3, QgsUnitTypes.LayoutMillimeters))
map_label.attemptMove(QgsLayoutPoint(225, 85, QgsUnitTypes.LayoutMillimeters))


#TO
to = 'TO'
map_label = QgsLayoutItemLabel(layout)
map_label.setText(to)
map_label.setFont(QFont("Arial", 6))
map_label.setItemOpacity(1.0)
map_label.setBackgroundEnabled(1)
map_label.adjustSizeToText()
layout.addLayoutItem(map_label)
map_label.attemptResize(QgsLayoutSize(5, 3, QgsUnitTypes.LayoutMillimeters))
map_label.attemptMove(QgsLayoutPoint(256, 71, QgsUnitTypes.LayoutMillimeters))


#BA
ba = 'BA'
map_label = QgsLayoutItemLabel(layout)
map_label.setText(ba)
map_label.setFont(QFont("Arial", 6))
map_label.setItemOpacity(1.0)
map_label.setBackgroundEnabled(1)
map_label.adjustSizeToText()
layout.addLayoutItem(map_label)
map_label.attemptResize(QgsLayoutSize(5, 3, QgsUnitTypes.LayoutMillimeters))
map_label.attemptMove(QgsLayoutPoint(280, 75, QgsUnitTypes.LayoutMillimeters))

#MG
mg = 'MG'
map_label = QgsLayoutItemLabel(layout)
map_label.setText(mg)
map_label.setFont(QFont("Arial", 6))
map_label.setItemOpacity(1.0)
map_label.setBackgroundEnabled(1)
map_label.adjustSizeToText()
layout.addLayoutItem(map_label)
map_label.attemptResize(QgsLayoutSize(5, 3, QgsUnitTypes.LayoutMillimeters))
map_label.attemptMove(QgsLayoutPoint(272, 105, QgsUnitTypes.LayoutMillimeters))

#MG
ms = 'MS'
map_label = QgsLayoutItemLabel(layout)
map_label.setText(ms)
map_label.setFont(QFont("Arial", 6))
map_label.setItemOpacity(1.0)
map_label.setBackgroundEnabled(1)
map_label.adjustSizeToText()
layout.addLayoutItem(map_label)
map_label.attemptResize(QgsLayoutSize(4, 3, QgsUnitTypes.LayoutMillimeters))
map_label.attemptMove(QgsLayoutPoint(222, 107, QgsUnitTypes.LayoutMillimeters))


# Criando Legenda
legenda = QgsLayoutItemLegend(layout)
legenda.setTitle("Legenda")
legenda_fonte = QFont("Arial", 8)
legenda.rstyle(QgsLegendStyle.Symbol).setMargin(QgsLegendStyle.Top, 2)
legenda.setSymbolHeight(3)
legenda.adjustBoxSize()
legenda.setStyleFont(QgsLegendStyle.Title, legenda_fonte)
legenda.setStyleFont(QgsLegendStyle.Subgroup, legenda_fonte)
legenda.setStyleFont(QgsLegendStyle.SymbolLabel, legenda_fonte)
legenda.attemptMove(QgsLayoutPoint(216, 120, QgsUnitTypes.LayoutMillimeters))
legenda.attemptResize(QgsLayoutSize(20, 20, QgsUnitTypes.LayoutMillimeters))
legenda.setLinkedMap(mapa)
legenda.setItemOpacity(1.0)
legenda.setBackgroundEnabled(0.5)
legenda.setLegendFilterByMapEnabled(True)
legenda.refresh()
layout.addLayoutItem(legenda)

# Isso adiciona titulo ao mapa
layer = project.mapLayersByName('Área do imóvel')[0]
nome = ""
proprietario = ""
municipio = ""
cpf = ""
wkt = ""
# Verifica se a camada está válida
if layer is not None:
 # Itera sobre as features selecionadas
    for feature in layer.getFeatures():
        nome = feature['nm_imovel']
        proprietario = feature['proprietar']
        cpf = feature['cpf_cnpj']
        municipio = feature['municipio']
        geom = feature.geometry()
        wkt = geom.asWkt(precision=4)

dados = 'MAPA DE SITUAÇÃO' + '\n' 'Propriedade: ' + nome + '\n' + 'Proprietário: ' + proprietario + '\n' + 'CPF/CNPJ: ' + cpf + '\n' + 'Municipio: ' + municipio + '\n' + 'Processo SEI:' + '\n'
title = QgsLayoutItemLabel(layout)
title.setText(dados)
title.setFont(QFont("Arial", 10))
title.adjustSizeToText()
title.setHAlign(Qt.AlignCenter)
layout.addLayoutItem(title)
title.attemptResize(QgsLayoutSize(75, 50, QgsUnitTypes.LayoutMillimeters))
title.attemptMove(QgsLayoutPoint(213, 35, QgsUnitTypes.LayoutMillimeters))

# Isso adiciona subtitulo ao mapa
dados_propriedade_subtitulo = f"""Sistema Geodésico: Sirgas 2000
Sistema de coordenada: Projetado-UTM
Formato: A4
Escala numérica: 1:{math.floor(mapa.scale())}
Fontes: SEMAD, CAR, MMA, Rede MAIS/MJSP
Elaboração: Raíssa Daher
GEGEO / SEMAD-GO
Data : {date.today().strftime("%d/%m/%Y")}
"""

subtitle = QgsLayoutItemLabel(layout)
subtitle.setText(dados_propriedade_subtitulo)
subtitle.setFont(QFont("Arial", 7))
subtitle.setRect(0, 0, 0, 0)
subtitle.adjustSizeToText()
subtitle.setHAlign(Qt.AlignCenter)
layout.addLayoutItem(subtitle)
subtitle.attemptMove(QgsLayoutPoint(215, 178, QgsUnitTypes.LayoutMillimeters))
subtitle.attemptResize(QgsLayoutSize(70, 27, QgsUnitTypes.LayoutMillimeters))

# inserir o Norte
north = QgsLayoutItemPicture(layout)
north.setPicturePath("C:\\Users\\raissa.alves\\Documents\\Atlas\\norte.svg")
layout.addLayoutItem(north)
north.attemptMove(QgsLayoutPoint(245, 158, QgsUnitTypes.LayoutMillimeters))
north.attemptResize(QgsLayoutSize(15, 15, QgsUnitTypes.LayoutMillimeters))

# inserir a logo
logo = QgsLayoutItemPicture(layout)
logo.setPicturePath("C:/Users/raissa.alves/Documents/Atlas/Semad_Abreviada_positivo.png")
layout.addLayoutItem(logo)
logo.attemptMove(QgsLayoutPoint(214, 10, QgsUnitTypes.LayoutMillimeters))
logo.attemptResize(QgsLayoutSize(75, 20.5, QgsUnitTypes.LayoutMillimeters))

# inserindo o CAR
area_imovel = project.mapLayersByName('Área do imóvel')[0]
CAR = ""
# Verifica se a camada está válida
if area_imovel is not None:
# Itera sobre as features selecionadas
    for feature in area_imovel.getFeatures():
        CAR = feature['cod_imovel']

dados = 'CAR: ' + CAR
title = QgsLayoutItemLabel(layout)
title.setText(dados)
title.setFont(QFont("Arial", 7))
title.adjustSizeToText()
title.setHAlign(Qt.AlignLeft)
layout.addLayoutItem(title)
title.attemptResize(QgsLayoutSize(75, 4, QgsUnitTypes.LayoutMillimeters))
title.attemptMove(QgsLayoutPoint(10, 202, QgsUnitTypes.LayoutMillimeters))

# inserindo grid
grid = QgsLayoutItemMapGrid("New grid", mapa)
mapa.grid().setEnabled(True)
mapa.grid().setUnits(QgsLayoutItemMapGrid.DynamicPageSizeBased)
mapa.grid().setMaximumIntervalWidth(50)
mapa.grid().setMinimumIntervalWidth(45)
mapa.grid().setAnnotationEnabled(True)
mapa.grid().setGridLineWidth(0.1)
#mapa.grid().setStyle(QgsLayoutItemMapGrid.GridStyle.FrameAnnotationsOnly)
#mapa.grid().setFrameStyle(QgsLayoutItemMapGrid.FrameStyle.InteriorTicks)
mapa.grid().setAnnotationPrecision(0)
mapa.grid().setAnnotationFrameDistance(1)
mapa.grid().setAnnotationFontColor(QColor(0, 0, 0))
mapa.grid().setAnnotationFont(QFont('Arial', 10))
mapa.grid().setAnnotationDisplay(QgsLayoutItemMapGrid.HideAll, QgsLayoutItemMapGrid.Right)
mapa.grid().setAnnotationDisplay(QgsLayoutItemMapGrid.ShowAll, QgsLayoutItemMapGrid.Top)
mapa.grid().setAnnotationDisplay(QgsLayoutItemMapGrid.HideAll, QgsLayoutItemMapGrid.Bottom)
mapa.grid().setAnnotationPosition(QgsLayoutItemMapGrid.OutsideMapFrame, QgsLayoutItemMapGrid.Bottom)
mapa.grid().setAnnotationDirection(QgsLayoutItemMapGrid.Horizontal, QgsLayoutItemMapGrid.Bottom)
mapa.grid().setAnnotationPosition(QgsLayoutItemMapGrid.OutsideMapFrame, QgsLayoutItemMapGrid.Left)
mapa.grid().setAnnotationDirection(QgsLayoutItemMapGrid.Vertical, QgsLayoutItemMapGrid.Left)
mapa.grid().setAnnotationDisplay(QgsLayoutItemMapGrid.ShowAll, QgsLayoutItemMapGrid.Left)

# Barra de escala
escala = QgsLayoutItemScaleBar(layout)
escala.setStyle('Caixa Simples')
escala.setLinkedMap(mapa)
escala.setHeight(2)
escala.setFont(QFont('Arial', 10))
escala.applyDefaultSize()
escala.attemptMove(QgsLayoutPoint(160, 185, QgsUnitTypes.LayoutMillimeters))
layout.addLayoutItem(escala)


# Adicionando a tabela de atributos
layer = project.mapLayersByName('Centroides gerais')[0]
tabela_atributos = QgsLayoutItemAttributeTable.create(layout)
tabela_atributos.setVectorLayer(layer)
tabela_atributos.setMaximumNumberOfFeatures(40)
layout.addMultiFrame(tabela_atributos)
frame2 = QgsLayoutFrame(layout, tabela_atributos)
frame2.attemptResize(QgsLayoutSize(198.200, 224), True)
frame2.attemptMove(QgsLayoutPoint(120, 220, QgsUnitTypes.LayoutMillimeters))
tabela_atributos.addFrame(frame2)
tabela_atributos.setResizeMode(1)

coluna = QgsLayoutTableColumn()
coluna.setAttribute('id') # First column name in your case. You can also put an expression
coluna.setSortOrder(0) # 0 = Asc, 1 Desc
tabela_atributos.setSortColumns([coluna])
layout.refresh()