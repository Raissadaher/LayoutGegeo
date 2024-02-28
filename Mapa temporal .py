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
from qgis.core import *
from qgis.utils import *


def imprime_layers():
    names = [mapLayers.name() for mapLayers in QgsProject.instance().mapLayers().values()]
    print(names)

# variaveis globais
project = QgsProject.instance()
manager = project.layoutManager()
layout = QgsPrintLayout(project)
layoutname = f"pagina_1_{random.randint(1, 500)}"
layout.initializeDefaults()
layout.setName(layoutname)
manager.addLayout(layout)

# adicionando poligono maior
rectangle_maior = QgsLayoutItemShape(layout)
rectangle_maior.setShapeType(QgsLayoutItemShape.Rectangle)
rectangle_maior.setRect(0, 0, 0, 0)
layout.addLayoutItem(rectangle_maior)
rectangle_maior.attemptMove(QgsLayoutPoint(5, 5, QgsUnitTypes.LayoutMillimeters))
rectangle_maior.attemptResize(QgsLayoutSize(287.5, 200, QgsUnitTypes.LayoutMillimeters))
iface.openLayoutDesigner(layout)

#adicionando_poligono_titulo
rectangle_titulo = QgsLayoutItemShape(layout)
rectangle_titulo.setShapeType(QgsLayoutItemShape.Rectangle)
rectangle_titulo.setRect(0, 0, 0, 0)
layout.addLayoutItem(rectangle_titulo)
rectangle_titulo.attemptMove(QgsLayoutPoint(212, 8, QgsUnitTypes.LayoutMillimeters))
rectangle_titulo.attemptResize(QgsLayoutSize(77, 193.3, QgsUnitTypes.LayoutMillimeters))

#renderizar mapa01
area_imovel :QgsMapLayer = project.mapLayersByName('Área do imóvel')[0]
mapa01 = QgsLayoutItemMap(layout)
mapa01.setId("mapa_mestre")
mapa01.setAtlasDriven(True)
mapa01.setFrameEnabled(True)
mapa01.setRect(0, 0, 200, 188)
mapa01.setLayers([area_imovel, centroides_gerais, area_de_preservacao_permanente, area_imovel, area_supressao, reserva_legal])
mapa01.setExtent(area_imovel.extent())
layout.addLayoutItem(mapa01)
mapa01.attemptMove(QgsLayoutPoint(8, 8, QgsUnitTypes.LayoutMillimeters))
mapa01.attemptResize(QgsLayoutSize(99, 94, QgsUnitTypes.LayoutMillimeters))

#adicionando_grid_mapa_01
grid = QgsLayoutItemMapGrid("New grid", mapa01)
mapa01.grid().setEnabled(True)
mapa01.grid().setUnits(QgsLayoutItemMapGrid.DynamicPageSizeBased)
mapa01.grid().setMaximumIntervalWidth(45)
mapa01.grid().setMinimumIntervalWidth(10)
mapa01.grid().setAnnotationEnabled(True)
mapa01.grid().setGridLineWidth(0.1)
mapa01.grid().setAnnotationPrecision(0)
mapa01.grid().setAnnotationFrameDistance(0)
mapa01.grid().setAnnotationFontColor(QColor(0, 0, 0))
mapa01.grid().setAnnotationFont(QFont('Arial', 8))
mapa01.grid().setAnnotationDisplay(QgsLayoutItemMapGrid.HideAll, QgsLayoutItemMapGrid.Right)
mapa01.grid().setAnnotationDisplay(QgsLayoutItemMapGrid.ShowAll, QgsLayoutItemMapGrid.Top)
mapa01.grid().setAnnotationDisplay(QgsLayoutItemMapGrid.HideAll, QgsLayoutItemMapGrid.Bottom)
mapa01.grid().setAnnotationPosition(QgsLayoutItemMapGrid.OutsideMapFrame, QgsLayoutItemMapGrid.Bottom)
mapa01.grid().setAnnotationDirection(QgsLayoutItemMapGrid.Horizontal, QgsLayoutItemMapGrid.Bottom)
mapa01.grid().setAnnotationPosition(QgsLayoutItemMapGrid.OutsideMapFrame, QgsLayoutItemMapGrid.Left)
mapa01.grid().setAnnotationDirection(QgsLayoutItemMapGrid.Vertical, QgsLayoutItemMapGrid.Left)
mapa01.grid().setAnnotationDisplay(QgsLayoutItemMapGrid.ShowAll, QgsLayoutItemMapGrid.Left)


