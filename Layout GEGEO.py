import random
import math

from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont, QPainter
from qgis.core import *
from qgis.core import QgsProject, QgsCoordinateReferenceSystem
from qgis.utils import iface
from datetime import date
from qgis.core import QgsLayoutItemScaleBar, QgsProject
from qgis.PyQt.QtGui import *
from PyQt5.QtCore import Qt


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

# # removendo camadas indesejadas
# mapa_layers_desejados = ["Reserva Legal", "Centroides gerais", "Área de supressão", "Área de Preservação Permanente", "Área do imóvel", "Área de supressão em APP", "Área de supressão em RL", "Danificar floresta ou '\n' qualquer tipo de vegetação nativa"]
# layers_indesejados = [i for i in project.mapLayers().values() if i.name() not in mapa_layers_desejados]
# for layer_indesejada in layers_indesejados:
#     project.removeMapLayer(layer_indesejada)
# # imprime_layers()

# Adicionando Poligono Maior
rectangle_maior = QgsLayoutItemShape(layout)
rectangle_maior.setShapeType(QgsLayoutItemShape.Rectangle)
rectangle_maior.setRect(0, 0, 0, 0)
layout.addLayoutItem(rectangle_maior)
rectangle_maior.attemptMove(QgsLayoutPoint(5, 5, QgsUnitTypes.LayoutMillimeters))
rectangle_maior.attemptResize(QgsLayoutSize(287.5, 200, QgsUnitTypes.LayoutMillimeters))
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
#mapa.setExtent(canvas.extent())
mapa.zoomToExtent(canvas.extent())
layout.addLayoutItem(mapa)
mapa.attemptMove(QgsLayoutPoint(10, 8, QgsUnitTypes.LayoutMillimeters))
mapa.attemptResize(QgsLayoutSize(200, 193, QgsUnitTypes.LayoutMillimeters))

# Criando Legenda
legenda = QgsLayoutItemLegend(layout)
legenda.setTitle("Legenda")
legenda_fonte = QFont("Arial", 11)
legenda.setStyleFont(QgsLegendStyle.Title, legenda_fonte)
legenda.setStyleFont(QgsLegendStyle.Subgroup, legenda_fonte)
legenda.setStyleFont(QgsLegendStyle.SymbolLabel, legenda_fonte)
legenda.attemptMove(QgsLayoutPoint(212, 65, QgsUnitTypes.LayoutMillimeters))
legenda.attemptResize(QgsLayoutSize(20, 20, QgsUnitTypes.LayoutMillimeters))
legenda.setItemOpacity(1.0)
legenda.setBackgroundEnabled(1)
legenda.setLinkedMap(mapa)
legenda.setLegendFilterByMapEnabled(True)
legenda.refresh()
layout.addLayoutItem(legenda)

# Isso adiciona rótulos ao mapa
layer = project.mapLayersByName('Área do imóvel')[0]
nome = ""
proprietario = ""
minicipio = ""
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
title.attemptResize(QgsLayoutSize(75, 60, QgsUnitTypes.LayoutMillimeters))
title.attemptMove(QgsLayoutPoint(215, 35, QgsUnitTypes.LayoutMillimeters))

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
subtitle.setFont(QFont("Arial", 12))
subtitle.setRect(0, 0, 0, 0)
subtitle.adjustSizeToText()
layout.addLayoutItem(subtitle)
subtitle.attemptMove(QgsLayoutPoint(215, 150, QgsUnitTypes.LayoutMillimeters))
subtitle.attemptResize(QgsLayoutSize(70, 50, QgsUnitTypes.LayoutMillimeters))

# inserir o Norte
north = QgsLayoutItemPicture(layout)
north.setPicturePath("C:\\Users\\raissa.alves\\Documents\\Atlas\\norte.svg")
layout.addLayoutItem(north)
north.attemptMove(QgsLayoutPoint(8, 5, QgsUnitTypes.LayoutMillimeters))
north.attemptResize(QgsLayoutSize(20, 20, QgsUnitTypes.LayoutMillimeters))

# inserir a logo
north = QgsLayoutItemPicture(layout)
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
title.setFont(QFont("Arial", 9))
title.adjustSizeToText()
title.setHAlign(Qt.AlignLeft)
layout.addLayoutItem(title)
title.attemptResize(QgsLayoutSize(100, 4, QgsUnitTypes.LayoutMillimeters))
title.attemptMove(QgsLayoutPoint(10, 201, QgsUnitTypes.LayoutMillimeters))

# inserindo grid
grid = QgsLayoutItemMapGrid("New grid", mapa)
mapa.grid().setEnabled(True)
mapa.grid().setUnits(QgsLayoutItemMapGrid.DynamicPageSizeBased)
# map.grid().setIntervalX(1000)
# map.grid().setIntervalY(1000)
mapa.grid().setMaximumIntervalWidth(100)
mapa.grid().setMinimumIntervalWidth(50)
mapa.grid().setAnnotationEnabled(True)
# map.grid().setGridLineColor(QColor(0, 176, 246))
mapa.grid().setGridLineWidth(0.1)
mapa.grid().setAnnotationPrecision(0)
mapa.grid().setAnnotationFrameDistance(1)
mapa.grid().setAnnotationFontColor(QColor(0, 0, 0))
# map.grid().setStyle(QgsLayoutItemMapGrid.FrameAnnotationsOnly)
# map.grid().setStyle(QgsLayoutItemMapGrid.Cross)
# map.grid().setStyle(QgsLayoutItemMapGrid.Markers)
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
escala.applyDefaultSize()
escala.attemptMove(QgsLayoutPoint(230, 135, QgsUnitTypes.LayoutMillimeters))
layout.addLayoutItem(escala)

# Adicionando a tabela de atributos
layer = project.mapLayersByName('Gerais')[0]
pdf_table = QgsLayoutItemAttributeTable.create(layout)
pdf_table.setVectorLayer(layer)
pdf_table.setMaximumNumberOfFeatures(40)
frame2 = QgsLayoutFrame(layout, pdf_table)
frame2.attemptResize(QgsLayoutSize(198.200, 224), True)
frame2.attemptMove(QgsLayoutPoint(120, 220, QgsUnitTypes.LayoutMillimeters))
pdf_table.addFrame(frame2)
pdf_table.setResizeMode(1)
