from locust import HttpLocust, TaskSet, between

def login(l):
    l.client.post("/wp-login.php", {"username":"locust", "password":"aTjZmW06h3LHA0Ztz2ryzPeh"})

def index(l):
    l.client.get("/")

def profile(l):
    l.client.get("/services")

class UserBehavior(TaskSet):
    tasks = {index: 2, profile: 1}

    def on_start(self):
        login(self)

    # def on_stop(self):
    #     logout(self)

class WebsiteUser(HttpLocust):
    task_set = UserBehavior
    wait_time = between(5.0, 9.0)