# Docker

**Containerization** - Operating system level virtualization
<br>
<br>  
Why containerize?
  - simplify versioning and dependecy management

### Terminology
- A container is an instance of an image
- a docker file builds an image
- every docker file starts with a FROM statement
  - This is kind of like an import statement
  - It determines the base image upon which you can build upon


smaller images are faster to load
- 1gb image can take like a minute to load
- 30 mb image will load almost instantly
> This is important because have a very large image would be annoying if you have to repeatedly run tasks that would normally take only a few seconds to run. Cause now that could take ocer a minute every time you want to run it. However a large image isn't a big deal if the task you are going to run takes hours.


The `RUN` command runs things when the container starts up   

Write thinngs to docker volume instead of the docker runtime layer.
- define a docker volume with the `VOLUME` command

`EXPOSE` command makes a port available to the host

Basically docker is good for containerizing an environment with certain requirements that can be transported and run on any OS.