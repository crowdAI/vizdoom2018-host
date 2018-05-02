# vizdoom2018-singleplayer-host

### Usage

#### Build Image
```
pip install jupyter-repo2docker
export image_tag="vizdoom2018_singleplayer_host_image"
repo2docker --no-run \
  --user-id 1001 \
  --user-name crowdai \
  --image-name ${image_tag} \
  --debug .
```

#### Run Host
```
export container_name="vizdoom2018_singleplayer_host"
export image_tag="vizdoom2018_singleplayer_host_image"
docker run \
    --user root \
    --net=host -ti \
    --rm --name \
    ${container_name} \
    --env="DISPLAY" --privileged \
    ${image_tag} \
    /home/crowdai/run.sh
```

### Author(s)
* Sharada Mohanty <sharada.mohanty@epfl.ch>   
* Marek@wydmuch.poznan.pl   
* kempka.michal@gmail.com   
