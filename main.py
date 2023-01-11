from locust import HttpUser, task


class DfStressTest(HttpUser):

    URL = "https://acosb.parksoncredit.com.my:8088/api/LoanApplication/SearchApplicationResultPage"
    AUTH_TOKEN = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJodHRwOi8vc2NoZW1hcy54bWxzb2FwLm9yZy93cy8yMDA1LzA1L2lkZW50aXR5L2NsYWltcy9uYW1lIjoiUDIwMjgwMDFfVEVTVCIsImh0dHA6Ly9zY2hlbWFzLnhtbHNvYXAub3JnL3dzLzIwMDUvMDUvaWRlbnRpdHkvY2xhaW1zL25hbWVpZGVudGlmaWVyIjoiMzQ4YzhlYWQtM2I2Ni00NThlLWFhY2YtODdhMDU4NzQ2MDJiIiwicGFzc3dvcmQiOiI1RjREQ0MzQjVBQTc2NUQ2MUQ4MzI3REVCODgyQ0Y5OSIsIm5iZiI6MTY3MzQxODU4NiwiZXhwIjoxNjczNTA0OTg2LCJpc3MiOiJodHRwczovL2Fjb3NiLnBhcmtzb25jcmVkaXQuY29tLm15OjgwODgiLCJhdWQiOiJodHRwczovL2Fjb3NiLnBhcmtzb25jcmVkaXQuY29tLm15OjgwODgifQ.zHqv1hkRVZ25ZgwC2qGSgbpHo_xcWO6CdDTX_NVW8DI"

    @task
    def on_attack(self):
        self.client.post(
            self.URL,
                         headers={"authorization": "Token " + self.AUTH_TOKEN},
                         json={
                            "pageNumber": 1,
                            "pageSize": 10,
                            "userId": "P2028001_TEST",
                            "loanNo": "LN00305137",
                            "dealerCode": "P2028001"
                        }
                         )