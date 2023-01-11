from locust import HttpUser, task


class DfStressTest(HttpUser):

    URL = "https://acosb.parksoncredit.com.my:8088/api/MyTask/CP/Overview"
    AUTH_TOKEN = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJodHRwOi8vc2NoZW1hcy54bWxzb2FwLm9yZy93cy8yMDA1LzA1L2lkZW50aXR5L2NsYWltcy9uYW1lIjoiUEMwMDBfUkFIQVlVIiwiaHR0cDovL3NjaGVtYXMueG1sc29hcC5vcmcvd3MvMjAwNS8wNS9pZGVudGl0eS9jbGFpbXMvbmFtZWlkZW50aWZpZXIiOiI5ODUyNjQ0Ni0wNGM4LTQxNzItYjJlNS1kMzk0MmYxNTM3ZDciLCJwYXNzd29yZCI6IjM2MzFCMzgzQTE0QzBDQTM0MzE4QkZBMjFCMUEwODcwIiwibmJmIjoxNjczNDE2NTk2LCJleHAiOjE2NzM1MDI5OTYsImlzcyI6Imh0dHBzOi8vYWNvc2IucGFya3NvbmNyZWRpdC5jb20ubXk6ODA4OCIsImF1ZCI6Imh0dHBzOi8vYWNvc2IucGFya3NvbmNyZWRpdC5jb20ubXk6ODA4OCJ9.gXfuKkDVlupyScUDeQUWnGeTbPfC0G19NuESVXgFNWY"

    @task
    def on_attack(self):
        self.client.get(
            self.URL,
                         headers={"Token": self.AUTH_TOKEN},
                        #  json={
                        #     "pageNumber": 1,
                        #     "pageSize": 10,
                        #     "userId": "P2028001_TEST",
                        #     "loanNo": "LN00305137",
                        #     "dealerCode": "P2028001"
                        # }
                         )