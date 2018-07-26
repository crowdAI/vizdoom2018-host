# vizdoom2018-singleplayer-host

### Usage

#### Build Image
```
pip install crowdai-repo2docker
export image_tag="vizdoom2018_host_image"
crowdai-repo2docker --no-run \
  --user-id 1001 \
  --user-name crowdai \
  --image-name ${image_tag} \
  --debug .
```

#### Run Host
```
export container_name="vizdoom2018_host"
export image_tag="vizdoom2018_host_image"
docker run \
    --user root \
    --net=host -ti \
    --rm --name \
    ${container_name} \
    --env="DISPLAY" --privileged \
    ${image_tag} \
    /home/crowdai/host.py <args>
```
The `args` in the above command can be replaced with : 
```
optional arguments:
  -h, --help            show this help message and exit
  -b BOTS_NUM, --bots BOTS_NUM
                        number of bots to add [0,15] (default: 0)
  -p PLAYERS_NUM, --players PLAYERS_NUM
                        number of players [1,16] (default: 1)
  -m MAP, --map MAP     map number [1,5] (default: 1)
  -t TIMELIMIT, --time TIMELIMIT
                        timelimit in minutes [1,999] (default: 5)
  -r RECORD_FILE, --record RECORD_FILE
                        file where the match will be recorded (default: None)
  -li LOG_INTERVAL, --log-interval LOG_INTERVAL
                        results logging inreval in minutes (default: None)
  -dc, --console        disables console output (default: False)
  -w, --watch           roam the map as a ghost spectator (default: True)
```

### Author(s)
* Sharada Mohanty <sharada.mohanty@epfl.ch>   
* Marek@wydmuch.poznan.pl   
* kempka.michal@gmail.com   
