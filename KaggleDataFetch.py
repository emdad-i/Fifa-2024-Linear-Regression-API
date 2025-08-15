import kaggle

kaggle.api.authenticate()

kaggle.api.dataset_download_file(dataset='stefanoleone992/ea-sports-fc-24-complete-player-dataset',file_name='male_players.csv',path='data')