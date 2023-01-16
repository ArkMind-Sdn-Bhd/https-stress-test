from locust import HttpUser, task


class DfStressTest(HttpUser):

    BASE_URL = "https://acosb.parksoncredit.com.my:8088"
    DEALER_TOKEN = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJodHRwOi8vc2NoZW1hcy54bWxzb2FwLm9yZy93cy8yMDA1LzA1L2lkZW50aXR5L2NsYWltcy9uYW1lIjoiUDIwMjgwMDFfVEVTVCIsImh0dHA6Ly9zY2hlbWFzLnhtbHNvYXAub3JnL3dzLzIwMDUvMDUvaWRlbnRpdHkvY2xhaW1zL25hbWVpZGVudGlmaWVyIjoiMzQ4YzhlYWQtM2I2Ni00NThlLWFhY2YtODdhMDU4NzQ2MDJiIiwicGFzc3dvcmQiOiI1RjREQ0MzQjVBQTc2NUQ2MUQ4MzI3REVCODgyQ0Y5OSIsIm5iZiI6MTY3MzgzNjIwNywiZXhwIjoxNjczOTIyNjA3LCJpc3MiOiJodHRwczovL2Fjb3NiLnBhcmtzb25jcmVkaXQuY29tLm15OjgwODgiLCJhdWQiOiJodHRwczovL2Fjb3NiLnBhcmtzb25jcmVkaXQuY29tLm15OjgwODgifQ.AQwhMecHrvKtIPxWn_giQ3D7H8p9Y61kx9HF115mROE"
    INTERNAL_TOKEN = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJodHRwOi8vc2NoZW1hcy54bWxzb2FwLm9yZy93cy8yMDA1LzA1L2lkZW50aXR5L2NsYWltcy9uYW1lIjoiUEMwMDBfUkFIQVlVIiwiaHR0cDovL3NjaGVtYXMueG1sc29hcC5vcmcvd3MvMjAwNS8wNS9pZGVudGl0eS9jbGFpbXMvbmFtZWlkZW50aWZpZXIiOiI5ODUyNjQ0Ni0wNGM4LTQxNzItYjJlNS1kMzk0MmYxNTM3ZDciLCJwYXNzd29yZCI6IjM2MzFCMzgzQTE0QzBDQTM0MzE4QkZBMjFCMUEwODcwIiwibmJmIjoxNjczODM2MTg5LCJleHAiOjE2NzM5MjI1ODksImlzcyI6Imh0dHBzOi8vYWNvc2IucGFya3NvbmNyZWRpdC5jb20ubXk6ODA4OCIsImF1ZCI6Imh0dHBzOi8vYWNvc2IucGFya3NvbmNyZWRpdC5jb20ubXk6ODA4OCJ9.WT6OgzT928QAGmkZ_GxJ-YjwAiYdbkNU1rCk4HY4wPc"

    @task
    def dealer_sales_claim_summary_status(self):
        self.client.get(
            self.BASE_URL + "/api/LoanApplication/GetSalesSummaryStatusListLite?pageNumber=1&pageSize=10",
            headers={"Token": self.DEALER_TOKEN}
        )

    @task
    def dealer_sales_claim_summary_status(self):
        self.client.post(
            self.BASE_URL + "/api/LoanApplication/GetEHakMilikByStatus?pageSize=10&pageNumber=1",
            headers={"Token": self.INTERNAL_TOKEN},
            json={
                "pageNumber": 1,
                "pageSize": 100,
                "status": "NEW",
                "nric": ""
            }
        )

    @task
    def business_development_application_status_list(self):
        self.client.post(
            self.BASE_URL + "/api/LoanApplication/GetAllApplicationStatusExceptPFList?pageSize=10&pageNumber=1",
            headers={"Token": self.INTERNAL_TOKEN},
            json={}
        )

    @task
    def business_development_application_status_list(self):
        self.client.post(
            self.BASE_URL + "/api/LoanApplication/GetAllApplicationStatusExceptPFList?pageSize=10&pageNumber=1",
            headers={"Token": self.INTERNAL_TOKEN},
            json={
                "pageSize": 10,
                "pageNumber": 1,
                "dealerCode": "",
                "applicantNRIC": "",
                "applicantName": "",
                "loanType": "",
                "status": ""
            }
        )

    @task
    def e_application_form_credit_accessment_page(self):
        self.client.post(
            self.BASE_URL + "/api/LoanApplication/GetDetails",
            headers={"Token": self.INTERNAL_TOKEN},
            json={
                "loanNo": "LN00293410",
                "userId": "PC000_RAHAYU"
            }
        )

    @task
    def e_application_form_credit_accessment_page(self):
        self.client.get(
            self.BASE_URL + "/api/SalesSettlement/v2/GetEligibleApplicationForSettlement/P2028001_TEST/P2028001/001?ListType=E-SETTLEMENT&pageNumber=1&pageSize=10",
            headers={"Token": self.DEALER_TOKEN},
        )

    @task
    def cep_internal_search(self):
        self.client.get(
            self.BASE_URL + "/api/LoanApplication/Internal/Search?AgreementNo=6192230781",
            headers={"Token": self.INTERNAL_TOKEN},
        )

    @task
    def e_settlement_softcopy_task_listing(self):
        self.client.get(
            self.BASE_URL + "/api/MyTask/GetOpenESettlements?PageNumber=1&PageSize=20&TAT=>=2&DocType=E-DOC&UserId=PC000_NURHIKMAH",
            headers={"Token": self.INTERNAL_TOKEN},
        )

    @task
    def document_search_and_view(self):
        self.client.post(
            self.BASE_URL + "/api/DocumentSearch/Search",
            headers={"Token": self.INTERNAL_TOKEN},
            json={
                "agreementNo": "6192227919",
                "nric": "",
                "vehicleNo": ""
            }
        )

    @task
    def unclaimed_sales_follow_up(self):
        self.client.get(
            self.BASE_URL + "/api/UnclaimedFollowUp/v2/GetUnclaimedSalesLoanApplication?dealerCode=P2028&PageNumber=1&PageSize=10",
            headers={"Token": self.INTERNAL_TOKEN},
        )

    @task
    def pf_application(self):
        self.client.get(
            self.BASE_URL + "/api/LoanApplication/OpenApplicationPF/Search?LoanType=PF&PageNumber=1&PageSize=10",
            headers={"Token": self.INTERNAL_TOKEN},
        )

    @task
    def pf_application_result(self):
        self.client.get(
            self.BASE_URL + "/api/LoanApplication/PFApplications?status=APPROVED&PageSize=10&PageNumber=1",
            headers={"Token": self.INTERNAL_TOKEN},
        )

    @task
    def get_application_status_list(self):
        self.client.post(
            self.BASE_URL + "/api/LoanApplication/GetApplicationStatusList",
            headers={"Token": self.DEALER_TOKEN},
            json={
                "pageNumber": 1,
                "pageSize": 10,
                "status": [
                    "IN PROCESS"
                ],
                "userId": "P2028001",
                "dealerCode": "P2028001"
            }
        )

    @task
    def search_application_result(self):
        self.client.post(
            self.BASE_URL + "/api/LoanApplication/SearchApplicationResultPage",
            headers={"Token": self.DEALER_TOKEN},
            json={
                "pageNumber": 1,
                "pageSize": 10,
                "userId": "P2028001_001",
                "loanNo": "LN00305137",
                "dealerCode": "P2028001"
            }
        )

    @task
    def dealer_search(self):
        self.client.get(
            self.BASE_URL + "/api/LoanApplication/Search?AgreementNo=6192300777&DealerCode=P2028001",
            headers={"Token": self.DEALER_TOKEN},
        )

    @task
    def dealer_search_details(self):
        self.client.get(
            self.BASE_URL + "/api/LoanApplication/Search/Details/LN00305137",
            headers={"Token": self.DEALER_TOKEN},
        )

    @task
    def case_assignment_get_details(self):
        self.client.get(
            self.BASE_URL + "/api/LoanApplication/v2/GetDetails/LN00293410",
            headers={"Token": self.INTERNAL_TOKEN},
        )

    @task
    def settlement_batch_tracking(self):
        self.client.get(
            self.BASE_URL + "/api/SalesSettlement/Dealer/SettlementBatchTracking/P2028001?PageNumber=0&PageSize=100",
            headers={"Token": self.DEALER_TOKEN},
        )

    @task
    def settlement_courier_summary(self):
        self.client.get(
            self.BASE_URL + "/api/SalesSettlement/SettlementCourierSummary?pageNumber=0&pageSize=10",
            headers={"Token": self.DEALER_TOKEN},
        )

    @task
    def cep_search_details(self):
        self.client.get(
            self.BASE_URL + "/api/LoanApplication/Internal/Search/Details/LN00305137",
            headers={"Token": self.INTERNAL_TOKEN},
        )