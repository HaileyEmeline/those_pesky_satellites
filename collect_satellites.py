from skyfield.api import load 

#TODO: Pull all satellites, track only those above horizon and within x range of FOV, print them

max_days = 0.5
name = 'stations.json'

url = "https://celestrak.org/NORAD/elements/gp.php?GROUP=active&FORMAT=json"

if not load.exists(name) or load.days_old(name) >= max_days:
    load.download(url, filename=name)