#barra_de_escala_mapa01
escala = QgsLayoutItemScaleBar(layout)
escala.setStyle('Caixa Simples')
escala.setLinkedMap(mapa01)
escala.setHeight(1)
escala.setLabelBarSpace(1)
escala.setBoxContentSpace(0.1)
escala.update()
escala.setBackgroundEnabled(True)
escala.setFont(QFont('Arial', 6))
escala.applyDefaultSize()
escala.attemptResize(QgsLayoutSize(5, 5, QgsUnitTypes.LayoutMillimeters))
escala.attemptMove(QgsLayoutPoint(85, 95, QgsUnitTypes.LayoutMillimeters))
layout.addLayoutItem(escala)


#renderizar_mapa02():
area_imovel :QgsMapLayer = project.mapLayersByName('Área do imóvel')[0]
mapa02 = QgsLayoutItemMap(layout)
mapa02.setId("mapa02")
mapa02.setAtlasDriven(True)
mapa02.setFrameEnabled(True)
mapa02.setRect(0, 0, 200, 188)
mapa02.setLayers([area_imovel, centroides_gerais, area_de_preservacao_permanente, area_imovel, area_supressao, reserva_legal])
mapa02.setExtent(area_imovel.extent())
layout.addLayoutItem(mapa02)
mapa02.attemptMove(QgsLayoutPoint(110, 8, QgsUnitTypes.LayoutMillimeters))
mapa02.attemptResize(QgsLayoutSize(99.699, 94.286, QgsUnitTypes.LayoutMillimeters))


#barra_de_escala_mapa02
escala = QgsLayoutItemScaleBar(layout)
escala.setStyle('Caixa Simples')
escala.setLinkedMap(mapa01)
escala.setHeight(1)
escala.setLabelBarSpace(1)
escala.setBoxContentSpace(0.1)
escala.update()
escala.setBackgroundEnabled(True)
escala.setFont(QFont('Arial', 6))
escala.applyDefaultSize()
escala.attemptResize(QgsLayoutSize(5, 5, QgsUnitTypes.LayoutMillimeters))
escala.attemptMove(QgsLayoutPoint(187, 95, QgsUnitTypes.LayoutMillimeters))
layout.addLayoutItem(escala)


#adicionando_grid_mapa_02
grid = QgsLayoutItemMapGrid("New grid", mapa01)
mapa02.grid().setEnabled(True)
mapa02.grid().setUnits(QgsLayoutItemMapGrid.DynamicPageSizeBased)
mapa02.grid().setMaximumIntervalWidth(45)
mapa02.grid().setMinimumIntervalWidth(10)
mapa02.grid().setAnnotationEnabled(True)
# map.grid().setGridLineColor(QColor(0, 176, 246))
mapa02.grid().setGridLineWidth(0.1)
mapa02.grid().setAnnotationPrecision(0)
mapa02.grid().setAnnotationFrameDistance(0)
mapa02.grid().setAnnotationFontColor(QColor(0, 0, 0))
mapa02.grid().setAnnotationFont(QFont('Arial', 8))
mapa02.grid().setAnnotationDisplay(QgsLayoutItemMapGrid.HideAll, QgsLayoutItemMapGrid.Right)
mapa02.grid().setAnnotationDisplay(QgsLayoutItemMapGrid.ShowAll, QgsLayoutItemMapGrid.Top)
mapa02.grid().setAnnotationDisplay(QgsLayoutItemMapGrid.HideAll, QgsLayoutItemMapGrid.Bottom)
mapa02.grid().setAnnotationPosition(QgsLayoutItemMapGrid.OutsideMapFrame, QgsLayoutItemMapGrid.Bottom)
mapa02.grid().setAnnotationDirection(QgsLayoutItemMapGrid.Horizontal, QgsLayoutItemMapGrid.Bottom)
mapa02.grid().setAnnotationPosition(QgsLayoutItemMapGrid.OutsideMapFrame, QgsLayoutItemMapGrid.Left)
mapa02.grid().setAnnotationDirection(QgsLayoutItemMapGrid.Vertical, QgsLayoutItemMapGrid.Left)
mapa02.grid().setAnnotationDisplay(QgsLayoutItemMapGrid.ShowAll, QgsLayoutItemMapGrid.Left)

