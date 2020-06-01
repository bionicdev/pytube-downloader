from pytube import Playlist


playlist='https://www.youtube.com/watch?v=ph-gNsKX2oA&list=PLl-K7zZEsYLnt1-3lFiY89YtAFQzLZo-O'

pl = Playlist("https://www.youtube.com/watch?v=Edpy1szoG80&list=PL153hDY-y1E00uQtCVCVC8xJ25TYX8yPU")

pl.download_all('./downloads')