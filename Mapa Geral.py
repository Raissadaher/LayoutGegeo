import random
import math

from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont, QPainter
from qgis.core import *
from qgis.core import QgsProject, QgsCoordinateReferenceSystem
from qgis.utils import iface
from datetime import date
from qgis.core import QgsLayoutItemScaleBar, QgsProject

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
mapa = QgsLayoutItemMap(layout)
mapa.setAtlasDriven(True)
mapa.setFrameEnabled(True)
mapa.setRect(0, 0, 200, 188)
canvas = iface.mapCanvas()
mapa.setExtent(canvas.extent())
layout.addLayoutItem(mapa)
mapa.attemptMove(QgsLayoutPoint(10, 8, QgsUnitTypes.LayoutMillimeters))
mapa.attemptResize(QgsLayoutSize(200, 193.3, QgsUnitTypes.LayoutMillimeters))

# Criando Legenda
legenda = QgsLayoutItemLegend(layout)
legenda.setTitle("Legenda")
legenda_fonte = QFont("Arial", 11)
legenda.setStyleFont(QgsLegendStyle.Title, legenda_fonte)
legenda.setStyleFont(QgsLegendStyle.Subgroup, legenda_fonte)
legenda.setStyleFont(QgsLegendStyle.SymbolLabel, legenda_fonte)
legenda.attemptMove(QgsLayoutPoint(212, 90, QgsUnitTypes.LayoutMillimeters))
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
subtitle.setFont(QFont("Arial", 10))
subtitle.setRect(0, 0, 0, 0)
subtitle.adjustSizeToText()
subtitle.setHAlign(Qt.AlignCenter)
layout.addLayoutItem(subtitle)
subtitle.attemptMove(QgsLayoutPoint(215, 165, QgsUnitTypes.LayoutMillimeters))
subtitle.attemptResize(QgsLayoutSize(70, 37, QgsUnitTypes.LayoutMillimeters))

# inserir o Norte
north = QgsLayoutItemPicture(layout)
north.setPicturePath("C:\\Users\\raissa.alves\\Documents\\Atlas\\norte.svg")
layout.addLayoutItem(north)
north.attemptMove(QgsLayoutPoint(240, 70, QgsUnitTypes.LayoutMillimeters))
north.attemptResize(QgsLayoutSize(20, 20, QgsUnitTypes.LayoutMillimeters))

# inserir a logo

caminho_base = "C:/Users/raissa.alves/Documents/Atlas/",
north = QgsLayoutItemPicture(layout)
north.setPicturePath("Semad_Abreviada_positivo.png")
north.setPicturePath("C:/Users/raissa.alves/Documents/Atlas/Semad_Abreviada_positivo.png")
layout.addLayoutItem(north)
north.attemptMove(QgsLayoutPoint(214, 10, QgsUnitTypes.LayoutMillimeters))
north.attemptResize(QgsLayoutSize(75, 20.5, QgsUnitTypes.LayoutMillimeters))

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
mapa.grid().setAnnotationPrecision(0)
mapa.grid().setAnnotationFrameDistance(1)
mapa.grid().setAnnotationFontColor(QColor(0, 0, 0))
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
escala.attemptMove(QgsLayoutPoint(240, 150, QgsUnitTypes.LayoutMillimeters))
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
