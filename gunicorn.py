
import multiprocessing

CPU_COUNT = multiprocessing.cpu_count()
bind = '0.0.0.0:80'
backlog = 1000  # num of connections waiting before error is returned

# DO NOT CHANGE THIS, it makes docker sad and thrashy, it will not increase
# throughput, instead you should increase the count of container instances
# suggested setting according to gunicorn docs is between 1 and 4
workers = CPU_COUNT * 1
threads = CPU_COUNT * 4

# log to std out
capture_output = True
accesslog = '-'


# assume this is the longest running request time lol
# the load balancer will timeout and throw a 504 on aws
timeout = 180

# suggested setting when running behind load balancer
# according to https://serverfault.com/questions/782022/keepalive-setting-for-gunicorn-behind-elb-without-nginx
keepalive = 75

# required or the workers will overwrite each others schema cache and restarts will die
preload_app = True

worker_class = "gthread"