#renderizar_mapa_03
area_imovel :QgsMapLayer = project.mapLayersByName('Área do imóvel')[0]
mapa03 = QgsLayoutItemMap(layout)
mapa03.setAtlasDriven(True)
mapa03.setFrameEnabled(True)
mapa03.setRect(0, 0, 200, 188)
mapa03.setLayers([area_imovel, centroides_gerais, area_de_preservacao_permanente, area_imovel, area_supressao, reserva_legal])
mapa03.setExtent(area_imovel.extent())
layout.addLayoutItem(mapa03)
mapa03.attemptMove(QgsLayoutPoint(8, 107, QgsUnitTypes.LayoutMillimeters))
mapa03.attemptResize(QgsLayoutSize(99.699, 94.286, QgsUnitTypes.LayoutMillimeters))

#barra_de_escala_mapa03():
escala = QgsLayoutItemScaleBar(layout)
escala.setStyle('Caixa Simples')
escala.setLinkedMap(mapa01)
escala.setHeight(1)
escala.setLabelBarSpace(1)
escala.setBoxContentSpace(0.1)
escala.update()
escala.setBackgroundEnabled(True)
escala.setFont(QFont('Arial', 6))
escala.applyDefaultSize()
escala.attemptResize(QgsLayoutSize(5, 5, QgsUnitTypes.LayoutMillimeters))
escala.attemptMove(QgsLayoutPoint(85, 195, QgsUnitTypes.LayoutMillimeters))
layout.addLayoutItem(escala)

#adicionando_grid_mapa_03
grid = QgsLayoutItemMapGrid("New grid", mapa01)
mapa03.grid().setEnabled(True)
mapa03.grid().setUnits(QgsLayoutItemMapGrid.DynamicPageSizeBased)
mapa03.grid().setMaximumIntervalWidth(45)
mapa03.grid().setMinimumIntervalWidth(10)
mapa03.grid().setAnnotationEnabled(True)
mapa03.grid().setGridLineWidth(0.1)
mapa03.grid().setAnnotationPrecision(0)
mapa03.grid().setAnnotationFrameDistance(0)
mapa03.grid().setAnnotationFontColor(QColor(0, 0, 0))
mapa03.grid().setAnnotationFont(QFont('Arial', 8))
mapa03.grid().setAnnotationDisplay(QgsLayoutItemMapGrid.HideAll, QgsLayoutItemMapGrid.Right)
mapa03.grid().setAnnotationDisplay(QgsLayoutItemMapGrid.ShowAll, QgsLayoutItemMapGrid.Top)
mapa03.grid().setAnnotationDisplay(QgsLayoutItemMapGrid.HideAll, QgsLayoutItemMapGrid.Bottom)
mapa03.grid().setAnnotationPosition(QgsLayoutItemMapGrid.OutsideMapFrame, QgsLayoutItemMapGrid.Bottom)
mapa03.grid().setAnnotationDirection(QgsLayoutItemMapGrid.Horizontal, QgsLayoutItemMapGrid.Bottom)
mapa03.grid().setAnnotationPosition(QgsLayoutItemMapGrid.OutsideMapFrame, QgsLayoutItemMapGrid.Left)
mapa03.grid().setAnnotationDirection(QgsLayoutItemMapGrid.Vertical, QgsLayoutItemMapGrid.Left)
mapa03.grid().setAnnotationDisplay(QgsLayoutItemMapGrid.ShowAll, QgsLayoutItemMapGrid.Left)

