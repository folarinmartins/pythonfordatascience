# df = read.csv('./Downloads/export.csv',header=FALSE);

# View(df);

# library(audio)
# audio.drivers()
# play(sin(1:10000/20)) # play a short sound of a fixed frequency

# x = rnorm(100)
# y = rnorm(100,sd=10)
# df = data.frame(x,y)
# # View(df)

# library(ggplot2)
# ggplot2::aes(x,y)
# ggplot(df,aes(x=x,y=y)) +  geom_point()
# 
# my_scatplot <- ggplot(mtcars,aes(x=wt,y=mpg))
# my_scatplot +  xlab('Weight (x 100lbs)') + ylab('Mileage (y mpg)')

# View(mtcars)

# library (datasets)
# data(iris)
# View(iris) 
# unique(iris$Species)

# library(GGally)
# ggpairs(iris, mapping=ggplot2::aes(colour = Species))

# https://dataplatform.cloud.ibm.com/ 
# Creating an interactive map in R with Shiny
library(shiny)
library(leaflet)
r_colors <- rgb(t(col2rgb(colors()) / 255))
names(r_colors) <- colors()
ui <- fluidPage(
  leafletOutput("mymap"),
  p(),
  actionButton("recalc", "New points"),
  p(),
  textOutput("coordinates")
)
server <- function(input, output, session) {
  points <- eventReactive(input$recalc, {
    points = cbind(rnorm(40) * 2 + 13, rnorm(40) + 48)
    
    observeEvent(input$Map_shape_click, { # update the location selectInput on map clicks
      output$coordinates <- renderText({
        "You have selected this"
      })
    })
    
    output$mymap <- renderLeaflet({
      leaflet() %>%
        addProviderTiles(providers$Stamen.TonerLite,
                         options = providerTileOptions(noWrap = TRUE)
        ) %>%
        
        addMarkers(data = points())
    })
  })
}


shinyApp(ui, server)

