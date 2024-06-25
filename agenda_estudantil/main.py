from flet import *


def notas(page: Page):
    #Configurações iniciais
    page.window.max_width = 1080
    page.window.max_height = 1920
    page.window.min_width = 1080/3.5
    page.window.min_height = 1920/3.5
    page.window.width = 1080/3
    page.window.height = 1920/3
    
    page.bgcolor = "#1d2742"
    page.title = "Agenda Estudantil"
    # Fim das configurações
    
    # Contrução da estrutura da página
    titleRow = Row(
        controls=[
            Text(
                value="Notas",
                size=30,
                color=colors.WHITE
                )
            ]
        )
    gradesColumn = Column(
        scroll=True, #Permite deslizar a coluna
        horizontal_alignment= CrossAxisAlignment.CENTER,
        width=360
    )
    #Fim da construção da estrutura
    #Card Matéria
    disciplineCard = Card(
        width=324,
        height=128,
        shape=RoundedRectangleBorder(radius=7),
        elevation=5
    )
    
    gradesColumn.controls.append(disciplineCard)
    page.add(titleRow, gradesColumn)
    
    page.update()

app(notas)