#renderizar_mapa_04
area_imovel :QgsMapLayer = project.mapLayersByName('Área do imóvel')[0]
mapa04 = QgsLayoutItemMap(layout)
mapa04.setAtlasDriven(True)
mapa04.setFrameEnabled(True)
mapa04.setRect(0, 0, 200, 188)
mapa04.setLayers([area_imovel, centroides_gerais, area_de_preservacao_permanente, area_imovel, area_supressao, reserva_legal])
mapa04.setExtent(area_imovel.extent())
layout.addLayoutItem(mapa04)
mapa04.attemptMove(QgsLayoutPoint(110, 107, QgsUnitTypes.LayoutMillimeters))
mapa04.attemptResize(QgsLayoutSize(99.699, 94.286, QgsUnitTypes.LayoutMillimeters))

#barra_de_escala_mapa04
escala = QgsLayoutItemScaleBar(layout)
escala.setStyle('Caixa Simples')
escala.setLinkedMap(mapa01)
escala.setHeight(1)
escala.setLabelBarSpace(1)
escala.setBoxContentSpace(0.1)
escala.update()
escala.setBackgroundEnabled(True)
escala.setFont(QFont('Arial', 6))
escala.applyDefaultSize()
escala.attemptResize(QgsLayoutSize(5, 5, QgsUnitTypes.LayoutMillimeters))
escala.attemptMove(QgsLayoutPoint(187, 195, QgsUnitTypes.LayoutMillimeters))
layout.addLayoutItem(escala)

#adicionando_grid_mapa_04():
grid = QgsLayoutItemMapGrid("New grid", mapa01)
mapa04.grid().setEnabled(True)
mapa04.grid().setUnits(QgsLayoutItemMapGrid.DynamicPageSizeBased)
mapa04.grid().setMaximumIntervalWidth(45)
mapa04.grid().setMinimumIntervalWidth(10)
mapa04.grid().setAnnotationEnabled(True)
mapa04.grid().setGridLineWidth(0.1)
mapa04.grid().setAnnotationPrecision(0)
mapa04.grid().setAnnotationFrameDistance(0)
mapa04.grid().setAnnotationFontColor(QColor(0, 0, 0))
mapa04.grid().setAnnotationFont(QFont('Arial', 8))
mapa04.grid().setAnnotationDisplay(QgsLayoutItemMapGrid.HideAll, QgsLayoutItemMapGrid.Right)
mapa04.grid().setAnnotationDisplay(QgsLayoutItemMapGrid.ShowAll, QgsLayoutItemMapGrid.Top)
mapa04.grid().setAnnotationDisplay(QgsLayoutItemMapGrid.HideAll, QgsLayoutItemMapGrid.Bottom)
mapa04.grid().setAnnotationPosition(QgsLayoutItemMapGrid.OutsideMapFrame, QgsLayoutItemMapGrid.Bottom)
mapa04.grid().setAnnotationDirection(QgsLayoutItemMapGrid.Horizontal, QgsLayoutItemMapGrid.Bottom)
mapa04.grid().setAnnotationPosition(QgsLayoutItemMapGrid.OutsideMapFrame, QgsLayoutItemMapGrid.Left)
mapa04.grid().setAnnotationDirection(QgsLayoutItemMapGrid.Vertical, QgsLayoutItemMapGrid.Left)
mapa04.grid().setAnnotationDisplay(QgsLayoutItemMapGrid.ShowAll, QgsLayoutItemMapGrid.Left)

# Mapa Localização
#frame_symbol = QgsFillSymbol.defaultSymbol(QgsWkbTypes.PolygonGeometry)
#frame_symbol.setColor(QColor(255, 50, 50, 50))
municipios :QgsMapLayer = project.mapLayersByName('Municipios')[0]
pais :QgsMapLayer = project.mapLayersByName('Brasil')[0]
mapa05 = QgsLayoutItemMap(layout)
mapa05.setId("mapa_municipios")
mapa05.setAtlasDriven(True)
mapa05.setFrameEnabled(True)
mapa05.setRect(0, 0, 170, 0)
src_crs = QgsCoordinateReferenceSystem(4674)
mapa05.setCrs(src_crs)
mapa05.setLayers([municipios, pais])
mapa05.setExtent(municipios.extent())
mapa05.overview().setLinkedMap(mapa01)
#mapa01.overview().setFrameSymbol(frame_symbol)
props2 = {"color": "0,255,0,100", "color_border": "red", "width_border": "2.0"}
fillSymbol2 = QgsFillSymbol.createSimple(props2)
mapa05.overview().setFrameSymbol(fillSymbol2)
mapa05.setScale(6500000)
layout.addLayoutItem(mapa05)
mapa05.attemptMove(QgsLayoutPoint(216, 70, QgsUnitTypes.LayoutMillimeters))
mapa05.attemptResize(QgsLayoutSize(69.700, 43.109, QgsUnitTypes.LayoutMillimeters))

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


