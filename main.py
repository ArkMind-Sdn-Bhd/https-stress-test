from locust import HttpUser, task


class DfStressTest(HttpUser):

    URL = ""
    AUTH_TOKEN = ""

    @task
    def on_login(self):
        self.client.post(self.URL,
                         headers={"authorization": "Token " + self.AUTH_TOKEN},
                         json={"username": "SUPER-ADMIN", "password": "password"}
                         )