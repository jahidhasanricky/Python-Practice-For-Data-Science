gme = yf.Ticker(GME)
gme_data = gme.history(period=max)
make_graph(gme_data, GME)