# # Linkando os mapas
# project = QgsProject.instance()
# layout_manager = project.layoutManager()
# layouts = layout_manager.printLayouts()
# if layouts:
#     layout = layouts[0]
#     map_items = [item for item in layout.items() if isinstance(item, QgsLayoutItemMap)]
#     if len(map_items) >= 4:
#         mapa01 = map_items[0]
#         mapa02 = map_items[1]
#         mapa03 = map_items[2]
#         mapa04 = map_items[3]
#         centroid = mapa01.extent().center()
#
#         diffx1 = mapa02.extent().xMaximum() - mapa02.extent().xMinimum()
#         diffy1 = mapa03.extent().yMaximum() - mapa03.extent().yMinimum()
#         diffy1 = mapa04.extent().yMaximum() - mapa04.extent().yMinimum()
#
#         diffx2 = mapa02.extent().xMaximum() - mapa02.extent().xMinimum()
#         diffy2 = mapa03.extent().yMaximum() - mapa03.extent().yMinimum()
#         diffy2 = mapa04.extent().yMaximum() - mapa04.extent().yMinimum()
#
#         newExtent1 = QgsRectangle(centroid[0] - (diffx1/2), centroid[1] - (diffy1/2), centroid[0] + (diffx1/2), centroid[1] + (diffy1/2))
#         newExtent2 = QgsRectangle(centroid[0] - (diffx2/2), centroid[1] - (diffy2/2), centroid[0] + (diffx2/2), centroid[1] + (diffy2/2))
#         newExtent3 = QgsRectangle(centroid[0] - (diffx2/2), centroid[1] - (diffy2/2), centroid[0] + (diffx2/2), centroid[1] + (diffy2/2))
#
#         mapa02.setExtent(newExtent1)
#         mapa03.setExtent(newExtent2)
#         mapa04.setExtent(newExtent3)
#


#legenda
legenda = QgsLayoutItemLegend(layout)
legenda.setTitle("Legenda")
legenda_fonte = QFont("Arial", 8)
legenda.setStyleFont(QgsLegendStyle.Title, legenda_fonte)
legenda.setStyleFont(QgsLegendStyle.Subgroup, legenda_fonte)
legenda.setStyleFont(QgsLegendStyle.SymbolLabel, legenda_fonte)
legenda.attemptMove(QgsLayoutPoint(216, 120, QgsUnitTypes.LayoutMillimeters))
legenda.attemptResize(QgsLayoutSize(20, 20, QgsUnitTypes.LayoutMillimeters))
legenda.setLinkedMap(mapa01)
legenda.setItemOpacity(1.0)
legenda.setBackgroundEnabled(0.5)
legenda.setLegendFilterByMapEnabled(True)
legenda.refresh()
layout.addLayoutItem(legenda)

#adicionando_titulo:
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

dados = 'MAPA DE ANÁLISE TEMPORAL' + '\n' 'Propriedade: ' + nome + '\n' + 'Proprietário: ' + proprietario + '\n' + 'CPF/CNPJ: ' + cpf + '\n' + 'Municipio: ' + municipio + '\n' + 'Processo SEI:' + '\n'
title = QgsLayoutItemLabel(layout)
title.setText(dados)
title.setFont(QFont("Arial", 9))
title.adjustSizeToText()
title.setHAlign(Qt.AlignCenter)
layout.addLayoutItem(title)
title.attemptResize(QgsLayoutSize(75, 40, QgsUnitTypes.LayoutMillimeters))
title.attemptMove(QgsLayoutPoint(213, 35, QgsUnitTypes.LayoutMillimeters))

