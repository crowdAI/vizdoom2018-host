# vizdoom2018-singleplayer-host

### Usage

#### Build Image
```
pip install jupyter-repo2docker
repo2docker --no-run \
  --user-id 1001 \
  --user-name crowdai \
  --image-name vizdoom2018_singleplayer_host_image \
  --debug .
```

#### Run Host
```
docker run \
  --name vizdoom2018_singleplayer_host \
  -it vizdoom2018_singleplayer_host_image \
  --net=host \
  --env="DISPLAY" \
  --privileged \
  /home/crowdai/run.sh
```

### Author(s)
* Sharada Mohanty <sharada.mohanty@epfl.ch>   
* Marek@wydmuch.poznan.pl   
* kempka.michal@gmail.com   
