#!/usr/bin/python3

import cgi
import subprocess #for running os commands
import time #for delaying in loading the output

print("content-type: text/html")
print()


#print("Scytop")

#print(subprocess.getoutput("date"))
#time.sleep(5)
#print(subprocess.getoutput("cal"))


field =  cgi.FieldStorage()
cmd = field.getvalue("x")


if "runpod"  in cmd.split():
    pod_name = cmd.split()[1]
    image_name = cmd.split()[2]
    print(subprocess.getoutput("sudo kubectl run {} --image={}".format(pod_name, image_name)))
elif "delpod" in cmd.split():
    pod_name = cmd.split()[1]
    print(subprocess.getoutput("sudo kubectl delete pod {}".format(pod_name)))
elif "deldeploy" in cmd.split():
    deployment_name = cmd.split()[1]
    print(subprocess.getoutput("sudo kubectl delete deployment {}".format(deployment_name)))
elif "createdeploy" in cmd.split():
    deployment_name = cmd.split()[1]
    image_name = cmd.split()[2]
    print(subprocess.getoutput("sudo kubectl create deployment {} --image={}".format(deployment_name, image_name)))
elif "expose" in cmd.split():
    deployment_name = cmd.split()[1]
    port_no = cmd.split()[2]
    print(subprocess.getoutput("sudo kubectl expose deployment {} --type=NodePort --port={}".format(deployment_name, port_no)))
elif "replicas" in cmd.split():
    deployment_name = cmd.split()[1]
    replicas = cmd.split()[2]
    print(subprocess.getoutput("sudo kubectl scale deployment {} --replicas={}".format(deployment_name, replicas)))
elif "delete" in cmd.split():
    print(subprocess.getoutput("sudo kubectl delete all --all"))
elif "show" in cmd.split():
    print(subprocess.getoutput("sudo kubectl get pods"))



