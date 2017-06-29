# Make state borders red
borders <- list(color = toRGB("red"))
# Set up some mapping options
map_options <- list(
  scope = 'usa',
  projection = list(type = 'albers usa'),
  showlakes = TRUE,
  lakecolor = toRGB('white')
)
map_plot_gatherer <- htmltools::tagList()
col_counter <- 1
for (msn_code in msn_codes$MSN) {
  plot_df <- msn_subsets_mtrx[[2, col_counter]]
  #Select a specific year
  year <- "2000"
  plot_df <- subset(plot_df, Year == year)
  if (nrow(plot_df) > 0) {
    map_plot_gatherer[[col_counter]] <- plot_ly(z = ~plot_df$value, text = ~plot_df$value, locations = ~plot_df$State, type = 'choropleth', locationmode = 'USA-states', color = plot_df$Value, colors = 'Blues', marker = list(line = borders)) %>%
    layout(title = paste("Debug sum value is -", sum(subset(plot_df, MSN == msn_code)$value)), geo = map_options)
  #The above is a debug title to see whether I realy am using different data sets
  #This is what the title should be:
  #layout(title = paste(msn_codes[msn_codes$MSN == msn_code, 2], "-", year, "-", msn_codes[msn_codes$MSN == msn_code, 4]), geo = map_options)
  }
  col_counter <- col_counter + 1
  #If more than two maps are created, then there is no data, just blank maps. See:
  #https://github.com/ropensci/plotly/issues/273
  #Stopping when col_counter > 2 works, to show two maps. Trying to show three did not work.
  if (col_counter > 3) {
    break
  }
}
map_plot_gatherer