dados_propriedade_subtitulo = f"""Sistema Geodésico: Sirgas 2000
    Sistema de coordenada: Projetado-UTM
    Formato: A4
    Escala numérica: 1:{math.floor(mapa01.scale())}
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

#inserindo_norte
norte = QgsLayoutItemPicture(layout)
norte.setPicturePath("C:\\Users\\raissa.alves\\Documents\\Atlas\\norte.svg")
layout.addLayoutItem(norte)
norte.setItemOpacity(1.0)
norte.setBackgroundEnabled(True)
norte.attemptMove(QgsLayoutPoint(245, 158, QgsUnitTypes.LayoutMillimeters))
norte.attemptResize(QgsLayoutSize(15, 15, QgsUnitTypes.LayoutMillimeters))

#inserindo_a_logo
logo = QgsLayoutItemPicture(layout)
logo.setPicturePath("C:/Users/raissa.alves/Documents/Atlas/Semad_Abreviada_positivo.png")
layout.addLayoutItem(logo)
logo.attemptMove(QgsLayoutPoint(214, 10, QgsUnitTypes.LayoutMillimeters))
logo.attemptResize(QgsLayoutSize(75, 20.5, QgsUnitTypes.LayoutMillimeters))

#inserindo_o_car
area_imovel = project.mapLayersByName('Área do imóvel')[0]
car = ""
# Verifica se a camada está válida
if area_imovel is not None:
# Itera sobre as features selecionadas
    for feature in area_imovel.getFeatures():
        car = feature['cod_imovel']

dados = 'CAR: ' + car
title = QgsLayoutItemLabel(layout)
title.setText(dados)
title.setFont(QFont("Arial", 7))
title.adjustSizeToText()
title.setHAlign(Qt.AlignLeft)
layout.addLayoutItem(title)
title.attemptResize(QgsLayoutSize(75, 4, QgsUnitTypes.LayoutMillimeters))
title.attemptMove(QgsLayoutPoint(10, 202, QgsUnitTypes.LayoutMillimeters))


#inserindo_texto_mapa_01
dados01 = '12/2024'
map_label = QgsLayoutItemLabel(layout)
map_label.setText(dados01)
map_label.setFont(QFont("Arial", 9))
map_label.setItemOpacity(1.0)
map_label.setBackgroundEnabled(1)
map_label.adjustSizeToText()
layout.addLayoutItem(map_label)
map_label.attemptResize(QgsLayoutSize(12, 3, QgsUnitTypes.LayoutMillimeters))
map_label.attemptMove(QgsLayoutPoint(8.5, 98, QgsUnitTypes.LayoutMillimeters))


#inserindo_texto_mapa_02
dados02 = '12/2024'
map_label = QgsLayoutItemLabel(layout)
map_label.setText(dados02)
map_label.setFont(QFont("Arial", 9))
map_label.setItemOpacity(1.0)
map_label.setBackgroundEnabled(1)
map_label.adjustSizeToText()
layout.addLayoutItem(map_label)
map_label.attemptResize(QgsLayoutSize(12, 3, QgsUnitTypes.LayoutMillimeters))
map_label.attemptMove(QgsLayoutPoint(111, 98, QgsUnitTypes.LayoutMillimeters))

#inserindo_texto_mapa_03
dados03 = '12/2024'
map_label = QgsLayoutItemLabel(layout)
map_label.setText(dados03)
map_label.setFont(QFont("Arial", 9))
map_label.setItemOpacity(1.0)
map_label.setBackgroundEnabled(1)
map_label.adjustSizeToText()
layout.addLayoutItem(map_label)
map_label.attemptResize(QgsLayoutSize(12, 3, QgsUnitTypes.LayoutMillimeters))
map_label.attemptMove(QgsLayoutPoint(8.5, 198, QgsUnitTypes.LayoutMillimeters))

#inserindo_texto_mapa_04
dados04 = '12/2024'
map_label = QgsLayoutItemLabel(layout)
map_label.setText(dados04)
map_label.setFont(QFont("Arial", 9))
map_label.setItemOpacity(1.0)
map_label.setBackgroundEnabled(1)
map_label.adjustSizeToText()
layout.addLayoutItem(map_label)
map_label.attemptResize(QgsLayoutSize(12, 3, QgsUnitTypes.LayoutMillimeters))
map_label.attemptMove(QgsLayoutPoint(111, 198, QgsUnitTypes.LayoutMillimeters))